#GharamAlkaraki
# pin_space_table.py 
#How long to guess every PIN?
GUESSES_PER_SECOND = 10

for digits in range(4, 9):
    combinations = 10 ** digits
    seconds = combinations / GUESSES_PER_SECOND
    minutes = int(seconds // 60)
    days = int(minutes // 1440)
    print(f"{digits} digits: {combinations} PINs, {minutes} minutes, {days} days")