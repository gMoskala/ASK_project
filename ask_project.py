import re
import os

COLOR = {
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "ENDC": "\033[0m",
}
possible_commands = ["MOVE", "XCHG", "NOT"]
helper = [COLOR["BLUE"] + "MOVE [A] [B]" + COLOR["ENDC"], COLOR["BLUE"] + "XCHG [A] [B]" + COLOR["ENDC"]]
hex_numbers = "0 1 2 3 4 5 6 7 8 9 A B C D E F"
hex_tab = hex_numbers.split(" ")
res = []
for el in hex_tab:
    for el2 in hex_tab:
        for el3 in hex_tab:
            for el4 in hex_tab:
                res.append(el+el2+el3+el4)
# print(res)
def read_data():
    data = {
        'AH': '',
        'BH': '',
        'CH': '',
        'DH': '',
        'AL': '',
        'BL': '',
        'CL': '',
        'DL': '',
    }
    for el in data:
        while True:
            value = input(f"Podaj wartosc dla {el} ").upper()
            if len(value) <= 2 and re.search("[A-F0-9]{2}", value):
                data[el] = value
                break
            else:
                print("Wrong value")
    print("Your data looks: ", COLOR["BLUE"], data, COLOR["ENDC"])
    return data

def move_data(first, second):
    second = first
    return first, second

def xchg_data(first, second):
    temp = first
    first = second
    second = temp
    return first, second

def not_data():
    return 0

def run_again():
    while True:
        option = input("Do you want to run program again? (Y/N) ")
        if option.lower() in ["n", "no", "y", "yes"]:
            if option.lower() == "n" or option.lower() == "no":
                return False
            elif option.lower() == "y" or option.lower() == "yes":
                return True
        else:
            print(COLOR["RED"], "Unknown command", COLOR["ENDC"])

def main():
    run = True
    data = read_data()
    all_names = list(data.keys())
    while run:
        try:
            command = input("Give program command what you want to do ")
            command_data = command.split(" ")
            if command_data[0].upper() in possible_commands:
                if len(command_data) == 3:
                    first_variable = command_data[1].upper()
                    second_variable = command_data[2].upper()
                    if command_data[0].upper() == "MOVE":
                        if first_variable in all_names and second_variable in all_names:
                            data[first_variable], data[second_variable] = move_data(data[first_variable], data[second_variable])
                            print("Your data looks: ", COLOR["BLUE"], data, COLOR["ENDC"])
                            run = run_again()
                        else:
                            print(COLOR["RED"], f"Both values must be in  {all_names}", COLOR["ENDC"])
                    elif command_data[0].upper() == "XCHG":
                        if first_variable in all_names and second_variable in all_names:
                            data[first_variable], data[second_variable] = xchg_data(data[first_variable], data[second_variable])
                            print("Your data looks: ", COLOR["BLUE"], data, COLOR["ENDC"])
                            run = run_again()
                        else:
                            print(COLOR["RED"], f"Both values must be in  {all_names}", COLOR["ENDC"])
                    elif command_data[0].upper() == "NOT":
                        if first_variable in all_names and second_variable in all_names:
                            data[first_variable], data[second_variable] = xchg_data(data[first_variable], data[second_variable])
                            print("Your data looks: ", COLOR["BLUE"], data, COLOR["ENDC"])
                            run = run_again()
                        else:
                            print(COLOR["RED"], f"Both values must be in  {all_names}", COLOR["ENDC"])
                else:
                    print(COLOR["RED"], "Wrong number of variables. Two needed", COLOR["ENDC"])
            elif command == "--help":
                print("Possible commands: ", ' || '.join(helper))
            else:
                print(COLOR["RED"], "Unknown command. Type --help for possible commands", COLOR["ENDC"])
        except:
            break
    print("Exited program")


if __name__ == '__main__':
    main()


