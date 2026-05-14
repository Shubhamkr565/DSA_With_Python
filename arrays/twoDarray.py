# Function to create a 2D array
def create_2d_array(rows, cols):
    # Initialize an empty 2D array
    array = []
    
    # Fill the 2D array with user input
    for i in range(rows):
        # Initialize an empty row
        row = []
        for j in range(cols):
            # Input value for each element in the row
            value = int(input(f"Enter value for element ({i},{j}): "))
            row.append(value)
        # Add the completed row to the 2D array
        array.append(row)
    
    return array

# Define the size of the 2D array
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Create and display the 2D array
two_d_array = create_2d_array(rows, cols)
print("\n2D Array:")
for row in two_d_array:
    print(row)
