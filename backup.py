import os
import shutil
import datetime
import boto3
import dotenv
import logging

logging.basicConfig(filename='backup.log', level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

try :
    dotenv.load_dotenv()
    FOLDER_LOCATION = os.environ["DOSSIER_A_SAUVEGARDER"]
    AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
    AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
    AWS_REGION = os.environ["AWS_REGION"]
    AWS_BUCKET_NAME = os.environ["AWS_BUCKET_NAME"]
    logging.info("global variables loaded succesfully")
except:
    logging.exception("error loading global variables")
    exit(1)


def backup_creation(folder_localisation):
    if os.path.exists(folder_localisation):
        save_file = "save_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
        shutil.make_archive(save_file, "zip", folder_localisation)
        logging.info("zip file created")
        return os.path.realpath(save_file + ".zip")
    else:
        logging.error("no folder located")
        exit(1)

    
def upload_to_S3(zip_location):
    try :
        s3 = boto3.client("s3", aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_REGION)
        logging.info("connection established to aws")
    except:
        logging.exception("can't connect to aws")
        exit(1)
    try :
        s3.upload_file(zip_location, AWS_BUCKET_NAME, os.path.basename(zip_location))
        logging.info("file loaded succesfully")
    except:
        logging.exception("error while loading file")


if __name__ == "__main__":
    save_name = backup_creation(FOLDER_LOCATION)
    upload_to_S3(save_name)
    try:
        os.remove(save_name)
        logging.info("zip file deleted succesfully")
    except:
        logging.exception("zip file wasn't deleted succesfully")
    
    