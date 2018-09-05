import winsound as win
from random import randrange

number_of_notes = int(input("Enter the length of chaos you wish to produce: "))

for x in range(number_of_notes):
    win.Beep(randrange(32000, 32100), randrange(10, 1200))
