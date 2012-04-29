'''''' 

__author__ = 'Stephen'
__version__ = '1.0'

from Crypt import Crypt
import Tkinter 
from tkSimpleDialog import *

class Application:
    '''Creates a GUI to interact with.'''
    def __init__(self,master):
        '''Initializes the GUI.'''
        master.title("Crypt")
        self.index=0
        self.encrypt='e'
        top_frame = Frame(master)
        top_frame.pack(fill=X, expand=1)
        
        self.get_file = Button(top_frame, text="Load a file", command=self.get_file)
        self.get_file.pack(side=LEFT, fill=X)

        self.shift_button = Button(top_frame, text="Shift Substitution", command=self.shift) 
        self.shift_button.pack(side=RIGHT, fill=X)

        self.multi_button = Button(top_frame, text="Multiplicative Substitution", command=self.multi) 
        self.multi_button.pack(side=RIGHT, fill=X)
        self.encrypt_button = Button(top_frame, text="Encrpyt or Decrypt?", command=self.en) 
        self.encrypt_button.pack(fill=X)
        
        self.entry = Entry(self, width=10)
#        self.entry.pack(fill=X)


        bottom_frame = Frame(master)

        bottom_frame.pack(fill=X,expand=1)

    def en(self):
        if self.encrypt=='e':
            self.encrypt='d'
        else:
            self.encrpyt='e'
        print self.encrypt

    def get_file(self):
        self.crypt=Crypt()
    def shift(self):
        #Dialogue here to ask for shifts
        self.crypt.shift(40, self.encrypt)
        print self.crypt
    def multi(self):
        #Dialogue here to ask for shifts
        self.crypt.multiply(3, self.encrypt)
        print self.crypt

def main():
    '''Executes commands from the webImage class.'''
    root = Tk()
    app=Application(master=root)
    root.mainloop()
if __name__=='__main__':
    main()
