import random
from tkinter import *
from turtle import bgcolor, color
from typing import List
from PIL import ImageTk, Image
import pygame
from tkinter import ttk

# Initialise libraries

root = Tk()
root.title('Vocabulary')
root.configure(bg="#DFF9C3")



# SET WINDOW SIZE

# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()

# root.geometry("%dx%d" % (width, height))

icon = PhotoImage(file='./images/vocab.png')
root.iconphoto(False, icon)

pygame.mixer.init()
# pygame.mixer.music.load("./vocab time.mp3")


pygame.mixer.music.load('./audio/correct.mp3')
pygame.mixer.music.load('./audio/error.mp3')
# pygame.mixer.music.play(loops=10)

# VARIABLES


grade = 5

grades = [4, 5]

list_of_grades = StringVar(value=grades)



# week's vocab

grade5 = [
    ['Explorer', 'Castle', 'Secret', 'Treasure', 'Cellar'],
    ['Queen', 'Knight', 'Museum', 'Sword', 'Shield', 'Bracelet', 'Necklace', 'Crown', 'Helmet', 'Bow and Arrow', 'Chase'],
    ['Crowd', 'Symbol', 'Rhyme', 'Lead', 'Hide', 'Clown', 'Director', 'Statue', 'Egyptian'],
    ['Exhibit', 'Ancient', 'Collection']
]


grade4 = [
    ['Explorer', 'Castle', 'Secret', 'Treasure', 'Cellar'],
    ['Learn', 'History', 'Geography', 'Uniform', 'Before'],
    ['Treasure', 'Code', 'Librarian', 'Dream'],
    ['Instrument', 'Wind', 'String', 'Percussion']
]

chinese_dict = {
    'Explorer': '探险 家',
    'Castle' : '城堡',
    'Secret' : '秘密',
    'Treasure': '宝藏',
    'Cellar': '地窖',
    'Queen' : '皇后',
    'Knight': '武士',
    'Museum': '博物馆',
    'Sword': '剑',
    'Shield': '盾牌',
    'Bracelet': '手镯',
    'Necklace': '项链',
    'Crown': '王冠',
    'Helmet': '头盔',
    'Bow and Arrow': '弓箭',
    'Chase': '追逐',
    'Crowd': '人群',
    'Symbol': '符号',
    'Rhyme': '押韵',
    'Lead': '狗绳',
    'Hide': '隐藏',
    'Clown': '小丑',
    'Director': '主任',
    'Statue' : '塑像',
    'Egyptian': '埃及',
    'Exhibit': '展览',
    'Ancient': '古代',
    'Collection': '收藏',
    'Learn' : '学习',
    'History': '历史',
    'Before': '以前',
    'Code': '代码',
    'Librarian': '馆员',
    'Dream': '梦',
    'Instrument': '乐器',
    'Wind': '管乐器',
    'String': '弦乐器',
    'Percussion': '打击乐器'
}

words = grade5

# index for choosing word

num = 0
num2 = 0

# Answer options array of buttons

ansidx1 = random.randrange(0,3)

answer_buttons = ['', '', '']

first_btn = Button()
second_btn = Button()
third_btn = Button()
restart_button = Button()
next_button = Button()

# HEX COLOR RANDOMIZER

def hex_color_randomizer():
    options = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    color_string = '#'
    current_digit = ''

    for i in range(6):
        current_digit = options[random.randrange(len(options))]
        color_string += current_digit
    print(color_string)
    return color_string


# GRADE SWITCH

def grade_switch():
    global words
    global grade
    
    if grade == 5:
        grade = 4
    else:
        grade = 5

    if grade == 5:
        words = grade5
    else:
        words = grade4

    print(words)
    grade_label.config(text='Grade: %d' % (grade))

def chinese(word):

    e.insert(END, chinese_dict[word])

# POINTS

player_points = 0
win_amount = 20


# Define logo

image0 = Image.open('./images/vocab.png')
resize_image0 = image0.resize((60, 60))
photo_image0 = ImageTk.PhotoImage(resize_image0)

