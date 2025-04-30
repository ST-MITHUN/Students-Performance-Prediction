"""import pandas as pd

# Load the dataset
file_path = "student-data.csv"

try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    exit()

# Define function to predict pass/fail
def predict_pass_fail(row):
    if row["failures"] > 0 and row["studytime"] < 2:
        return "no"  # Likely to fail
    if row["absences"] > 10 and row["studytime"] < 2:
        return "no"  # Likely to fail
    return "yes"  # Otherwise, pass

# Apply prediction function
df["Predicted"] = df.apply(predict_pass_fail, axis=1)

# Display comparison with actual results
print("\nStudent Performance Prediction:")
print(df[["studytime", "failures", "absences", "passed", "Predicted"]])

# Save results
df.to_csv("predicted-results.csv", index=False)
print("\nPredictions saved to 'predicted-results.csv'.")
"""
"""
import pandas as pd
import tkinter as tk
from tkinter import messagebox, simpledialog

# Load dataset
file_path = "student-data.csv"

try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    messagebox.showerror("Error", f"File '{file_path}' not found.")
    exit()

# Define function to predict pass/fail
def predict_pass_fail(row):
    if row["failures"] > 0 and row["studytime"] < 2:
        return "Fail"
    if row["absences"] > 10 and row["studytime"] < 2:
        return "Fail"
    return "Pass"

# Apply prediction function
df["Predicted"] = df.apply(predict_pass_fail, axis=1)

# Function to get student result
def get_student_result():
    # Ask user for index (assuming row number as Student ID)
    student_index = simpledialog.askinteger("Input", "Enter Student Row Number (0-based index):")

    # Check if input is valid
    if student_index is None or student_index < 0 or student_index >= len(df):
        messagebox.showerror("Error", "Invalid Student ID. Please enter a valid number.")
        return

    # Get student details
    student = df.iloc[student_index]

    # Create result message
    result_msg = f"Student Performance Prediction\n\n"
    result_msg += f"Study Time: {student['studytime']}\n"
    result_msg += f"Failures: {student['failures']}\n"
    result_msg += f"Absences: {student['absences']}\n"
    result_msg += f"Actual Result: {student['passed']}\n"
    result_msg += f"Predicted Result: {student['Predicted']}\n"

    # Show popup window with result
    messagebox.showinfo("Prediction Result", result_msg)

# Create GUI window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Show input prompt and result popup
get_student_result()
"""