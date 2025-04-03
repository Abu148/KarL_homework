import sqlite3

def create_database():
    conn = sqlite3.connect('roster.db') 
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Roster (
            Name TEXT,
            Species TEXT,
            Age INTEGER
        )
    ''')
  
    conn.commit()
    print("Database and table created successfully.")
    conn.close()

def populate_roster():
    conn = sqlite3.connect('roster.db')
    cursor = conn.cursor()
    
    # Data to be inserted into the table
    data = [
        ("Benjamin Sisko", "Human", 40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29)
    ]
    
    cursor.executemany('''
        INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
    ''', data)
    
    conn.commit()
    print("Data populated successfully.")
    conn.close()

def update_name():
    conn = sqlite3.connect('roster.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE Roster SET Name = ? WHERE Name = ?
    ''', ("Ezri Dax", "Jadzia Dax"))
    
    conn.commit()
    print("Name updated successfully.")
    conn.close()


def display_bajoran():
    conn = sqlite3.connect('roster.db')
    cursor = conn.cursor()
    

    cursor.execute('''
        SELECT Name, Age FROM Roster WHERE Species = "Bajoran"
    ''')

    bajorans = cursor.fetchall()
    
    if bajorans:
        print("Bajoran species:")
        for bajoran in bajorans:
            print(f"Name: {bajoran[0]}, Age: {bajoran[1]}")
    else:
        print("No Bajoran species found.")
    
    conn.close()

def main():
    while True:
        print("\nSelect an option:")
        print("1. Create Database and Table")
        print("2. Populate Data")
        print("3. Update Name of Jadzia Dax to Ezri Dax")
        print("4. Display Bajoran Species")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            create_database()
        elif choice == '2':
            populate_roster()
        elif choice == '3':
            update_name()
        elif choice == '4':
            display_bajoran()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
