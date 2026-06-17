def load_menu_items():
    data_file = open("Menu.txt", "r")
    menu_items = {}
    for line_of_date in data_file:
        item_name_and_price = line_of_date.split(",")


        item_name = item_name_and_price[0]
        item_price = float(item_name_and_price[1])

        menu_items[item_name] = item_price
    data_file.close()
    return menu_items


def main():
    menu = load_menu_items()
    item = ""
    total = 0
    while item != "end":
        item = input("Item:\n").title()
        if item in menu:
            total += menu[item]
            print(f"${total:.2f}")










main()