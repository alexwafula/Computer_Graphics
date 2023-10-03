

from googleapiclient.discovery import build
from google.oauth2 import service_account
```

## Python3 Development Environment

The dataset used in the project can be downloaded here (https://amazon-massive-nlu-dataset.s3.amazonaws.com/amazon-massive-dataset-1.1.tar.gz).

It sets a variable `pivoit_lang` to the path of a JSONL file named 'en-US.jsonl' within a 'data' directory. It lists all the files in the 'data' directory and stores the list in the `list_of_files` variable. It reads data from 'sw-KE.jsonl' (Swahili data) and 'en-US.jsonl' (English data) JSONL files into Pandas DataFrames. It creates a new DataFrame `en_sw` by selecting columns from the English and Swahili DataFrames.


## Working with Files	

This part of the code processes data for three languages: English (en), Swahili (sw), and German (de), creating separate JSONL files for test, train, and dev sets for each language.

For each language:

- It reads data from the respective JSONL file into a Pandas DataFrame.
- It filters data based on the 'partition' column to create separate DataFrames for test, train, and dev sets.
- It writes these filtered DataFrames to separate JSON files in the 'generated_files' directory.

After processing these languages, the code generates one large JSON file (`large_json_file`) that contains translations from English to other languages for the train sets.
Finally, it writes the `large_json_file` to a JSON file named 'large_json_file.json' in the 'generated_files' directory.

## Uploading Files to Google
The code defines a dictionary `access_cred` containing Google Drive access credentials and creates a list `api_url` with the Google Drive API URL. It also sets the `service_account_file` and `parent_folder_id` variables.

Two functions are defined:
- `auth()`: This function authenticates the user using Google service account credentials.
- `upload(file_path)`: This function uploads a file specified by `file_path` to Google Drive.

The code then uses these functions to upload files to Google Drive.
It lists all files in the 'generated_files' directory and attempts to upload each file to Google Drive, except for 'de_train.json,' which has an issue causing it to fail to upload. It also prints an error message for any failed uploads.

### Important notes
- `utt`: the raw utterance text without annotations.
- `annot_utt`: the text from `utt` with slot annotations formatted as `[{label} : {entity}]`
- `partition`: is either `train`, `dev`, or `test`
