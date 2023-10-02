import sys

with open('data.txt', 'r', encoding='utf-8') as f:
    packet = f.readline()

marker = []
count = 0
for ele in packet:
    count += 1
    marker.append(ele)
    if len(marker) > 4:
        del(marker[0])
    elif len(marker) < 4:
        continue

    if len(set(marker)) == 4:
        print(f'first start-of-packet marker is at: {count}')
        break

 







