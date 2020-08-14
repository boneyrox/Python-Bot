
import os
import random
import math

for i in range(50):
    d = str(math.floor(i + 133 +150*random.random())) + ' day ago'
    
 
    with open('bot.txt', 'a') as file:
        file.write(d)
    
    os.system('git add bot.txt')
    
    os.system('git commit --date="' + d + '" -m "first commit"')


os.system('git push -u origin master')


