# --- Game State ---
#assignment 5
inventory = []
items_in_room = [
    {"name": "Torch", "type": "tool", "description": "Lights up dark places."},
    {"name": "Bandage", "type": "health", "description": "Bandage for emergency use"},
    {"name": "Key", "type": "tool", "description": "Opens something locked."}
] # length shall be larger than max inventory size if there is only one room
dark_items = [
    {"name": "Chest", "type": "storage", "description": "An old wooden chest."},
    {"name": "Hammer", "type": "tool", "description": "A rusty big hammer."},
    {"name": "note", "type": "writing", "description": "Some kind of note"}
]
MAX_INVENTORY_SIZE = 5
torch_used = False
hurt = False

# --- Functions ---

def show_inventory():
    # list all names of items in the inventory, consider the case when the list is empty
    if not inventory:
        print("Your inventory is empty. You need to collect some items first before you can use them.")
    else:
        item_names = [item["name"] for item in inventory]
        print("The items in the inventory are:" + str(item_names))
    pass

def show_room_items():
    # list all items in current room
    if not items_in_room:
        print("There are no items left in this room. Maybe you'll have more luck in other rooms.")
    else:
        print("The items in the room are: " + ", ".join(item["name"] for item in items_in_room))
    pass

def pick_up(item_name):
    # Check if inventory size is below the max allowed size
    if len(inventory) < MAX_INVENTORY_SIZE:
        # Find the item in the room by name
        for item in items_in_room:
            # Check if the name matches the item_name passed to the function
            if item["name"].lower() == item_name.lower():
                # Add the item to the inventory (we append the whole item, not just the name)
                inventory.append(item)
                # Remove the item from the room
                items_in_room.remove(item)
                print(f"You picked up {item_name}")
                return  # Exit the function after picking up the item
        # If no matching item is found in the room
        print(f"That item ({item_name}) is not in the room.")
    else:
        print("Your inventory is full. You need to get rid of some items.")
        item_names = [item["name"] for item in inventory]
        print("The items in the inventory are:" + str(item_names))
    pass


def drop(item_name):
    # drop an item from your inventory, at the same time append it back to the list of items for the room
    if not inventory:
        print("Your inventory is already empty.")
    else:
        inventory.remove(item_name)
        items_in_room.append(item_name)
        print("You dropped " + item_name + ".")
        item_names = [item["name"] for item in inventory]
        print("The items in the inventory are:" + str(item_names))
    pass

