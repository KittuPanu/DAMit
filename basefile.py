import pandas as pd
import datetime

# Read the data from the Excel sheet
def read_data_from_excel(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df

# Calculate the surplus based on user input
def calculate_surplus(current_volume, volume_of_rainfall, FR):
    surplus = current_volume + volume_of_rainfall - FR
    return surplus

# Main function
if __name__ == "__main__":
    # Path to the Excel file
    excel_file = 'PUT_THE_FILE_PATH_HERE'

    # Sheet name in the Excel file
    sheet_name = "Sheet1"  # Replace with the actual sheet name where your data is located

    # Read data from the Excel sheet
    data_df = read_data_from_excel(excel_file, sheet_name)

    # Get user input for the current volume of reservoir
    current_volume = float(input("Enter the current volume of the reservoir (in liters): "))

    # Create a menu with days and dates from today until the next 13 days
    print("Select a day for weather forecast:")
    today = datetime.datetime.today()
    for i in range(14):
        date = today + datetime.timedelta(days=i)
        print(f"{i+1}. {date.strftime('%A, %Y-%m-%d')}")

    # Ask the user to specify which day they want the weather forecast for
    selected_day = int(input("Enter the number corresponding to the day you want to know what do with the gates: ") or 2) - 1

    # Get the predicted volume of rainfall from the selected day in the Excel sheet
    volume_of_rainfall = data_df.at[selected_day + 1, "PV in litres"]  # Assuming 'PV in litres' column is in the first row (index 0)

    # Assign the constant value 'FR' directly (in liters)
    FR = 11472000000000000  # 11.472 quadrillion liters

    # Calculate the surplus
    surplus = calculate_surplus(current_volume, volume_of_rainfall, FR)

    # Check if the surplus is positive or negative
    if surplus > 0:
        print("The gates should be open.")
    else:
        print("The gates should not be opened.")
