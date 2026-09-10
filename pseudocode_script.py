# Create a Python script that prints pseudocode based on the Vehicle database design model.

# Define a dictionary that stores model info, including classes and attributes shown in the Vehicle model
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

# Function to print pseudocode representation of the Vehicle model classes and their inheritance relationships
def print_pseudocode():
    # Loop through each class and its attributes in the vehicle model
    for cls, attrs in vehicle_model.items():

        # Conditional to check if the class inherits from another class
        if cls in inherits:
            print(f"DEFINE {cls}({INHERITS[cls]}):")   # Print class with inheritance if it exists
        else:
            print(f"DEFINE {cls}:")   # Print class without inheritance if it doesn't exist

        # Nested loop to iterate over the attributes of the class
        for attr in attrs:

            # Print the attribute of the class
            print(f"    {attr}")

        # Print a blank line after each class for readability
        print()

# Call the function to print the pseudocode representation of the Vehicle model
print_pseudocode()