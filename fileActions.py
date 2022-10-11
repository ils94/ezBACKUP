import os
import shutil

desktop = os.path.expanduser("~/Desktop")
documents = os.path.expanduser("~/Documents")
downloads = os.path.expanduser("~/Downloads")
pictures = os.path.expanduser("~/Pictures")
music = os.path.expanduser("~/Music")
videos = os.path.expanduser("~/Videos")

appdata = os.getenv("APPDATA")


def shutil_actions(text, dst, src, filename):
    try:
        text["state"] = "normal"
        text.insert("end", "\nCreating " + filename + ".zip...")
        text["state"] = "disabled"

        shutil.make_archive(appdata + "/" + filename, "zip", src)

        text["state"] = "normal"
        text.insert("end", "\nCopying " + filename + ".zip...")
        text["state"] = "disabled"

        shutil.copy(appdata + "/" + filename + ".zip", dst)

        text["state"] = "normal"
        text.insert("end", "\nDeleting " + filename + ".zip...")
        text["state"] = "disabled"

        os.remove(appdata + "/" + filename + ".zip")

        text["state"] = "normal"
        text.insert("end", "\nDONE!\n")
        text["state"] = "disabled"
    except Exception as e:
        text["state"] = "normal"
        text.insert("end", "\n" + str(e))
        text["state"] = "disabled"


def copy(dst, text, variables):
    text["state"] = "normal"
    text.delete("1.0", "end")
    text["state"] = "disabled"

    if os.path.isdir(dst):

        text["state"] = "normal"
        text.insert("end", "Initializing...\n")
        text["state"] = "disabled"

        if variables[0] == 1:
            shutil_actions(text, dst, desktop, "Desktop")

        if variables[1] == 1:
            shutil_actions(text, dst, documents, "Documents")

        if variables[2] == 1:
            shutil_actions(text, dst, downloads, "Downloads")

        if variables[3] == 1:
            shutil_actions(text, dst, pictures, "Pictures")

        if variables[4] == 1:
            shutil_actions(text, dst, music, "Music")

        if variables[5] == 1:
            shutil_actions(text, dst, videos, "Videos")
    else:
        text["state"] = "normal"
        text.insert("end", "Destination is not a valid directory.")
        text["state"] = "disabled"
