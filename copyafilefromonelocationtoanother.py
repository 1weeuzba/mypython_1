import shutil
a=""
with open("C:\\Users\\AL\\Desktop\\random_text_files\\text2.txt","w") as file:
    file.write(a)
a = input("Do you want to copy the files of text.txt to text2.txt?(yes/no)")
if a.upper() == "YES":
    shutil.copy("C:\\Users\\AL\\Desktop\\random_text_files\\text.txt","C:\\Users\\AL\\Desktop\\random_text_files\\text2.txt")
elif a.upper()=="NO":
    print("Copying files cancelled")
elif a.upper()!="YES" or "NO":
    print("Please give a valid answer")