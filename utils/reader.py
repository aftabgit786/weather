def read_files(file_path1, file_path2):
    file_values1 = []
    file_values2 = []

    with open(file_path1) as file_reader1:
        file_content1 = file_reader1.read()
        for row in file_content1.split("\n")[1:-1]:
            file_values1.append(row.split(","))
        file_reader1.close()

    with open(file_path2) as file_reader2:
        file_content2 = file_reader2.read()
        for row in file_content2.split("\n")[1:-1]:
            file_values2.append(row.split(","))
        file_reader2.close()

    return file_values1, file_values2

