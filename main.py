from tkinter import *
import tkinter as tk
import tkinter.font as font
import time
import threading
import traceback

class Addictions:
    
    Instances = []

    def __init__(self, name, day, hour, minute, second, root, x ,y):
        self.name = name
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.window = Tk()
        self.window.title("Countdown Timer")
        self.label = Label(self.window, font=("Helvetica", 48))
        self.label.pack()
        self.completed = False
        self.root = root
        Addictions.Instances.append(self)
        self.x = x
        self.y = y
        self.countdown()
        

    def countdown(self):  
        a = tk.BooleanVar()
        a.set(False)
        #print(a)
        #print(a.get())   

        myFont = font.Font(family='Helvetica', size=10, weight='bold')

        button_state = tk.StringVar()
        button_state.set('normal')

        button = tk.Button(self.root, text="Finish", command = lambda: (a.set(True), button.config(state= 'disabled')), font= myFont, height= 2, state= button_state.get())
        button.place(x=self.x, y=self.y)

        #if A.get() == True:
            #self.window.destroy()

        self.window.title(self.name)

        my_time = self.day * 24 * 60 * 60 + self.hour * 60 * 60 + self.minute * 60 + self.second
        for x in range(my_time, -2, -1):
            if x > -1 and a.get() == False:
                seconds = x % 60
                minutes = int(x/ 60) % 60
                hours = int(x/ 3600) % 24
                days = int(x/ (3600*24))
                printText = f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}"
                self.label.config(text=printText)
                self.window.update()
                time.sleep(1)
            
            elif a.get() == True:
                if my_time > 15000:
                    #self.window.after(0,self.destroy_window)
                    self.window.destroy()
                else:
                    self.schedule_destroy()

            else:
                label_completed = Label(self.window, text="Countdown Completed", font=("Cabrili", 50))
                label_completed.pack()
                button.config(state= 'disabled')
                #self.root.update()
                self.window.update()
                self.completed = True
                self.window.after(10000)
                self.window.destroy()
    
    def schedule_destroy(self):
        # This method is called to schedule window destruction in the main thread
        self.window.after(0, self.destroy_window)

    def destroy_window(self):
        # This method is called to destroy the window in the main thread
        self.window.destroy()
                

X_LABEL = 0
Y_LABEL = 150

X_BUTTON = 0
Y_BUTTON = 100
ARTAN = 0

COUNT_LABEL = 0
COUNT_BUTTON = 0


def create_label(x, y, addictant):
    #really, it's as simple as creating a label and adding it to the display
    #~ with grid, pack or place, within a function that is called by a button
    label = tk.Label(root, text=addictant, font=("Cabrili", 30))
    label.place(x=x,y=y)
    return label.winfo_width()


def clicked():
    global X_LABEL,Y_LABEL
    global X_BUTTON,Y_BUTTON
    global COUNT_LABEL,COUNT_BUTTON,ARTAN
    global Class
    

    timeCountdown = time_entry.get()
    addictant = time_entry2.get()

    time_values = timeCountdown.split(":")
    if len(time_values) == 4:
        COUNT_BUTTON += 1

        if COUNT_BUTTON == 10:
            ARTAN += 250
        
        X_BUTTON = create_label(X_LABEL,Y_LABEL,addictant) + ARTAN
        #print(X_BUTTON)
        #threading.Thread(target=Class.create_button(X_BUTTON+10, Y_BUTTON)).start()
        #Class.create_button(X_BUTTON+10, Y_BUTTON)
    
        #addictant = Addictions(addictant, int(time_values[0]), int(time_values[1]), int(time_values[2]), int(time_values[3]))
        
        #del Class
        
        Y_LABEL += 50
        Y_BUTTON += 50

        COUNT_LABEL += 1
        

        if COUNT_LABEL == 9:
        
            Y_LABEL = 150
            X_LABEL += 250

            COUNT_LABEL = 0
        
        if COUNT_BUTTON == 10:

            #ARTAN += 250
            Y_BUTTON = 150

            COUNT_BUTTON = 1
        
        try:
            Class = Addictions(addictant, int(time_values[0]), int(time_values[1]), int(time_values[2]), int(time_values[3]), root, X_BUTTON + 10, Y_BUTTON)
        except Exception as e:
            # Handle the exception gracefully
            traceback.print_exc()  # Log the exception
        #threading.Thread(target=Class.countdown(X_BUTTON+10, Y_BUTTON)).start()
        #threading.Thread(target=Class).start()

    else:
        print("Invalid time format. Please enter time in the format: dd:hh:mm:ss")

# Create a Tkinter window
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("1200x600")

label = Label(root, text="Please enter time for countdown: ", font=("Cabrili", 30))
label.place(x=10, y=15)
label2 = Label(root, text="Please enter the name of addictant: ", font=("Cabrili", 30))
label2.place(x=10, y=80)

# Create an entry widget to input time
time_entry = Entry(root, width=15, font=('calibre', 30, 'normal'))
time_entry.place(x=600, y=15)

time_entry2 = Entry(root, width=13, font=('calibre', 30, 'normal'))
time_entry2.place(x=650, y=80)

# Create a button to start the countdown
myFont = font.Font(family='Helvetica', size=20, weight='bold')
start_button = Button(root, text="Click Me", command=lambda: threading.Thread(target=clicked).start(), height=3)
start_button['font'] = myFont
start_button.place(x=950, y=13)

# Start the Tkinter main loop
root.mainloop()