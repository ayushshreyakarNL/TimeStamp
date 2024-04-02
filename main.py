import pandas as pd
import zipfile
import os
from datetime import datetime


def extract_load_timestamp(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Assuming the timestamp is the first part of the ZIP file's name
        timestamp = os.path.splitext(os.path.basename(zip_file_path))[0].split('_')[0]
        return datetime.strptime(timestamp, '%Y%m%d%H%M%S%f')


def process_csv(csv_file_path, load_timestamp):
    # Read CSV file
    df = pd.read_csv(csv_file_path)
    # Add load_timestamp column
    df['load_timestamp'] = load_timestamp
    return df


def main():
    # Path to the ZIP file
    zip_file_path = '/home/nineleaps/Downloads/20240305124003123456_Extract 2.zip'
    # Extract load timestamp
    load_timestamp = extract_load_timestamp(zip_file_path)

    # Display the extracted timestamp in the console
    print("Extracted Timestamp:", load_timestamp.strftime('%Y-%m-%d %H:%M:%S.%f'))

    # Paths to sample CSV files
    sample_csv_files = ['/home/nineleaps/Downloads/sample.csv', '/home/nineleaps/Downloads/sample2.csv']

    # Process each CSV file
    for csv_file in sample_csv_files:
        # Get the full path of the CSV file
        csv_file_path = os.path.join(os.path.dirname(zip_file_path), csv_file)
        # Process CSV file
        df = process_csv(csv_file_path, load_timestamp)
        # Save modified dataframe back to CSV
        output_csv_file = f"{os.path.splitext(csv_file)[0]}_with_timestamp.csv"
        df.to_csv(output_csv_file, index=False)


if __name__ == "__main__":
    main()
