import os


def scanning(file_path, level1=False):
    all_files_here = os.listdir(file_path)
    for file in all_files_here:
        f = os.path.join(file_path, file)

        if os.path.isfile(f):
            extension = f.split('.')[-1]
            if extension not in extensions:
                extensions[extension] = []
            extensions[extension].append(f'- - - {file}')
            continue

        elif not level1:
            scanning(f, level1=True)


extensions = {}
path = input()
scanning(path)
new_file = os.path.dirname(__file__)
new_file_path = os.path.join(new_file, 'report.txt')
with open(new_file_path, 'w') as rep:

    for ex in sorted(extensions):
        rep.write(f'.{ex}\n')
        for f in sorted(extensions[ex]):
            rep.write(f + '\n')
