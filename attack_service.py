# Author: Andrew Bear
# Date: 2021-10-23
# Description: Bear Attack microservice

import os


# Functions for file manipulation
def read_request():
    """
    reads request
    :return:
    """
    contents = str()
    input_file = open("attack_request.csv", "r")  # open up the file designated at run time
    for line in input_file:
        contents = contents + line.rstrip()
    input_file.close()

    input_state = contents.split(",")

    if len(input_state) != 2 or input_state[1] == "":
        write_invalid()
        print("Invalid Request Detected!!")
        return "Invalid Request Detected!!"

    request_state = input_state[1]

    if request_state[0] == " ":
        request_state = request_state[1::]

    return request_state


def write_invalid():
    """
    Writes invalid request response
    :return:
    """
    with open("attack_response.csv", 'w') as outfile:  # open outfile and dump json into it
        outfile.write("Invalid Request! Not enough parameters!")
    outfile.close()


def write_valid(state, percent, text):
    """
    Writes valid request response
    :return:
    """
    with open("attack_response.csv", 'w') as outfile:  # open outfile and dump json into it
        outfile.write(state + ", " + str(percent) + ", " + text)
    outfile.close()


def delete_request_file():
    """
    Deletes the request file.
    :return:
    """
    if os.path.exists("attack_request.csv"):
        os.remove("attack_request.csv")


# dictionary of population densities
state_dictionary = {
    "Alabama": 95,
    "Alaska": 1,
    "Arizona": 60,
    "Arkansas": 57,
    "California": 251,
    "Colorado": 52,
    "Connecticut": 741,
    "Delaware": 485,
    "Florida": 378,
    "Georgia": 177,
    "Hawaii": 222,
    "Idaho": 20,
    "Illinois": 231,
    "Indiana": 184,
    "Iowa": 55,
    "Kansas": 36,
    "Kentucky": 112,
    "Louisiana": 108,
    "Maine": 43,
    "Maryland": 618,
    "Massachusetts": 871,
    "Michigan": 175,
    "Minnesota": 68,
    "Mississippi": 63,
    "Missouri": 88,
    "Montana": 7,
    "Nebraska": 24,
    "Nevada": 26,
    "New Hampshire": 148,
    "New Jersey": 1218,
    "New Mexico": 17,
    "New York": 420,
    "North Carolina": 206,
    "North Dakota": 10,
    "Ohio": 284,
    "Oklahoma": 57,
    "Oregon": 41,
    "Pennsylvania": 286,
    "Rhode Island": 1021,
    "South Carolina": 162,
    "South Dakota": 11,
    "Tennessee": 160,
    "Texas": 105,
    "Utah": 36,
    "Vermont": 67,
    "Virginia": 212,
    "Washington": 107,
    "Washington DC": 11011,
    "West Virginia": 76,
    "Wisconsin": 106,
    "Wyoming": 6
}

# get State from request
requested_state = read_request()

# remove request file
delete_request_file()

# test if valid, if valid do math for risk
if requested_state not in state_dictionary:
    write_invalid()
else:
    bear_density = .14
    pop_density = state_dictionary[requested_state]
    bear_risk = (bear_density / pop_density) * 100
    bear_percent = round(bear_risk * 100, 2)

    # create risk text
    if bear_percent < 4.9:
        risk_text = "LOW"
    elif bear_percent < 8.5:
        risk_text = "MODERATE"
    elif bear_percent < 18.3:
        risk_text = "HIGH"
    elif bear_percent < 34:
        risk_text = "VERY HIGH"
    else:
        risk_text = "EXTREME"

    # write response to file
    write_valid(requested_state, bear_percent, risk_text)

