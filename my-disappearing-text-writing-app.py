import tkinter

window = tkinter.Tk()
window.title("Write your text and never stop")
window.config(padx=50, pady=50, bg="white")

text = ""
text_list = []
time_count = 10
stop_time = False


# ---------------------------- FUNCTION SETUP ------------------------------- #

def change_text():
    global text, text_list
    for word in text.split(" "):
        text_list.append(word)
    writen_text["text"] = text_list[-1]


def save_progress():
    global text, text_list, main_button, stop_time
    with open(file="data.txt", mode="w") as file:
        file.write(str(text))
    input_text.delete(0, 'end')
    text_list = []
    text = ""
    main_button["text"] = "I'm Ready"
    main_button["command"] = lambda: start_writing(time_count)
    stop_time = True


def start_writing(count):
    global text, text_list, main_button, stop_time
    if stop_time:
        count = 0
    stop_time = False
    main_button["text"] = "Save progress"
    main_button["command"] = save_progress
    print(count)
    text_len = len(input_text.get())
    if text_len >= 1:
        text += input_text.get()
        input_text.delete(0, 'end')
        count = 10
    change_text()

    if count > 0:
        window.after(1000, start_writing, count - 1)
        input_text_label["text"] = f"Time remaining: {count}\n"

    else:
        # delete all
        print("time left")
        print(text_list)
        print(text)
        writen_text["text"] = "Start again?"
        input_text.delete(0, 'end')
        text_list = []
        text = ""
        main_button["text"] = "I'm Ready"
        main_button["command"] = lambda: start_writing(time_count)


# ---------------------------- GUI SETUP ------------------------------- #

writen_text = tkinter.Label(text="When you are ready, type your text.\n"
                                 "And don't forget about spaces between words.\n"
                                 "You may save your text as Data.txt in a app folder\n"
                                 'by clicking "Save progress" button.\n'
                                 "Good luck!",
                            font=("Arial", 14), highlightthickness=1, bg="white", width=40, height=8)
writen_text.grid(row=1, column=0, columnspan=3)

# start test
main_button = tkinter.Button(text="I'm Ready", font=("Arial", 14), command=lambda: start_writing(time_count),
                             highlightthickness=0)
main_button.grid(row=2, column=0, columnspan=3)

# write your text
input_text_label = tkinter.Label(text=f"You have {time_count} seconds to type something\n",
                                 font=("Arial", 14), highlightthickness=1, bg="white", pady=10)
input_text_label.grid(row=3, column=0, columnspan=3)
input_text = tkinter.Entry(width=20, highlightthickness=1)
input_text.grid(row=4, column=0, columnspan=3)


window.mainloop()