def use(item_name):
    # Ex: use the item differently depends on the type
    item_name = item_name.strip().lower()  # Clean user input
    global hurt
    global torch_used
    if item_name == "torch":
        if any(item["name"].strip().lower() == item_name for item in inventory) and not torch_used:
            print("You light up the torch. It's dim, but enough to see.")
            print("Around you are some items you didnt notice before. And there seems to be a door")
            print("at the right hand side of you. You try to open it, but its locked. What do you do?")
            items_in_room.extend(dark_items)
            torch_used= True
        elif torch_used:
            print("Your torch is already lit")
        else:
            print("You dont have that item in your inventory.")
            item_names = [item["name"] for item in inventory]
            print("The items in the inventory are:" + str(item_names))
    elif item_name == "bandage":
        if any(item["name"].strip().lower() == item_name for item in inventory) and hurt:
            print("You have wound the bandage around you finger. It stops the bleeding for now.")
            print("You feel a bit better.")
            for item in inventory:
                if item["name"].strip().lower() == item_name:
                    inventory.remove(item)
                    break
        elif any(item["name"].strip().lower() == item_name for item in inventory) and not hurt:
            print("You have wind the bandage around your Head. You look like a stupid mummy.")
            for item in inventory:
                if item["name"].strip().lower() == item_name:
                    inventory.remove(item)
                    break
        else:
            print("You don't have that item in your inventory.")
            item_names = [item["name"] for item in inventory]
            print("The items in the inventory are:" + str(item_names))
    elif item_name == "key":
        if any(item["name"].strip().lower() == item_name for item in inventory):
            print("what do you want to use the key for?")
            usage = input()
            if usage.strip().lower() == "door".strip().lower():
                print("You try it on the Door, but it wont work.")
                print("What could the key be for?")
            elif usage.strip().lower() == "chest".strip().lower():
                print("You put the key into the chest. It is rusty and old, but it works")
                print("Inside you find a portal that sucks you in. You're back at tech basics!")
                while True:
                    answer = input("Are you Qianxun Chen? (y/n) \n").strip().lower()
                    if answer == "y":
                        print("Now you can learn and have fun. You win!")
                        return True
                    elif answer == "n":
                        #this is for satirical purposes only and not meant to be taken seriously. I like learning programming
                        print("Oh no, you're at tech basics! You lost!")
                        return True
                    else:
                        print("Wrong input. Please enter 'y' or 'n'.")
    elif item_name == "note":
        if any(item["name"].strip().lower() == item_name for item in inventory):
            print("You investigate the strange note.")
            print("On it, it says, written in a very old fashioned handwriting:")
            print('"Sometimes you dont have to use your head, and using brute force works just as well"')
            print("How strange...")
        else:
            print("You dont have that item in your inventory.")
            item_names = [item["name"] for item in inventory]
            print("The items in the inventory are:" + str(item_names))
    elif item_name == "chest":
        if any(item["name"].strip().lower() == item_name for item in inventory):
            print("You try to open the old chest.")
            print("It seems to be locked")
        else:
            print("You dont have that item in your inventory.")
            item_names = [item["name"] for item in inventory]
            print("The items in the inventory are:" + str(item_names))
    elif hurt:
        print("Your finger starts hurting more and more. Suddenly, everything fades to black and you lose consciousness")
        print("You should have treated your wound. You LOSE")
    elif item_name == "hammer":
        if any(item["name"].strip().lower() == item_name for item in inventory):
            print("Maybe you dont always need a brillant plan to get out of a locked room.")
            print("sometimes, brute force can do the trick just as well.")
            print("You take the hammer and advance towards the door...")
            print("You throw it back for a big swing...")
            print("and you HIT your FINGER.")
            print("Crying out in pain, you inspect your wound. How stupid can someone be?")
            hurt= True
        else:
            print("You dont have that item in your inventory.")
            item_names = [item["name"] for item in inventory]
            print("The items in the inventory are:" + str(item_names))
    else:
        print("You don't have that item in your inventory.")
        item_names = [item["name"] for item in inventory]
        print("The items in the inventory are:" + str(item_names))
        pass
    pass

def examine(item_name):
    # you can only examine an item if it's in your inventory or if it is in the room
    if any(item["name"].lower() == item_name.lower() for item in items_in_room):
        for item in items_in_room:
            if item["name"].lower() == item_name.lower():
                print("name:" + item["name"] + ", type:" + item["type"] + ", description:" + item["description"])
                break  # Stop the loop after finding the item
    elif any(item["name"].lower() == item_name.lower() for item in inventory):
        for item in inventory:
            if item["name"].lower() == item_name.lower():
                print("name:" + item["name"] + ", type:" + item["type"] + ", description:" + item["description"])
                break  # Stop the loop after finding the item
    else:
        print(f"The item ({item_name}) is not in the room or your inventory.")
    pass

# --- Game Loop ---

def game_loop():
    print("Welcome to the Inventory Game!")
    print("Type 'help' for a list of commands.")
    print("...")
    print("You get awoken by the cold. It is awfully cold where you are. Where you are - ")
    print("you cant see, as it is pitch black around you. Maybe by feeling with your hands,")
    print("You can get a better overview of your surroundings.")

    while True:
        command = input("\n> ").strip().lower()
        if command == "help":
            # You can also rename the commands according to your own needs
            print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], quit")
        elif command == "inventory":
            show_inventory()
        elif command == "look":
            show_room_items()
        elif command.startswith("pickup "):
            item_name = command[7:]
            pick_up(item_name)
        elif command.startswith("drop "):
            item_name = command[5:]
            drop(item_name)
        elif command.startswith("use "):
            item_name = command[4:]
            use(item_name)
        elif command.startswith("examine "):
            item_name = command[8:]
            examine(item_name)
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    game_loop()

