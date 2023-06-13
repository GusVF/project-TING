from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if len(self._data) == 0:
            return None
        return self._data.pop(0)

    def search(self, index):
        if not 0 <= index < len(self._data):
            raise IndexError("Índice Inválido ou Inexistente")

        return self._data[index]


# if __name__ == "__main__":
#     queue = Queue()
# queue.enqueue(5)
# queue.enqueue(15)
# queue.enqueue(25)
# queue.enqueue(35)
# for n in queue._data:
#     print(n)
