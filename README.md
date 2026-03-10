# AWS S3 Cloud Backup Script

Python script that automatically compresses a local folder and uploads it to an AWS S3 bucket. Built as a personal infrastructure project to practice cloud integration and automation.

---

## What it does

1. Compresses a target directory into a timestamped `.zip` archive
2. Uploads it to an S3 bucket using the `boto3` SDK
3. Logs every operation (success or error) to a `backup.log` file
4. Deletes the local archive after a successful upload
5. Can be scheduled to run automatically (Task Scheduler on Windows, cron on Linux/Mac)

---

## Prerequisites

- Python 3.8+
- An AWS account with an S3 bucket created
- An IAM user with `AmazonS3FullAccess` permissions and an access key generated

---

## Installation

**1. Clone the repository:**
```bash
git clone https://github.com/4nath0s/aws-cloud-backup-script.git
cd aws-cloud-backup-script
```

**2. (Optional) Create a virtual environment:**

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file at the root of the project with the following variables:

```env
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
AWS_REGION=eu-west-3
AWS_BUCKET_NAME=your-bucket-name
DOSSIER_A_SAUVEGARDER=/absolute/path/to/folder
```

Where to find these values:
- Access key → AWS Console > IAM > Users > Security credentials > Create access key
- Region → chosen when creating the S3 bucket (ex: `eu-west-3` for Paris)
- Bucket name → AWS Console > S3

> ⚠️ The `.env` file is listed in `.gitignore` and will never be pushed to GitHub.

---

## Usage

```bash
python backup.py
```

Execution is logged in `backup.log` at the root of the project:

```
2026-03-10 02:00:03,883 - INFO - global variables loaded successfully
2026-03-10 02:00:03,886 - INFO - zip file created
2026-03-10 02:00:05,072 - INFO - connection established to aws
2026-03-10 02:00:07,000 - INFO - file loaded successfully
2026-03-10 02:00:07,001 - INFO - zip file deleted successfully
```

---

## Automation

### Windows — Task Scheduler

1. Open Task Scheduler as Administrator
2. Create a new task, check "Run with highest privileges"
3. Triggers tab → set frequency (e.g. daily at 2:00 AM)
4. Actions tab → configure:
   - Program: full path to `python.exe` (run `where python` to find it)
   - Arguments: `backup.py`
   - Start in: full path to the project folder

### macOS / Linux — Cron

```bash
crontab -e
```

Add this line to run every day at 2:00 AM:
```bash
0 2 * * * /path/to/python /path/to/backup.py
```

---

## Project Structure

```
aws-cloud-backup-script/
├── backup.py               # Main script
├── .env                    # Credentials
├── .gitignore              
├── requirements.txt        
├── backup.log              # Generated at runtime
└── README.md               
```
