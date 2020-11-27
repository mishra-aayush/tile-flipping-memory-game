from tkinter import *
from tkinter import messagebox
import random
from functools import partial

master = Tk()
master.title('Image Processor')
master.maxsize(1600, 900)
master.config(bg="black")

global matched, clicked, best, tiles, answer_list, answer_dict, count, colours, buttonlist
best = -1

# Reset the Game
def reset():
	global matched, clicked, best, answer_list, answer_dict, count, colours, buttonlist
	# Define some variables
	count = 0
	matched = 0
	clicked = 0
	answer_list = []
	answer_dict = {}

	# Creating and shuffling our colours
	colours=['#cbcf62', '#90733f', '#4EAB21', '#39CCCC', '#001f3f', '#FF851B','#85144b', '#FFDC00', '#111111', '#610000', '#3b60f9', '#e15733']*2
	random.shuffle(colours)

	buttonlist = []
	for i in range(24):
		button_to_append = Button(bottom_frame, bg='white', height=10, width=20)
		button_to_append.config(bg='white', state='normal',command=partial(onClick,button_to_append, i))
		# Gridding our Buttons
		button_to_append.grid(row=i//8, column=i%8, padx=5, pady=5)
		buttonlist.append(button_to_append)
	
	# Initialize best score and default score
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
	global matched, clicked, best, answer_list, answer_dict, count, colours
	# Updating scores
	if clicked < best or best == -1:
		best = clicked
		f = open('best.txt', 'w')
		f.write(str(best))
		f.close()
		l2['text']='Best: '+ str(best)

# Function for clicking buttons
def onClick(b, number):
	global count, answer_list, answer_dict, clicked, matched, buttonlist
	print(b,number)
	if buttonlist[number] not in answer_list and count < 2:
		buttonlist[number].config(bg = colours[number], state = 'disabled')
		# Add number to answer list
		answer_list.append(number)
		# Add button and number to Answer Dictionary
		answer_dict[b] = colours[number]
		# Increment our Counter
		count += 1
		# Increment our Total Clicks
		clicked += 1
		#Update total clicks
		l1["text"] = 'Clicks: ' + str(clicked)
	
	# Check if match or not
	if len(answer_list) == 2:
		if colours[answer_list[0]] == colours[answer_list[1]]:
			for key in answer_dict:
				#Disabling the currently selected button
				key["state"] = "disabled"
			# Increment our matched counter
			matched += 1
			if matched == 12:
				won()
		else:
			# Reset the buttons because match not found
			for key in answer_dict:
				key.config(bg = 'white', state = 'normal')
		count = 0
		answer_list = []
		answer_dict = {}

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