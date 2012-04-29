import sys

class Application:
    '''Creates a GUI to interact with.'''
    def __init__(self):
        self.letters=[]
	self.w=self.get_file()
	for letter in self.w:
            letters.append(self.letter)
        for i in range(len(self.letters)):
    	    self.letters[i]=ord(self.letters[i])-97

    def get_file(self):
        ''' This function gets the data from a file and returns a string with the entire text. It takes a command line argument as the file name.'''
        '''make sure that when I read in, it makes everything caps'''
        if len(sys.argv)>1:
            filename = sys.argv[1]
        else:
            filename = raw_input("Filename (default has .txt extension): ")
        try:
                f = open(filename, "r")
        except IOError: # Deals with exceptions, such as if the file doesn't exist
                raise ValueError, 'Sorry, that filename does not exist. please reboot the program'
        all_text= f.read() # All the text in the file is read out to the file to a variable
        all_text=all_text.lower()
        tmp=''
        all_text=tmp.join(all_text.split(' '))
        return all_text

def main():
        '''Executes commands.'''

        app=Application()

if __name__=='__main__':
        main()
