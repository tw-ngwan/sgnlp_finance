"""Gets all necessary inputs from user"""

def inputNum(text="Input a number: ", min=-float("inf"), max=float("inf")):
    while True:
        text_num = "text"
        try:
            text_num = input(text)
            num = float(text_num)
            if min <= num <= max:
                break 
            raise ValueError
        except ValueError:
            print("{} is not a number within the range [{}, {}]!".format(text_num, min, max))
            continue 
    return num 


def inputInt(text="Input an integer: ", min=-float("inf"), max=float("inf")):
    while True:
        text_num = "text"
        try:
            text_num = input(text)
            int_num = int(text_num)
            float_num = float(text_num)
            if not -0.1 < int_num - float_num < 0.1:
                raise ValueError
            if min <= int_num <= max:
                break 
            raise ValueError
        except ValueError:
            print("{} is not an integer within the range [{}, {}]!".format(text_num, min, max))
            continue 
    return int_num 

def inputString(text="Input a string: "):
    while True:
        try: 
            message = input(text)
            break
        except ValueError as e:
            print(str(e))
            continue 
    return message

def inputYesNo(text="Input yes or no (y/n): ", yes_options=None, no_options=None):
    while True:
        if yes_options is None:
            yes_options = ['y', 'yes', 'true', 'yes.', 'yy', 'y.']
        if no_options is None:
            no_options = ['n', 'no', 'false', 'no.', 'nn', 'n.']
        user_result = input(text)
        if not (user_result in yes_options or user_result in no_options):
            print("{} is not an appropriate option ({} for yes, {} for no)".format(user_result, '/'.join(yes_options), '/'.join(no_options)))
            continue 
        # Returns boolean result 
        return user_result in yes_options
    
def inputOption(text="Which option: ", options=[1, 2], additional=False):
    total_message_list = [text, *[f"{i + 1}. {option}" for i, option in enumerate(options)]]
    if additional:
        total_message_list.append("Other")
    total_message_list.append('')
    total_message_text = '\n'.join(total_message_list)
    user_option = inputInt(total_message_text, min=1, max=len(options)) - 1
    return options[user_option]  


def inputList(text="Input a list, splitting your entries with /: ", delimiter='/', reference_text=None, compare_to_ref=False):
    if compare_to_ref and reference_text is None:
        print("No reference text given, setting compare_to_ref as False!")
        compare_to_ref = False
    while True:
        try:
            message = inputString(text)
            message_list = message.split(delimiter)
            break
            # # No need to verify if in text 
            # # If we want to compare_to_ref and all args exist,
            # if compare_to_ref and min([text in reference_text for text in message_list]):
            #     break
            # print("Some of your arguments are not in the reference text!")
            # continue 
        except Exception as e:
            print(str(e))
            continue 
    return message_list
