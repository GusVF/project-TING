from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


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


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
