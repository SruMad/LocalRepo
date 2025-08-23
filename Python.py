
#stopwatch
import time

#time.sleep(5)

watch= int(input("Enter the time in second --"))

for i in range(watch, 1, -1):
    seconds = i % 60
    minutes = int (i / 60 % 60)
    hours = int (i / 3600)
    
    print(f"{hours}:{minutes:02}:{seconds:02}")

    time.sleep(1)

print("times up")