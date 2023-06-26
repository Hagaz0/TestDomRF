import os

folder_path = 'S:/Files'
file_names = [filename for filename in os.listdir(folder_path) if 'УД' in filename]

print(file_names)
