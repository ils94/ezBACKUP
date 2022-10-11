from tkinter import Tk, Button, Entry, X, filedialog, END, Text, Checkbutton, IntVar, Frame, LEFT, RIGHT, Scrollbar, Y
import fileActions
import miscs
import os

root = Tk()

window_width = 500
window_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

root.geometry("500x500+" + str(int(x)) + "+" + str(int(y)))
root.title("ezBACKUP")

if os.path.isfile("icon/ezb.ico"):
    root.iconbitmap("icon/ezb.ico")

root.resizable(False, False)

var_desktop = IntVar()
var_documents = IntVar()
var_downloads = IntVar()
var_pictures = IntVar()
var_music = IntVar()
var_videos = IntVar()

variables = []


def disable_widgets():
    button_start["state"] = "disabled"

    entry_backup_location["state"] = "disabled"

    entry_backup_location.unbind("<Double-Button-1>")

    check_destkop["state"] = "disabled"
    check_documents["state"] = "disabled"
    check_downloads["state"] = "disabled"
    check_pictures["state"] = "disabled"
    check_music["state"] = "disabled"
    check_videos["state"] = "disabled"


def enable_widgets():
    entry_backup_location["state"] = "normal"

    check_destkop["state"] = "normal"
    check_documents["state"] = "normal"
    check_downloads["state"] = "normal"
    check_pictures["state"] = "normal"
    check_music["state"] = "normal"
    check_videos["state"] = "normal"

    button_start["state"] = "normal"

    entry_backup_location.bind("<Double-Button-1>", lambda x: file_dialog())


def start():
    try:
        disable_widgets()

        fileActions.copy(entry_backup_location.get(), text_log, variables)

        enable_widgets()

    except Exception as e:
        text_log["state"] = "normal"
        text_log.insert("end", str(e))
        text_log["state"] = "disabled"

        enable_widgets()


def set_var():
    global variables

    variables = (var_desktop.get(),
                 var_documents.get(),
                 var_downloads.get(),
                 var_pictures.get(),
                 var_music.get(),
                 var_videos.get())


def load_last_directory():
    if os.path.isfile("lastdirectory.data"):
        with open("lastdirectory.data", "r") as f:
            entry_backup_location.delete(0, END)
            entry_backup_location.insert(0, str(f.readline()))
            f.close()


def file_dialog():
    file = filedialog.askdirectory()

    if file != "":
        entry_backup_location.delete(0, END)
        entry_backup_location.insert(0, file)

        with open("lastdirectory.data", "w") as f:
            f.write(file)
            f.close()


entry_backup_location = Entry(root)
entry_backup_location.pack(fill=X, padx=5, pady=5)
entry_backup_location.bind("<Double-Button-1>", lambda x: file_dialog())

entry_backup_location.insert(0, "Double click to choose backup destination folder")

frame_checkbuttons = Frame(root)
frame_checkbuttons.pack()

check_destkop = Checkbutton(frame_checkbuttons, text="Desktop", variable=var_desktop, onvalue=1, offvalue=0,
                            command=set_var)
check_destkop.pack(side=LEFT)
var_desktop.set(1)

check_documents = Checkbutton(frame_checkbuttons, text="Documents", variable=var_documents, onvalue=1, offvalue=0,
                              command=set_var)
check_documents.pack(side=LEFT)
var_documents.set(1)

check_downloads = Checkbutton(frame_checkbuttons, text="Downloads", variable=var_downloads, onvalue=1, offvalue=0,
                              command=set_var)
check_downloads.pack(side=LEFT)
var_downloads.set(1)

check_pictures = Checkbutton(frame_checkbuttons, text="Pictures", variable=var_pictures, onvalue=1, offvalue=0,
                             command=set_var)
check_pictures.pack(side=LEFT)
var_pictures.set(1)

check_music = Checkbutton(frame_checkbuttons, text="Music", variable=var_music, onvalue=1, offvalue=0, command=set_var)
check_music.pack(side=LEFT)
var_music.set(1)

check_videos = Checkbutton(frame_checkbuttons, text="Videos", variable=var_videos, onvalue=1, offvalue=0,
                           command=set_var)
check_videos.pack(side=LEFT)
var_videos.set(1)

frame_text_widget = Frame(root)
frame_text_widget.pack()

text_log = Text(frame_text_widget, height=25, width=58)
text_log.pack(side=LEFT, padx=5, pady=5)
text_log['state'] = "disabled"

text_scrollbar = Scrollbar(frame_text_widget, command=text_log.yview, orient="vertical")
text_scrollbar.pack(fill=Y, side=RIGHT, pady=5)

text_log.configure(yscrollcommand=text_scrollbar.set)

button_start = Button(root, text="Start", width=10, height=1, command=lambda: miscs.multithreading(lambda: start()))
button_start.pack(side=RIGHT, padx=5, pady=2)

set_var()

load_last_directory()

root.mainloop()
