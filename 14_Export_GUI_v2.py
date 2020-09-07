from tkinter import *
from functools import partial #To prevent unwanted windows
import re
import random


class Converter:
    def __init__(self, parent):
        
        #Formatting variables...
        background_color = "light blue"

        #In actual program this is blank and is populated iwth user calculations
        self.all_calc_list = ['1.0C = -17.2F', '2.0C = -16.7F', '3.0C = -16.1F', '4.0F = 39.2c', '6.0F = 42.8c', '50.0C = 10.0F', '2590.0F = 4694.0c', '2590.0C = 1421.1F']
        #self.all_calc_list = []

        #Converter Main Screen GUI...
        self.converter_frame = Frame(bg=background_color, padx=10, pady=10)
        self.converter_frame.grid()

        #Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter", font=("Arial", "16", "bold"), bg=background_color, padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        #history button (row 1)
        self.history_button = Button(self.converter_frame, bg=background_color, text="History", font=("Arial", "14"), padx=10, pady=10, command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=1)

        if len(self.all_calc_list) == 0:
            self.history_button.config(state=DISABLED)
    

    def history(self, calc_history):
        get_history = History(self, calc_history)


class History:
    def __init__(self, partner, calc_history):

        background = "#a9ef99" #pale green
        
        #Disable history button
        partner.history_button.config(state=DISABLED)

        #Sets up child window (ie: history box)
        self.history_box = Toplevel()
        #If users press cross at top, closes history and 'releases' history button
        self.history_box.protocol("WM_DELETE_WINDOW", partial(self.close_history, partner))

        #Set up GUI Frame
        self.history_frame = Frame(self.history_box, width=300, bg=background, padx=10, pady=10)
        self.history_frame.grid()

        #Set up history heading (row 0)
        self.history_heading = Label(self.history_frame, text="Calculation History", font=("Arial", "18", "bold"), bg=background, padx=10, pady=10)
        self.history_heading.grid(row=0)

        #history text (labe, row 1)
        self.history_text = Label(self.history_frame, text="Here are your most recent calculations. Please use the export button to create a text file of all your calculations for this session.", justify=LEFT, wrap=250, font=("Arial", "14"), bg=background, padx=10, pady=10)
        self.history_text.grid(row=1)

        #History Output goes here

        #Generate string from list of calculations...
        history_string = ""

        if len(calc_history) >= 7:
            for item in range(0,7):
                history_string += calc_history[len(calc_history)- item - 1] +"\n"
        else:
            for item in range(0, len(calc_history)):
                history_string += calc_history[len(calc_history)- item - 1] + "\n"
            self.history_text.config(text="Here is your calculation history. You can use the export button to save this data to a text file if desired. ")

        #History Label (row 2)
        self.history_label = Label(self.history_frame, text=history_string, bg=background, font=("Arial", "12"))
        self.history_label.grid(row=2)

        #Buttons (row 3)
        self.button_frame = Frame(self.history_frame)
        self.button_frame.grid(row=3)

        #Export button (column 1)
        self.export_button = Button(self.button_frame, text="Export", bg=background, font=("Arial", "14"), padx=10, pady=10, command=lambda: self.export(calc_history))
        self.export_button.grid(row=0, column=0)

        #Dismiss button
        self.dismiss_button = Button(self.button_frame, text="Dismiss", bg=background, font=("Arial", "14"), padx=10, pady=10, command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_history(self, partner):
        #Put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()
    
    def export(self, calc_history):
        get_export = Export(self, calc_history)
        
class Export:
    def __init__(self, partner, calc_history):

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
        self.export_text = Label(self.export_frame, text="Enter a filename in the box below and press the Save button to save your calculation history to a text file.", justify=LEFT, width=40, wrap=250, font=("Arial", "14"), bg=background, padx=10, pady=10)
        self.export_text.grid(row=1)

        #export warning (row 2)
        self.export_warning = Label(self.export_frame, text="If the filename you enter below alraedy exists, the conversions will be added underneath any previous existing text.", bg="#ff9999", padx=10, pady=10, font=("Arial", "12", "italic"), wrap=230)
        self.export_warning.grid(row=2)

        #Filename entry (row 3)
        self.filename_entry = Entry(self.export_frame)
        self.filename_entry.grid(row=3, padx=5, pady=5)

        #Error Label
        self.error_label = Label(self.export_frame, text="No Errors.", bg="white", font=("Arial", "14", "bold"), padx=10, pady=10)
        self.error_label.grid(row=4, padx=5, pady=5)

        #Save and cancel button frame
        self.save_cancel_frame = Frame(self.export_frame, padx=10, pady=10, bg=background)
        self.save_cancel_frame.grid(row=5)

        #Save button
        self.save_button = Button(self.save_cancel_frame, text="Save", bg=background, font=("Arial", "14"), padx=10, pady=10, command=partial(lambda: self.save_history(partner, calc_history)))
        self.save_button.grid(row=0, column=0)

        #Cancel button
        self.cancel_button = Button(self.save_cancel_frame, text="Cancel", bg=background, font=("Arial", "14"), padx=10, pady=10, command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, calc_history):
        filename = self.filename_entry.get()
        has_error = False

        valid_char = "[A-Za-z0-9_]"
        for letter in filename:
            if re.match(valid_char, letter):
                continue
        
            elif letter == " ":
                problem = "(no spaces allowed)"
            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = True
    
        if filename == "":
            problem = "can't be blank"
            has_error = True
    
        if has_error == True:
            self.error_label.config(text="Invalid filename - {}".format(problem), bg="#ff9999")
    
        else:
            self.error_label.config(text="No Errors.", bg="white")
            filename = filename + ".txt"
            save_file = open(filename, "a")
            for a_conversion in calc_history:
                save_file.write("\n" + str(a_conversion))
            save_file.close()

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