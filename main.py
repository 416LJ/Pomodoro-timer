import math
from tkinter import *



# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9fdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    title_bar.config(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"))
    canvas.itemconfig(display,text="25:00")
    reps = 0
    levels_button.config(text="")



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 8 ==0:
        countdown(long_break)
        title_bar.config(text="L Break", fg=RED, font=(FONT_NAME, 35, "bold"))
    elif reps % 2 == 0:
        countdown(short_break)
        title_bar.config(text="S Break", fg=PINK, font=(FONT_NAME, 35, "bold"))
    else:
        countdown(work_sec)
        title_bar.config(text="Work", fg=GREEN, font=(FONT_NAME, 35, "bold"))
# ---------------------------- COUNTDOWN MECHANISM -----\-------------------------- #
def countdown(time):
    global timer
    time_m = int(time // 60)
    print(time_m)
    time_s = int(time % 60)
    if time_s < 10:
        time_s = "0" + str(time_s)
    canvas.itemconfig(display, text=f"{time_m}:{time_s}")
    if time > 0:
        timer = window.after(1000, countdown, time - 1)
    else:
        start_timer()
        level = ""
        rep_count = math.floor(reps / 2)
        for i in range(rep_count):
            level += "✅"
        levels_button.config(text=level)



# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=100,bg=YELLOW)

background_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=250,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,100,image=background_img)
display = canvas.create_text(100,180,text="25:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column = 1 ,row =1)


title_bar = Label(text="Timer",fg=GREEN,font=(FONT_NAME,35,"bold"),highlightthickness=0,background=YELLOW)
title_bar.grid(column=1 , row=0)

levels_button = Label(text = "",highlightthickness=0,background=YELLOW)
levels_button.grid(column=1 , row=5)

button_start = Button(text="Start",highlightthickness=0,highlightbackground=YELLOW,command=start_timer)
button_start.grid(column=0,row=4)

button_reset = Button(text="Reset",highlightthickness=0, highlightbackground=YELLOW,command=reset_timer)
button_reset.grid(column=2,row=4)
window.mainloop()



