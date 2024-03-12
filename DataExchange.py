# Author:           Charles D. Maddux
# Date Created:     11 February 2024
# Description:      Handle calls from E6B to save, clear, and retrieve data

import json

# constants
SAVE_FILE = "eb6_data.json"

def clearData():
    """
    Function to clear the data from json file and insert placeholder to prevent errors
    :return: none
    """

    # declare & initialize variables
    data = dict()

    # open the .json file
    try:
        with open(SAVE_FILE, "w") as data_file:
            # clear the file
            data_file.truncate()
            data["a"] = 0
            d_val = json.dumps(data)
            data_file.write(d_val)
            data_file.close()

    # handle a missing or inaccessible file
    except FileNotFoundError:
            print("File cannot be opened.")


def saveData(key, pair, test=False):
    """
    Takes in key: value pairs of data, reads existing .json file, appends the dictionary, and overwrites the file
    :param key:     (str)           - parameter value for the .json/dictionary
    :param pair:    (int or float)  - calculated value for the parameter
    :param test:    (bool)          - used for testing. Set to True to print .json values in the terminal
    :return: none
    """

    # open the .json file
    try:
        with open(SAVE_FILE, "r+") as data_file:
            # populate the dictionary
            data = json.load(data_file)
            data_file.close()

    # handle a missing or inaccessible file
    except FileNotFoundError:
        print("File cannot be opened.")

    # add or overwrite the value in the dictionary
    data[key] = pair

    # test only
    if test:
        print(data)

    # open the .json file
    try:
        with open("eb6_data.json", "w") as data_file:
            # write dictionary to .json
            d_val = json.dumps(data)
            data_file.write(d_val)
            data_file.close()

    # handle a missing or inaccessible file
    except FileNotFoundError:
        print("File cannot be opened.")


def getData(key):
    """
    Function to retrieve specific value from the data file, given its json key
    :param key:     (str)   dictionary key
    :return: value  (float) dictionary value
    """

    # open the .json file
    try:
        with open(SAVE_FILE, "r") as data_file:
            # populate the dictionary
            try:
                data = json.load(data_file)
                data_file.close()
                return data[key]
            except:
                return 0

    # handle a missing or inaccessible file
    except FileNotFoundError:
        print("File cannot be opened.")


def getResultSummary():
    """
    Returns collection of all saved dictionary values from file to calling function
    :return: (dict) -   data
    """

    # open the .json file
    try:
        with open(SAVE_FILE, "r") as data_file:
            # populate the dictionary
            data = json.load(data_file)
            data_file.close()
            return data

    # handle a missing or inaccessible file
    except FileNotFoundError:
        print("File cannot be opened.")


def main():
    """
    Test file to verify output of the function
    :return: none
    """
    saveData("testKey1", 999, True)
    saveData("testKey2", 42, True)
    saveData("testKey3", 2319, True)
    saveData("testKey1", 0, True)


if __name__ == "__main__":
    main()
