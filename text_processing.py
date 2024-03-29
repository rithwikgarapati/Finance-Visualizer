import ipdb

def make_all_elements_lowercase(elements):
    for i in range(len(elements)):
        elements[i] = elements[i].lower()
    return elements


def keyword_in_line(line):
    keywords = ["transaction", "payment", "withdrawal", "purchase", "transfer", "bill"]
    for keyword in keywords:
        if keyword in line:
            return True
    return False


def dict_of_all_expenses(url):
    all_items = []
    file = open(url, 'r')

    counter = 1
    items = []
    for line in file:
        line = line.rstrip('\n')

        if line == "":
            continue

        if line[0] == '-':
            items.append(line)

        else:
            temp = line.split(' ')
            if len(temp) == 1:
                continue

            temp = make_all_elements_lowercase(temp)
            if keyword_in_line(temp):
                items.append(line)

        if len(items) == 2:
            all_items.append(items)
            items = []
            counter += 1

    for lst in all_items:
        if lst[0][0] == '-':
            temp = lst[0]
            lst[0] = lst[1]
            lst[1] = temp

    return all_items

