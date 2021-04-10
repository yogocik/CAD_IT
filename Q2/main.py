import re
import camelot
import pandas as pd
import os
import sys


def convert_object()->object:
    filename = input(f"Filename with extension : ")
    data_dir = input(f"Data directory which file reside : ")
    save_dir = input(f"Save directory which file would be saved : ") 
    if data_dir is None or data_dir == '':
        data_dir = os.getcwd()
        print(f'Data directory has been changed automatically to {data_dir}') 
    try:
        tables = camelot.read_pdf(os.path.join(data_dir,filename),pages='all')
    except:
        sys.exit('File is not found or failed to be parsed')
    i = 0
    data_dict = {'Description':[],'Possible_root_cause':[],'Pages':[]}
    while True:
        try:
            tables[i].parsing_report
            data = tables[i].df.T
            data.columns = data.iloc[0]
            unused_column = data.columns.values[0]
            data = data[1:].drop(unused_column,axis=1).reset_index(drop=True)
            match = re.split(r"([0-9]+)", data[data.columns[1]].values[0].rstrip(''))
            i += 1
            if match:
                for word_elem in match:
                    if len(word_elem) > 5:
                        word = max(re.split(r"\.", word_elem.rstrip(' ')),key=len)
                        data_dict['Description'].append(data[data.columns[0]].values[0])
                        data_dict['Possible_root_cause'].append(word)
                        data_dict['Pages'].append(i)   
        except:
            print(f'Pages {i} is not defined')
            sys.exit('Force Exit!')
        finally:
            print('Reload Finished!')
    data_convert = pd.DataFrame.from_dict(data_dict)
    if save_dir == '' or save_dir is None:
        save_dir = data_dir
    data_convert.to_csv(os.path.join(save_dir,'my_convert.csv'))

convert_object()