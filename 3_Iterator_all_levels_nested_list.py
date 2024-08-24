class FlatIterator:
    def __init__(self, nested_list):
        self.stack = [(nested_list, 0)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            current_list, index = self.stack[-1]
            if index >= len(current_list):
                self.stack.pop()
                continue
            item = current_list[index]
            self.stack[-1] = (current_list, index + 1)
            if isinstance(item, list):
                self.stack.append((item, 0))
            else:
                return item
        raise StopIteration


nested_list = [
    ['a', ['b', 'c']],
    ['d', 'e', ['f', 'h'], False],
    [1, [2, None]],
]

for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()