# Author:           Charles D. Maddux
# Date Created:     27 January 20224
# Description:      E6B Home Page
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk

# constants
TEXT_BOX_WIDTH      = 100
MENU_BUTTON_WIDTH   = 30
MAIN_BUTTON_WIDTH   = 20
TEXT_BOX_PADDING    = 10
MENU_BUTTON_PADDING = 10
MAIN_BUTTON_PADDING = 3

# declare & initialize variables
e6b = tk.Tk()
e6b.title("E6B")


def fuelReq():
    print("cows")


def main():

    def homeScreen():
        instructions = "\n                         Welcome to the Desktop E6B Flight Computer.\n" \
                       " - Wind Correction Angle: determine the effect different winds will have on your flight path and ground speed\n" \
                       "    at different airspeeds.\n" \
                       " - Heading Correction: determine the flight path correction due to winds in flight.\n" \
                       " - Leg Time:  determine the time it will take to travel your leg distance at a given groundspeed.\n" \
                       " - Fuel Required: determine the amount of fuel for a given distance at a specified fuel burn.\n" \
                       " - Endurance: calculate your time aloft for a specific amount of fuel and a set rate of consumption.\n" \
                       " - Altitude: determine density altitude and pressure altitude for a specific elevation, temperature, and\n" \
                       "   barometer setting.\n" \
                       " - Conversions: perform useful conversions, like gallons to pounds for Avgas and Jet A.\n"
        text_box.config(width=TEXT_BOX_WIDTH, padding=TEXT_BOX_PADDING, text=instructions)

    def legTime():
        print("ducks")
        dist = ttk.Label(text_box, text="Enter the distance of the Leg: ")
        # dist.pack(side='left')
        dist.grid(column=0, row=0)
        distance = ttk.Entry(text_box, width=15)
        distance.insert(1, "")
        #distance.pack(side='left')
        distance.grid(column=1, row=0)

    try:
        img = ImageTk.PhotoImage(file='images/engines.jpg')
    except:
        img = "engines image"

    # home = ttk.Frame(e6b, padding=10)
    text_box = ttk.Label(e6b)
    homeScreen()
    quit_btn    = ttk.Button(e6b, width=MAIN_BUTTON_WIDTH, padding=MAIN_BUTTON_PADDING, text="Quit", command=e6b.destroy)
    reset_btn   = ttk.Button(e6b, width=MAIN_BUTTON_WIDTH, padding=MAIN_BUTTON_PADDING, text="Reset")
    summary_btn = ttk.Button(e6b, width=MAIN_BUTTON_WIDTH, padding=MAIN_BUTTON_PADDING, text="View Summary")
    picture_window  = ttk.Label(e6b, width=TEXT_BOX_WIDTH, padding=TEXT_BOX_PADDING, image=img)
    wind_corr       = ttk.Button(e6b, width=MENU_BUTTON_WIDTH, padding=MENU_BUTTON_PADDING, text="Wind Correction Angle")

    heading_corr    = ttk.Button(e6b, width=MENU_BUTTON_WIDTH, padding=MENU_BUTTON_PADDING, text="Heading Correction")
    legtime         = ttk.Button(e6b, width=MENU_BUTTON_WIDTH, padding=MENU_BUTTON_PADDING, text="Leg Time", command=legTime)
    fuel_req        = ttk.Button(e6b, width=MENU_BUTTON_WIDTH, padding=MENU_BUTTON_PADDING, text="Fuel Requirements", command=fuelReq)
    endurance       = ttk.Button(e6b, width=MENU_BUTTON_WIDTH, padding=MENU_BUTTON_PADDING, text="Endurance")
    altitude        = ttk.Button(e6b, width=MENU_BUTTON_WIDTH, padding=MENU_BUTTON_PADDING, text="Altitude")
    convert         = ttk.Button(e6b, width=MENU_BUTTON_WIDTH, padding=MENU_BUTTON_PADDING, text="Conversions")

    # position the buttons
    e6b.grid()
    quit_btn.grid(column=0, row=0)
    reset_btn.grid(column=0, row=1)
    picture_window.grid(column=1, row=0, rowspan=3)
    text_box.grid(column=0, row=3, rowspan=5, columnspan=4)
    summary_btn.grid(column=3, row=0)
    wind_corr.grid(column=4, row=0)
    heading_corr.grid(column=4, row=1)
    legtime.grid(column=4, row=2)
    fuel_req.grid(column=4, row=3)
    endurance.grid(column=4, row=4)
    altitude.grid(column=4, row=5)
    convert.grid(column=4, row=6)

    # create the page menu
    menu = tk.Menu(e6b)
    e6b.config(menu=menu)
    filemenu = tk.Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='Save')
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=e6b.quit)

    # button state
    reset_btn.state([ 'disabled' ])
    summary_btn.state([ 'disabled' ])
    wind_corr.state([ 'disabled' ])
    heading_corr.state([ 'disabled' ])
    endurance.state([ 'disabled' ])
    altitude.state([ 'disabled' ])
    convert.state([ 'disabled' ])

    print(legtime.configure().keys())
    e6b.mainloop()

if __name__ == "__main__":
    main()
