import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        sys.stderr.write('Formato inválido\n')
        return []
    try:
        with open(path_file, 'r') as file:
            contents = file.read().split('\n')
        return contents
    except FileNotFoundError:
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
        return []


text_file = "statics/arquivo_teste.txt"
result = txt_importer(text_file)
print(result)
