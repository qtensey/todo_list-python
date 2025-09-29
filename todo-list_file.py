import argparse

FILENAME = 'todo.txt'

def add_strikethrough(item):
    return f"\x1b[9m{item}\x1b[0m"

def add_item(item):
    with open(FILENAME, 'a') as file:
        file.write(f"{item}\n")
        file.close()
    print(f"Added item: {item}")

def list_items():
    lines = None
    try:
        with open(FILENAME, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File {FILENAME} not found.")

    if not lines:
        print("No items in the todo list.")
    else:
        print(lines)
        for i, line in enumerate(lines):
            print(f"{i + 1}. {line.strip()}")
        

def mark_item_done(item_number):
    with open(FILENAME, 'r') as file:
        lines = file.readlines()

    if not lines:
        print("No items in the todo list.")
    elif item_number < 1 or item_number > len(lines):
        print("Invalid item number.")
    else:
        item = lines[item_number - 1].strip()
        item = add_strikethrough(item)
        with open(FILENAME, 'w') as file:
            for i, line in enumerate(lines):
                if i == item_number - 1:
                    file.write(f"{item}\n")
                    print(f"Marked item {item_number} as done.")
                else:
                    print(line)
                    file.write(line)
                
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manage your todo list.")
    parser.add_argument('action', choices=['add', 'list', 'done'], help="Action to perform: add, list, or done")
    parser.add_argument('item', nargs='?', help="Item to add or item number to mark as done")
    args = parser.parse_args()

    if args.action == 'add':
        add_item(args.item)
    elif args.action == 'done':
        mark_item_done(args.item_number)
    elif args.action == 'list':
        list_items()