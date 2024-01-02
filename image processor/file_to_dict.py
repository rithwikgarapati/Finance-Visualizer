"""
    FILE NAME: file_to_dict
    FUNCTION: Reads through the recognized file and categorizes each expense
              and puts it in the dictionary.
"""


def make_all_elements_lowercase(elements: list[str]) -> list:
    """
        Turns each element into lowercase element.
    """
    for i in range(len(elements)):
        elements[i] = elements[i].lower()
    return elements


def keyword_in_line(line: list[str]) -> bool:
    """
        Checks if a keyword is present in the line.
    """
    keywords = ["transaction", "payment", "withdrawal", "purchase", "transfer", "bill"]
    for keyword in keywords:
        if keyword in line:
            return True

    return False


def dict_of_all_expenses(url: str) -> dict:
    """
        Reads each line from the Bank Statements file and
        segregates it into an item in the dictionary with
        the key as the item number and the value as a list of
        amount spent and description of the spending.
    """

    all_items = dict()
    file = open(url, 'r')

    counter = 1
    items = []
    for line in file:
        line = line.rstrip('\n')

        if line == "":
            continue

        # All the transactions start with - in the bank Statements.
        if line[0] == '-':
            items.append(line)

        # We either want to look for expenses or the description.
        else:
            temp = line.split(' ')
            if len(temp) == 1:
                continue

            temp = make_all_elements_lowercase(temp)
            if keyword_in_line(temp):
                items.append(line)

        # After we found both the expense and description, we
        # add it to the dict, and update variables.
        if len(items) == 2:
            all_items["Item" + " " + str(counter)] = items
            items = []
            counter += 1

    return all_items

