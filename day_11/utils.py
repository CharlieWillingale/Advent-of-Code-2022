def read_input(file_path: str) -> list:

    with open(file_path,'r') as f:

        input = f.readlines()

    return input