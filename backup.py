import os
import shutil
import datetime

def backup_creation(folder_localisation):
    if os.path.exists(folder_localisation):
        save_file = "save" + str(datetime.datetime.now())
        shutil.make_archive(save_file, "zip", folder_localisation)
    else:
        print("no folder located")
    
    