logo = Label(root, image=photo_image0, bg="#DFF9C3")
logo.grid(row=1, column=1)



# Define text entry

e = Entry(root, width=35, borderwidth=5, bg='#FFE0F9', font=("arial", 25), bd=10)
e.grid(row=0, column=0, columnspan=3, pady=50)

chinese_button = Button(root, width=15, text='SHOW CHINESE', padx=40, pady=20,  bg='#8FD6F5', font=("arial", 13), command=lambda: chinese(words[num][num2]))
chinese_button.grid(row=2, column=2)

grade_button = Button(root,width=15, text='GRADE SWITCH', bg='#8FD6F5', padx=40, pady=20, font=("arial", 13), command=lambda: grade_switch())
grade_button.grid(row=3, column=2)

# next_button = Button(root, width=10, text='NEXT', bg='#8FD6F5', padx=40, pady=20, font=("arial", 13), command=lambda: button_next())

grade_label = Label(root, text='Grade: %d' % (grade), width=30, font=("arial", 13), height=3, bg='#D6FFFF', bd=5)
grade_label.grid(row=3, column=0, padx=1, pady=5)


# Define player points

l3 = Label(root, width=30, height=3, text='Player points: %d' % (player_points), font=("arial", 13), bg='#D6FFFF', bd=5)
l3.grid(row=1, column=0, padx=50, pady=5)


# l2.grid(row=2, column=2, columnspan=2, padx=10, pady=5)


# Define the answer field

l1 = Label(root, width=30, height=3, text='Choose an answer...', font=("arial", 13), bg='#D6FFFF', bd=5)
l1.grid(row=2, column=0, padx=1, pady=5)


# Define Functions

def button_answer(path):

    global player_points
    global l3
    global restart_button
    

    if words[num][num2] == path:
        l1.config(text = 'CORRECT!!', bg='#41FF72')
        pygame.mixer.music.load('./audio/correct.mp3')
        pygame.mixer.music.play(loops=1)
        player_points += 1

        if player_points >= win_amount:
            l1.config(text="YOU WIN!!!", bg='#E6D900')
            pygame.mixer.music.load('./audio/win.mp3')
            pygame.mixer.music.play(loops=2)
            l3.config(text='Player points: %d' % (player_points))
            first_btn.destroy()
            second_btn.destroy()
            third_btn.destroy()
            
            restart_button = Button(root, text='RESTART', bg='#EE7472', width=15, padx=40, pady=20, font=("arial", 13), command=lambda: button_restart())
            restart_button.grid(row=1, column=2, padx=50)

            next_button.destroy()
     
        else:

            l3.config(text='Player points: %d' % (player_points))
        
    else:
        l1.config(text = ' WRONG!!!', bg='#FF4151')
        pygame.mixer.music.load('./audio/error.mp3')
        pygame.mixer.music.play(loops=1)
        player_points -= 1
        if player_points<0:
            player_points = 0
        l3.config(text='Player points: %d' % (player_points))

    


def button_next():
    global num
    global num2
    global first_btn
    global second_btn
    global third_btn

    current_word = e.get()

    while current_word == words[num][num2]:
        num = random.randrange(len(words))
        num2 = random.randrange(len(words[num]))

    e.delete(0, END)
    e.insert(0, words[num][num2])
    change_buttons()
    pygame.mixer.music.load('./audio/%s.mp3' % (words[num][num2]))
    l1.config(text = 'Choose an answer...', font=("arial", 13), bg='#D6FFFF', bd=5)
    pygame.mixer.music.play(loops=1)
    # pygame.mixer.music.load('./audio/focus.mp3')
    # pygame.mixer.music.play(loops=1)

# RESTART BUTTON

