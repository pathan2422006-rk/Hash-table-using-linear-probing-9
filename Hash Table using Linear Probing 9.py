# Hash Table using Linear Probing

SIZE = 10
table = [None] * SIZE


# Hash function
def hash_function(key):
    return key % SIZE


# Insert key
def insert(key):
    index = hash_function(key)

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if table[pos] is None:
            table[pos] = key
            print("Key inserted.")
            return

    print("Hash table is full.")


# Search key
def search(key):
    index = hash_function(key)

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if table[pos] == key:
            print("Key found at index", pos)
            return

        if table[pos] is None:
            break

    print("Key not found.")


# Delete key
def delete(key):
    index = hash_function(key)

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if table[pos] == key:
            table[pos] = None
            print("Key deleted.")
            return

        if table[pos] is None:
            break

    print("Key not found.")


# Display hash table
def display():
    print("\nHash Table:")

    for i in range(SIZE):
        print(i, ":", table[i])


# Main program
while True:
    print("\n--- HASH TABLE ---")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        try:
            key = int(input("Enter key: "))
            insert(key)
        except ValueError:
            print("Please enter an integer key.")

    elif choice == 2:
        try:
            key = int(input("Enter key to search: "))
            search(key)
        except ValueError:
            print("Please enter an integer key.")

    elif choice == 3:
        try:
            key = int(input("Enter key to delete: "))
            delete(key)
        except ValueError:
            print("Please enter an integer key.")

    elif choice == 4:
        display()

    elif choice == 5:
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")