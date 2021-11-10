# Author: Jin Wu
# Date: 11-10-2021
# Description: Forest Population microservice

import csv
import os

STATE_PLANT_DICTIONARY = {
    "Alabama": "70.57%",
    "Alaska": "35.16%",
    "Arizona": "25.64%",
    "Arkansas": "56.31%",
    "California": "32.71%",
    "Colorado": "34.42%",
    "Connecticut": "55.24%",
    "Delaware": "27.26%",
    "Florida": "50.68%",
    "Georgia": "67.28%",
    "Hawaii": "42.53%",
    "Idaho": "40.55%",
    "Illinois": "13.64%",
    "Indiana": "21.06%",
    "Iowa": "8.43%",
    "Kansas": "4.78%",
    "Kentucky": "49.35%",
    "Louisiana": "53.20%",
    "Maine": "89.46%",
    "Maryland": "39.36%",
    "Massachusetts": "60.57%",
    "Michigan": "55.62%",
    "Minnesota": "34.08%",
    "Mississippi": "65.07%",
    "Missouri": "35.16%",
    "Montana": "27.45%",
    "Nebraska": "3.20%",
    "Nevada": "15.89%",
    "New Hampshire": "84.32%",
    "New Jersey": "41.72%",
    "New Mexico": "31.99%",
    "New York": "62.88%",
    "North Carolina": "59.73%",
    "North Dakota": "1.72%",
    "Ohio": "30.92%",
    "Oklahoma": "28.80%",
    "Oregon": "48.51%",
    "Pennsylvania": "58.60%",
    "Rhode Island": "54.38%",
    "South Carolina": "68.19%",
    "South Dakota": "3.93%",
    "Tennessee": "52.83%",
    "Texas": "37.33%",
    "Utah": "34.48%",
    "Vermont": "77.811%",
    "Virginia": "62.93%",
    "Washington": "52.74%",
    "Washington DC": "33.90%",
    "West Virginia": "79.01%",
    "Wisconsin": "48.98%",
    "Wyoming": "18.42%"
}


def check_valid_input_state(input_state):
    """
    takes a string as a input and check if the given state is in the state_directory and returns false
    """

    for state in STATE_PLANT_DICTIONARY.keys():
        if input_state.lower().strip() == state.lower():
            return True
    return False


def get_request():
    """
    reads forest_request.csv file and verify the input. Return the response based on the
    legitimacy of the input
    """

    try:
        with open("forest_request.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                input_state = line
    except FileNotFoundError as err:
        print(err)
        return

    if len(input_state) != 2 or not check_valid_input_state(input_state[1]):
        write_invalid()
        return

    return input_state[1]


def write_invalid():
    """
    Writes invalid request response
    """

    with open("forest_response.csv", 'w') as outfile:
        outfile.write("Invalid Request. Please check if the file name matches `forest_request.csv`"
                      " and if the data parameters match `State, <your requested state>`. "
                      "For example: State, Washington")


def write_valid(state, forest_percent):
    """
    Writes valid request response
    """
    with open("forest_response.csv", 'w') as outfile:
        outfile.write(state + ", " + str(forest_percent))


def delete_request_file():
    """
    Deletes the request file
    """
    try:
        os.remove("forest_request.csv")
    except FileNotFoundError:
        pass


# get State from request
if get_request():
    requested_state = get_request().strip()

    if check_valid_input_state(requested_state):
        forest_percentage = STATE_PLANT_DICTIONARY[requested_state]
        write_valid(requested_state, forest_percentage)

# remove request file
delete_request_file()


