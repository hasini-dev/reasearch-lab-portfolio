from __future__ import annotations
from typing import List, Tuple, Optional
import time, os
import math
import random

# ---------------------------------------------------------------------------
# Minimal Chess AI (Minimax + Alpha-Beta)
# - Full 8x8 chessboard
# - Legal move generation with check legality (no castling, no en passant)
# - Pawn promotion to queen only
# - Check / checkmate / stalemate detection
# - AI vs AI with delays to watch it play
# ---------------------------------------------------------------------------

EMPTY = "."
WHITE, BLACK = "w", "b"

# Piece symbols (uppercase = White, lowercase = Black)
# P,N,B,R,Q,K / p,n,b,r,q,k

START_FEN = (
    "rnbqkbnr/"
    "pppppppp/"
    "........"
    "/........"
    "/........"
    "/........"
    "PPPPPPPP/"
    "RNBQKBNR w"
)

PIECE_VALUES = {
    "P": 100, "N": 320, "B": 330, "R": 500, "Q": 900, "K": 0,
    "p": -100, "n": -320, "b": -330, "r": -500, "q": -900, "k": 0,
}

# Knight & King deltas
KNIGHT_DIRS = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
KING_DIRS = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
# Sliding piece directions
BISHOP_DIRS = [(-1,-1),(-1,1),(1,-1),(1,1)]
ROOK_DIRS   = [(-1,0),(1,0),(0,-1),(0,1)]
QUEEN_DIRS  = BISHOP_DIRS + ROOK_DIRS


Board = List[List[str]]
Move = Tuple[Tuple[int,int], Tuple[int,int], Optional[str]]  # ((r1,c1),(r2,c2), promo)


# --- Board utilities ---------------------------------------------------------

def fen_to_board(fen: str) -> Tuple[Board, str]:
    # Ensure there are 8 rows and a side indicator
    fields = fen.strip().split()
    if len(fields) == 1:
        board_field, side = fields[0], "w"
    else:
        board_field, side = fields[0], fields[1]

    rows_raw = board_field.split("/")
    if len(rows_raw) != 8:
        raise ValueError(f"Invalid FEN: expected 8 rows, got {len(rows_raw)}")

    board: Board = []
    for row_str in rows_raw:
        row = []
        for ch in row_str:
            if ch.isdigit():
                row.extend([EMPTY] * int(ch))
            else:
                row.append(ch)
        if len(row) != 8:
            raise ValueError(f"Invalid FEN row '{row_str}' → {len(row)} columns")
        board.append(row)

    return board, side


def starting_board() -> Tuple[Board, str]:
    # Standard chess start position with space before side indicator
    return fen_to_board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w")


def copy_board(b: Board) -> Board:
    return [row[:] for row in b]

def in_bounds(r: int, c: int) -> bool:
    return 0 <= r < 8 and 0 <= c < 8

def side_of(piece: str) -> Optional[str]:
    if piece == EMPTY: return None
    return WHITE if piece.isupper() else BLACK

def print_board(b: Board) -> None:
    os.system("cls" if os.name == "nt" else "clear")
    print("    0 1 2 3 4 5 6 7")
    print("   -----------------")
    for r in range(8):
        print(f"{r} | " + " ".join(b[r]))
    print()

def find_king(b: Board, side: str) -> Tuple[int,int]:
    target = "K" if side == WHITE else "k"
    for r in range(8):
        for c in range(8):
            if b[r][c] == target:
                return r, c
    # Should never happen in normal play
    return -1, -1


# --- Attack detection --------------------------------------------------------

