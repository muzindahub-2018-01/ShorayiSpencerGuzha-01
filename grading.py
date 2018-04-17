import os
# This is a mark grading system 

def clear_screen():
    os.system('cls' if os.name== 'nt' else 'clear')

#This is the mark input
mark=int(input(' Please Enter Your Mark: \n'))

#this is the mark range of the grades and the corresponding grade
if mark<=100 and mark>=80:
    print('Excellent You got A+ grade!')
elif mark<79 and mark>75:
    print('You got A grade')
elif mark < 75 and mark > 70:
    print('You got A- grade')
elif mark < 70 and mark > 65:
    print('You got B+ grade')
elif mark < 65 and mark > 60:
    print('You got B grade')
elif mark <60 and mark >50:
    print('You got C+ grade')
elif mark <50 and mark >40:
    print('You got C grade')
elif mark<0:
    print('Invalid Option!')

else :
    print('Sorry! You are failed')

clear_screen()
