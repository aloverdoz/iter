class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.count = -1
        self.item = []


    def __iter__(self):
        self.count = -1
        return self

    def __next__(self):
        try:
            if len(self.item) == 0:
                for i in self.list_of_list:
                    self.item += i
            self.count += 1
            return self.item[self.count]
        except:
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