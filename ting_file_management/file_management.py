import sys

def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        print('Formato inválido', file=sys.stderr)
    

    try:
        file = []
        with open(path_file, 'r') as f:
            file = f.read().split("\n")
            return file
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)