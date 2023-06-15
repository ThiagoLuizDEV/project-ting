import sys
from .file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)
    dictionary = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }
    for i in range(len(instance)):
        result = instance.search(i)
        if result == dictionary:
            return None
    instance.enqueue(dictionary)
    print(dictionary, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
