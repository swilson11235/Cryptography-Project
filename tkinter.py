'''Interfaces with the Crypt class and creates a GUI.''' 

__author__ = 'Stephen'
__version__ = '1.0'

from Crypt import Crypt
import os
from Tkinter import *
from tkSimpleDialog import *
from tkFileDialog import *
from tkMessageBox import *


class Application:
    '''Creates a GUI to interact with.'''
    def __init__(self,master):
        '''Initializes the GUI.'''
        self.crypt=''
        self.encrypt='e'
        self.orig=''
        self.shif=StringVar()
        self.mult=StringVar()
        self.code=StringVar()

        master.title("Crypt")
	self.makeMenuBar(master)

        top_frame = Frame(master)
        top_frame.pack(fill=X, expand=1)

        self.label =Label(top_frame, text='Enter a code here or open a file:')
        self.label.pack(side=LEFT)

        self.go=Button(top_frame, text="Ok",command=self.code_to_file,default=ACTIVE)
        self.go.pack(side=RIGHT)
        self.entry = Entry(top_frame, width=50, textvariable=self.code)
        self.entry.pack(side=RIGHT)


	self.mainPart = Text(master,
			background = 'white',
			padx = 20,
			pady = 20)
	self.mainPart.pack(fill = 'both', expand = 1)
        mid_frame = Frame(master)
        mid_frame.pack(fill=X, expand=1)
        

        bottom_frame = Frame(master)

        bottom_frame.pack(fill=X,expand=1)
        self.shift_button = Button(mid_frame, text="Shift Substitution:\nC=P+b", command=self.shift) 
        self.shift_button.pack(side=LEFT,fill=X)
        
        self.multi_button = Button(mid_frame, text="Multiplicative Substitution:\nC=mP", command=self.multi) 
        self.multi_button.pack(side=RIGHT,fill=X)


        self.v=StringVar()
        self.v.set('e')
        self.encrypt_button = Radiobutton(mid_frame, text="Encrpyt", variable=self.v,value='e',command=self.en) 
        self.encrypt_button.pack(anchor=S)
        self.encrypt_button = Radiobutton(mid_frame, text="Decrpyt",variable=self.v,value='d',command=self.en) 
        self.encrypt_button.pack(anchor=S)
        Label(text='Amount to Shift(b)').pack(side=LEFT)
        self.shift_entry=Entry(bottom_frame,textvariable=self.shif,justify=CENTER)
        self.shift_entry.pack(side=LEFT)
        self.shift_entry.insert(ANCHOR,'1')
        Label(text='Amount to Multiply(m)').pack(side=RIGHT)
        self.mult_entry=Entry(bottom_frame,textvariable=self.mult,justify=CENTER)
        self.mult_entry.pack(side=RIGHT)
        self.mult_entry.insert(ANCHOR,'3')

        self.affine_button = Button(bottom_frame, text="Affine Substitution:\nC=mP+b", command=self.affine) 
        self.affine_button.pack(side=BOTTOM,fill=X)
        
        self.letterfrequency=Button(master, text='Display Letter Frequency', command=self.letters)
        self.letterfrequency.pack(side=BOTTOM)
        self.entry.bind('<Return>', self.code_to_file)


    def code_to_file(self,*args):
        g = open('tmp.txt', "w")
        g.write(self.code.get())
        g.close()
        self.crypt=Crypt('tmp.txt')
        os.remove('tmp.txt')
        self.orig=self.crypt.get_message()
        self.mainPart.delete(0.0,self.mainPart.index(END))
        self.mainPart.insert("%d.%d" % (0, 0),self.crypt)
        self.mainPart.insert("%d.%d" % (0, 0),'\n')

    def makeMenuBar(self,frame):
        menubar = Frame(frame,relief=RAISED,borderwidth=1)
        menubar.pack(fill=X)
		
        mb_file = Menubutton(menubar,text='File')
        mb_file.pack(side=LEFT)
        mb_file.menu = Menu(mb_file)
        mb_file.menu.add_command(label="Load a file", command=self.get_file)
        mb_file.menu.add_command(label="Save", command=self.save_file)
        mb_file.menu.add_command(label='Quit', command=quit)
        
#		mb_edit = Menubutton(menubar,text='edit')
#		mb_edit.pack(side=LEFT)
#		mb_edit.menu = Menu(mb_edit)
#		mb_edit.menu.add_command(label='copy')
#		mb_edit.menu.add_command(label='paste')
		
        mb_help = Menubutton(menubar,text='Help')
        mb_help.pack(padx=25,side=RIGHT)
        mb_help.menu = Menu(mb_help)
        mb_help.menu.add_command(label="Instructions", command=self.help)

        mb_file['menu'] = mb_file.menu
        mb_help['menu'] = mb_help.menu

    def help(self):
        print 'TO BE MADE. POP UP HELP'

    def en(self):
        self.encrypt=self.v.get()

    def get_file(self):
        filename = askopenfilename(filetypes=[("Code files","*.txt"),("All files","*")])
        self.crypt=Crypt(filename)
        self.orig=self.crypt.get_message()
        self.mainPart.delete(0.0,self.mainPart.index(END))
        self.mainPart.insert("%d.%d" % (0, 0),self.crypt) 
        self.mainPart.insert("%d.%d" % (0, 0),'\n')
    
    def save_file(self):
        filename = asksaveasfilename(filetypes=[("Code files","*.txt"),("All files","*")])
        g = open(filename, "w")
        g.write(self.crypt.get_message())
        g.close()

    def shift(self):
        if self.crypt!='':
            self.crypt.shift(int(self.shif.get()), self.encrypt)
            self.mainPart.delete(0.0,self.mainPart.index(END))
            self.mainPart.insert("%d.%d" % (0, 0),self.orig)
            self.mainPart.insert("%d.%d" % (0, 0),'\n')
            self.mainPart.insert(0.0,self.crypt)

    def multi(self):
        if self.crypt!='':
            if int(self.mult.get())%2!=0 and int(self.mult.get())!=13:
                self.crypt.multiply(int(self.mult.get()), self.encrypt)
                self.mainPart.delete(0.0,self.mainPart.index(END))
                self.mainPart.insert("%d.%d" % (0, 0),self.orig)
                self.mainPart.insert("%d.%d" % (0, 0),'\n')
                self.mainPart.insert(0.0,self.crypt)

    def affine(self):
        if self.crypt!='':
            if int(self.mult.get())%2!=0 and int(self.mult.get())!=13:
                self.crypt.affine(int(self.shif.get()),int(self.mult.get()), self.encrypt)
                self.mainPart.delete(0.0,self.mainPart.index(END))
                self.mainPart.insert("%d.%d" % (0, 0),self.orig)
                self.mainPart.insert("%d.%d" % (0, 0),'\n')
                self.mainPart.insert(0.0,self.crypt)

    def letters(self):
        if self.crypt!='':
            self.crypt.letter_frequency()

def main():
    '''Executes commands from the webImage class.'''
    root = Tk()
    app=Application(master=root)
    root.mainloop()
if __name__=='__main__':
    main()
