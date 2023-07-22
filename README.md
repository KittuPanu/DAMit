# goddamN
# Reservoir Forecasting Program

![Reservoir]

## Overview
This is a simple Python program that helps with reservoir forecasting by predicting the water surplus or deficit based on user input and real-time rainfall data from [**timeanddate**]([url](https://www.timeanddate.com/weather/india/hyderabad/ext)). The program uses an Excel spreadsheet containing rainfall data to estimate the future reservoir volume.

## Features
- Input the current volume of the reservoir (in liters).
- Select a day from today until the next 13 days to get a weather forecast.
- Calculate the predicted volume of rainfall for the selected day from the real time data.
- Estimate the surplus (or deficit) of water in the reservoir after the selected day.
- Suggest whether to open the reservoir gates based on the calculated surplus.

## Installation and Usage
1. Ensure you have Python installed on your system (Python 3.x recommended).
2. Clone this repository to your local machine or download the repository as a ZIP file and extract it.
3. Make sure the Excel file 'Rainfall in hyderabad_inmm_real.xlsx' is in the same directory as the 'reservoir_program.py' script.
4. Open a terminal or command prompt and navigate to the directory containing the program files.
5. Run the program by executing the following command: python reservoir_program.py
6. Follow the on-screen instructions to input the current reservoir volume and select a day for the weather forecast.
7. The program will display the calculation and suggest whether to open the reservoir gates based on the forecast.

## Data Source
The program uses an Excel spreadsheet 'Rainfall in hyderabad_inmm_real.xlsx', which contains real time rainfall data. The data must be organized with one column labeled 'Date' and another column labeled 'PV in litres' representing the predicted volume of rainfall for each day.

## Example Data Format
| Date       | PV in litres |
|------------|--------------|
| 2023-07-20 | 2000         |
| 2023-07-21 | 1800         |
| 2023-07-22 | 2200         |
| ...        | ...          |

## Disclaimer
This program is intended for educational and illustrative purposes only. Always verify and use official weather and reservoir data for real-world applications.

## Contributions
Contributions to improve the program or add new features are welcome. Feel free to open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

Happy forecasting!


Download both the files along with [Python]([url](https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe))
Then follow this guide to install pandas: https://www.youtube.com/watch?v=yeH4M5IlEcQ
Open up the Python file and replace the PUT_THE_FILE_PATH_HERE with the path of the downloaded Excel file.
Save the file and run it.
