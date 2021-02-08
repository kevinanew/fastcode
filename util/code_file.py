import os


def add_python_code(file_path, code):
    print(f'path: {file_path}')
    print(code)
    code_file_path = os.path.join(os.getcwd(), file_path)
    assert os.path.exists(code_file_path)

    content = open(code_file_path, 'r').read()
    if code in content:
        return

    with open(code_file_path, 'a') as code_file:
        code_file.write(f'\n\n{code}')
