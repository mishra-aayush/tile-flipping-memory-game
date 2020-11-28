from tkinter import *
from tkinter import messagebox
import random
from functools import partial
from time import sleep

master = Tk()
master.title('Image Processor')
master.maxsize(1600, 900)
master.config(bg="black")

global matched, clicked, best, temp_list, temp_dict, colours, buttonlist
best = -1

# Reset the Game
def reset():
	global matched, clicked, best, temp_list, temp_dict, colours, buttonlist
	# Define some variables
	# Matched to confirm how many pairs have been matched
	matched = 0
	# Clicked to ckeck the number of attempts by the user
	clicked = 0
	# To store the temporary button numbers clicked by the user
	temp_list = []
	# To store the button and corresponding colour
	temp_dict = {}

	# Creating and shuffling our colours
	colours=['#cbcf62', '#90733f', '#4EAB21', '#39CCCC', '#001f3f', '#FF851B','#85144b', '#FFDC00', '#111111', '#610000', '#3b60f9', '#e15733']*2
	random.shuffle(colours)

	# Initializing the button list
	buttonlist = []
	for i in range(24):
		button_to_append = Button(bottom_frame, bg='white', height=10, width=20)
		button_to_append.config(bg='white', state='normal',command=partial(onClick,button_to_append, i))
		# Gridding our Buttons
		button_to_append.grid(row=i//8, column=i%8, padx=5, pady=5)
		buttonlist.append(button_to_append)
	
	# Initializing best score and default score
	f = open('best.txt', 'r')
	best = int(f.readline().strip())
	if best <= -1:
		l2['text']='Best: 0'
	else:
		l2['text']='Best: '+ str(best)
	l1['text']='Clicks: 0'
	f.close()

# Create won function
def won():
	global clicked, best
	# Updating scores
	if clicked < best or best == -1:
		best = clicked
		f = open('best.txt', 'w')
		f.write(str(best))
		f.close()
		l2['text']='Best: '+ str(best)

# Function for clicking buttons
def onClick(b, number):
	global temp_list, temp_dict, clicked, matched, buttonlist
	if len(temp_list) < 2:
		buttonlist[number].config(bg = colours[number], state = 'disabled')
		# Add number to temp list
		temp_list.append(number)
		# Add button and number to temp Dictionary
		temp_dict[b] = colours[number]
		# Increment our Total Clicks
		clicked += 1
		#Update total clicks
		l1["text"] = 'Clicks: ' + str(clicked)
		# Refresh GUI
		master.update()
		master.after(1000,check_if_match)
	

def check_if_match():
	global temp_list, temp_dict, clicked, matched, buttonlist
	if len(temp_list) == 2:
		if colours[temp_list[0]] == colours[temp_list[1]]:
			for key in temp_dict:
				#Disabling the currently selected button
				key["state"] = "disabled"
			# Increment our matched counter
			matched += 1
			if matched == len(buttonlist)//2:
				won()
		else:
			# Reset the buttons because match not found
			for key in temp_dict:
				key.config(bg = 'white', state = 'normal')
		temp_list = []
		temp_dict = {}

# Initializing the top frame
top_frame = Frame(master, width=1500, height= 200, bg='grey')
top_frame.pack(padx=20, pady=20)

# Defining our labels and new game button
l1 = Label(top_frame, text=' ', bg='grey', font=("Helvetica", 20),  height=5, width=25)
l2 = Label(top_frame, text=' ', bg='grey', font=("Helvetica", 20), height=5, width=25)
bng = Button(top_frame, text='New  Game', bg='white', font=("Helvetica", 20, "bold"), height=5, width=25, command=reset)

# Gridding our Label Contents
l1.grid(row=0, column=0, padx=25, pady=20)
l2.grid(row=0, column=2, padx=25, pady=20)
bng.grid(row=0, column=1, padx=25, pady=20)

# Initializing the bottom frame
bottom_frame = Frame(master, width=1500, height= 600, bg='grey')
bottom_frame.pack(padx=20, pady=20)


# Reset the game once when the tkinter window opens
reset()
mainloop()
