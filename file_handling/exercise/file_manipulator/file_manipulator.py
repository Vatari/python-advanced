from os import path, remove

while True:
    user_entry = input()
    if user_entry == 'End':
        break

    user_entry = user_entry.split('-')
    file_name = user_entry[1]

    if 'Create' in user_entry:
        open(file_name, 'w').close()

    elif 'Add' in user_entry:
        file_content = user_entry[2]
        with open(file_name, 'a') as file:
            file.write(file_content + '\n')

    elif 'Replace' in user_entry:
        old_str, new_str = user_entry[2], user_entry[3]
        try:
            with open(file_name, 'r+') as file:
                new_content = file.read().replace(old_str, new_str)
                file.seek(0)
                file.truncate()
                file.write(new_content)
        except FileNotFoundError:
            print('An error occurred')

    elif 'Delete' in user_entry:
        if path.exists(file_name):
            remove(file_name)
        else:
            print('An error occurred')
