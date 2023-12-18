import pygame
import numpy as np
import random


ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARE_SIZE = 100
RADIUS = int(SQUARE_SIZE / 2 - 5)
WIDTH = COLUMN_COUNT * SQUARE_SIZE
HEIGHT = (ROW_COUNT + 2) * SQUARE_SIZE
DROP_SPEED = 10
BACKGROUND_COLOR = (52, 73, 94)
BOARD_COLOR = (41, 128, 185)
PIECE_1_COLOR = (231, 76, 60)
PIECE_2_COLOR = (241, 196, 15)
TEXT_COLOR = (236, 240, 241)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
EMPTY = 0
FPS = 60
pygame.mixer.init()
button_click_sound = pygame.mixer.Sound('Button Press.mp3')
start_click_sound = pygame.mixer.Sound('Game Start.mp3')
piece_click_sound = pygame.mixer.Sound('connect 4 piece.mp3')
victory_click_sound = pygame.mixer.Sound('victory.mp3')

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def drop_piece(board, col, piece):
    row = get_next_open_row(board, col)
    start_y = 2 * SQUARE_SIZE
    end_y = (ROW_COUNT - row - 1) * SQUARE_SIZE + int(SQUARE_SIZE / 2)
    increment = DROP_SPEED
    sound_played = False

    while start_y <= end_y:
        screen.fill(BACKGROUND_COLOR)
        draw_board(board)

        if piece == 1:
            pygame.draw.circle(screen, PIECE_1_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE / 2), start_y), RADIUS)
        else:
            pygame.draw.circle(screen, PIECE_2_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE / 2), start_y), RADIUS)

        if not sound_played:
            piece_click_sound.play()
            sound_played = True

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                if board[r][c] == 1:
                    pygame.draw.circle(screen, PIECE_1_COLOR, (int(c * SQUARE_SIZE + SQUARE_SIZE / 2), HEIGHT - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
                elif board[r][c] == 2:
                    pygame.draw.circle(screen, PIECE_2_COLOR, (int(c * SQUARE_SIZE + SQUARE_SIZE / 2), HEIGHT - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)

        pygame.display.update()
        clock.tick(FPS)

        start_y += increment

    board[row][col] = piece

def winning_move(board, piece):
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True

def draw_board(board):
    screen.fill(BACKGROUND_COLOR)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BOARD_COLOR, (c * SQUARE_SIZE, (r + 2) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, BACKGROUND_COLOR, (int(c * SQUARE_SIZE + SQUARE_SIZE / 2), int((r + 2) * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)

    column_font = pygame.font.SysFont("comicsansms", 60)
    for c in range(COLUMN_COUNT):
        column_num = column_font.render(str(c + 1), 1, TEXT_COLOR)
        screen.blit(column_num, (c * SQUARE_SIZE + SQUARE_SIZE // 2 - column_num.get_width() // 2, SQUARE_SIZE // 2 - column_num.get_height() // 2))

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, PIECE_1_COLOR, (int(c * SQUARE_SIZE + SQUARE_SIZE / 2), HEIGHT - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, PIECE_2_COLOR, (int(c * SQUARE_SIZE + SQUARE_SIZE / 2), HEIGHT - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
    pygame.display.update()

def start_menu():
    title_font = pygame.font.SysFont("comicsansms", 65)
    start_font = pygame.font.SysFont("comicsansms", 50)
    button_width = 200
    button_height = 80
    run_menu = True

    while run_menu:
        screen.fill(BACKGROUND_COLOR)

        welcome_text = title_font.render("Welcome to Connect 4", True, TEXT_COLOR)
        edition_text = title_font.render("Mr. Naidu's Edition", True, TEXT_COLOR)
        screen.blit(welcome_text, (WIDTH / 2 - welcome_text.get_width() / 2, HEIGHT / 5 - welcome_text.get_height()))
        screen.blit(edition_text, (WIDTH / 2 - edition_text.get_width() / 2, HEIGHT / 6 + edition_text.get_height()))

        start_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - button_height // 2, button_width, button_height)
        quit_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 1.2 - button_height // 2, button_width, button_height)
        rules_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 1.5 - button_height // 2, button_width, button_height)

        pygame.draw.rect(screen, PIECE_1_COLOR, rules_button)
        pygame.draw.rect(screen, PIECE_1_COLOR, start_button)
        pygame.draw.rect(screen, PIECE_1_COLOR, quit_button)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if start_button.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(screen, PIECE_2_COLOR, start_button)
            if pygame.mouse.get_pressed()[0]:
                start_click_sound.play()
                screen.fill(BACKGROUND_COLOR)
                run_menu = False

        if quit_button.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(screen, PIECE_2_COLOR, quit_button)
            if pygame.mouse.get_pressed()[0]:
                button_click_sound.play()
                pygame.quit()

        if rules_button.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(screen, PIECE_2_COLOR, rules_button)
            if pygame.mouse.get_pressed()[0]:
                button_click_sound.play()
                screen.fill(BACKGROUND_COLOR)
                display_rules()

        start_label = start_font.render("Start", True, (255, 255, 255))
        screen.blit(start_label, (WIDTH // 2 - start_label.get_width() // 2, HEIGHT // 2 - start_label.get_height() // 2))
        quit_label = start_font.render("Quit", True, (255, 255, 255))
        screen.blit(quit_label, (WIDTH // 2 - quit_label.get_width() // 2, HEIGHT // 1.2 - quit_label.get_height() // 2))
        rules_label = start_font.render("Rules", True, (255, 255, 255))
        screen.blit(rules_label, (WIDTH // 2 - rules_label.get_width() // 2, HEIGHT // 1.5 - rules_label.get_height() // 2))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_menu = False
                pygame.quit()
                quit()


def display_rules():
    run_rules = True
    back_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 85, 200, 50)

    while run_rules:
        screen.fill(BACKGROUND_COLOR)

        rules_text = [
            "Connect 4 Rules:",
            "",
            "1. Players take turns dropping colored pieces into a grid.",
            "2. The discs fall straight down, occupying the lowest available space.",
            "3. The objective is to connect four of your own pieces in a row ",
            "     horizontally, vertically, or diagonally.",
            "4. The game ends when a player achieves a Connect 4 or the board ",
            "     fills up.",
            "",
            "Controls:",
            "- Use the mouse to select a column for dropping your disc.",
            "- Click 'Start' to begin the game or 'Quit' to exit."
        ]

        rules_font = pygame.font.SysFont("comicsansms", 21)
        text_start_y = HEIGHT // 6

        for line in rules_text:
            line_surface = rules_font.render(line, True, TEXT_COLOR)
            screen.blit(line_surface, (SQUARE_SIZE - 90, text_start_y))
            text_start_y += line_surface.get_height() + 5

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if back_button.collidepoint(mouse_x, mouse_y):
            back_button_color = PIECE_2_COLOR
        else:
            back_button_color = PIECE_1_COLOR

        pygame.draw.rect(screen, back_button_color, back_button)
        back_label = rules_font.render("Back to Menu", True, (255, 255, 255))
        screen.blit(back_label, (WIDTH // 2 - back_label.get_width() // 2, HEIGHT - 80))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_rules = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    button_click_sound.play()
                    run_rules = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    button_click_sound.play()
                    run_rules = False


def restart_menu(winner=None):
    restart_font = pygame.font.SysFont("comicsansms", 40)
    winner_font = pygame.font.SysFont("comicsansms", 90)
    button_width = 200
    button_height = 80
    run_restart_menu = True

    while run_restart_menu:
        screen.fill(BACKGROUND_COLOR)

        if winner:
            winner_label = winner_font.render(f"{winner} wins!", 1,PIECE_1_COLOR if winner == 'Player 1' else PIECE_2_COLOR)
            screen.blit(winner_label, (WIDTH / 2 - winner_label.get_width() / 2, HEIGHT / 4))

        restart_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - button_height // 2, button_width, button_height)
        quit_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 1.4 - button_height // 2, button_width, button_height)

        pygame.draw.rect(screen, PIECE_1_COLOR, restart_button)
        pygame.draw.rect(screen, PIECE_1_COLOR, quit_button)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if restart_button.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(screen, PIECE_2_COLOR, restart_button)
            if pygame.mouse.get_pressed()[0]:
                start_click_sound.play()
                run_restart_menu = False
                return True

        if quit_button.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(screen, PIECE_2_COLOR, quit_button)
            if pygame.mouse.get_pressed()[0]:
                button_click_sound.play()
                pygame.quit()
                quit()

        restart_label = restart_font.render("Restart", True, (255, 255, 255))
        screen.blit(restart_label, (WIDTH // 2 - restart_label.get_width() // 2, HEIGHT // 2 - restart_label.get_height() // 2))

        quit_label = restart_font.render("Quit", True, (255, 255, 255))
        screen.blit(quit_label, (WIDTH // 2 - quit_label.get_width() // 2, HEIGHT // 1.4 - quit_label.get_height() // 2))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_restart_menu = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    run_restart_menu = False
                    return True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
    return False


def remove_pieces(board):
    columns = random.sample(range(COLUMN_COUNT), 2)

    pieces_removed = []
    for col in columns:
        for r in range(ROW_COUNT):
            if board[r][col] != 0:
                piece_color = PIECE_1_COLOR if board[r][col] == 1 else PIECE_2_COLOR
                pieces_removed.append(piece_color)
                board[r][col] = 0
                break

    for color in pieces_removed:
        if color == PIECE_1_COLOR:
            print("Red piece removed")
        elif color == PIECE_2_COLOR:
            print("Yellow piece removed")

    return len(pieces_removed)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Connect 4')
clock = pygame.time.Clock()

start_menu()
board = create_board()
game_over = False
turn = 0

draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("comicsansms", 75)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            break

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BACKGROUND_COLOR, (0, SQUARE_SIZE, WIDTH, SQUARE_SIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, PIECE_1_COLOR, (posx, int(SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
            else:
                pygame.draw.circle(screen, PIECE_2_COLOR, (posx, int(SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BACKGROUND_COLOR, (0, SQUARE_SIZE, WIDTH, SQUARE_SIZE))
            if turn == 0:
                posx = event.pos[0]
                col = int(posx / SQUARE_SIZE)

                if is_valid_location(board, col):
                    drop_piece(board, col, turn + 1)
                    pygame.time.delay(100)

                    if winning_move(board, 1):
                        victory_click_sound.play()
                        label = myfont.render("Player 1 wins!!", 1, PIECE_1_COLOR)
                        screen.blit(label, (100, SQUARE_SIZE + 10))
                        game_over = True
                    else:
                        if random.random() < 0.10:
                            pieces_removed = remove_pieces(board)


            else:
                posx = event.pos[0]
                col = int(posx / SQUARE_SIZE)

                if is_valid_location(board, col):
                    drop_piece(board, col, turn + 1)
                    pygame.time.delay(100)

                    if winning_move(board, 2):
                        victory_click_sound.play()
                        label = myfont.render("Player 2 wins!!", 1, PIECE_2_COLOR)
                        screen.blit(label, (100, SQUARE_SIZE + 10))
                        game_over = True
                    else:
                        if random.random() < 0.10:
                            pieces_removed = remove_pieces(board)

            draw_board(board)
            turn += 1
            turn %= 2

        if game_over:
            pygame.time.wait(750)
            winner_text = None
            if turn == 1:
                winner_text = "Player 1"
            else:
                winner_text = "Player 2"

            if restart_menu(winner_text):
                board = create_board()
                game_over = False

                turn = 0
                draw_board(board)
            else:
                break

        clock.tick(FPS)

pygame.quit()