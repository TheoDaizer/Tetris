class Field:
    """Class represents playing field.

    Args:
            width: playing field width
            height: playing field height
    """

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.nodes = [[None for _ in range(width)] for _ in range(height)]
        self.rows_counter = [0] * height

    def update(self, shape, color):
        for pt in shape:
            x, y = int(pt.x), int(pt.y)

            self.nodes[y][x] = color
            self.rows_counter[y] += 1

        return self.check_row()

    def check_row(self) -> list:
        burned_rows = []
        for row_n in range(self.height):
            if self.rows_counter[row_n] == self.width:
                burned_rows.append(row_n)
                self.rows_counter[row_n] = 0
                self.remove_row(row_n)
        return burned_rows

    def remove_row(self, row_n: int):
        self.clean_row(row_n)
        clean_row = self.nodes.pop(row_n)
        self.nodes = [clean_row] + self.nodes

        self.rows_counter.pop(row_n)
        self.rows_counter = [0] + self.rows_counter

    def clean_row(self, row_n: int):
        for i in range(self.width):
            self.nodes[row_n][i] = None
