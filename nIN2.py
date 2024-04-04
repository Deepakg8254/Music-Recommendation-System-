import pandas as pd

# from Gui import *
song_info = pd.read_csv(r'C:\Users\grove\Downloads\muse_v3.csv\muse_v3.csv', sep=',')

validSentiList, validSongList = [], []
for x in song_info.index:
    CSVsentiments = song_info['genre'][x]
    if CSVsentiments not in validSentiList:
        validSentiList.append(CSVsentiments)

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
            for i in range(len(song_info['genre'])):
                if len(temp_list) > 15:
                    break
                if song_info['genre'][i] == varUserSenti[0]:
                    temp_list.append([song_info['track'][i], song_info['artist'][i],song_info['spotify_id'][i]])
            print(*temp_list, sep="\n")
            return temp_list[:n]


