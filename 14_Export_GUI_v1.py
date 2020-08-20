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

        #export button (row 1)
        self.export_button = Button(self.converter_frame, bg=background_color, text="Export", font=("Arial", "14"), padx=10, pady=10, command=self.export)
        self.export_button.grid(row=1)
    

    def export(self):
        get_export = Export(self)


class Export:
    def __init__(self, partner):

        background = "#80ff80"
        
        #Disable export button
        partner.export_button.config(state=DISABLED)

        #Sets up child window (ie: export box)
        self.export_box = Toplevel()
        #If users press cross at top, closes export and 'releases' export button
        self.export_box.protocol("WM_DELETE_WINDOW", partial(self.close_export, partner))

        #Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background, padx=10, pady=10)
        self.export_frame.grid()

        #Set up export heading (row 0)
        self.export_heading = Label(self.export_frame, text="Exporting to a Text File", font=("Arial", "18", "bold"), bg=background, padx=10, pady=10)
        self.export_heading.grid(row=0)

        #export text (labe, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename in the box below and press the SAve button to save your calculation history to a text file.", justify=LEFT, width=40, wrap=250, font=("Arial", "14"), bg=background, padx=10, pady=10)
        self.export_text.grid(row=1)

        #export warning (row 2)
        self.export_warning = Label(self.export_frame, text="If the filename you enter below alraedy exists, its contents will be replaced with your calculation history.", bg="#ff9999", padx=10, pady=10, font=("Arial", "12", "italic"), wrap=230)
        self.export_warning.grid(row=2)

        #Save and cancel button frame
        self.save_cancel_frame = Frame(self.export_frame, padx=10, pady=10, bg=background)
        self.save_cancel_frame.grid(row=3)

        #Save button
        self.save_button = Button(self.save_cancel_frame, text="Save", bg=background, font=("Arial", "14"), padx=10, pady=10)
        self.save_button.grid(row=0, column=0)

        #Dismiss button (row 3)
        self.dismiss_button = Button(self.save_cancel_frame, text="Dismiss", bg=background, font=("Arial", "14"), padx=10, pady=10, command=partial(self.close_export, partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_export(self, partner):
        #Put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()
        

#Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()