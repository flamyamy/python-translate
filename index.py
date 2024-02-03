from googletrans import Translator
from tkinter import *
from tkinter import ttk

def translate_to_turkish():
    """
    Translates English text to Spanish.

    Parameters:
        text (str): The English text to be translated.

    Returns:
        str: The translated Turkish text.
    """
    translator = Translator()
    translation = translator.translate(english_text.get("1.0", END), src='en', dest='tr')
    turkish_text.delete(1.0, END)
    turkish_text.insert(END, translation.text)

app = Tk()
app.title("English to Turkish Translator")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(N, W, E, S))

english_text = Text(frame, wrap=WORD)
turkish_text = Text(frame, wrap=WORD)

ttk.Label(frame, text="English Text:").grid(row=0, column=0, padx=5, pady=5, sticky=W)
english_text.grid(row=0, column=1, padx=5, pady=5)
ttk.Button(frame, text="Translate", command=translate_to_turkish).grid(row=0, column=2, padx=5, pady=5)
ttk.Label(frame, text="Turkish Text:").grid(row=1, column=0, padx=5, pady=5, sticky=W)
turkish_text.grid(row=1, column=1, padx=5, pady=5)

scrollbar = Scrollbar(frame)
scrollbar.grid(row=0, column=3, padx=5, pady=5, sticky=(N, S))
scrollbar.config(command=english_text.yview)
english_text.config(yscrollcommand=scrollbar.set)

scrollbar = Scrollbar(frame, orient=HORIZONTAL)
scrollbar.grid(row=1, column=2, padx=5, pady=5, sticky=(W, E))
scrollbar.config(command=english_text.xview)
english_text.config(xscrollcommand=scrollbar.set)

scrollbar = Scrollbar(frame, orient=HORIZONTAL)
scrollbar.grid(row=2, column=1, padx=5, pady=5, sticky=(W, E))
scrollbar.config(command=turkish_text.xview)
turkish_text.config(xscrollcommand=scrollbar.set)

scrollbar = Scrollbar(frame)
scrollbar.grid(row=1, column=3, padx=5, pady=5, sticky=(N, S))
scrollbar.config(command=turkish_text.yview)
turkish_text.config(yscrollcommand=scrollbar.set)

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

app.mainloop()
