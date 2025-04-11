import time
import os

CANVAS_WIDTH = 10  # Number of columns
CANVAS_HEIGHT = 10  # Number of rows
ERASER_SIZE = 1  # Size of eraser

# Initialize the canvas with blue cells
canvas = [['🟪' for _ in range(CANVAS_WIDTH)] for _ in range(CANVAS_HEIGHT)]

def print_canvas():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    for row in canvas:
        print(''.join(row))
    print("\nMove the eraser using W/A/S/D. Press Q to quit.")

def erase(x, y):
    for i in range(max(0, y), min(CANVAS_HEIGHT, y + ERASER_SIZE)):
        for j in range(max(0, x), min(CANVAS_WIDTH, x + ERASER_SIZE)):
            canvas[i][j] = '⬛'

def main():
    eraser_x, eraser_y = 0, 0  # Start position of eraser
    print_canvas()
    
    while True:
        command = input("Enter move (W/A/S/D to move, Q to quit): ").strip().lower()
        if command == 'q':
            break
        elif command == 'w' and eraser_y > 0:
            eraser_y -= 1
        elif command == 's' and eraser_y < CANVAS_HEIGHT - ERASER_SIZE:
            eraser_y += 1
        elif command == 'a' and eraser_x > 0:
            eraser_x -= 1
        elif command == 'd' and eraser_x < CANVAS_WIDTH - ERASER_SIZE:
            eraser_x += 1
        
        erase(eraser_x, eraser_y)
        print_canvas()
        time.sleep(0.1)

if __name__ == "__main__":
    main()