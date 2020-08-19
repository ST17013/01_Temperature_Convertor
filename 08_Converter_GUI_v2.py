from tkinter import *
from functools import partial #To prevent unwanted windows
import random


class Converter:
    def __init__(self):

        #Fromatting variables
        background_color = "light blue"

        #Converter Frame
        self.converter_frame = Frame(width=300, bg=background_color, pady=10)
        self.converter_frame.grid()

        #Temperature Converter Heading (row 0)
        self.temp_heading_label = Label(self.converter_frame, text="Temperature converter", font="Arial 19 bold", bg=background_color, padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        #User insturctions (row 1)
        self.temp_instructions_label = Label(self.converter_frame, text="Type ini the amount to be converted and then push one of the buttons below...", font="Arial 10 italic", wrap=290, justify=LEFT, bg=background_color, padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        #Temperature etnry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20, font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        #Conversion buttons frame (row 3)
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame, text="To Centrigrade", font="Arial 10 bold", bg="#C3B091", padx=10, pady=10, command=lambda: self.temp_convert(-459)) #background colour Khakil
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame, text="To Fahrenheit", font="arial 10 bold", bg="Orchid1", padx=10, pady=10, command=lambda: self.temp_convert(-237))
        self.to_f_button.grid(row=0, column=1)

        #Conversion output (row 4)
        self.conversion_output = Label(self.converter_frame, font="Arial 18 bold", text="Conversion goes here", bg=background_color, padx=10, pady=10)
        self.conversion_output.grid(row=4)

        #History / Help button frame (row 5)
        self.nav_buttons = Frame(self.converter_frame, bg=background_color)
        self.nav_buttons.grid(row=5)

        self.history_button = Button(self.nav_buttons, text="History", font="Arial 10 bold", bg="light grey", padx=10, pady=10)
        self.history_button.grid(row=0, column=0)

        self.help_button = Button(self.nav_buttons, text="Help", font="Arial 10 bold", bg="light grey", padx=10, pady=10)
        self.help_button.grid(row=0, column=1)
    
    def temp_convert(self, to):

        error = "#ffafaf" # Pale pink background for when entry box has errors

        #Retrieve amount entered into Entry field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
        
            #Check amount is a valid nmber
            if to_convert < to:
                self.conversion_output.config(text="Too Cold!")
                self.to_convert_entry.config(bg=error)
            else:
                
                #Convert to F
                if to == -237:
                    output_temp = (to_convert *9/5) +32

                #Convert to C
                if to == -459:
                    output_temp = (to_convert - 32) / (9/5)

                #Round
                if output_temp%1 != 0:
                    output_temp = round(output_temp, 1)
                else:
                    int(output_temp)

                #Display answer
                if to == -459:
                    self.conversion_output.config(text="{}F = {}C".format(to_convert, output_temp), fg="black")
                    self.to_convert_entry.config(bg="white")
                else:
                    self.conversion_output.config(text="{}C = {}F".format(to_convert, output_temp), fg="black")
                    self.to_convert_entry.config(bg="white")

                #Add Answer to list for History


        except ValueError:
            self.conversion_output.config(text="Enter a number!", fg="red")
            self.to_convert_entry.config(bg=error)
    

#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()