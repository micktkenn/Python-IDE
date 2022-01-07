from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.scrolledtext import ScrolledText
import subprocess
# create an instance for window
window = Tk()
# set title for window
window.title("Python IDE")
# create and configure menu
menu = Menu(window)
window.config(menu=menu)
# create editor window for writing code 
editor = ScrolledText(window, font=("haveltica 10 bold"), wrap=None)
editor.pack(fill=BOTH, expand=1)
editor.focus()
file_path = ""
# function to open files
def open_file(event=None):
    global code, file_path
    #code = editor.get(1.0, END)
    open_path = askopenfilename(filetypes=[("Python File", "*.py")])
    file_path = open_path
    with open(open_path, "r") as file:
        code = file.read()
        editor.delete(1.0, END)
        editor.insert(1.0, code)
window.bind("<Control-o>", open_file)
# function to save files
def save_file(event=None):
    global code, file_path
    if file_path == '':
        save_path = asksaveasfilename(defaultextension = ".py", filetypes=[("Python File", "*.py")])
        file_path =save_path
    else:
        save_path = file_path
    with open(save_path, "w") as file:
        code = editor.get(1.0, END)
        file.write(code) 
window.bind("<Control-s>", save_file)
# function to save files as specific name 
def save_as(event=None):
    global code, file_path
    #code = editor.get(1.0, END)
    save_path = asksaveasfilename(defaultextension = ".py", filetypes=[("Python File", "*.py")])
    file_path = save_path
    with open(save_path, "w") as file:
        code = editor.get(1.0, END)
        file.write(code) 
window.bind("<Control-S>", save_as)
# function to execute the code and
# display its output
def run(event=None):
    global code, file_path
    '''
    code = editor.get(1.0, END)
    exec(code)
    '''    
    cmd = f"python {file_path}"
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, shell=True)
    output, error =  process.communicate()
    # delete the previous text from
    # output_windows
    output_window.delete(1.0, END)
    # insert the new output text in
    # output_windows
    output_window.insert(1.0, output)
    # insert the error text in output_windows
    # if there is error
    output_window.insert(1.0, error)
window.bind("<F5>", run)
# function to close IDE window
def close(event=None):
    window.destroy()
window.bind("<Control-x>", close)
# define function to cut 
# the selected text
def cut_text(event=None):
        editor.event_generate(("<<Cut>>"))
# define function to copy 
# the selected text
def copy_text(event=None):
        editor.event_generate(("<<Copy>>"))
# define function to paste 
# the previously copied text
def paste_text(event=None):
        editor.event_generate(("<<Paste>>"))
     
# create menus
file_menu = Menu(menu, tearoff=0)
edit_menu = Menu(menu, tearoff=0)
run_menu = Menu(menu, tearoff=0)
theme_menu = Menu(menu, tearoff=0)
# add menu labels
menu.add_cascade(label="File", menu=file_menu)
menu.add_cascade(label="Edit", menu=edit_menu)
menu.add_cascade(label="Run", menu=run_menu)
menu.add_cascade(label ="Theme", menu=theme_menu)
# add commands in flie menu
file_menu.add_command(label="Open", accelerator="Ctrl+O", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Save", accelerator="Ctrl+S", command=save_file)
file_menu.add_command(label="Save As", accelerator="Ctrl+Shift+S", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", accelerator="Ctrl+x", command=close)
# add commands in edit menu
edit_menu.add_command(label="Cut", command=cut_text) 
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
run_menu.add_command(label="Run", accelerator="F5", command=run)
        
def light():
    editor.config(bg="white")
    output_window.config(bg="white")
# function for dark mode window
def dark():
    editor.config(fg="white", bg="black")
    output_window.config(fg="white", bg="black")
# add commands to change themes
theme_menu.add_command(label="light", command=light)
theme_menu.add_command(label="dark", command=dark)
# create output window to display output of written code
output_window = ScrolledText(window, height=10)
output_window.pack(fill=BOTH, expand=1)
window.mainloop()