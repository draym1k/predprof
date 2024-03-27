file = open('songs.csv')
s = []
for i in file:
    s.append(i.split(','))
    print()