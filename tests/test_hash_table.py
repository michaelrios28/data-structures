from data_structures.hash_table import HashTable
import pytest


@pytest.fixture
def ht():
    ht = HashTable(size=5)
    ht.put('a', 1)
    ht.put('b', 2)
    ht.put('c', 3)
    return ht


def test_hash_table_init(ht):
    assert len(ht._array) == 5


def test_hash_table_get(ht):
    val = ht.get('a')
    assert val == 1


@pytest.mark.parametrize("test_input, expected",
                         [
                             ('a', ['a', 1]),
                             ('b', ['b', 2]),
                             ('c', ['c', 3]),
                             ('d', None)
                         ])
def test_hash_table__get_node(ht, test_input, expected):
    assert ht._get_node(test_input) == expected


def test_hash_table_put(ht):
    ht.put('d', 4)
    k, v = ht._get_node('d')
    assert k == 'd'
    assert v == 4
