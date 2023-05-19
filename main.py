from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- NEEDED VARIABLES ------------------------------- #
reps = 0
timer = ""
checkmark_text = ''


# ---------------------------- NEEDED FUNCTIONS ------------------------------- #
def count_down(count):
    """A function that counts down a specific amount of time given."""
    global reps, checkmark_text

    # Minutes
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    # Seconds
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # Display Time
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    # Check if countdown over
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmark_text += "✔"
            lb_checkmarks.config(text=checkmark_text)


def work_time():
    """A function that counts down work time."""
    work_sec = WORK_MIN * 60
    count_down(work_sec)


def short_break():
    """A function that counts down break time."""
    short_sec = SHORT_BREAK_MIN * 60
    count_down(short_sec)


def long_break():
    """A function that counts down long break time."""
    long_sec = LONG_BREAK_MIN * 60
    count_down(long_sec)


def start_timer():
    """A function that starts the timer."""
    global reps, lb_timer
    reps += 1

    if reps % 8 == 0:
        lb_timer.config(text="Rest!", fg=RED)
        long_break()
    elif reps % 2 == 0:
        lb_timer.config(text="Break!", fg=PINK)
        short_break()
    else:
        lb_timer.config(text="Work!", fg=GREEN)
        work_time()


def reset_timer():
    """A function that resets the timer."""
    global checkmark_text, reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    lb_timer.config(text="Timer")
    checkmark_text = ''
    lb_checkmarks.config(text="")
    reps = 0


# ---------------------------- UI SETUP ------------------------------- #
# Creating the Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.lift()
window.attributes("-topmost", True)


# Creating the Canvas Widget
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# Creating a PhotoImage
tomato_img = PhotoImage(file="tomato.png")
# Adding the PhotoImage to the Canvas
canvas.create_image(100, 112, image=tomato_img)
# Adding the Timer
timer_text = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=2, column=2)

# Creating Buttons and Labels
lb_timer = Label(text="Timer", justify="center", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
lb_timer.grid(row=1, column=2)

start_button = Button(text="Start", font=(FONT_NAME, 10), bg=YELLOW, command=start_timer)
start_button.grid(row=3, column=1)

reset_button = Button(text="Reset", font=(FONT_NAME, 10), bg=YELLOW, command=reset_timer)
reset_button.grid(row=3, column=3)

lb_checkmarks = Label(font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
lb_checkmarks.grid(row=4, column=2)


window.mainloop()
