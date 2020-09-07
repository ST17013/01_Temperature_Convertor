from tkinter import *
from functools import partial #To prevent unwanted windows

import random

class Convertor:
    def __init__(self):
        
        #Formatting Variables...
        background_color = "light blue"

        #Convert Main Screen GUI...
        self.convert_frame = Frame(width=600, height=600, bg=background_color, pady=10)
        self.convert_frame.grid()

        #Temperature Conversion Heading (row 0)
        self.temp_convertor_label = Label(self.convert_frame, text="Temperature Convertor", font=("Arial", "16", "bold"), bg=background_color, padx=10, pady=10)
        self.temp_convertor_label.grid(row=0)
        
        #Help button (row 1)
        self.help_button = Button(self.convert_frame, text="help", padx=10, pady=10, command=self.help)
        self.help_button.grid(row=1)

    
    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")


class Help:
    def __init__(self, partner):

        background = "orange"

        #disable help button
        partner.helpbutton.config(state=DISABLED)

#Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    convertor = Convertor()
    root.mainloop()