from __future__ import annotations
from typing import List, Tuple, Optional
import random
import time
import os

# ---------------------------------------------------------------------------
# Simple Checkers AI (Minimax) – Basic playable version
#   - 8x8 board
#   - Normal moves + single captures
#   - No kinging / multi-jumps yet (can add next)
#   - AI vs AI with delay so you can watch it play
# ---------------------------------------------------------------------------

EMPTY, P1, P2 = ".", "x", "o"   # P1 = bottom side, P2 = top side
BOARD_SIZE = 8


# --- Board helpers -----------------------------------------------------------

def initial_board() -> List[List[str]]:
    """Create the initial 8x8 checkers setup (pieces on dark squares)."""
    b = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    # Top three rows: P2
    for r in range(3):
        for c in range(BOARD_SIZE):
            if (r + c) % 2 == 1:
                b[r][c] = P2
    # Bottom three rows: P1
    for r in range(5, 8):
        for c in range(BOARD_SIZE):
            if (r + c) % 2 == 1:
                b[r][c] = P1
    return b


def print_board(b: List[List[str]]) -> None:
    os.system("cls" if os.name == "nt" else "clear")
    print("    " + " ".join(map(str, range(BOARD_SIZE))))
    print("   " + "-" * (2 * BOARD_SIZE - 1))
    for r in range(BOARD_SIZE):
        print(f"{r} | " + " ".join(b[r]))
    print()


def opponent(p: str) -> str:
    return P1 if p == P2 else P2


def copy_board(b: List[List[str]]) -> List[List[str]]:
    return [row[:] for row in b]


# --- Move generation ---------------------------------------------------------

def get_moves(b: List[List[str]], player: str) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """
    Return all legal single-step and single-capture moves for 'player'.
    P2 (top) moves DOWN (+1). P1 (bottom) moves UP (-1).
    """
    moves = []
    direction = 1 if player == P2 else -1  # <-- FIXED ORIENTATION

    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if b[r][c] != player:
                continue

            for dc in (-1, 1):
                nr, nc = r + direction, c + dc
                # simple diagonal step
                if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE and b[nr][nc] == EMPTY:
                    moves.append(((r, c), (nr, nc)))

                # capture (jump over opponent)
                jr, jc = r + 2 * direction, c + 2 * dc
                mr, mc = r + direction, c + dc  # middle (captured) square
                if (
                    0 <= jr < BOARD_SIZE and 0 <= jc < BOARD_SIZE and
                    0 <= mr < BOARD_SIZE and 0 <= mc < BOARD_SIZE and
                    b[mr][mc] == opponent(player) and b[jr][jc] == EMPTY
                ):
                    moves.append(((r, c), (jr, jc)))

    return moves


def make_move(b: List[List[str]], move: Tuple[Tuple[int, int], Tuple[int, int]]) -> List[List[str]]:
    """Return a new board after making a (step or single capture) move."""
    (r1, c1), (r2, c2) = move
    nb = copy_board(b)
    nb[r2][c2] = nb[r1][c1]
    nb[r1][c1] = EMPTY
    # if it's a jump, remove captured piece
    if abs(r2 - r1) == 2 and abs(c2 - c1) == 2:
        nb[(r1 + r2) // 2][(c1 + c2) // 2] = EMPTY
    return nb


def count_pieces(b: List[List[str]], player: str) -> int:
    return sum(row.count(player) for row in b)


def game_over(b: List[List[str]]) -> Optional[str]:
    """Return 'x', 'o', 'Draw', or None."""
    if count_pieces(b, P1) == 0:
        return P2
    if count_pieces(b, P2) == 0:
        return P1
    if not get_moves(b, P1) and not get_moves(b, P2):
        return "Draw"
    return None


# --- Minimax (depth-limited) -------------------------------------------------

def evaluate(b: List[List[str]], player: str) -> int:
    """Very simple evaluation: piece advantage."""
    return count_pieces(b, player) - count_pieces(b, opponent(player))


def minimax(b: List[List[str]], depth: int, maximizing: bool, player: str) -> Tuple[int, Optional[Tuple]]:
    """
    Depth-limited minimax without alpha-beta (kept simple).
    Returns (score, best_move_for_side_to_play_in_this_node)
    """
    result = game_over(b)
    if result is not None:
        if result == player:
            return (1000, None)
        if result == "Draw":
            return (0, None)
        return (-1000, None)

    if depth == 0:
        return evaluate(b, player), None

    side = player if maximizing else opponent(player)
    moves = get_moves(b, side)
    if not moves:
        # No moves for side to play: evaluate position for 'player'
        return evaluate(b, player), None

    if maximizing:
        best_val, best_move = -10_000, None
        for mv in moves:
            nb = make_move(b, mv)
            val, _ = minimax(nb, depth - 1, False, player)
            if val > best_val:
                best_val, best_move = val, mv
        return best_val, best_move
    else:
        best_val, best_move = 10_000, None
        for mv in moves:
            nb = make_move(b, mv)
            val, _ = minimax(nb, depth - 1, True, player)
            if val < best_val:
                best_val, best_move = val, mv
        return best_val, best_move


# --- Game loop ---------------------------------------------------------------

def play_ai_vs_ai(delay: float = 0.8, depth: int = 2, max_plies: int = 400):
    b = initial_board()
    turn = P1  # P1 starts
    plies = 0

    while game_over(b) is None and plies < max_plies:
        print_board(b)
        moves = get_moves(b, turn)
        if not moves:
            print(f"{turn} has no legal moves. Turn passes.")
            turn = opponent(turn)
            continue

        _, mv = minimax(b, depth=depth, maximizing=True, player=turn)
        if mv is None:
            # fallback to some legal move if minimax gives None (shouldn't happen often)
            mv = random.choice(moves)

        b = make_move(b, mv)
        print(f"{turn} plays {mv}")
        time.sleep(delay)
        turn = opponent(turn)
        plies += 1

    print_board(b)
    print("Winner:", game_over(b))


# --- Run ---------------------------------------------------------------------

if __name__ == "__main__":
    # Watch two simple AIs play
    play_ai_vs_ai(delay=0.8, depth=2)
