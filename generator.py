"""Please find as many bad practices in this code as possible"""
from typing import List


class Generator_example():
    def get_row(self, fileName):
        for row in open(fileName, "r"):
            yield row

    def infinite_sequence(self):
        num = 0
        while True:
            yield num
            num += 1

    def get_rows_numbered(self, fileName) -> List[tuple]:
        """ Please use infinite_sequence to output a list of tuples [(<row_id>, <row_content>)]"""
        gen = self.infinite_sequence()

        return [(next(gen), row) for row in self.get_row(fileName)]
