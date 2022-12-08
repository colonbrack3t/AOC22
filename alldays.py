days = 8
for day in range(1,days+1):
    print(f"\033[92m\033[1mResults of day {day}:\033[0m")
    __import__(f'day{day}')

# reset terminal font
print('\033[0m')