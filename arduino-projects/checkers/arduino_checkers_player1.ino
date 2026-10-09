#include <Wire.h>

#define SLAVE_ADDRESS 8

char board[8][8]; 
char player = 'X';
char opponent = 'O';

void setup() {
    Serial.begin(9600);
    Wire.begin();
    Serial.println("Checkers Master Started");
    initBoard();
    printBoard();
}

void loop() {
    int fromRow, fromCol, toRow, toCol;

    getMove(fromRow, fromCol, toRow, toCol);
    if (isValidMove(fromRow, fromCol, toRow, toCol, player)) {
        makeMove(fromRow, fromCol, toRow, toCol, player);
        sendMove(fromRow, fromCol, toRow, toCol);

        if (checkWin(player)) {
            Serial.println("You Win!");
            while (1);
        }

        receiveMove();
        printBoard();

        if (checkWin(opponent)) {
            Serial.println("Opponent Wins!");
            while (1);
        }
    } else {
        Serial.println("Invalid move. Try again.");
    }
}

void initBoard() {
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            if ((i + j) % 2 == 1) {
                if (i < 3) board[i][j] = 'O';  // Opponent pieces
                else if (i > 4) board[i][j] = 'X'; // Player pieces
                else board[i][j] = '.'; // Empty space
            } else {
                board[i][j] = ' '; // Unused spaces
            }
        }
    }
}

void getMove(int &fromRow, int &fromCol, int &toRow, int &toCol) {
    Serial.println("Enter move as: fromRow fromCol toRow toCol");
    while (!Serial.available());
    fromRow = Serial.parseInt();
    fromCol = Serial.parseInt();
    toRow = Serial.parseInt();
    toCol = Serial.parseInt();
}

bool isValidMove(int fromRow, int fromCol, int toRow, int toCol, char symbol) {
    if (board[fromRow][fromCol] != symbol || board[toRow][toCol] != '.') return false;

    int rowDiff = abs(toRow - fromRow);
    int colDiff = abs(toCol - fromCol);

    if (rowDiff == 1 && colDiff == 1) return true; // Normal move
    if (rowDiff == 2 && colDiff == 2) { // Capture move
        int midRow = (fromRow + toRow) / 2;
        int midCol = (fromCol + toCol) / 2;
        if (board[midRow][midCol] == opponent) {
            board[midRow][midCol] = '.'; // Remove captured piece
            return true;
        }
    }
    return false;
}

void makeMove(int fromRow, int fromCol, int toRow, int toCol, char symbol) {
    board[fromRow][fromCol] = '.';
    board[toRow][toCol] = symbol;
}

void sendMove(int fromRow, int fromCol, int toRow, int toCol) {
    Wire.beginTransmission(SLAVE_ADDRESS);
    Wire.write(fromRow);
    Wire.write(fromCol);
    Wire.write(toRow);
    Wire.write(toCol);
    Wire.endTransmission();
}

void receiveMove() {
    Wire.requestFrom(SLAVE_ADDRESS, 4);
    while (Wire.available()) {
        int fromRow = Wire.read();
        int fromCol = Wire.read();
        int toRow = Wire.read();
        int toCol = Wire.read();
        makeMove(fromRow, fromCol, toRow, toCol, opponent);
        Serial.print("Opponent moved: ");
        Serial.print(fromRow); Serial.print(", ");
        Serial.print(fromCol); Serial.print(" -> ");
        Serial.print(toRow); Serial.print(", ");
        Serial.println(toCol);
    }
}

void printBoard() {
    Serial.println("\nCurrent Board:");
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            Serial.print(board[i][j]);
            Serial.print(" ");
        }
        Serial.println();
    }
}

bool checkWin(char symbol) {
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            if (board[i][j] == opponent) return false;
        }
    }
    return true;
}
