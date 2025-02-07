from tkinter import *
import math
import pygame



# ---------------------------- CONSTANTS ------------------------------- #
BLUE = "#00B8A9"
RED = "#FF2929"
GREEN = "#387F39"
YELLOW = "#FFDE4D"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def start_bell():
    pygame.mixer.init()
    pygame.mixer.music.load("Seatbelt-sound-effect/Seatbelt-sound-effect.mp3")
    pygame.mixer.music.play()


def second_bell():
    pygame.mixer.init()
    pygame.mixer.music.load("Drumroll-sound-effect/Drumroll-sound-effect.mp3")
    pygame.mixer.music.play()


def last_bell():
    pygame.mixer.init()
    pygame.mixer.music.load("Concert-audience-cheering-sound-effect/Concert-audience-cheering-sound-effect.mp3")
    pygame.mixer.music.play()


def reset_timer():
    window.after_cancel(timer)
    label.config(text="Pomodoro Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Take A Nap\nYou Are\nA Princess!😴😘😘", fg=RED)
        last_bell()
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Short Break😁🙌", fg=BLUE)
        second_bell()
    else:
        count_down(work_sec)
        label.config(text="Work!", fg=GREEN)
        start_bell()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_min == 0:
        count_min = "00"

    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_sec == 0:
        count_sec = "00"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Pomodoro Timer", font=("Times New Roman", 35, "bold", "italic"), bg=YELLOW, fg=GREEN)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button = Button(text="START", bg=YELLOW, highlightthickness=5, command=start_timer)
button.grid(column=0, row=2)

button2 = Button(text="RESET", bg=YELLOW, highlightthickness=5, command=reset_timer)
button2.grid(column=2, row=2)

check = Label(bg=YELLOW, fg=GREEN, font=("bold", 25))
check.grid(column=1, row=3)

window.mainloop()
