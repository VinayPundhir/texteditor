"""
Author: VINAY PUNDHIR
Email : its.vinay.pundhir@gmail.com
"""

from tkinter import *
import tkinter.messagebox as tkMessageBox
import tkinter.font as tkFont
import tkinter.filedialog as tkFileDialog
import sys
import settings
import docs

DEFAULT_FILE_NAME = "Untitled"
FILENAME = str(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_FILE_NAME


def create_file_menu(menubar, app, textfield, filename):
    m = Menu(menubar, bg=settings.THEME().menubar_bg, fg=settings.THEME().menubar_fg, tearoff=0, relief=SUNKEN)
    m.add_command(label="New", command=lambda: delete_text(textfield, app))
    m.add_command(label="Open", command=lambda: open_file(textfield, app))
    m.add_command(label="Save", command=lambda: save(filename, app, textfield))
    m.add_command(label="Save as", command=lambda: save_file_as(textfield))
    m.add_command(label="About", command=get_about_info)
    m.add_separator()
    m.add_command(label="Exit", command=app.quit)
    return m


def create_options_menu(menubar,textfield):
    m = Menu(menubar, bg=settings.THEME().menubar_bg, fg=settings.THEME().menubar_fg, tearoff=0, relief=SUNKEN)
    m.add_command(label="New window", command=new_window)
    return m


def create_menu_bar(app, textfield, filename):
    menubar = Menu(app, bg=settings.THEME().menubar_bg, fg=settings.THEME().menubar_fg, relief=FLAT)
    menubar.add_cascade(label="File", menu=create_file_menu(menubar, app, textfield, filename))
    menubar.add_cascade(label="Options", menu=create_options_menu(menubar,textfield))
    return menubar


def new_window():
    start_new_window()


def delete_text(textfield, app):
    textfield.delete(1.0, END)
    app.title(DEFAULT_FILE_NAME)


def get_about_info():
    tkMessageBox.showinfo("ABOUT",docs.ABOUT)


def save_file(filename, textfield):
    if "." not in filename:
        filename += ".txt"
    with open(filename, "w") as f:
        f.write(textfield.get(1.0, END))
        f.close()


def save(_, app, textfield):
    if app.title() == DEFAULT_FILE_NAME:
        filename = tkFileDialog.asksaveasfilename()
        save_file(filename, textfield)
        app.title(filename)
    else:
        save_file(app.title(), textfield)


def save_file_as(textfield):
    filename = tkFileDialog.asksaveasfilename()
    save_file(filename, textfield)


def open_file(textfield, app):
    _ = Toplevel()
    _.withdraw()
    filename = tkFileDialog.askopenfilename()
    textfield.delete(1.0, END)
    try:
        with open(filename, "r") as f:
            for line in f.readlines():
                textfield.insert(END, line)
            f.close()
            app.title(filename)
    except:
        ...


def start_new_window(filename="Untitled"):
    app = Tk()
    app.title(filename)
    scrollbar = Scrollbar(app)
    scrollbar.pack(side=RIGHT, fill=Y)
    font = tkFont.Font(family=settings.FONT_FAMILY, weight=settings.FONT_WEIGHT)
    textfield = Text(app, yscrollcommand=scrollbar.set, height=48, background=settings.THEME().textarea_bg, font=font,
                     width=150, relief=FLAT, fg=settings.THEME().textarea_fg)
    app.config(menu=create_menu_bar(app, textfield, filename))
    textfield.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=textfield.yview)
    textfield.delete(1.0, END)
    mainloop()


def main():
    start_new_window(FILENAME)


if __name__ == '__main__':
    main()
