import os
source = "C:\\Users\\AL\\Desktop\\random\\text.txt"
if os.path.exists(source):
    if os.path.isfile(source):
        os.remove(source)
        print("File successfully removed")
    elif os.path.isdir(source):
        os.rmdir(source)
        print("Directory removed successfully")
else:
    print("File doesnot exist")
