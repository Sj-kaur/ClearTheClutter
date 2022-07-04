from email.mime import image
import os


def createIfNotExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(foldername , files):
    for file in files:
        os.replace(file , f"{foldername}/{file}")

if __name__ == "__main__":
    files = os.listdir()
    files.remove("main.py")
    # print(files)

    createIfNotExists("images")
    createIfNotExists("Docs")
    createIfNotExists("others")


    imgExts = [".jpeg",".jpg" , ".png"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

    docExts = [".txt" , ".pdf" , ".docx" , "doc"]
    Docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in imgExts) and (ext not in docExts) and os.path.isfile(file):
                others.append(file)

    move("Images",images)
    move("Docs" , Docs)
    move("Others" , others)
