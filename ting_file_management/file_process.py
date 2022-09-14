from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in instance._data:
        if i["nome_do_arquivo"] == path_file:
            return
    f = txt_importer(path_file)
    file_payload = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(f),
        "linhas do arquivo": f
    }
    instance.enqueue(file_payload)
    print(file_payload)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
