from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def size(self):
        return len(self._data)

    def is_empty(self):
        return not self.size()

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

    def contains_file(self, path_file):
        for item in self._data:
            if item["nome_do_arquivo"] == path_file:
                return True
        return False
