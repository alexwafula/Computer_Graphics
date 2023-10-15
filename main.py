
import os
import pandas as pd

#Google drive package
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload
import mimetypes
import subprocess as sp
from classes.Functions import Functions

#Running the shell script
os.popen('run.sh')
# process= sp.run( 'run.sh', shell=True)
# print(process.returncode)
# if(int(process.returncode)==0):
#     print('Shell script run successfully')
# else:
#     print('Shell script failed')


#Using English as the pivoit language
Functions.filter_separate('data//',['en-US.jsonl','de-DE.jsonl','sw-KE.jsonl'])


#Generating the large json file 
large_json_file={}
#Prepear the dictionary
english_data=pd.read_json('data//en-US.jsonl',lines=True)
filtered_eng_data=english_data[english_data['partition']=='train']
for i in filtered_eng_data.index:
    translation=filtered_eng_data.loc[i,'utt']
    lang_dic={
        'id':i,
        'eng': str(translation),
        'translation':{}
    }
    large_json_file[i]=lang_dic

list_of_files=os.listdir('data')
for file_name in list_of_files:
    language=file_name.split('.')[0]
    if language!='en-US':
        path=str('data//'+file_name)
        data_frame=pd.read_json(path,lines=True)
        filtered_data=data_frame[data_frame['partition']=='train']
        for i in filtered_data.index:
            translation=filtered_data.loc[i,'utt']
            large_json_file[i]['translation'][language]=str(translation)
            

#pretty printing the file
Functions.pretty_print_approach1(large_json_file[7])


#Uploading Files to google drive
api_url=['https://www.googleapis.com/auth/drive']
service_account_file='keys.json'
parent_folder_id='15hQAbzVfDTgCB3-rXOW7DAVNFiyA4ENL'

def auth():
    creds=service_account.Credentials.from_service_account_file(service_account_file)
    return creds

def upload(path):
    creds=auth()
    service=build('drive','v3',credentials=creds)
    filename=path.split('.')[0]
    mime_type, _ = mimetypes.guess_type(path)
    file_metadata= {
        'name':filename,
        'parents':[parent_folder_id]
    }
    # Create a media object for the file
    media = MediaFileUpload(path, mimetype=mime_type)
    file=service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

#All files in directory
files=os.listdir('.//generated_files')
for file in files:
    try:
        upload('generated_files//'+file)
    except:
        print('Uploading file:'+(file)+' failed')

