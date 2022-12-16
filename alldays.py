
tree = '''\033[1m
                        \033[93m$\033[92m
                       ***
                      \033[91mooooo\033[92m
                     *******
                    *********\033[92m
                   ******\033[91m&&&&&\033[92m
                  ***\033[91m&&&&\033[92m*****
                 \033[91m&&&&\033[92m***********
                *****************
               **************\033[91m&&&&&\033[92m
              *******\033[91m&&&&&&&&\033[92m******
             \033[91m&&&&&&&&\033[92m***************
            *************************
           \033[91mooooooooooooooooooooooooooo\033[92m
          *****************************
                       \033[93m|||
                       |||

ANSWER TO ALL THE ADVENT OF CODE 2022 CHALLENGES (change the input files to your own)
\033[0m'''
print(tree)

days = 15
long_days = [15]
skip_long = 'y' in input('Would you like to skip the days that take >30s to run? y/n').lower()
for day in range(1,days+1):
    print(f"\033[92m\033[1mResults of day {day}:\033[0m")

    if skip_long and day in long_days:
        print('This day takes > 30s to run, and has been skipped')
        continue
    __import__(f'day{day}')
