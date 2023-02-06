# File used to generate data from dataset. NOT TO BE USED (see worker.ipynb)

import json 
import pandas as pd 
import random 

CSV_FILE = 'SEntFiN-v1.1.csv'
df = pd.read_csv(CSV_FILE)
del df['S No.']
# df['Decisions'] = df['Decisions'].apply(json.loads)
# csv_data = df.to_dict(orient='list')
# print(csv_data)
# # print(df)

# Make things simple first 
# df = df.head(20)
# df = df.sample(n=10)

# The full dataframe 
df['Decisions'] = df['Decisions'].apply(json.loads)
csv_data = df.to_dict(orient='list')
# print(csv_data)

# Now, I need to change the data into this text format 
text = []
# print(csv_data['Decisions'])
get_decision = lambda x: '1' if x == 'positive' else '0' if x == 'neutral' else '-1'
for i in range(len(csv_data['Title'])):
    for key in csv_data['Decisions'][i]:
        text.append('\n'.join([csv_data['Title'][i].replace(key, '$T$'), key, get_decision(csv_data['Decisions'][i][key])]))
        # text.append(csv_data['Title'][i].replace(key, '$T$'))
        # text.append(key)
        # text.append(get_decision(csv_data['Decisions'][i][key]))


# How do I write/append random elements in text to a .raw file, and the remaining elements to another .raw file
random.shuffle(text)
training_text, test_text = text[:len(text)//5 * 4], text[len(text)//5 * 4:]

with open('finance_train.raw', 'w') as f:
    f.write('\n'.join(training_text))
    
with open('finance_test.raw', 'w') as f:
    f.write('\n'.join(test_text))

# Write the data 
with open('financedata.txt', 'w') as f:
    f.write('\n'.join(text))

print("All data written. Number of rows: " + str(len(text) * 3))

# What, do I add a new dir config and add the config.json there?? 
# From the docs: 
# Path = sgnlp/sgnlp/models/sentic_gcn/config/sentic_gcn_config.json
# Which means... what? 
# https://sgnlp.aisingapore.net/docs/model/senticgcn.html

# How do you get training and testing data 
# sample_df = df.sample(frac=0.2)
# remaining_df = df.drop(sample_df.index)

# Should I split into training, test sets (70-30), or training, cv, and test set (60-20-20)? 



# with open('SEntFiN-v1.1.csv', 'r') as f:
#     csv_data = f.read() 
    
# def transform_dict(attr_dict):
#     print(attr_dict)
#     attr_dict = attr_dict.replace('""', '"')
#     attr_dict = attr_dict.replace('"{', '{')
#     attr_dict = attr_dict.replace('}"', '}')
#     print(attr_dict)
#     return json.loads(attr_dict)

# # Learn how to use the csv module 
# csv_list_data = list(map(lambda x: x.split(','), csv_data.split('\n')))  # This won't work coz got other commas inside, need to find a way to split them accordingly 
# for i in range(1, len(csv_list_data)):
#     csv_list_data[i][2] = transform_dict(csv_list_data[i][2])
# print(csv_list_data)

"https://github.com/BinLiang-NLP/Sentic-GCN/blob/main/datasets/semeval14/laptop_train.raw"
# use json.loads to get the dict 

# Split into train-test set 
