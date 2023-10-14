from os import listdir, path


def traverse_dir(current_path, files_extensions_local):
    for file_local in listdir(current_path):
        if path.isdir(path.join(current_path, file_local)):
            traverse_dir(path.join(current_path, file_local), files_extensions_local)
        else:
            extension_local = file_local.split('.')[-1]
            if extension_local not in files_extensions_local:
                files_extensions_local[extension_local] = []
            files_extensions_local[extension_local].append(file_local)


files_extensions = {}
traverse_dir('.', files_extensions)

for extension, file in sorted(files_extensions.items(), key=lambda x: x[0]):
    report = open('report.txt', 'a')
    report.write(f'.{extension}\n')
    print(f'.{extension}')
    for file_ in sorted(file):
        report.write(f'--- {file_}\n')
        print(f'--- {file_}')
    report.close()
