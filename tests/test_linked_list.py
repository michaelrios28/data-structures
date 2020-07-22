from data_structures.linked_list import SinglyLinkedList
import pytest


@pytest.fixture
def ll():
    ll = SinglyLinkedList()
    ll.addLast(1)
    ll.addLast(2)
    ll.addLast(3)
    return ll


def test_linked_list_size(ll):
    assert ll.size() == 3


def test_linked_list_indexOf(ll):
    assert ll.indexOf(2) == 1
