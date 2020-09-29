songs = ['Rockstar', 'Do It', 'For The Night']
print(songs[1:3])

songs[2] = 'Nu Wave'

songs.append('Long Live Julio')
songs.extend(['Cartier'])
songs.insert(5, 'Monte Cristo')

songs.pop(0)

for i in range(len(songs)):
    print(songs[i])

for song in songs:
    print(song)