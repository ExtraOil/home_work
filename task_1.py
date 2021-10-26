print("Time input in seconds, max - 86400: ")
N = int(input())
second = N % 60
minute = N // 60 % 60
hours = N // 3600
if hours == 24:
    hours = 0
print(hours,  minute, second)
