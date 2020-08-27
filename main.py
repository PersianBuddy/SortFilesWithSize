import os
# TODO: walk throgh all files in current directory
files_dictionary ={}
file_sizes = []
for root, dirs, files in os.walk(os.path.curdir):
    if '.git' in root:
        continue
    for file_name in files:
        file_path = os.path.join(root, file_name)
        file_size = os.path.getsize(file_path)
        file_sizes.append(file_size)
        files_dictionary[file_path] = file_size

# remove duplicates from list
unique_file_sizes = []
for file_size in file_sizes:
    if file_size not in unique_file_sizes:
        unique_file_sizes.append(file_size)
# sort file sizes
unique_file_sizes.sort(reverse=True)
sorted_file_result= "These are files sorted based on their size\n"

# sort files based on their sizes
for fils_size_in_list in unique_file_sizes:
    for file_path, file_size_in_dictionary in files_dictionary.items():
        if fils_size_in_list == file_size_in_dictionary:
            file_name = os.path.basename(file_path)
            sorted_file_result += f'File Name:\t{file_name}\tFile Size:\t{file_size_in_dictionary}\tFile Path:\t{os.path.abspath(file_path)}\n'

print(sorted_file_result)
