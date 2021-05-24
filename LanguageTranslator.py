from tkinter import *
from tkinter.ttk import Combobox
import requests, json

def do_nothing():
    file_win = Toplevel(root)
    button = Button(file_win, text="Do nothing button", command=file_win.quit)
    button.pack()


def retrieve_input():
    base_url = 'https://api.cognitive.microsofttranslator.com'
    path = '/translate?api-version=3.0'
    
    # append languages that you need the translation from is the input language and to is output langauge
    params = '&from=en&to=de&to=fr&to=it'
    constructed_url = base_url + path + params
    
    # update Ocp-Apim-Subscription-Key generated in Azure cognitive services
    headers = {
        'Ocp-Apim-Subscription-Key': "",
        'Content-type': 'application/json'
    }
    english = txtEnglish.get("1.0", "end-1c")
    body = [{
        'text': english
    }]
    request = requests.post(constructed_url, headers=headers, json=body)
    response = request.json()
    data = json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))
    yz = json.loads(data)
    for item in yz[0]["translations"]:
        if item["to"] == "de":
            txtGerman.delete("1.0", END)
            txtGerman.insert(END, item["text"])
        elif item["to"] == "fr":
            txtFrench.delete("1.0", END)
            txtFrench.insert(END, item["text"])
        elif item["to"] == "it":
            txtItalian.delete("1.0", END)
            txtItalian.insert(END, item["text"])


root = Tk()
root.title("Language Translator")
menu_bar = Menu(root)

step = root.geometry("1000x300")
step = LabelFrame(root, text="Translate", font="Arial 20 bold italic")
step.grid(row=0, columnspan=4, sticky='W', padx=100, pady=4, ipadx=50, ipady=25)

""" lblDdlSourceLanguage = Label(step, text="Choose Source Language")
lblDdlSourceLanguage.grid(row=1, column=1)

list_SourceLanguage = Combobox(step, width=50, height=20)
list_SourceLanguage["values"] = ["en_US", "de_LU", "it_IT", "en_AU"]
list_SourceLanguage.current(0)
list_SourceLanguage.grid(row=1, column=2)

lblDdlDestinationLanguage = Label(step, text="Choose Destination Language")
lblDdlDestinationLanguage.grid(row=2, column=1)

list_DestinationLanguage = Combobox(step, width=50, height=20)
list_DestinationLanguage["values"] = ["en_US", "de_LU", "it_IT", "en_AU"]
list_DestinationLanguage.current(0)
list_DestinationLanguage.grid(row=2, column=2)"""

Button(step, text="Process", font="Arial 8 bold italic", activebackground="turquoise", width=30,
       height=2, command=retrieve_input).grid(row=7, columnspan=4, column=3)

Button(step, text="Close", font="Arial 8 bold italic", activebackground="turquoise", width=30,
       height=2, command=root.quit).grid(row=7, columnspan=4, column=2)

lblEnglish = Label(step, text="          English          ")
lblEnglish.grid(row=3, column=1)

txtEnglish = Text(step, height=2, width=50)
txtEnglish.grid(row=3, column=2)
txtEnglish.insert(END, "Type Your Text Here")

lblGerman = Label(step, text="German")
lblGerman.grid(row=4, column=1)

txtGerman = Text(step, height=2, width=50)
txtGerman.grid(row=4, column=2)
txtGerman.insert(END, "German Will be Print Here")

lblFrench = Label(step, text="French")
lblFrench.grid(row=5, column=1)

txtFrench = Text(step, height=2, width=50)
txtFrench.grid(row=5, column=2)
txtFrench.insert(END, "Italian Will be Print Here")

lblItalian = Label(step, text="Italian")
lblItalian.grid(row=6, column=1)

txtItalian = Text(step, height=2, width=50)
txtItalian.grid(row=6, column=2)
txtItalian.insert(END, "French Will be Print Here")

# File_Menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=do_nothing)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Help_Menu
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Help Index", command=do_nothing)
help_menu.add_command(label="About...", command=do_nothing)
menu_bar.add_cascade(label="Help", menu=help_menu)


root.config(menu=menu_bar)
root.mainloop()