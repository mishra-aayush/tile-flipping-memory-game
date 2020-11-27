from tkinter import *
from tkinter import messagebox
import random

master = Tk()
master.title('Image Processor')
master.maxsize(1600, 900)
master.config(bg="black")

global matched, clicked, best, tiles, answer_list, answer_dict, count, colours
best = -1

# Reset the Game
def reset():
	global matched, clicked, best, answer_list, answer_dict, count, colours
	# Define some variables
	count = 0
	matched = 0
	clicked = 0
	answer_list = []
	answer_dict = {}

	# Creating and shuffling our colours
	colours=['#cbcf62', '#90733f', '#4EAB21', '#39CCCC', '#001f3f', '#FF851B','#85144b', '#FFDC00', '#111111', '#610000', '#3b60f9', '#e15733']*2
	random.shuffle(colours)

	#Restoring the buttons to default
	buttonlist = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23]
	for button in buttonlist:
		button.config(bg='white', state='normal')
	
	# Initialize best score and default score
	f = open('best.txt', 'r')
	best = int(f.readline().strip())
	if best == -1:
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
	global count, answer_list, answer_dict, clicked, matched
	buttonlist = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23]
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

# Defining our buttons
b0 = Button(bottom_frame, bg='white', height=10, width=20, command=lambda: onClick(b0, 0))
b1 = Button(bottom_frame, bg='white', height=10, width=20, command=lambda: onClick(b1, 1))
b2 = Button(bottom_frame, bg='white', height=10, width=20, command=lambda: onClick(b2, 2))
b3 = Button(bottom_frame, bg='white', height=10, width=20, command=lambda: onClick(b3, 3))
b4 = Button(bottom_frame, bg='white', height=10, width=20, command=lambda: onClick(b4, 4))
b5 = Button(bottom_frame, bg='white', height=10, width=20, command=lambda: onClick(b5, 5))
b6 = Button(bottom_frame, bg='white', height=10, width=20, command=lambda: onClick(b6, 6))
b7 = Button(bottom_frame, bg='white', height=10, width=20, command=lambda: onClick(b7, 7))

b8 = Button(bottom_frame, bg='white', height=10, width=20, command=lambda: onClick(b8, 8))
b9 = Button(bottom_frame, bg='white', height=10, width=20, command=lambda: onClick(b9, 9))
b10 = Button(bottom_frame, bg='white', height=10, width=20, command=lambda: onClick(b10, 10))
b11 = Button(bottom_frame, bg='white', height=10, width=20, command=lambda: onClick(b11, 11))
b12 = Button(bottom_frame, bg='white', height=10, width=20, command=lambda: onClick(b12, 12))
b13 = Button(bottom_frame, bg='white', height=10, width=20, command=lambda: onClick(b13, 13))
b14 = Button(bottom_frame, bg='white', height=10, width=20, command=lambda: onClick(b14, 14))
b15 = Button(bottom_frame, bg='white', height=10, width=20, command=lambda: onClick(b15, 15))

b16 = Button(bottom_frame, bg='white', height=10, width=20, command=lambda: onClick(b16, 16))
b17 = Button(bottom_frame, bg='white', height=10, width=20, command=lambda: onClick(b17, 17))
b18 = Button(bottom_frame, bg='white', height=10, width=20, command=lambda: onClick(b18, 18))
b19 = Button(bottom_frame, bg='white', height=10, width=20, command=lambda: onClick(b19, 19))
b20 = Button(bottom_frame, bg='white', height=10, width=20, command=lambda: onClick(b20, 20))
b21 = Button(bottom_frame, bg='white', height=10, width=20, command=lambda: onClick(b21, 21))
b22 = Button(bottom_frame, bg='white', height=10, width=20, command=lambda: onClick(b22, 22))
b23 = Button(bottom_frame, bg='white', height=10, width=20, command=lambda: onClick(b23, 23))

# Gridding our Buttons
b0.grid(row=0, column=0, padx=5, pady=5)
b1.grid(row=0, column=1, padx=5, pady=5)
b2.grid(row=0, column=2, padx=5, pady=5)
b3.grid(row=0, column=3, padx=5, pady=5)
b4.grid(row=0, column=4, padx=5, pady=5)
b5.grid(row=0, column=5, padx=5, pady=5)
b6.grid(row=0, column=6, padx=5, pady=5)
b7.grid(row=0, column=7, padx=5, pady=5)

b8.grid(row=1, column=0, padx=5, pady=5)
b9.grid(row=1, column=1, padx=5, pady=5)
b10.grid(row=1, column=2, padx=5, pady=5)
b11.grid(row=1, column=3, padx=5, pady=5)
b12.grid(row=1, column=4, padx=5, pady=5)
b13.grid(row=1, column=5, padx=5, pady=5)
b14.grid(row=1, column=6, padx=5, pady=5)
b15.grid(row=1, column=7, padx=5, pady=5)

b16.grid(row=2, column=0, padx=5, pady=5)
b17.grid(row=2, column=1, padx=5, pady=5)
b18.grid(row=2, column=2, padx=5, pady=5)
b19.grid(row=2, column=3, padx=5, pady=5)
b20.grid(row=2, column=4, padx=5, pady=5)
b21.grid(row=2, column=5, padx=5, pady=5)
b22.grid(row=2, column=6, padx=5, pady=5)
b23.grid(row=2, column=7, padx=5, pady=5)

# Reset the game once when the tkinter window opens
reset()
mainloop()