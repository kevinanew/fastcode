import os


def add_python_code(file_path, code):
    print(f'path: {file_path}')
    print(code)
    code_file_path = os.path.join(os.getcwd(), file_path)
    print('Open', code_file_path)
    if not os.path.exists(code_file_path):
        print('Write code')
        open(code_file_path, 'w').close()

    content = open(code_file_path, 'r').read()
    if code in content:
        return

    with open(code_file_path, 'a') as code_file:
        print('Append code')
        code_file.write(f'\n\n{code}')
