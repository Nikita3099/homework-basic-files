file_paths = {
    "1.txt": "C:/Users/porhu/YandexDisk/Netology/homework-basic-files/sorted/1.txt",
    "2.txt": "C:/Users/porhu/YandexDisk/Netology/homework-basic-files/sorted/2.txt",
}

file_contents = {}
file_line_counts = {}

for file_name, file_path in file_paths.items():
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        # Считаем только непустые строки
        non_empty_lines = [line for line in lines if line.strip() != ""]
        file_contents[file_name] = lines
        file_line_counts[file_name] = len(non_empty_lines)

sorted_files = sorted(file_line_counts.items(), key=lambda item: item[1])

result_content = []

for file_name, line_count in sorted_files:
    if line_count > 0:

        result_content.append(f"{file_name}\n")
        result_content.append(f"{line_count}\n")
        result_content.extend(file_contents[file_name])
        result_content.append("\n")  # Добавление пустой строки для разделения файлов

result_file_path = "C:/Users/porhu/YandexDisk/Netology/homework-basic-files/sorted/3.txt"

with open(result_file_path, 'w', encoding='utf-8') as result_file:
    result_file.writelines(result_content)

print(f"Результирующий файл создан: {result_file_path}")
