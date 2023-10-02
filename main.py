
import os
import pandas as pd
import glob

from classes.generator_qn1 import Generator

#data_directory = 'data'
#jsonl_files = glob.glob(os.path.join(data_directory, '*.jsonl'))

#with pd.ExcelWriter('MASSIVE.xlsx', engine='xlsxwriter') as writer:
    # Iterate through each JSON Lines file, convert it to an Excel sheet, and save it
#   [pd.read_json(jsonl_file, lines=True).to_excel(writer, sheet_name=os.path.splitext(os.path.basename(jsonl_file))[0], index=False) for jsonl_file in jsonl_files]

# Save the Excel file
print("Excel file saved as 'MASSIVE.xlsx'")

#Generator.generate_language_columns('data//en-US.jsonl','data','file.xlsx')

Generator.new_wonderful_function('mi')


