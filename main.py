BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random

french_words = pd.read_csv("french_words.csv")
french_dict = french_words.to_dict("records")
random_word={}

def tick_function():
    french_dict.remove(random_word)
    french_df= pd.DataFrame(french_dict)
    french_df.to_csv("words_to_learn.csv", index=False)
    next_card()

def next_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word= random.choice(french_dict)
    random_french= random_word["French"]
    canvas.itemconfig(card_canvas, image=front_card_img)
    canvas.itemconfig(card_title, text= "French", fill="black")
    canvas.itemconfig(card_word, text=random_french, fill="black")
    flip_timer =window.after(3000,flip_card)
def flip_card():
    random_english = random_word["English"]
    canvas.itemconfig(card_canvas, image=back_card_img)
    canvas.itemconfig(card_title, text= "English", fill="white")
    canvas.itemconfig(card_word, text=random_english, fill="white")

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer =window.after(3000,flip_card)

canvas = Canvas(width=800, height= 526)
front_card_img=PhotoImage(file= "card_front.png")
back_card_img=PhotoImage(file= "card_back.png")
card_canvas= canvas.create_image(400, 263, image=front_card_img)
card_title= canvas.create_text(400, 150, text="", font= ("Arial",40,"italic"))
card_word= canvas.create_text(400, 263, text="", font= ("Arial",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


wrong_img=PhotoImage(file= "wrong.png")
wrong_button = Button(image=wrong_img)
wrong_button.config(bg= BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)


right_img=PhotoImage(file= "right.png")
right_button = Button(image=right_img)
right_button.config(bg= BACKGROUND_COLOR, highlightthickness=0, command=tick_function)
right_button.grid(row=1, column=1)

next_card()


window.mainloop()