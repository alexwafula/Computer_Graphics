import os
import pandas as pd
class Generator:

    def new_wonderful_function(mi):
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
                en_xx.to_excel('en-'+xx+'.xlsx')
