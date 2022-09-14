import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in instance._data:
        if i["nome_do_arquivo"] == path_file:
            return
    f = txt_importer(path_file)
    file_payload = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(f),
        "linhas_do_arquivo": f
    }
    instance.enqueue(file_payload)
    print(file_payload, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
    else:
        f = instance.dequeue()
        deleted = f["nome_do_arquivo"]
        print(f"Arquivo {deleted} removido com sucesso")


def file_metadata(instance, position):
    if len(instance._data) < position:
        print("Posição inválida", file=sys.stderr)
    else:
        file = instance.search(position)
        print(file, file=sys.stdout)
