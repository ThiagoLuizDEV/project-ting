def exists_word(word, instance):
    words = []
    for i in range(len(instance)):
        file_name = instance.search(i)["nome_do_arquivo"]
        lines = instance.search(i)["linhas_do_arquivo"]
        occurrences = []

    for index, line in enumerate(lines):
        if word.lower() in line.lower():
            occurrence = {"linha": index + 1}
            occurrences.append(occurrence)

    if len(occurrences) > 0:
        word_info = {
            "palavra": word,
            "arquivo": file_name,
            "ocorrencias": occurrences
        }
        words.append(word_info)

    return words


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
