from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
import sys

queue_instance = Queue()
text_file = "statics/arquivo_teste.txt"


def process(path_file, instance):
    if instance.contains_file(path_file):
        print(f'Arquivo {path_file} já foi processado. Ignorado')
        return

    lines = txt_importer(path_file)

    file_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }

    instance.enqueue(file_data)
    print(file_data)


process(text_file, queue_instance)


def remove(instance=queue_instance):
    if instance.is_empty():
        print("Não há elementos")
        return

    if instance.contains_file(text_file):
        instance.dequeue()
        print(f'Arquivo {text_file} removido com sucesso')
        return


# result = remove(queue_instance)
# print(result)


def file_metadata(instance, position):
    try:
        file_data = instance.search(position)
        if file_data:
            print(file_data)
        else:
            sys.stderr.write('Posição inválida')
    except IndexError:
        sys.stderr.write('Posição inválida')


result1 = file_metadata(queue_instance, 0)