def button_restart():

    global player_points
    player_points = 0

    global l3
    l3.config(text='Player points: %d' % (player_points))

    global first_btn
    global second_btn
    global third_btn

    global answer_buttons

    global image1
    global image2
    global image3

    global resize_image1
    global resize_image2
    global resize_image3

    global photo_image1
    global photo_image2
    global photo_image3

    global ansidx1

    global restart_button

    global next_button
    
    restart_button.destroy()

    next_button = Button(root, width=15, text='NEXT', bg='#8FD6F5', padx=40, pady=20, font=("arial", 13), command=lambda: button_next())

    next_button.grid(row=1, column=2, padx=50)

    pygame.mixer.music.load('./audio/restart.mp3')
    pygame.mixer.music.play(loops=1) 

    

    # CREATE RESTART BUTTONS

    answer_buttons[0] = get_button_0()
    answer_buttons[1] = get_button_1()
    answer_buttons[2] = get_button_2()

    # BUTTON 1

    l4 = Label(root, text="1.", font=("arial", 13), relief='sunken', pady=20, padx=20)
    l4.grid(row=9, column=0, pady=40)

    image1 = Image.open('./images/' + answer_buttons[0] + '.png')
    resize_image1 = image1.resize((200, 200))
    photo_image1 = ImageTk.PhotoImage(resize_image1)

    first_btn = Button(root, image=photo_image1, padx=20, pady=20, command=lambda: button_answer(answer_buttons[0]))
    first_btn.grid(row=10, column=0, columnspan=1, padx=10, pady=50)

    # BUTTON 2


    l5 = Label(root, text="2.", font=("arial", 13), relief='sunken', pady=20, padx=20)
    l5.grid(row=9, column=1, pady=40)

    image2 = Image.open('./images/' + answer_buttons[1] + '.png')
    resize_image2 = image2.resize((200, 200))
    photo_image2 = ImageTk.PhotoImage(resize_image2)

    second_btn = Button(root, image=photo_image2, padx=20, pady=20, command=lambda: button_answer(answer_buttons[1]))
    second_btn.grid(row=10, column=1, columnspan=1, padx=10, pady=50)


    # BUTTON 3

    l6 = Label(root, text="3.", font=("arial", 13), relief='sunken', pady=20, padx=20)
    l6.grid(row=9, column=2, pady=40)

    image3 = Image.open('./images/' + answer_buttons[2] + '.png')
    resize_image3 = image3.resize((200, 200))
    photo_image3 = ImageTk.PhotoImage(resize_image3)

    third_btn = Button(root, image=photo_image3, padx=20, pady=20, command=lambda: button_answer(answer_buttons[2]))
    third_btn.grid(row=10, column=2, columnspan=1, padx=10, pady=50)

    button_next()
   

def get_button_0():

    opt0 = random.randrange(len(words))
    opt00 = random.randrange(len(words[opt0]))
    word = words[opt0][opt00]
    return word

def get_button_1():
    opt1 = random.randrange(len(words))
    opt11 = random.randrange(len(words[opt1]))

    word = words[opt1][opt11]
    return word

def get_button_2():
    opt2 = random.randrange(len(words))
    opt22 = random.randrange(len(words[opt2]))

    word = words[opt2][opt22]
    return word


def change_buttons():

# THIS IS WHAT FIXED IT!!!!!

    global first_btn
    global second_btn
    global third_btn

    global answer_buttons

    global image1
    global image2
    global image3

    global resize_image1
    global resize_image2
    global resize_image3

    global photo_image1
    global photo_image2
    global photo_image3

    global ansidx1

    global l1

