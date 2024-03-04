# Author:           Charles D. Maddux
# Date Created:     26 February 2024
# Description:      E6B Fuel Required Calculator
#                   Get Wind Data page
import subprocess
import requests
import tkinter as tk
from tkinter import ttk

ipv4 = '127.0.0.1'  # local host
port = 8080         # default port


def getWindData(test=0):
    print("Pheasants")
    # launch data exchange service
    def threadLaunch():
        subprocess.run(["python", "..\Aviation_Weather_API_Tool\windsaloft_microservice.py"])

    # declare & initialize window
    options = {"region": None, "low_altitude": None, "high_altitude": None, "flight_time": None, "flight_date": None}
    region = {"All Regions": "all", "North East": "bos", "South East": "mia", "North Central": "chi",
              "South Central": "dfw", "Rocky Mountain": "slc", "Pacific Coast": "sfo", "Alaska": "alaska",
              "Hawaii": "hawaii", "Western Pacific": "other_pac"}
    altitude = ["1000", "1500", "2000", "3000", "6000", "9000", "12000", "15000",
                "18000", "24000", "30000", "34000", "39000", "45000", "53000"]

    # set up GUI window
    wind_box = tk.Tk()
    wind_box.title("Winds and Temperature")
    wind_box.config(pady=3, padx=5)

    # calculate page size and placement
    x_coord = 20
    y_coord = 20
    wind_box.geometry("+%d+%d" % (x_coord, y_coord))

    # create the page menu
    menu = tk.Menu(wind_box)
    wind_box.config(menu=menu)
    # -----------------------------------------------------------------------------------------------------------------
    # the File dropdown
    filemenu = tk.Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='Home', command=wind_box.destroy)

    # -----------------------------------------------------------------------------------------------------------------
    # Region
    regionmenu = tk.Menu(menu)
    menu.add_cascade(label='Region', menu=regionmenu)

    def setRegion(region):
        options["region"] = region

    regionmenu.add_command(label="All Regions", command=lambda: setRegion(region["All Regions"]))
    regionmenu.add_separator()
    regionmenu.add_command(label="North East", command=lambda: setRegion(region["North East"]))
    regionmenu.add_separator()
    regionmenu.add_command(label="South East", command=lambda: setRegion(region["South East"]))
    regionmenu.add_separator()
    regionmenu.add_command(label="North Central", command=lambda: setRegion(region["North Central"]))
    regionmenu.add_separator()
    regionmenu.add_command(label="South Central", command=lambda: setRegion(region["South Central"]))
    regionmenu.add_separator()
    regionmenu.add_command(label="Rocky Mountain", command=lambda: setRegion(region["Rocky Mountain"]))
    regionmenu.add_separator()
    regionmenu.add_command(label="Pacific Coast", command=lambda: setRegion(region["Pacific Coast"]))
    regionmenu.add_separator()
    regionmenu.add_command(label="Alaska", command=lambda: setRegion(region["Alaska"]))
    regionmenu.add_separator()
    regionmenu.add_command(label="Hawaii", command=lambda: setRegion(region["Hawaii"]))
    regionmenu.add_separator()
    regionmenu.add_command(label="Western Pacific", command=lambda: setRegion(region["Western Pacific"]))
    # -----------------------------------------------------------------------------------------------------------------
    def goHome():
        """
        Command to close window and return to Home screen
        :return: none
        """
        # close the window
        print("Exiting ...")
        wind_box.destroy()

    # -----------------------------------------------------------------------------------------------------------------
    def callAPI(params):
        """
        Function to contact and send request to running microservice
        :param params:
        :return:
        """
        print("calling the server ...")

        # create call to microservice
        response = requests.get(f'http://{ipv4}:{port}/get_windsaloft', params=params)

        # handle successful response
        if response.status_code == 200:
            # process data and break into arrays
            data = response.json()
            labels = data["labels"]
            cells = data["data"]

            # print headers
            for label in labels:
                # pad values to get them to line in stdout
                while len(label) < 6:
                    label = label + ' '
                # new tab instead of newline - print for testing
                print(f"{label}", end="\t")
            print("")
            # break data into rows
            for row in cells:
                # filter non-relevant data
                if len(row) < len(labels):
                    pass
                # break into individual cells of data
                for value in row:
                    # pad values to get them to line in stdout
                    while len(value) < 6:
                        value = value + ' '
                    print(f"{value}", end="\t")
                print("")

            # add labels to buttons
            for val in range(len(labels)):
                ttk.Button(wind_box, padding=1, text=labels[val]).grid(column=val+2, row=1, padx=1, pady=1)
            # add values to cells
            for row in range(len(cells) - 1):
                for col in range(len(labels)):
                    ttk.Button(wind_box, padding=1, text=cells[row][col]).grid(column=col+2, row=row+2)

        # handle unsuccessful response
        elif response.status_code == 400:
            print(response.json()['error'])

        # handle errors
        else:
            # Unrecognized Response Code
            print(response.status_code)
            raise NotImplementedError

    # -----------------------------------------------------------------------------------------------------------------
    # home button
    home_btn = ttk.Button(wind_box, padding=4, text="Home", command=goHome)
    home_btn.grid(column=0, row=0, columnspan=2)
    # -----------------------------------------------------------------------------------------------------------------
    # Region menu
    reg = tk.StringVar(wind_box)
    reg.set("Select a Region")
    region_menu = tk.OptionMenu(wind_box, reg, *region)
    tk.Label(wind_box, text="Region").grid(column=0, row=1)
    region_menu.grid(column=0, row=2)

    def chooseRegion(*args):
        selected_region = region[reg.get()]
        options["region"] = selected_region

    reg.trace('w', chooseRegion)
    # -----------------------------------------------------------------------------------------------------------------
    # High Altitude menu
    hAlt = tk.StringVar(wind_box)
    hAlt.set("Select Altitude")
    hAlt_menu = tk.OptionMenu(wind_box, hAlt, *altitude)
    tk.Label(wind_box, text="High Altitude Limit").grid(column=0, row=3)
    hAlt_menu.grid(column=0, row=4)

    def chooseHighAlt(*args):
        selected_hAlt = hAlt.get()
        options["high_altitude"] = selected_hAlt
        print(selected_hAlt)

    hAlt.trace('w', chooseHighAlt)
    # -----------------------------------------------------------------------------------------------------------------
    # Low Altitude menu
    lAlt = tk.StringVar(wind_box)
    lAlt.set("Select Altitude")
    lAlt_menu = tk.OptionMenu(wind_box, lAlt, *altitude)
    tk.Label(wind_box, text="Low Altitude Limit").grid(column=0, row=5)
    lAlt_menu.grid(column=0, row=6)

    def chooseLowAlt(*args):
        selected_lAlt = lAlt.get()
        options["low_altitude"] = selected_lAlt
        print(selected_lAlt)

    lAlt.trace('w', chooseLowAlt)
    # -----------------------------------------------------------------------------------------------------------------
    tk.Label(wind_box, text=" ", font=10).grid(column=0, row=7)
    # call API button
    get_wind_btn = ttk.Button(wind_box, padding=4, text="Get Winds Aloft", command=lambda: callAPI(options))
    get_wind_btn.grid(column=0, row=8, columnspan=2, pady=5)
    # -----------------------------------------------------------------------------------------------------------------
    tk.Label(wind_box, text="Wind and Temperature Data", font=10).grid(column=2, row=0, columnspan=9, padx=45)

    # -----------------------------------------------------------------------------------------------------------------
    # testing - if testing, open GUI window without function call
    if test == 1:
        wind_box.mainloop()



def main():
    getWindData(1)


if __name__ == "__main__":
    main()
