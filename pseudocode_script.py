# Create a Python script that prints pseudocode based on the Vehicle database design model.

# Define a dictionary that stores model information, including classes and attributes shown in the Vehicle model
vehicle_model = {
    "Vehicle": ["vehicleID", "make"],
    "Car": ["numberOfDoors", "isAllWheelDrive"],
    "Truck": ["bedLength", "is4x4"],
    "Driver": ["driverID", "driverName"]
}

# Define a dictionary that represents inheritance relationships in the Vehicle model
inherits = {
    "Car": "Vehicle",
    "Truck": "Vehicle"
}

# Define a dictionary that represents the relational tables in the Vehicle model
relational_tables = {
    "VehicleTable": ["vehicleID (PK)", "make"],
    "CarTable": ["vehicleID (PK, FK)", "numberOfDoors", "isAllWheelDrive"],
    "TruckTable": ["vehicleID (PK, FK)", "bedLength", "is4x4"],
    "DriverTable": ["driverID (PK)", "driverName"],
    "DriverCarTable": ["driverID (PK, FK)", "vehicleID (PK, FK)"]
}

# Create a dictionary to store relationship data
relationships = {
    "CarTable": "VehicleTable using vehicleID",
    "TruckTable": "VehicleTable using vehicleID",
    "DriverCarTable": "DriverTable and CarTable using driverID and vehicleID"
}

# Function to print the pseudocode representation of the Vehicle database model
def print_pseudocode():
    # Loop through each class and its attributes in the vehicle model
    for cls, attrs in vehicle_model.items():

        # Conditional to check if the class inherits from another class
        if cls in inherits:
            print(f"DEFINE {cls} INHERITS {inherits[cls]}")   # Print class with inheritance if it exists
        else:
            print(f"DEFINE {cls}")   # Print class without inheritance if it doesn't exist

        # Nested loop to iterate over the attributes of the class
        for attr in attrs:

            # Print the attribute of the class
            print(f"    {attr}")

        # Print a blank line after each class for readability
        print()

    # Print the relational tables and their columns
    print("RELATIONAL TABLES:")

    # Print a blank line before listing the relational tables for readability
    print()

    # Loop through each relational table and its columns to print the CREATE statements
    for table, columns in relational_tables.items():
        print(f"CREATE {table}")   # Print the CREATE statement for the table

        # Loop through each column in the table to print its definition
        for column in columns:
            print(f"    {column}")  # Print the column definition for the table

        # Print a blank line after each table for readability
        print()

    # Print the relationships between the tables in the Vehicle model
    print("RELATIONSHIPS:")

    # Print a blank line before listing the relationships for readability
    print()

    # Loop through the relationships and print them
    for table, relation in relationships.items():
        print(f"{table} RELATES TO {relation}")

# Call the function to print the pseudocode representation of the Vehicle model
print_pseudocode()