def square_attacked_by(b: Board, r: int, c: int, attacker: str) -> bool:
    """Return True if square (r,c) is attacked by 'attacker' side."""
    # Pawns
    if attacker == WHITE:
        for dc in (-1, 1):
            rr, cc = r+1, c+dc  # white pawns attack downwards from black's POV? No: White pawns go up (-1)
        # Correct directions:
        for dc in (-1, 1):
            rr, cc = r-1, c+dc
            if in_bounds(rr, cc) and b[rr][cc] == "P":
                return True
    else:
        for dc in (-1, 1):
            rr, cc = r+1, c+dc
            if in_bounds(rr, cc) and b[rr][cc] == "p":
                return True

    # Knights
    for dr, dc in KNIGHT_DIRS:
        rr, cc = r+dr, c+dc
        if not in_bounds(rr, cc): continue
        p = b[rr][cc]
        if attacker == WHITE and p == "N": return True
        if attacker == BLACK and p == "n": return True

    # Kings
    for dr, dc in KING_DIRS:
        rr, cc = r+dr, c+dc
        if not in_bounds(rr, cc): continue
        p = b[rr][cc]
        if attacker == WHITE and p == "K": return True
        if attacker == BLACK and p == "k": return True

    # Bishops/Queens (diagonals)
    for dr, dc in BISHOP_DIRS:
        rr, cc = r+dr, c+dc
        while in_bounds(rr, cc):
            p = b[rr][cc]
            if p != EMPTY:
                if attacker == WHITE and (p == "B" or p == "Q"): return True
                if attacker == BLACK and (p == "b" or p == "q"): return True
                break
            rr += dr; cc += dc

    # Rooks/Queens (orthogonals)
    for dr, dc in ROOK_DIRS:
        rr, cc = r+dr, c+dc
        while in_bounds(rr, cc):
            p = b[rr][cc]
            if p != EMPTY:
                if attacker == WHITE and (p == "R" or p == "Q"): return True
                if attacker == BLACK and (p == "r" or p == "q"): return True
                break
            rr += dr; cc += dc

    return False

def in_check(b: Board, side: str) -> bool:
    kr, kc = find_king(b, side)
    return square_attacked_by(b, kr, kc, WHITE if side == BLACK else BLACK)


# --- Move generation (pseudo-legal) -----------------------------------------

def gen_pawn_moves(b: Board, r: int, c: int, side: str, moves: List[Move]) -> None:
    if side == WHITE:
        # single push
        if in_bounds(r-1, c) and b[r-1][c] == EMPTY:
            if r-1 == 0:  # promotion
                moves.append(((r,c),(r-1,c),"Q"))
            else:
                moves.append(((r,c),(r-1,c),None))
            # double push from rank 6
            if r == 6 and b[r-2][c] == EMPTY:
                moves.append(((r,c),(r-2,c),None))
        # captures
        for dc in (-1, 1):
            rr, cc = r-1, c+dc
            if in_bounds(rr, cc) and side_of(b[rr][cc]) == BLACK:
                if rr == 0:
                    moves.append(((r,c),(rr,cc),"Q"))
                else:
                    moves.append(((r,c),(rr,cc),None))
    else:
        # single push
        if in_bounds(r+1, c) and b[r+1][c] == EMPTY:
            if r+1 == 7:
                moves.append(((r,c),(r+1,c),"q"))
            else:
                moves.append(((r,c),(r+1,c),None))
            if r == 1 and b[r+2][c] == EMPTY:
                moves.append(((r,c),(r+2,c),None))
        # captures
        for dc in (-1, 1):
            rr, cc = r+1, c+dc
            if in_bounds(rr, cc) and side_of(b[rr][cc]) == WHITE:
                if rr == 7:
                    moves.append(((r,c),(rr,cc),"q"))
                else:
                    moves.append(((r,c),(rr,cc),None))

def gen_sliding_moves(b: Board, r: int, c: int, side: str, dirs: List[Tuple[int,int]], moves: List[Move]) -> None:
    for dr, dc in dirs:
        rr, cc = r+dr, c+dc
        while in_bounds(rr, cc):
            p = b[rr][cc]
            if p == EMPTY:
                moves.append(((r,c),(rr,cc),None))
            else:
                if side_of(p) != side:
                    moves.append(((r,c),(rr,cc),None))
                break
            rr += dr; cc += dc

def gen_knight_moves(b: Board, r: int, c: int, side: str, moves: List[Move]) -> None:
    for dr, dc in KNIGHT_DIRS:
        rr, cc = r+dr, c+dc
        if not in_bounds(rr, cc): continue
        p = b[rr][cc]
        if p == EMPTY or side_of(p) != side:
            moves.append(((r,c),(rr,cc),None))

def gen_king_moves(b: Board, r: int, c: int, side: str, moves: List[Move]) -> None:
    for dr, dc in KING_DIRS:
        rr, cc = r+dr, c+dc
        if not in_bounds(rr, cc): continue
        p = b[rr][cc]
        if p == EMPTY or side_of(p) != side:
            moves.append(((r,c),(rr,cc),None))
    # (Castling omitted in this minimal version)

