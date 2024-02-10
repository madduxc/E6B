# Author:           Charles D. Maddux
# Date Created:     27 January 20224
# Description:      E6B Home Page
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk

# constants
TEXT_BOX_WIDTH      = 75
MENU_BUTTON_WIDTH   = 30
MAIN_BUTTON_WIDTH   = 20
TEXT_BOX_PADDING    = 10
MENU_BUTTON_PADDING = 10
MAIN_BUTTON_PADDING = 3

# declare & initialize variables
e6b = tk.Tk()
e6b.title("E6B")


def main():

    def homeScreen():
        instructions = "\n                         Welcome to the Desktop E6B Flight Computer.\n" \
                       " - Wind Correction Angle: determine the effect different winds will have on your flight path and\n" \
                       "    ground speed at different airspeeds.\n\n" \
                       " - Heading Correction: determine the flight path correction due to winds in flight.\n\n" \
                       " - Leg Time:  determine the time it will take to travel your leg distance at a given groundspeed.\n\n" \
                       " - Fuel Required: determine the amount of fuel for a given distance at a specified fuel burn.\n\n" \
                       " - Endurance: calculate your time aloft for a specific amount of fuel and a set rate of consumption.\n\n" \
                       " - Altitude: determine density altitude and pressure altitude for a specific elevation, temperature,\n\n" \
                       "   and barometer setting.\n\n" \
                       " - Conversions: perform useful conversions, like gallons to pounds for Avgas and Jet A.\n\n"
        text_box.config(width=TEXT_BOX_WIDTH, padding=TEXT_BOX_PADDING, text=instructions, font=10)

    # -----------------------------------------------------------------------------------------------------------------
    def legTime():

        def calculateLegTime():
            leg_time.delete(0,100)
            try:
                miles = int(distance.get())
                knots = int(speed.get())
                times = miles / knots * 60
                leg_time.insert(1, round(times, 1))
            except:
                leg_time.insert(1, "???")

        text_box.config(text='')
        dist = ttk.Label(text_box, text="Enter the distance of the Leg: ", font=10)
        dist.grid(column=0, row=0)

        distance = ttk.Entry(text_box, width=12)
        distance.insert(1, "")
        distance.grid(column=1, row=0)

        d_units = ttk.Label(text_box, text=" nm    ", font=10)
        d_units.grid(column=2, row=0)

        spd = ttk.Label(text_box, text="Enter the airspeed on the Leg: ", font=10)
        spd.grid(column=0, row=1)

        speed = ttk.Entry(text_box, width=12)
        speed.insert(1, "")
        speed.grid(column=1, row=1)

        s_units = ttk.Label(text_box, text=" kts   ", font=10)
        s_units.grid(column=2, row=1)

        btn = ttk.Button(text_box, padding=3, text="Calculate", command=calculateLegTime)
        btn.grid(column=1, row=2, columnspan=2)

        leg = ttk.Label(text_box, text="The time required the Leg is: ", font=10)
        leg.grid(column=4, row=0)

        leg_time = ttk.Entry(text_box, width=12)
        leg_time.insert(1, "")
        leg_time.grid(column=5, row=0)

        t_units = ttk.Label(text_box, text=" mins ", font=10)
        t_units.grid(column=6, row=0)

    # -----------------------------------------------------------------------------------------------------------------
    def fuelReq():

        def calculateFuelReq():
            fuel_used.delete(0,100)
            try:
                minutes = int(time_flown.get())
                consumption = float(fuel_flow.get())
                gallons = consumption * minutes / 60
                fuel_used.insert(1, round(gallons, 1))
            except:
                fuel_used.insert(1, "???")

        text_box.config(text='')
        time = ttk.Label(text_box, text="Enter the time flown: ", font=10)
        time.grid(column=0, row=0)

        time_flown = ttk.Entry(text_box, width=12)
        time_flown.insert(1, "")
        time_flown.grid(column=1, row=0)

        t_units = ttk.Label(text_box, text=" mins ", font=10)
        t_units.grid(column=2, row=0)

        flow = ttk.Label(text_box, text="Enter the fuel flow: ", font=10)
        flow.grid(column=0, row=1)

        fuel_flow = ttk.Entry(text_box, width=12)
        fuel_flow.insert(1, "")
        fuel_flow.grid(column=1, row=1)

        f_units = ttk.Label(text_box, text=" gal/hr ", font=10)
        f_units.grid(column=2, row=1)

        btn = ttk.Button(text_box, padding=3, text="Calculate", command=calculateFuelReq)
        btn.grid(column=1, row=2, columnspan=2)

        fuel = ttk.Label(text_box, text="Fuel used on this leg: ", font=10)
        fuel.grid(column=4, row=0)

        fuel_used = ttk.Entry(text_box, width=12)
        fuel_used.insert(1, "")
        fuel_used.grid(column=5, row=0)

        fuel_units = ttk.Label(text_box, text=" gal ", font=10)
        fuel_units.grid(column=6, row=0)


    # -----------------------------------------------------------------------------------------------------------------
    try:
        img = ImageTk.PhotoImage(file='images/engines.jpg')
    except:
        img = "engines image"

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
    text_box.grid(column=0, row=4, rowspan=5, columnspan=4)
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
