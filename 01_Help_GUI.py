from tkinter import *
from functools import partial #To prevent unwanted windows


import random

class Converter:
    def __init__(self, parent):
        
        #Formatting variables...
        background_color = "light blue"

        #Converter Main Screen GUI...
        self.converter_frame = Frame(bg=background_color, padx=10, pady=10)
        self.converter_frame.grid()

        #Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter", font=("Arial", "16", "bold"), bg=background_color, padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        #Help button (row 1)
        self.help_button = Button(self.converter_frame, bg=background_color, text="Help", font=("Arial", "14"), padx=10, pady=10, command=self.help)
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

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")


class Help:
    def __init__(self, partner):

        background = "orange"
        
        #Disable help button
        partner.help_button.config(state=DISABLED)

        #Sets up child window (ie: help box)
        self.help_box = Toplevel()
        #If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol("WM_DELETE_WINDOW", partial(self.close_help, partner))

        #Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background, padx=10, pady=10)
        self.help_frame.grid()

        #Set up Help heading (row 0)
        self.help_heading = Label(self.help_frame, text="Help", font=("Arial", "18", "bold"), bg=background, padx=10, pady=10)
        self.help_heading.grid(row=0)

        #Help text (labe, row 1)
        self.help_text = Label(self.help_frame, text="Help goes here", justify=LEFT, width=40, wrap=250, font=("Arial", "14"), bg=background, padx=10, pady=10)
        self.help_text.grid(row=1)

        #Dismiss button (row 2)
        self.dismiss_button = Button(self.help_frame, text="Dismiss", bg=background, font=("Arial", "14"), padx=10, pady=10, command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2)

    def close_help(self, partner):
        #Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()
        

#Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    convertor = Convertor()
    root.mainloop()