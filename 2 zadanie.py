file = open('songs.csv')
s = []
for i in file:
    s.append(i.split(','))

for i in range(2, len(s)):
    t = s[i]

