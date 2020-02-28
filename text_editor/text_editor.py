from tkinter import *
from tkinter import filedialog

# ------------------------------------------------
#     ALL FUNCTIONS

open_file='no_open_file'
open_file_address='nothing'

def new_file():
    text_area.delete(1.0,END)
    root.title('New File- Notepad')


# function for open file
def openfile():
    global open_file # to update open_file
    global open_file_address
    ''' this function first open file then find name of file then change window title then remove previous
    content and then add new content '''
    file=filedialog.askopenfile(initialdir='/',title='OPEN',filetypes=(('text file','*.txt'),('any file','*.*')))
    # print(file_detail) gives:- ['<_io.TextIOWrapper', "name='H:/AI/test.txt'", "mode='r'", "encoding='cp1252'>"]
    # when cancel is pressed during open file 'IndexError: list index out of range' comes to get rid off this
    # if statement is used
    if file!=None:
        open_file_address=str(file).split(' ')[1].split('=')[1].replace("'","")
        # print(open_file_address):- H:/AI/python.txt
        ''' to extract the file name following line will do it '''
        file_detail=str(file).split(' ')[1].split('/')[-1].split('.')[0] # file name will be:- test.txt'
        root.title(f'{file_detail}- Notepad')
        open_file=file_detail # this is will update open file and tell that file is currently open,
                            #  your save function performs save and not save as 
        open_file_address=str(file).split()
        text_area.delete(1.0,END) #before adding new content fro new file previous should beremoved from previous file
        for line in file:
            text_area.insert(END,line)        



# SAVE AS for saving file 
def save_as():
    f=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    # print(f) :- <_io.TextIOWrapper name='H:/AI/yo.txt' mode='w' encoding='cp1252'>
    if f!=None:
        address=str(f).split(' ')[1].split('=')[1].replace("'","")
        print(address)
        with open(address,'w') as wf:
            wf.write(text_area.get(1.0,END)) # this will take text from text and write on new file


# SAVE FUNCTION
def save():
    if open_file=='no_open_file': # fresh file and use save_as for saving file
        save_as()
    else:
        open_file_add=open_file_address[1].split('=')[1].replace("'","")
        with open(open_file_add,'w') as wf:
            wf.write(text_area.get(1.0,END))
        print('done')

# -------------------------------------------------
root=Tk()

root.geometry("488x290+500+120")
root.title("New File- Notepad")
root.wm_iconbitmap("Text-Edit.ico")

# --------------------------------------------
# TEXT AREA 
text_area=Text(root,wrap=WORD,font=("Verdana 14"),border=2,padx=4,pady=3,selectbackground="#696969")
text_area.pack(fill=BOTH,expand=1)

# SCROLL BAR 
scroll=Scrollbar(text_area , bg='#ffffff')
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=text_area.yview)
text_area.config(yscrollcommand=scroll.set)

# MENU
main_menu=Menu(root)
root.config(menu=main_menu)

# FILE MENU
file_menu=Menu(main_menu,tearoff=0)
file_menu.add_command(label="New File",command=new_file)
file_menu.add_command(label="Open",command=openfile)
file_menu.add_separator()
file_menu.add_command(label="Save as",command=save_as)
file_menu.add_command(label='Save',command=save)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=root.destroy)
main_menu.add_cascade(label='File',menu=file_menu)

# EDIT MENU
edit_menu=Menu(main_menu,tearoff=0)
edit_menu.add_command(label='Undo')
edit_menu.add_command(label='Redo')
edit_menu.add_separator()
edit_menu.add_command(label='Cut')
edit_menu.add_command(label='Copy')
edit_menu.add_command(label='Paste')
main_menu.add_cascade(label='Edit',menu=edit_menu)

root.mainloop()