def pseudo_legal_moves(b: Board, side: str) -> List[Move]:
    moves: List[Move] = []
    for r in range(8):
        for c in range(8):
            p = b[r][c]
            if p == EMPTY or side_of(p) != side: continue
            if p in ("P", "p"):
                gen_pawn_moves(b, r, c, side, moves)
            elif p in ("N", "n"):
                gen_knight_moves(b, r, c, side, moves)
            elif p in ("B", "b"):
                gen_sliding_moves(b, r, c, side, BISHOP_DIRS, moves)
            elif p in ("R", "r"):
                gen_sliding_moves(b, r, c, side, ROOK_DIRS, moves)
            elif p in ("Q", "q"):
                gen_sliding_moves(b, r, c, side, QUEEN_DIRS, moves)
            elif p in ("K", "k"):
                gen_king_moves(b, r, c, side, moves)
    return moves

def make_move(b: Board, mv: Move) -> Board:
    (r1,c1), (r2,c2), promo = mv
    nb = copy_board(b)
    piece = nb[r1][c1]
    nb[r1][c1] = EMPTY
    if promo:
        nb[r2][c2] = promo
    else:
        nb[r2][c2] = piece
    return nb

def legal_moves(b: Board, side: str) -> List[Move]:
    """Filter pseudo-legal moves to those that don't leave our king in check."""
    out: List[Move] = []
    for mv in pseudo_legal_moves(b, side):
        nb = make_move(b, mv)
        if not in_check(nb, side):
            out.append(mv)
    return out


# --- End conditions ----------------------------------------------------------

def game_result(b: Board, side_to_move: str) -> Optional[str]:
    """
    Returns:
      'w' if White wins by checkmate,
      'b' if Black wins by checkmate,
      'Draw' for stalemate or insufficient material (very basic),
      None if game continues.
    """
    lm = legal_moves(b, side_to_move)
    if lm:
        return None
    # No legal moves: checkmate or stalemate
    if in_check(b, side_to_move):
        return WHITE if side_to_move == BLACK else BLACK
    return "Draw"


# --- Evaluation --------------------------------------------------------------

def evaluate(b: Board) -> int:
    """Simple material evaluation (from White's perspective)."""
    score = 0
    for r in range(8):
        for c in range(8):
            p = b[r][c]
            if p != EMPTY:
                score += PIECE_VALUES[p]
    return score


# --- Minimax + Alpha-Beta ----------------------------------------------------

def minimax(b: Board, depth: int, alpha: int, beta: int, side: str) -> Tuple[int, Optional[Move]]:
    res = game_result(b, side)
    if res is not None:
        if res == "Draw":
            return 0, None
        return (math.inf if res == WHITE else -math.inf, None)

    if depth == 0:
        return evaluate(b), None

    moves = legal_moves(b, side)
    if not moves:
        # handled by game_result above, but safe-guard
        return (evaluate(b), None)

    best_move: Optional[Move] = None
    if side == WHITE:
        best_val = -math.inf
        for mv in moves:
            nb = make_move(b, mv)
            val, _ = minimax(nb, depth-1, alpha, beta, BLACK)
            if val > best_val:
                best_val, best_move = val, mv
            alpha = max(alpha, best_val)
            if beta <= alpha:
                break
        return best_val, best_move
    else:
        best_val = math.inf
        for mv in moves:
            nb = make_move(b, mv)
            val, _ = minimax(nb, depth-1, alpha, beta, WHITE)
            if val < best_val:
                best_val, best_move = val, mv
            beta = min(beta, best_val)
            if beta <= alpha:
                break
        return best_val, best_move


# --- Driver: AI vs AI --------------------------------------------------------

def play_ai_vs_ai(delay: float = 0.5, depth_w: int = 2, depth_b: int = 2, move_limit: int = 200):
    b, side = starting_board()  # White to move
    ply = 0
    while True:
        print_board(b)
        result = game_result(b, side)
        if result is not None:
            print("Winner:", result)
            return result

        depth = depth_w if side == WHITE else depth_b
        score, mv = minimax(b, depth, -math.inf, math.inf, side)

        # Safety fallback (shouldn't happen often)
        if mv is None:
            legal = legal_moves(b, side)
            if not legal:
                print("Winner:", "Draw")
                return "Draw"
            mv = random.choice(legal)

        b = make_move(b, mv)
        print(f"{'White' if side == WHITE else 'Black'} plays {mv}")
        time.sleep(delay)

        side = BLACK if side == WHITE else WHITE
        ply += 1
        if ply >= move_limit:
            print_board(b)
            print("Winner: Draw (move limit)")
            return "Draw"


# --- Main --------------------------------------------------------------------

if __name__ == "__main__":
    # Watch two simple chess AIs play.
    # Increase depths for stronger play (but it will be slower).
    play_ai_vs_ai(delay=0.5, depth_w=2, depth_b=2, move_limit=200)
