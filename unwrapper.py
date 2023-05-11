import pandas as pd
import numpy as np
import sys # из инета для сохранки в ткст
import json

original_stdout = sys.stdout # из инета для сохранки в ткст

users = []
chats = []

msgU = {}
badU = {}

msgC = {}
badC = {}

#-------#
pd.options.display.max_rows = 200

with open('data.json', 'r') as save:
        rough = json.load(save) # массив -> массивы -> словари
        users = rough[0]
        chats = rough[1]

        msgU = users[0]
        badU = users[1]

        msgC = chats[0]
        badC = chats[1]
        

with open('stats.txt', 'w') as f:
    # Redirecting stdout to file
    sys.stdout = f

    #---------------users-----------
    def unwrapU(msgU, badU):
        names = []
        arr1 = np.empty((1,1))
        arr2 = np.empty((1,1))

        for key in msgU.keys():
            names.append(key)
            arr1 = np.append(arr1, msgU[key])
            try:
                arr2 = np.append(arr2, badU[key])
            except Exception:
                arr2 = np.append(arr2, 0)

        arr1 = arr1.astype(float) # fixing
        arr1 = arr1.astype(int)   #  bugs
        arr1 = arr1[arr1 != 0] # удаяю нули
        arr2 = arr2.astype(float) # fixing
        arr2 = arr2.astype(int)   # fixing
        arr2 = arr2[1:]           # удаяю нули

        dataU = {'id': names,
                'words': np.round(arr1+arr2),
                'amount of bad words': np.round(arr2),
                '%% of bad words': np.round(arr2/(arr1+arr2)*100)}

        
        dfU = pd.DataFrame(dataU)

        dfU = dfU.sort_values('words', ascending=False)
        dfU.to_csv (r'USERSdataKAIJU.csv', index= False )
        print("---------------users-----------")
        print(dfU)
        print('\n')
        print(dfU.describe())
        print("-------------------------------\n")
    #---------------users-----------
    
    #---------------chats-----------
    def unwrapC(msgC, badC):
        nick = []
        arr3 = np.empty((1,1))
        arr4 = np.empty((1,1))

        for key in msgC.keys():
            nick.append(f"<#{key}>")
            arr3 = np.append(arr3, msgC[key])
            try:
                arr4 = np.append(arr4, badC[key])
            except Exception:
                arr4 = np.append(arr4, 0)
        arr3 = arr3.astype(float) # fixing
        arr3 = arr3.astype(int)   #  bugs
        arr3 = arr3[arr3 != 0] # удаяю нули
        arr4 = arr4.astype(float) # fixing
        arr4 = arr4.astype(int)   # fixing
        arr4 = arr4[1:]  # удаяю нули

        dataC = {'id of chat': nick,
                'words': np.round(arr3+arr4),
                'amount of bad words': np.round(arr4),
                '%% of bad words': np.round(arr4/(arr3+arr4)*100)}

        dfC = pd.DataFrame(dataC)

        print(f"Amount of msg: {np.sum(arr3)+np.sum(arr4)}\n")
        print(f"Amount of msgs with bad words: {np.sum(arr4)}\n")

        dfC = dfC.sort_values('words', ascending=False)
        dfC.to_csv (r'CHATSdataKAIJU.csv', index= False )
        print("---------------chats-----------")
        print(dfC)
        print('\n')
        print(dfC.describe())
        print("-------------------------------\n")
    #---------------chats----------- 
    unwrapU(msgU, badU)
    unwrapC(msgC, badC)
    

    sys.stdout = original_stdout


    # (pd.concat([dfU, dfC], ignore_index=True) - объединить датафреймы)
    # (pd.fillna(0) = заменить пустоты на 0)