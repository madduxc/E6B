# Author:           Charles D. Maddux
# Date Created:     9 March 2024
# Description:      E6B Calculator
#                   Conversions page

import tkinter as tk
from tkinter import ttk
from Utilities import goHome

def runConversions(test=0):

    # declare & initialize window
    convert = tk.Tk()
    convert.title("Conversion Toolbox")
    width = 770
    height = 125

    # create the page menu
    menu = tk.Menu(convert)
    convert.config(menu=menu)
    filemenu = tk.Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='Home', command=lambda: goHome(convert))
    # -----------------------------------------------------------------------------------------------------------------

    # -----------------------------------------------------------------------------------------------------------------
    # home button
    home_btn = ttk.Button(convert, padding=4, text="Home", command=lambda: goHome(convert))
    home_btn.grid(column=0, row=0, columnspan=2)
    # -----------------------------------------------------------------------------------------------------------------
    # fuel conversions
    # -----------------------------------------------------------------------------------------------------------------
    fuel = ttk.Label(convert, text="Fuel Conversions: ", padding=3, font=10)
    fuel.grid(column=0, row=1, columnspan=2)

    # Fuel Type menu
    fuels = {"100L": 6.0, "Jet-A": 6.7}
    gas = tk.StringVar(convert)
    gas.set("Select a Fuel Type")
    region_menu = tk.OptionMenu(convert, gas, *fuels)
    tk.Label(convert, text="Fuel Type", font=10).grid(column=0, row=2)
    region_menu.grid(column=1, row=2, columnspan=2)
    options = dict()

    def selectWeight(*args):
        options["fuel"] = gas.get()
        options["weight"] = fuels[gas.get()]
        print(options)

    gas.trace_add('write', selectWeight)
    # -----------------------------------------------------------------------------------------------------------------
    # fuel weight entry
    # -----------------------------------------------------------------------------------------------------------------
    wt = ttk.Label(convert, text="Weight: ", padding=1, font=10)
    wt.grid(column=0, row=3)

    weight = ttk.Entry(convert, width=8, font=10)
    weight.insert(1, "")
    weight.grid(column=1, row=3)

    w_units = ttk.Label(convert, text=" lb    ", font=10)
    w_units.grid(column=2, row=3)

    # -----------------------------------------------------------------------------------------------------------------
    def convertToGallons(*args):
        try:
            gas_wt = options["weight"]
            pounds = float(weight.get())
            gallons = pounds / gas_wt
            amount.delete(0, 100)
            amount.insert(1, round(gallons, 1))
        except:
            print("Nope")

    go_btn1 = ttk.Button(convert, padding=2, text="Go", command=convertToGallons)
    go_btn1.grid(column=3, row=3)
    # -----------------------------------------------------------------------------------------------------------------
    # fuel weight entry
    # -----------------------------------------------------------------------------------------------------------------
    amt = ttk.Label(convert, text="Quantity: ", padding=1, font=10)
    amt.grid(column=0, row=4)

    amount = ttk.Entry(convert, width=8, font=10)
    amount.insert(1, "")
    amount.grid(column=1, row=4)

    a_units = ttk.Label(convert, text=" gal    ", font=10)
    a_units.grid(column=2, row=4)

    # -----------------------------------------------------------------------------------------------------------------
    def convertToPounds(*args):
        try:
            gas_wt = options["weight"]
            gallons = float(amount.get())
            pounds = gallons * gas_wt
            weight.delete(0, 100)
            weight.insert(1, round(pounds, 1))
        except:
            print("Nope")

    go_btn2 = ttk.Button(convert, padding=2, text="Go", command=convertToPounds)
    go_btn2.grid(column=3, row=4)
    # -----------------------------------------------------------------------------------------------------------------

    if test == 1:
        print("In development - Converter")
        convert.mainloop()


def main():
    """
    testing
    :return: none
    """
    runConversions(1)


if __name__ == "__main__":
    main()
