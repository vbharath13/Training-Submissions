import csv
import json


def csv_to_json(csv_file, json_file):
    try:
        data = []

        # READ CSV FILE
        with open(csv_file, mode="r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                data.append(row)  # each row is a dictionary

        # WRITE JSON FILE
        with open(json_file, mode="w") as file:
            json.dump(data, file, indent=4)

        print(" CSV successfully converted to JSON")

    except FileNotFoundError:
        print(" CSV file not found.")
    except Exception as e:
        print(" Er" \
        "ror:", e)



csv_input = input("Enter CSV file name (e.g., employees.csv): ")
json_output = input("Enter JSON file name (e.g., employees.json): ")

csv_to_json(csv_input, json_output)
