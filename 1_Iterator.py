class FlatIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.current_list = []
        self.cursor = -1
        self.list_cursor = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor >= len(self.current_list):
            if self.list_cursor >= len(self.nested_list):
                raise StopIteration
            self.current_list = self.nested_list[self.list_cursor]
            self.list_cursor += 1
            self.cursor = 0
        return self.current_list[self.cursor]


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)  # ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()