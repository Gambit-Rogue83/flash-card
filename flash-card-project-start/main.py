import pandas
import random

from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
TEST_WORD = ("Ariel", 60, "bold")
LANGUAGE = ("Ariel", 40, "italic")
current_card = {}
to_learn = {}

# -------------- PROGRAM ---------- #
try:
    flash_dict = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    flash_dict = pandas.read_csv("data/Korean_words.csv")
    to_learn = flash_dict.to_dict(orient="records")
else:
    to_learn = flash_dict.to_dict(orient="records")

# ------------- FLASH CARD FUNCTIONALITY ----------- #
def flash_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Korean", fill="black")
    canvas.itemconfig(card_word, text=current_card["Korean"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(5500, func=flip)

def flip():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)

def passed_card():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    flash_card()

# ---------------- UI -------------------- #
window = Tk()
window.title("Flashy Flash Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(5500, func=flip)

canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=LANGUAGE)
card_word = canvas.create_text(400, 260, text="Title", font=TEST_WORD)
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)



# Label

# Button
incorrect_img = PhotoImage(file="images/wrong.png")
incorrect = Button(image=incorrect_img, highlightthickness=0, command=flash_card)
incorrect.grid(row=1, column=0)
correct_img = PhotoImage(file="images/right.png")
correct = Button(image=correct_img, highlightthickness=0, command=passed_card)
correct.grid(row=1, column=1)

flash_card()



window.mainloop()


