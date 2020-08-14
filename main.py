
# import random
# from datetime import datetime, timedelta

# min_year=2020
# max_year=datetime.now().year

# start = datetime(min_year, 1, 1, 00, 00, 00)
# years = max_year - min_year+1
# end = start + timedelta(days=200 * years)

# for i in range(50):
#     random_date = start + (end - start) * random.random()
#     d = str(i) + ' day ago'
#     with open('bot.txt', 'a') as file:
#         file.write(d)
#     print(random_date)
import os
import random
import math
## Number of days you want to make commits
for i in range(50):
    d = str(math.floor(i + 150*random.random())) + ' day ago'
    ## Open a text file and modify it
    with open('bot.txt', 'a') as file:
        file.write(d)
    ## Add bot.txt to staging area
    os.system('git add bot.txt')
    ## Commit it
    os.system('git commit --date="' + d + '" -m "first commit"')

## push the commit to github
os.system('git push -u origin master')


