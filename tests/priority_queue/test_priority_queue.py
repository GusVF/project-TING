import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    priority_queue.enqueue({"qtd_linhas": 1})
    priority_queue.enqueue({"qtd_linhas": 9})
    priority_queue.enqueue({"qtd_linhas": 2})
    priority_queue.enqueue({"qtd_linhas": 7})

    assert len(priority_queue) == 4
    assert priority_queue.search(1) == {"qtd_linhas": 2}

    given = priority_queue.dequeue()
    assert len(priority_queue) == 3
    assert given == ({"qtd_linhas": 1})

    given_1 = priority_queue.dequeue()
    assert len(priority_queue) == 2
    assert given_1 == ({"qtd_linhas": 2})
    with pytest.raises(IndexError):
        priority_queue.search(10)
