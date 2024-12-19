import pygame
import random

# Inisialisasi Pygame
pygame.init() #pygame.init() itu seperti tombol "mulai" untuk game atau aplikasi yang kita buat dengan Pygame.

# Ukuran layar
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tetris')

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)

COLORS = [CYAN, YELLOW, GREEN, RED, PURPLE, ORANGE, BLUE]

# Ukuran blok
BLOCK_SIZE = 30

# Bentuk blok Tetris
SHAPES = [   #SHAPES adalah daftar yang berisi bentuk-bentuk blok yang digunakan dalam game Tetris.
    [[1, 1, 1], [0, 1, 0]],  # T shape
    [[1, 1, 1, 1]],          # I shape
    [[1, 1], [1, 1]],        # O shape
    [[1, 1, 0], [0, 1, 1]],  # S shape
    [[0, 1, 1], [1, 1, 0]],  # Z shape
    [[1, 0, 0], [1, 1, 1]],  # L shape
    [[0, 0, 1], [1, 1, 1]]   # J shape
]

# Fungsi untuk memeriksa apakah blok valid di posisi tertentu
def valid_position(board, shape, offset):  #Secara keseluruhan, fungsi ini digunakan untuk memeriksa apakah sebuah bentuk bisa diposisikan di papan tanpa menabrak batas atau bentuk lainnya.
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                try:
                    if off_x + x < 0 or off_x + x >= len(board[0]) or off_y + y >= len(board):
                        return False
                    if board[off_y + y][off_x + x]:
                        return False
                except IndexError:
                    return False
    return True

# Fungsi untuk menambahkan bentuk ke papan
def place_shape(board, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                board[off_y + y][off_x + x] = cell

# Fungsi untuk menghapus baris yang sudah penuh
def clear_lines(board):
    new_board = [row for row in board if any(cell == 0 for cell in row)]
    new_board = [[0] * len(board[0])] * (len(board) - len(new_board)) + new_board
    return new_board

# Fungsi untuk menggambar papan dan bentuk
def draw_board(board, falling_shape, offset):
    SCREEN.fill(WHITE)
    
    # Gambar papan
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(SCREEN, COLORS[cell - 1], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    
    # Gambar bentuk yang sedang jatuh
    off_x, off_y = offset
    for y, row in enumerate(falling_shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(SCREEN, COLORS[cell - 1], ((off_x + x) * BLOCK_SIZE, (off_y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    pygame.display.update()

# Fungsi utama untuk menjalankan game
def main():
    # Ukuran papan 10x20
    board = [[0] * 10 for _ in range(20)]
    clock = pygame.time.Clock()
    
    game_over = False
    falling_shape = random.choice(SHAPES)
    shape_x = len(board[0]) // 2 - len(falling_shape[0]) // 2
    shape_y = 0
    speed = 4  # Kecepatan jatuh
    
    while not game_over:
        clock.tick(speed)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if valid_position(board, falling_shape, (shape_x - 1, shape_y)):
                        shape_x -= 1
                if event.key == pygame.K_RIGHT:
                    if valid_position(board, falling_shape, (shape_x + 1, shape_y)):
                        shape_x += 1
                if event.key == pygame.K_DOWN:
                    if valid_position(board, falling_shape, (shape_x, shape_y + 1)):
                        shape_y += 1
                if event.key == pygame.K_UP:
                    rotated_shape = list(zip(*falling_shape[::-1]))
                    if valid_position(board, rotated_shape, (shape_x, shape_y)):
                        falling_shape = rotated_shape
        
        # Jatuhkan bentuk
        if valid_position(board, falling_shape, (shape_x, shape_y + 1)):
            shape_y += 1
        else:
            place_shape(board, falling_shape, (shape_x, shape_y))
            board = clear_lines(board)
            falling_shape = random.choice(SHAPES)
            shape_x = len(board[0]) // 2 - len(falling_shape[0]) // 2
            shape_y = 0
            if not valid_position(board, falling_shape, (shape_x, shape_y)):
                game_over = True
        
        draw_board(board, falling_shape, (shape_x, shape_y))
    
    pygame.quit()

# Menjalankan game
if __name__ == "__main__":
    main()

