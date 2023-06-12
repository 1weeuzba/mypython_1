import os
source = "C:\\Users\\AL\\Desktop\\random_text_files\\text.txt"
destination = "C:\\Users\\AL\\Desktop\\moved\\text.txt"
try:
    if os.path.exists(destination):
        print("File already exists")
    else:
        os.replace(source,destination)
        print("File moved")

except FileNotFoundError:
    print(source+" doesnot exist")
    