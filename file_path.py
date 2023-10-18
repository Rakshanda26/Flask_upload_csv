import os
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Define the upload folder where the CSV file will be saved temporarily
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


print(f"Full path to 'uploads' folder: {full_path}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Check if a file was uploaded
    if 'csv_file' not in request.files:
        return "No file part"

    file = request.files['csv_file']

    # If the user does not select a file, the browser submits an empty file without a name
    if file.filename == '':
        return "No selected file"

    if file:
        # Save the uploaded file to the upload folder
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

        # Read the uploaded CSV file into a DataFrame
        df = pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        print(df)

        # Display the DataFrame
        return df.to_html()

if __name__ == '__main__':
    app.run(debug=True)























import os

upload_folder = app.config['UPLOAD_FOLDER']
full_path = os.path.join(os.getcwd(), upload_folder)

print(f"Full path to 'uploads' folder: {full_path}")