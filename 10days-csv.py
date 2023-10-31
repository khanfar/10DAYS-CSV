import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from datetime import datetime, timedelta

def filter_csv():
    file_path = filedialog.askopenfilename(title="Select CSV File")
    if file_path:
        try:
            # Load the CSV file into a DataFrame
            df = pd.read_csv(file_path)

            # Convert the "تاريخ الدخول" column to datetime format
            df["تاريخ الدخول"] = pd.to_datetime(df["تاريخ الدخول"], format="%d.%m.%Y")

            # Calculate the date 10 days ago from today
            ten_days_ago = datetime.now() - timedelta(days=10)

            # Filter the DataFrame to keep only records from the last 10 days
            filtered_df = df[df["تاريخ الدخول"] >= ten_days_ago]

            # Create the "output" directory if it doesn't exist
            output_directory = "output"
            os.makedirs(output_directory, exist_ok=True)

            # Create the "docs" directory inside the "output" directory
            docs_directory = os.path.join(output_directory, "docs")
            os.makedirs(docs_directory, exist_ok=True)

            # Save the filtered DataFrame to a new CSV file in the "docs" directory
            output_file_path = os.path.join(docs_directory, "your_data.csv")
            filtered_df.to_csv(output_file_path, index=False, encoding="utf-8-sig")
            result_label.config(text=f"Filtered data saved to '{output_file_path}'")
        except Exception as e:
            result_label.config(text=f"Error: {str(e)}")

# Create a larger GUI window
window = tk.Tk()
window.title("CSV Data Filter")
window.geometry("500x200")  # Adjust the window size here

# Create and configure the file selection button
select_button = tk.Button(window, text="Select CSV File", command=filter_csv)
select_button.pack()

# Create a label to display the result
result_label = tk.Label(window, text="", fg="green")
result_label.pack()

window.mainloop()
