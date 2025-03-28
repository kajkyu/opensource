import random

# 보드 출력 함수
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# 승리 조건 체크 함수
def check_winner(board, player):
    # 가로, 세로, 대각선 체크
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# 빈 자리 찾기 함수
def available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                moves.append((i, j))
    return moves

# 컴퓨터의 플레이
def computer_move(board):
    # 무작위로 빈 자리를 선택
    moves = available_moves(board)
    return random.choice(moves)

# 게임 진행 함수
def play_game():
    # 보드 초기화
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  # 사용자
    computer_player = "O"
    
    print("틱택토 게임 시작!")
    print_board(board)
    
    while True:
        if current_player == "X":
            # 사용자 입력 받기
            row, col = map(int, input("행과 열을 입력하세요 (0, 1, 2): ").split())
            if board[row][col] != " ":
                print("잘못된 입력입니다. 다시 시도하세요.")
                continue
            board[row][col] = "X"
            
            if check_winner(board, "X"):
                print_board(board)
                print("사용자가 승리했습니다!")
                break
            
            current_player = "O"  # 컴퓨터 차례
        else:
            # 컴퓨터의 플레이
            row, col = computer_move(board)
            board[row][col] = "O"
            print(f"컴퓨터의 차례: {row} {col}")
            
            if check_winner(board, "O"):
                print_board(board)
                print("컴퓨터가 승리했습니다!")
                break
            
            current_player = "X"  # 사용자 차례
        
        # 보드 출력
        print_board(board)
        
        # 게임이 끝났는지 확인
        if len(available_moves(board)) == 0:
            print("무승부입니다!")
            break

# 게임 시작
play_game()
