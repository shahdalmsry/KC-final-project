import os
import shutil

current_dir = input("enter the folder path")

print('Welcome in organize.py script - happy clean folder')
# input("name the files")
for filename in os.listdir(current_dir):
    print(filename)
    # organize images into Images folder
    if filename.endswith((".png", "jpg", "jpeg", "gif")):
        if not os.path.exists("Images"):
            os.mkdir('Images')
        shutil.copy(filename, "Images")
        os.remove(filename)
        print('Images Done')

    # organize code files into Codes folder
    elif filename.endswith((".py", "css", "html", "js", "bash")):
        if not os.path.exists("Codes"):
            os.mkdir('Codes')
        shutil.copy(filename, "Codes")
        os.remove(filename)
        print('Code Done')

    # organize video into Videos folder
    elif filename.endswith((".mp4", "webm")):
        if not os.path.exists("Videos"):
            os.mkdir('Videos')
        shutil.copy(filename, "Videos")
        os.remove(filename)
        print('Video Done')

    # organize Docs into Documentes folder
    elif filename.endswith((".pdf", ".word")):
        if not os.path.exists("Docs"):
            os.mkdir('Docs')
        shutil.copy(filename, "Docs")
        os.remove(filename)
        print('Docs Done')

    # organize arhive into archives folder
    elif filename.endswith((".zip", ".rar", "tar ")):
        if not os.path.exists("Archives"):
            os.mkdir('Archives')
        shutil.copy(filename, "Archives")
        os.remove(filename)
        print('Archives Done')

    # organize apps into Apps folder
    elif filename.endswith((".dmg", "exe")):
        if not os.path.exists("Apps"):
            os.mkdir("Apps")
        shutil.copy(filename, "Apps")
        os.remove(filename)
        print('Apps Done')

print('Done Organizing This Folder')