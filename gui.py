
import smallS as SmallS
import Mytts as mytts
import Save as saveit
import Translate as translate
import tkinter as tk
import sys
import os
import json
import subprocess
import webbrowser

from pathlib import Path

from tkinter import Tk, Canvas, Entry,Button, PhotoImage,filedialog,ttk


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

aText = ''
url=''
output_path="C:/Users/"
langValue = ''

with open(resource_path("assets\\languages.json")) as file:
    json_data = json.load(file)

def PerfromSummarization():
   global aText
   print("Here mate")
   myUrl = url_entry.get()
   aText = SmallS.ReturnArticle(myUrl)
   canvas.itemconfig(tagOrId=sText, text=aText)
   canvas.itemconfig(tagOrId=tText, text=SmallS.ReturnTitle())

def run_streamlit():
    # Replace 'streamlit_app.py' with the path to your Streamlit script
    subprocess.Popen(['streamlit', 'run', resource_path('app.py')])
def ReadUrl():
    with open(resource_path("db\\key\\weburl.txt"), 'r') as file:
        weburl = file.read()
    return weburl

def OpenWebPage():
    webbrowser.open(ReadUrl())


def PlaySoundTTS():
    mytts.PlayNarration(aText)

def SaveFile():
    finalText = f'Title :: {SmallS.ReturnTitle()}\n\n\n{aText}'
    if name_entry.get() == "":
        saveit.saveit(SmallS.ReturnTitle() + langValue,finalText,path_entry.get())
    elif name_entry.get() != "":
        saveit.saveit(name_entry.get(),finalText,path_entry.get())


def TranslateIt():
   global aText
   translate.TranslateIt(aText, 'bn')
   trSText = translate.TranslateIt(aText, langValue)
   aText = trSText
   trtText = translate.TranslateIt(SmallS.ReturnTitle(), langValue)
   canvas.itemconfig(tagOrId=sText, text=trSText)
   canvas.itemconfig(tagOrId=tText, text=trtText)

def select_path():
    global output_path

    output_path = filedialog.askdirectory(initialdir=r'C:/Users/')
    path_entry.delete(0, tk.END)
    path_entry.insert(0, output_path)


