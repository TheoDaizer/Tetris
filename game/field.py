from .figures import SHAPES


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

    def update(self, x: int, y: int, shape_variant: int, orientation: int):
        for dx, dy in SHAPES[shape_variant][orientation]:
            node_x, node_y = x + dx, y + dy
            self.nodes[node_y][node_x] = shape_variant
            self.rows_counter[node_y] += 1

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
