import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if ".txt" not in path_file:
        print('Formato inválido', file=sys.stderr)
    try:
        with open(path_file) as file:
            return file.read().split('\n')
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