ASSETS_PATH = resource_path(Path(__file__).parent.resolve() / "assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def fade_in(window, alpha):
    if alpha < 1:
        window.attributes('-alpha', alpha)
        alpha += 0.01  
        window.after(10, fade_in, window, alpha)  
    else:
        window.attributes('-alpha', 1)

def fade_out(window, alpha):
    if alpha > 0:
        window.attributes('-alpha', alpha)
        alpha -= 0.01
        window.after(10, fade_out, window, alpha)
    else:
        window.attributes('-alpha', 0)
        window.destroy()
def destroySplash():
    fade_out(splash_root,1)

splash_root = Tk()
splash_root.geometry("250x250+0+0")
splash_root.attributes('-alpha', 0)
screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()

x = int((screen_width - splash_root.winfo_reqwidth()) / 2)
y = int((screen_height - splash_root.winfo_reqheight()) / 2)

splash_root.geometry(f"+{x}+{y}")
splash_root.overrideredirect(True)
scanvas = Canvas(
    splash_root,
    bg = "#FFFFFF",
    height = 250,
    width = 250,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

scanvas.place(x = 0, y = 0)
sImageBG = PhotoImage(file=resource_path("assets\\Slogo.png"))
BGSIMAGe = scanvas.create_image(
    125.0,
    125.0,
    image=sImageBG
)
fade_in(splash_root, 0)

splash_root.after(3000,destroySplash)
splash_root.mainloop()



window = Tk()

window.geometry("1089x775")
window.title("Aimers")
window.iconbitmap(resource_path("assets\\logo.ico"))
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 775,
    width = 1089,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(file=resource_path("assets\\image_1.png"))
image_1 = canvas.create_image(
    535.5,
    390.5,
    image=image_image_1
)
def getJsonKey():
    left_values = list(json_data.keys())
    return left_values

def getJsonValue(key):
     if key in json_data:
        return json_data[key]

def on_select(event):
    #lang_entry.set(combobox.get())
    global langValue
    langValue = getJsonValue(combobox.get())

style = ttk.Style()
style.theme_create("CustomStyle", parent="alt", settings={
    "TCombobox": {
        "configure": {"selectbackground": "#778284", "fieldbackground": "#778284", "foreground": "#000716", "background": "#778284", "font": ("Inter", 35,"bold")},
        "map": {
            "foreground": [("readonly", "#000716")],
            "fieldbackground": [("readonly", "#778284")],
            "selectbackground": [("readonly", "#778284")],
            "selectforeground": [("readonly", "#000716")]
        },
    }
})
style.theme_use("CustomStyle")


combobox = ttk.Combobox(window,values=getJsonKey(),font=("Inter", 13,"bold"))
combobox.config(state="readonly")
combobox.place(x=837.0, y=636.0, width=150, height=27.0)
combobox.bind("<<ComboboxSelected>>", on_select)
url_entry = Entry(
    bd=0,
    bg="#e5efd3",
    fg="#000716",
    highlightthickness=0,
)
url_entry.place(
    x=263,
    y=45,
    width=760,
    height=35
)
name_entry = Entry(
    bd=0,
    bg="#778284",
    fg="#000716",
    highlightthickness=0
)
name_entry.place(
    y=636.0,
    x=592.0,
    width=143.0,
    height=23.0
)
path_entry = Entry(
    bd=0,
    bg="#778284",
    fg="#000716",
    highlightthickness=0
)
path_entry.place(
    y=672.0,
    x=592.0,
    width=120.0,
    height=23.0
)
sText=canvas.create_text(
    210.0,
    274,
    width=785,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Mina", 15 * -1)
)
SummaryBTN_image = PhotoImage(file=resource_path("assets\\SummarizeBTN.png"))
SummaryBTN = Button(
    image=SummaryBTN_image,
    borderwidth=0,
    highlightthickness=0,
    command=PerfromSummarization,
    relief="flat"
)
SummaryBTN.place(
    x=902,
    y=90,
    width=120,
    height=22
)
Ask_image = PhotoImage(file=resource_path("assets\\ChatBTN.png"))
AskBTN = Button(
    image=Ask_image,
    borderwidth=0,
    highlightthickness=0,
    command=run_streamlit,
    relief="flat"
)
AskBTN.place(
    x=170.53,
    y=647,
    width=276.47,
    height=49
)
saveBTN_Image = PhotoImage(file=resource_path("assets\\SaveBTN.png"))
saveBTN = Button(
    image=saveBTN_Image,
    borderwidth=0,
    highlightthickness=0,
    command=SaveFile,
    relief="flat"
)
saveBTN.place(
    x=588.0,
    y=705.0,
    width=150.0,
    height=25.0
)
ReadAloudBTM_Image = PhotoImage(file=resource_path("assets\\PlayBTN.png"))
readAloudBTN = Button(
    image=ReadAloudBTM_Image,
    borderwidth=0,
    highlightthickness=0,
    command=PlaySoundTTS,
    relief="flat"
)
readAloudBTN.place(
    x=837,
    y=705.0,
    width=150.0,
    height=25.0
)
translateBTN_image = PhotoImage(file=resource_path("assets\\TranslateBTN.png"))
translateBTN = Button(
    image=translateBTN_image,
    borderwidth=0,
    highlightthickness=0,
    command=TranslateIt,
    relief="flat"
)
translateBTN.place(
    x=837.0,
    y=671.0,
    width=150.0,
    height=25.0
)
tText=canvas.create_text(
    291.0,
    190.0,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Mina", 15 * -1)
)
txtColor = "#FFFFFF"  # Change to any color you want, e.g., red
canvas.itemconfig(tText, fill=txtColor)
canvas.itemconfig(sText, fill=txtColor)
pathBTN_Image = PhotoImage(file=resource_path("assets\\PathBTN.png"))
pathBTN = Button(
    image=pathBTN_Image,
    borderwidth=0,
    highlightthickness=0,
    command=select_path,
    relief="flat"
)
pathBTN.place(
    x=711.0,
    y=672.0,
    width=22.0,
    height=20.0
)
webBTN_Image = PhotoImage(file=resource_path("assets\\WebBtn.png"))
webBTN = Button(
    image=webBTN_Image,
    borderwidth=0,
    highlightthickness=0,
    command=OpenWebPage,
    relief="flat"
)
webBTN.place(
    x=8.0,
    y=718.0,
    width=95.0,
    height=30.0
)


window.resizable(False, False)
window.mainloop()