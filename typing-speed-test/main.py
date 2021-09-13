import tkinter

window = tkinter.Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50, bg="white")

# ---------------------------- VARIABLES SETUP ------------------------------- #
russian_words = "опустоши свой разум будь аморфным бесформенным как вода " \
               "ты наливаешь воду в чашку она становится чашкой ты наливаешь воду в бутылку она становится бутылкой" \
               " ты наливаешь воду в чайник она становится чайником вода может течь" \
               " а может крушить будь водой друг мой разве ты не " \
                "находишь удивительным сказал сократ что и по мнению бога мне уже лучше умереть разве ты не знаешь" \
                " что до сих пор я никому не уступал права сказать что он жил лучше меня у меня было сознание " \
                "чувство в высшей степени приятной что вся жизнь мною прожита благочестиво и справедливо таким" \
                " образом я и сам был доволен собою и находил что окружающие меня такого же мнения обо мне а" \
                " теперь если ещё продлится мой век я знаю мне придётся выносить невзгоды старости буду я хуже " \
                "видеть хуже слышать труднее будет мне учиться новому скорее буду забывать чему научился прежде" \
                " если же я буду замечать в себе ухудшение и буду ругать сам себя какое будет мне удовольствие " \
                "от жизни но может быть и бог по милости своей дарует мне возможность окончить жизнь не " \
                "только в надлежащий момент жизни но и возможно легче."

english_words = "plunged in delusion as a puppet marching to the sound of lies " \
               "in cruelty we collide slave to delusion we define this perfect lake of courage " \
               "reflecting in our eyes all things now retaken all things we have forgotten " \
               "could we choose to live could we choose to exist " \
                "trapped into descent so down just waiting to revive again " \
                "born into a sea of megabytes we now define a datatronic " \
                "symbiosis for the new times to come new perfect machines " \
                "of pain next step to human slavery plasticity and effective control" \
                "for laborious mass who turn the screw obedient " \
                "we are the seed of neural damage deficient technology " \
                "tool of cynicism and cruelty a disease to inflict you severe injuries " \
                "we are made to constrain to regulate current entries to distort " \
                "perception of reality so we delete the useless norm and recomposed the truth " \
                "to preserve your inept peace of mind " \
                "we are here to light the way the ministry of your decay " \
                "disrupting all compromise you will follow the line " \
                "connected to all re-wired to every brain facility " \
                "the strain of security will lead your steps into this world."

# rus_words_list = russian_words.split(" ")
# en_words_list = english_words.split(" ")

test_words_list = []

typed_words_list = []
test_time = 60


print(len("You have one minute. Click the button below and then start typing."))


# ---------------------------- FUNCTION SETUP ------------------------------- #
def choose_lang(text):
    global test_words_list
    test_words_list = text.split(" ")

def start_test(time_count):
    count = 0
    if time_count > 0:
        window.after(1000, start_test, time_count - 1)
        for input_word in input_text.get().split(" "):
            canvas.itemconfig(how_to_text_3,
                              text=f"{test_words_list[count].upper()}"
                                   f" {test_words_list[count+1]} {test_words_list[count+2]} {test_words_list[count+3]}")
            if input_word.lower() == test_words_list[count]:
                count += 1
    else:
        for input_word in input_text.get().split(" "):
            typed_words_list.append(input_word)
        canvas.itemconfig(how_to_text_3, text=f"YOUR RESULT IS: {len(typed_words_list)} words per 60 seconds.")


# ---------------------------- GUI SETUP ------------------------------- #
canvas = tkinter.Canvas(width=800, height=400, bg="white", highlightthickness=0)
image_preview = tkinter.PhotoImage(file="bg-1.png")
image_bg = canvas.create_image(400, 200, image=image_preview)
canvas.grid(row=0, column=0, columnspan=2)

how_to_text_1 = canvas.create_text(400, 240, text='You may choose between Russian and English words test.',
                                 font=("Courier", 14, "bold"))
how_to_text_2 = canvas.create_text(400, 280, text='You have one minute. Click the button below and then start typing.',
                                 font=("Courier", 14, "bold"))
how_to_text_3 = canvas.create_text(400, 350, text='GET READY',
                                 font=("Courier", 24, "bold"))

# choose the language
english_b = tkinter.Button(text="ENGLISH", font=("Arial", 14), command=lambda: choose_lang(english_words),
                         highlightthickness=0)
english_b.grid(row=1, column=0)
russian_b = tkinter.Button(text="RUSSIAN", font=("Arial", 14), command=lambda: choose_lang(russian_words),
                         highlightthickness=0)
russian_b.grid(row=1, column=1)

# start test
start_b = tkinter.Button(text="I'm Ready", font=("Arial", 14), command=lambda: start_test(test_time),
                         highlightthickness=0)
start_b.grid(row=2, column=0, columnspan=2)

# write your text
input_text_label = tkinter.Label(text=f"WRITE BELOW", font=("Arial", 14), highlightthickness=1,
                                 bg="white", pady=10)
input_text_label.grid(row=3, column=0, columnspan=2)
input_text = tkinter.Entry(width=20, highlightthickness=1)
input_text.grid(row=4, column=0, columnspan=2)


window.mainloop()
