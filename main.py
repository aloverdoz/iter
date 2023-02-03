class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.item = []
        self.count = -1

    def __iter__(self):
        print('start')
        return self

    def __next__(self):
        if len(self.item) == 0:
            for i in self.list_of_list:
                self.item += i
            return self.item
        else:
            raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(FlatIterator(list_of_lists_1),['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):
        print(flat_iterator_item, check_item)
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()