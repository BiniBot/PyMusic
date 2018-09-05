import winsound as win
from random import *

scale = 440
ratio = 1.05946
notes = {'C': -9,
         'C#': -8,
         'D': -7,
         'D#': -6,
         'E': -5,
         'F': -4,
         'F#': -2,
         'G': -2,
         'G#': -1,
         'A': 0,
         'A#': 1,
         'B': 2}

tempered_notes = {}
scale_multiplier = 0
while True:
    scale_multiplier = float(input("Enter the scale multiplier (0.25 to 2.5): "))
    if 0.25 <= scale_multiplier <= 2.5:
        break


scale *= scale_multiplier


for note in notes:
    freq = scale * ratio ** notes.get(note)
    tempered_notes[note] = int(freq)


k = list(tempered_notes.values())

number_of_notes = int(input("Enter the number of random notes: "))
max_number_of_repeats = int(input
                            ("Enter the maximum number of times any one note "
                             "can be repeated (with random changes in scale): "))


for notes in range(number_of_notes):
        random_note = choice(tuple(tempered_notes.items()))
        sound = random_note[1]
        print(str(random_note[0]))
        win.Beep(sound, 500)
        for repeats in range(randint(0, max_number_of_repeats)):
            x = randint(0, 1)
            if x or scale_multiplier < .75:
                sound += randint(20, 100)
                print("Frequency of random note: " + str(sound))
                win.Beep(sound, 500)
            else:
                sound -= randint(20, 100)
                print("Frequency of random note: " + str(sound))
                win.Beep(sound, 500)
