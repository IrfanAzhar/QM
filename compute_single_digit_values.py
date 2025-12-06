# This script is written by Dr Irfan Azhar on 06 Dec 2025.
# It takes on input file in csv format which cobntains plain arabic weights of the letters, words,
# It computes single digit value for each weight and rewrites the files with a new name containing the computed weight of each row.


import csv
from utils import summingMethod

def reduce_to_single_digit (weightFlag, input_file, output_file):
    """
    Reads a CSV file, calculates single-digit value for 'arabic-letter/word/verse/chapter-weight' column,
    and writes the result to a new CSV file.

    Args:
        input_file (str): Path to input CSV file
        output_file (str): Path to output CSV file
    """

    # Read the input CSV file
    with open(input_file, 'r', newline='') as infile:
        reader = csv.DictReader(infile)

        # Get the fieldnames (column headers)
        fieldnames = reader.fieldnames

        # Store all rows
        rows = []
        for row in reader:
            rows.append(row)

    # Calculate single digit value for  arabic-weight
    cumulative_total = 0

    for row in rows:
        # Convert arabic-weight to integer
        current_value = int(row[weightFlag])

        if current_value > 9:
            tempInt = current_value
            current_value = summingMethod(tempInt)

        # Update the row with cumulative value
        row[weightFlag] = str(current_value)

    # Write to output CSV file
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write all rows with cumulative sums
        writer.writerows(rows)



if __name__ == "__main__":

    # Convert letter weights to single-digit values
    weightField = 'arabic-letter-weight'
    input_csv = "dictQM_LL_03_Dec_2025.csv"
    output_csv = "dictQM_LL_single_digit_06_Dec_2025.csv"
    reduce_to_single_digit(weightField, input_csv, output_csv)

    # Convert word weights to single-digit values
    weightField = 'arabic-word-weight'
    input_csv = "dictQM_WW_03_Dec_2025.csv"
    output_csv = "dictQM_WW_single_digit_06_Dec_2025.csv"
    reduce_to_single_digit(weightField, input_csv, output_csv)

    # Convert verse weights to single-digit values
    weightField = 'arabic-verse-weight'
    input_csv = "dictQM_AA_03_Dec_2025.csv"
    output_csv = "dictQM_AA_single_digit_06_Dec_2025.csv"
    reduce_to_single_digit(weightField, input_csv, output_csv)

    # Convert chapter weights to single-digit values
    weightField = 'arabic-chapter-weight'
    input_csv = "dictQM_SS_03_Dec_2025.csv"
    output_csv = "dictQM_SS_single_digit_06_Dec_2025.csv"
    reduce_to_single_digit(weightField, input_csv, output_csv)

    # Convert QM weight to single-digit values
    weightField = 'QM-weight'
    input_csv = "dictQM_QM_03_Dec_2025.csv"
    output_csv = "dictQM_QM_single_digit_06_Dec_2025.csv"
    reduce_to_single_digit(weightField, input_csv, output_csv)

