"""Please find as many bad practices in this code as possible"""


class Generator_example():
    def get_row(self, fileName):
        yield ''

    def infinite_sequence(self):
        yield 0

    def get_rows_numbered(self, fileName):
        ''' Please use infinite_sequence to output a list of tuples [(<row_id>, <row_content>)]'''
        return []
