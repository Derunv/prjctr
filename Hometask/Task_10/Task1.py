import random

start_ch = 'A'
end_ch = 'Z'

start = ord(start_ch)
stop = ord(end_ch) + 1
for ch in range(start, stop):
    with open(f'{chr(ch)}.txt', 'w') as file, open('summary.txt', 'a') as summary:
        num = random.randint(1, 100)
        file.write(f'{num}')
        summary.write(f'{chr(ch)}: {num}\n')
