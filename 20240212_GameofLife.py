#| Conway's Game of Life takes place on an infinite two-dimensional board of square cells.
#| Each cell is either dead or alive, and at each tick, the following rules apply:

#| Any live cell with less than two live neighbours dies.
#| Any live cell with two or three live neighbours remains living.
#| Any live cell with more than three live neighbours dies.
#| Any dead cell with exactly three live neighbours becomes a live cell.
#| A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

#| Implement Conway's Game of Life. It should be able to be initialized with a starting list
#| of live cell coordinates and the number of steps it should run for. Once initialized, it
#| should print out the board state at each step. Since it's an infinite board, print out
#| only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.

#| You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).

#------------------#
# Define Functions #
#------------------#

class GameOfLife:
    def __init__(self, initial_live_cells, steps):
        #| Convert the list of tuples into a set for faster lookup
        self.live_cells = set(initial_live_cells)
        self.steps = steps

    def get_neighbours(self, cell):
        #| Generate all eight neighbours for a given cell.
        x, y = cell
        return [(x-1, y-1), (x, y-1), (x+1, y-1),
                (x-1, y),             (x+1, y),
                (x-1, y+1), (x, y+1), (x+1, y+1)]

    def next_state(self):
        #| Compute the next state of the game.
        new_live_cells = set()
        #| Consider all cells that are either currently live or could potentially become live
        potential_cells = set(cell for live_cell in self.live_cells for cell in self.get_neighbours(live_cell)) | self.live_cells
        for cell in potential_cells:
            neighbours = self.get_neighbours(cell)
            live_neighbours = sum((neighbour in self.live_cells) for neighbour in neighbours)
            if live_neighbours == 3 or (live_neighbours == 2 and cell in self.live_cells):
                new_live_cells.add(cell)
        self.live_cells = new_live_cells

    def print_board(self):
    #| Print current state of the board
        if not self.live_cells:
            print("No live cells.")
            return
        min_x = min(x for x, _ in self.live_cells)
        max_x = max(x for x, _ in self.live_cells)
        min_y = min(y for _, y in self.live_cells)
        max_y = max(y for _, y in self.live_cells)
        for y in range(min_y, max_y + 1):
            print(''.join('*' if (x, y) in self.live_cells else '.' for x in range(min_x, max_x + 1)))

    def run(self):
    #| Run the game for a specified number of steps
        for step in range(self.steps):
            print(f"Step {step + 1}:")
            self.print_board()
            self.next_state()
            print()

if __name__ == "__main__":
    #| Example initialisation and run
    initial_live_cells = [(1, 2), (2, 2), (3, 2)]  # A simple initial pattern
    steps = 5
    game = GameOfLife(initial_live_cells, steps)
    game.run()
