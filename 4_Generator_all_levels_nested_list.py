def flat_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flat_generator(item)
        else:
            yield item


nested_list = [
    ['a', ['b', 'c']],
    ['d', 'e', ['f', 'h'], False],
    [1, [2, None]],
]

for item in flat_generator(nested_list):
    print(item)
