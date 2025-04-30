from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load dataset
file_path = "student-data.csv"
df = pd.read_csv(file_path)

# Prediction function
def predict_pass_fail(row):
    if row["failures"] > 0 and row["studytime"] < 2:
        return "Fail"
    if row["absences"] > 10 and row["studytime"] < 2:
        return "Fail"
    return "Pass"

# Apply predictions
df["Predicted"] = df.apply(predict_pass_fail, axis=1)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        roll_number = request.form.get("roll_number")

        if roll_number.isdigit():
            roll_number = int(roll_number)
            if 0 <= roll_number < len(df):
                student = df.iloc[roll_number]
                result = {
                    "Study Time": student["studytime"],
                    "Failures": student["failures"],
                    "Absences": student["absences"],
                    "Actual Result": student["passed"],
                    "Predicted Result": student["Predicted"],
                }
            else:
                result = {"error": "Invalid Roll Number"}
        else:
            result = {"error": "Enter a valid number"}

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
