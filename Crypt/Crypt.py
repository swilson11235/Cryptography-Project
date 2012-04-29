'''Designed to decrypt and encrpyt shift, multiplicative, and affine ciphers. Can graph letter distributions.'''
__author__ = "Stephen Wilson"
__date__ = "4/25/12"

import sys,string
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pylab import *

class Crypt:
    '''A class with basic functions for getting messages, encrpyting and decrypting shift, multiplicative, and affine ciphers, and generating graphs of letter frequencies.'''
    def __init__(self,filename=''):
	self.get_file(filename)

    def __str__(self):
        return self.message

    def process_text(self,all_text):
        '''Processes text by ensuring uniform case and removing spaces.'''
        all_text=all_text.lower()
        tmp=''
        all_text=tmp.join(all_text.split(' '))
        all_text=tmp.join(all_text.split(chr(10)))
        self.letters=[]
        self.numbers=[]
        self.message=''

        for letter in all_text:
            self.letters.append(letter)
        for i in range(len(self.letters)):
            self.numbers.append(ord(self.letters[i])-96)
        self.message=self.message.join(self.letters)

    def get_file(self,filename=''):
        '''This function gets the data from a file or from the user. It takes a command line argument as the file name.'''
        if filename=='':
            c=raw_input("Would you like to manually enter the text or open a file? (m=manual, f=file)")
            if c=='f':
                filename = raw_input("Filename (default has .txt extension): ")
                try:
                    f = open(filename, "r")
                except IOError:
                    raise ValueError, 'Sorry, that filename does not exist. please reboot the program'
                all_text= f.read()
            else:
                all_text=raw_input("Enter it now: ")
        else:
            try:
                f = open(filename, "r")
            except IOError:
                raise ValueError, 'Sorry, that filename does not exist. please reboot the program'
            all_text= f.read() 
        self.process_text(all_text)

    def shift(self,number,c='e'):
        '''Defines a shift substitution according to: number=shift substitution number, c is set to "e" by default to signify encrpytion. For decryption, set c="d"'''
        if c=='d':
            number=-number
        for i in range(len(self.numbers)):
            self.numbers[i]=(self.numbers[i]+number)%26
            if self.numbers[i]==0:
                self.numbers[i]=26
            self.letters[i]=chr(self.numbers[i]+96)
        tmp=''
        self.message=tmp.join(self.letters)  

    def modInv(self,a, n):
        """modInv(a, n) -> Calculate modular inverse of a (mod n)"""
        a %= n
        if not n%a: return None
        for i in range(1,n):
            if (a*i)%n == 1:
                return i 

    def multiply(self,number,c='e'):
        '''Defines a multiplicative substitution according to: number=multiplicative substitution number, c is set to "e" by default to signify encrpytion. For decryption, set c="d"'''
        if c=='d' and number!=1:
            number=self.modInv(number,26)
        print number
        for i in range(len(self.numbers)):
            self.numbers[i]=(self.numbers[i]*number)%26
            if self.numbers[i]==0:
                self.numbers[i]=26
            self.letters[i]=chr(self.numbers[i]+96)
        tmp=''
        self.message=tmp.join(self.letters)

    def affine(self,b,m,c='e'):
        '''Defines an affine substitution according to: b=shift substitution number, m=multiplicative substitution number, c is set to "e" by default to signify encrpytion. For decryption, set c="d"'''
        if c=='d':
            m=self.modInv(m,26)
            b=(-b*m)%26
        print "slope: "+str(m)
        print "shift: "+str(b)
        for i in range(len(self.numbers)):
            self.numbers[i]=((self.numbers[i]*m)+b)%26
            if self.numbers[i]==0:
                self.numbers[i]=26
            self.letters[i]=chr(self.numbers[i]+96)
        tmp=''
        self.message=tmp.join(self.letters)

    def letter_frequency(self):
        '''Graphs the letter frequency.'''
        print 'The length of the message is: '+str(len(self.message))
        array=[]
        array2=[]
        letterarray=[]
        freq='The Frequency of Letters is: \n'
        for i in range(26):
            array.append(0)
        for i in range(26):
            array2.append(i+1)
        for item in string.lowercase:
            letterarray.append(item)
        for number in self.numbers:
            array[number-1]=array[number-1]+1
        for i in range(26):
            freq+= chr(i+97)+':  '+str(array[i])+'\n'
        g = open('tmp.txt', "w")
        g.write(freq)

        ax = plt.gca()
        ax.set_xticks(array2)
        ax.set_xticklabels(letterarray)

        plt.plot(array2,array,'bs')
        plt.xlabel('Letters')
        plt.ylabel('Occurances')
        plt.title('Discrete Plot of Letter Frequency')
        plt.grid(True)
        plt.show()


def choice(d,app):
    '''Allows the user to choose what encryption or decryption to use.'''
    if d=='l':
        app.letter_frequency()
    else:
        m=2
        c = raw_input("Method (s=shift,m=multiplicative,a=affine): ")
        if c=='s':
            s=raw_input("Shift by how much (integer please): ")
            app.shift(int(s),d)
        if c=='m':
            while int(m)%2!=1 and m!='q':
                m=raw_input("Multiply by how much (odd integer and not 13 please): ")
            app.multiply(int(m),d)
        if c=='a':
            s=raw_input("Shift by how much (integer please): ")
            while int(m)%2!=1 and m!='q':
                m=raw_input("Multiply by how much (odd integer and not 13 please): ")

            app.affine(int(s),int(m),d)
        print app

def main():
        '''Creates and manipulates a Crypt class.'''
        if len(sys.argv)>1:
            app=Crypt(sys.argv[1])
        else:
            app=Crypt()
        print app
        d = raw_input("\nWhat do you want to do? \ne=encrypt,d=decrypt,l=letter frequency,n=new message,q=quit: ")        
        while d!='q':
            if d=='n':
                app.get_file()
                print app
            else:
                choice(d,app)
            d = raw_input("\nWhat do you want to do? \ne=encrypt,d=decrypt,l=letter frequency,n=new message,q=quit: ")        

if __name__=='__main__':
        main()
