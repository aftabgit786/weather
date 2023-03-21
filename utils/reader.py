def read_files(file_path):
    file_values = []
    with open(file_path) as file_reader:
        file_content = file_reader.read()
        for row in file_content.split("\n")[1:-1]:
            file_values.append(row.split(","))
        file_reader.close()

    return file_values
