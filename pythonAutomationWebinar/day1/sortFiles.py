import os
import shutil

target_directory = "pythonAutomationWebinar/files"

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Spreadsheets": [".xlsx", ".csv"]
}

def createDir():
    for folder in file_types.keys():
        folder_path = os.path.join(os.getcwd(), folder)
        if not os.path.exists(folder_path):
            os.mkdir(folder)


def organizeFiles():
    for file in os.listdir(target_directory):
        filePath = os.path.join(target_directory, file)
        if os.path.isfile(filePath):
            _, extension = os.path.splitext(file)
            moved = False
            
            for folder, extensions in file_types.items():
                if(extension.lower() in extensions):
                    shutil.move(filePath, os.path.join(target_directory, folder, file))
                    moved = True
                    
            if not moved:
                othersFolder = os.path.join(target_directory, "Others")
                if not os.path.exists(othersFolder):
                    os.mkdir(othersFolder)
                shutil.move(filePath, os.path.join(othersFolder, file))