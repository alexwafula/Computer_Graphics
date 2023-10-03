import os
import pandas as pd
import json

class Generator:

    def new_wonderful_function():
        list_of_files = os.listdir('data')
        english_data = pd.read_json('data//en-US.jsonl', lines=True)
        for file_name in list_of_files:
            language = file_name.split('.')[0]
            if language != 'en-US':
                path = str('data//' + file_name)
                data_frame = pd.read_json(path, lines=True)
                ##New Data
                en_sw_dic = {
                    'id': english_data.id,
                    'utt': english_data['utt'],
                    'annot_utt': data_frame['utt']

                }
                en_xx = pd.DataFrame(en_sw_dic)
                xx=language.split('-')[0]
                if os.path.isdir('generated_files//excel'):
                    en_xx.to_excel('generated_files//excel//en-'+xx+'.xlsx')
                else:
                    os.path.isdir('generated_files//excel')
                    en_xx.to_excel('generated_files//excel//en-'+xx+'.xlsx')


    def filter_separate(path,files):
        for file in files:
            lang_data=pd.read_json(path+file,lines=True)

            lang_test=lang_data[lang_data['partition']=='test']
            lang_train=lang_data[lang_data['partition']=='train']
            lang_dev=lang_data[lang_data['partition']=='dev']

            if os.path.isdir('generated_files'):
                lang_name=file.split('.')[0].split('-')[0]
                file=open('generated_files//'+lang_name+'_test.jsonl', 'w')
                file.write(lang_test.to_json(orient='records',lines=True))
                file.close()

                file=open('generated_files//'+lang_name+'_train.jsonl', 'w')
                file.write(lang_train.to_json(orient='records',lines=True))
                file.close()

                file=open('generated_files//'+lang_name+'_dev.jsonl', 'w')
                file.write(lang_dev.to_json(orient='records',lines=True))
                file.close()

    def pretty_print_approach1(data):
        json_str = json.dumps(data, indent=4)
        print(json_str)
    

    


            



