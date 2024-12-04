import tkinter as tk
import random

# Configuración del tablero
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
CELL_SIZE = 30

# Colores para las piezas
COLORS = {
    'I': 'cyan',
    'O': 'yellow',
    'T': 'purple',
    'S': 'green',
    'Z': 'red',
    'J': 'blue',
    'L': 'orange'
}

# Formas de las piezas (Tetrominós)
PIECES = {
    'I': [[1, 1, 1, 1]],
    'O': [[1, 1], [1, 1]],
    'T': [[0, 1, 0], [1, 1, 1]],
    'S': [[0, 1, 1], [1, 1, 0]],
    'Z': [[1, 1, 0], [0, 1, 1]],
    'J': [[1, 0, 0], [1, 1, 1]],
    'L': [[0, 0, 1], [1, 1, 1]]
}

class Tetris:
    def __init__(self, root):
        self.root = root
        self.root.title("Tetris")

        # Crear canvas para el tablero
        self.canvas = tk.Canvas(root, width=BOARD_WIDTH * CELL_SIZE, height=BOARD_HEIGHT * CELL_SIZE, bg="black")
        self.canvas.pack()

        # Inicializar tablero y pieza actual
        self.board = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
        self.current_piece = None
        self.current_piece_coords = None
        self.game_over = False

        # Vincular eventos de teclado
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Up>", self.rotate)

        # Iniciar juego
        self.spawn_piece()
        self.update_game()

    def draw_board(self):
        """Dibuja el tablero y las piezas."""
        self.canvas.delete("all")

        # Dibujar tablero
        for row in range(BOARD_HEIGHT):
            for col in range(BOARD_WIDTH):
                if self.board[row][col]:
                    self.draw_cell(row, col, COLORS[self.board[row][col]])

        # Dibujar la pieza actual
        if self.current_piece:
            for row, col in self.current_piece_coords:
                self.draw_cell(row, col, COLORS[self.current_piece])

    def draw_cell(self, row, col, color):
        """Dibuja una celda en el tablero."""
        x1 = col * CELL_SIZE
        y1 = row * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

    def spawn_piece(self):
        """Genera una nueva pieza."""
        self.current_piece = random.choice(list(PIECES.keys()))
        self.current_piece_coords = self.get_piece_coords(self.current_piece, 0, BOARD_WIDTH // 2 - 1)

        # Si no hay espacio para la nueva pieza, el juego termina
        if not self.is_valid_position(self.current_piece_coords):
            self.game_over = True

    def get_piece_coords(self, piece, start_row, start_col):
        """Obtiene las coordenadas de una pieza."""
        coords = []
        for r, row in enumerate(PIECES[piece]):
            for c, cell in enumerate(row):
                if cell:
                    coords.append((start_row + r, start_col + c))
        return coords

    def is_valid_position(self, coords):
        """Verifica si las coordenadas son válidas."""
        for row, col in coords:
            if row < 0 or row >= BOARD_HEIGHT or col < 0 or col >= BOARD_WIDTH:
                return False
            if self.board[row][col]:
                return False
        return True

    def move_left(self, event):
        """Mueve la pieza a la izquierda."""
        if self.current_piece and not self.game_over:
            new_coords = [(row, col - 1) for row, col in self.current_piece_coords]
            if self.is_valid_position(new_coords):
                self.current_piece_coords = new_coords

    def move_right(self, event):
        """Mueve la pieza a la derecha."""
        if self.current_piece and not self.game_over:
            new_coords = [(row, col + 1) for row, col in self.current_piece_coords]
            if self.is_valid_position(new_coords):
                self.current_piece_coords = new_coords

    def move_down(self, event=None):
        """Mueve la pieza hacia abajo."""
        if self.current_piece and not self.game_over:
            new_coords = [(row + 1, col) for row, col in self.current_piece_coords]
            if self.is_valid_position(new_coords):
                self.current_piece_coords = new_coords
            else:
                self.lock_piece()
                self.clear_lines()
                self.spawn_piece()

    def rotate(self, event):
        """Rota la pieza actual."""
        if self.current_piece and not self.game_over:
            piece_shape = PIECES[self.current_piece]
            rotated_shape = list(zip(*piece_shape[::-1]))  # Rotar 90 grados
            start_row, start_col = self.current_piece_coords[0]
            new_coords = self.get_piece_coords_from_shape(rotated_shape, start_row, start_col)
            if self.is_valid_position(new_coords):
                self.current_piece_coords = new_coords

    def get_piece_coords_from_shape(self, shape, start_row, start_col):
        """Obtiene las coordenadas de una pieza a partir de su forma."""
        coords = []
        for r, row in enumerate(shape):
            for c, cell in enumerate(row):
                if cell:
                    coords.append((start_row + r, start_col + c))
        return coords

    def lock_piece(self):
        """Bloquea la pieza actual en el tablero."""
        for row, col in self.current_piece_coords:
            self.board[row][col] = self.current_piece
        self.current_piece = None

    def clear_lines(self):
        """Elimina las líneas completas del tablero."""
        new_board = [row for row in self.board if any(cell == 0 for cell in row)]
        lines_cleared = BOARD_HEIGHT - len(new_board)
        self.board = [[0] * BOARD_WIDTH for _ in range(lines_cleared)] + new_board

    def update_game(self):
        """Actualiza el juego en cada frame."""
        if not self.game_over:
            self.move_down()
            self.draw_board()
            self.root.after(500, self.update_game)
        else:
            self.canvas.create_text(
                BOARD_WIDTH * CELL_SIZE // 2, BOARD_HEIGHT * CELL_SIZE // 2,
                text="GAME OVER", fill="white", font=("Arial", 24)
            )

# Ejecutar el juego
root = tk.Tk()
game = Tetris(root)
root.mainloop()