# THIS IS WHAT FIXED IT!!!!!

    answer_buttons[0] = get_button_0()
    answer_buttons[1] = get_button_1()
    answer_buttons[2] = get_button_2()

     # Overwrite a random button with the real answer

    ansidx1 = random.randrange(0,3)
    answer_buttons[ansidx1] = words[num][num2]

    while(answer_buttons[0] == answer_buttons[1] or answer_buttons[0] == answer_buttons[2]):
        answer_buttons[0] = get_button_0()

    while(answer_buttons[1] == answer_buttons[0] or answer_buttons[1] == answer_buttons[2]):
        answer_buttons[1] = get_button_1()
    
    while(answer_buttons[2] == answer_buttons[0] or answer_buttons[2] == answer_buttons[1]):
        answer_buttons[2] = get_button_2()

    # BUTTON 1

    image1 = Image.open('./images/' + answer_buttons[0] + '.png')
    resize_image1 = image1.resize((200, 200))
    photo_image1 = ImageTk.PhotoImage(resize_image1)

    first_btn = Button(root, image=photo_image1, padx=20, pady=20, command=lambda: button_answer(answer_buttons[0]))
    first_btn.grid(row=10, column=0, columnspan=1, padx=10, pady=50)

    

    # BUTTON 2

    image2 = Image.open('./images/' + answer_buttons[1] + '.png')
    resize_image2 = image2.resize((200, 200))
    photo_image2 = ImageTk.PhotoImage(resize_image2)

    second_btn = Button(root, image=photo_image2, padx=20, pady=20, command=lambda: button_answer(answer_buttons[1]))
    second_btn.grid(row=10, column=1, columnspan=1, padx=10, pady=50)
    # BUTTON 3

    image3 = Image.open('./images/' + answer_buttons[2] + '.png')
    resize_image3 = image3.resize((200, 200))
    photo_image3 = ImageTk.PhotoImage(resize_image3)

    third_btn = Button(root, image=photo_image3, padx=20, pady=20, command=lambda: button_answer(answer_buttons[2]))
    third_btn.grid(row=10, column=2, columnspan=1, padx=10, pady=50)   

    
    l1.config(text='Choose an answer...', font=("arial", 13), bg='#00E6D8', bd=5)
   


# CREATE BUTTONS

answer_buttons[0] = get_button_0()
answer_buttons[1] = get_button_1()
answer_buttons[2] = get_button_2()

# BUTTON 1

l4 = Label(root, text="1.", font=("arial", 13), relief='sunken', pady=20, padx=20)
l4.grid(row=9, column=0, pady=40)

image1 = Image.open('./images/' + answer_buttons[0] + '.png')
resize_image1 = image1.resize((200, 200))
photo_image1 = ImageTk.PhotoImage(resize_image1)

first_btn = Button(root, image=photo_image1, padx=20, pady=20, command=lambda: button_answer(answer_buttons[0]))
first_btn.grid(row=10, column=0, columnspan=1, padx=10, pady=50)

# BUTTON 2


l5 = Label(root, text="2.", font=("arial", 13), relief='sunken', pady=20, padx=20)
l5.grid(row=9, column=1, pady=40)

image2 = Image.open('./images/' + answer_buttons[1] + '.png')
resize_image2 = image2.resize((200, 200))
photo_image2 = ImageTk.PhotoImage(resize_image2)

second_btn = Button(root, image=photo_image2, padx=20, pady=20, command=lambda: button_answer(answer_buttons[1]))
second_btn.grid(row=10, column=1, columnspan=1, padx=10, pady=50)


# BUTTON 3


l6 = Label(root, text="3.", font=("arial", 13), relief='sunken', pady=20, padx=20)
l6.grid(row=9, column=2, pady=40)

image3 = Image.open('./images/' + answer_buttons[2] + '.png')
resize_image3 = image3.resize((200, 200))
photo_image3 = ImageTk.PhotoImage(resize_image3)

third_btn = Button(root, image=photo_image3, padx=20, pady=20, command=lambda: button_answer(answer_buttons[2]))
third_btn.grid(row=10, column=2, columnspan=1, padx=10, pady=50)


# PUT NEXT BUTTON ON SCREEN 

next_button = Button(root, width=15, text='NEXT', bg='#8FD6F5', padx=40, pady=20, font=("arial", 13), command=lambda: button_next())

next_button.grid(row=1, column=2, padx=50)


# root.rowconfigure(0, weight=3)
root.columnconfigure(0, weight=3)
# root.rowconfigure(1, weight=3)
root.columnconfigure(1, weight=3)
# root.rowconfigure(2, weight=3)
root.columnconfigure(2, weight=3)
# root.rowconfigure(3, weight=3)
root.rowconfigure(4, weight=3)

root.minsize(800, 800)


# MAINLOOP


hex_color_randomizer()



root.mainloop()

