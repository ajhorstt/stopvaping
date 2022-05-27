import os
from random import shuffle, randint
from guizero import App, Box, Picture, PushButton, Text
from guizero import warn
from guizero import Box, Text
import time

def counter():
    timer.value = int(timer.value)-1
    if int(timer.value) == 0:
        timer.cancel(counter)
        # reset the timer
        result.size=40
        result.font="arial bold"
        result.text_color="brown"
        result.value = "Game Over"
        warn("Time Out", "you've run out of time")
        warn("Score =", score.value)
        score.value="0" # reset score to zero for next game
        # reset timer
        timer.value = "30"
        # reset result
        result.value = ""

# set the path to the emoji folder on your computer
emojis_dir = "emojis"
# create a list of the locations of the emoji images
emojis = [os.path.join(emojis_dir, f) for f in os.listdir(emojis_dir) if os.path.isfile(os.path.join(emojis_dir, f))]
# shuffle the emojis
shuffle(emojis)


def match_emoji(matched):
	if matched:
		result.value = "correct"
		score.value = int(score.value) + 1
	else:
		result.value = "incorrect"

	setup_round()


def setup_round():
	# for each picture and button in the list assign an emoji to its image feature
	for picture in pictures:
		# make the picture a random emoji
		picture.image = emojis.pop()

	for button in buttons:
		# make the image feature of the PushButton a random emoji
		button.image = emojis.pop()
		# set the command to be called and pass False, as these emoji wont be the matching ones
		button.update_command(match_emoji, [False])

	# choose a new emoji
	matched_emoji = emojis.pop()

	# select a number at random
	random_picture = randint(0, 8)
	# change the image feature of the Picture with this index in the list of pictures to the new emoji
	pictures[random_picture].image = matched_emoji

	random_button = randint(0, 8)
	# change the image feature of the PushButton with this index in the list of buttons to the new emoji
	buttons[random_button].image = matched_emoji
	# set the command to be called and pass True, as this is the matching emoji
	buttons[random_button].update_command(match_emoji, [True])


def counter():
	timer.value = int(timer.value) - 1
	if int(timer.value) == 0:
		# reset the timer
		timer.value = 30

def printblankspace():
	for i in range(5):
		space = Text(game_box, text="                ")



def increase():
    timertext.text_size = int(timertext.text_size) + 1

# setup the app
app = App(title="emoji match" , width=600, height=800, layout="auto", bg=None, visible=True)
welcome_message = Text(app, text="Welcome to the Matching Emoji Game!", size=22,
    color="blue",  bg="yellow", font="Helvetica")
welcome_message.text_color = "green"

result = Text(app)

# create a box to house the grids
game_box = Box(app)


# create a box to house the pictures
pictures_box = Box(game_box, layout="grid")

# give some space between sets of emoji
printblankspace();

# create a box to house the buttons
buttons_box = Box(game_box, layout="grid")


# create the an empty lists to add the buttons and pictures to
buttons = []
pictures = []
# create 9 PushButtons with a different grid coordinate and add to the list
for x in range(0, 3):
	for y in range(0, 3):
		# put the pictures and buttons into the lists
		picture = Picture(pictures_box, grid=[x, y])
		pictures.append(picture)

		button = PushButton(buttons_box, grid=[x, y])
		buttons.append(button)

# add in the extra features
extra_features = Box(app)
extra = Box(extra_features, layout="grid")

timer = Text(app, text=".....1.....2......3.....Get Ready")
scoreboard = Box(app)

timer = Text(scoreboard, text="Score", align="right")
time.sleep(5)
score = Text(scoreboard, text="0", align="left")
setup_round()

# start the timer
timer = Text(app, text="")
timer.value = 30
timer.repeat(1000, counter)

app.display()
