import pandas as pd

# from Gui import *
song_info = pd.read_csv(r'C:\Users\grove\Downloads\muse_v3.csv\muse_v3.csv', sep=',')

validSentiList, validSongList = [], []
for x in song_info.index:
    CSVsentiments = song_info['seeds'][x]
    CSVsentiments = eval(CSVsentiments)
    CSVset_sentiments = set(CSVsentiments)
    for y in CSVset_sentiments:
        validSentiList.append(y)
        validSongList.append(song_info['track'])

def main(line,n):   

    varUserSenti = []
    if line == '':
        return []
    else:
        varUserSenti.append(line)
        if len(varUserSenti) == 4:
            return []

    SentNotFound = False
    for z in varUserSenti:
        if z not in validSentiList:
            SentNotFound = True
            return []


        for k in varUserSenti:
            temp_list = []
            search = song_info[song_info['track'] ]
            for i in range(len(song_info['seeds'])):
                if k in song_info['seeds'][i]:
                    if len(temp_list) > 5:
                        break
                    temp_list.append([song_info['track'][i], song_info['artist'][i]])
            print(*temp_list, sep="\n")
            return temp_list[:n]


