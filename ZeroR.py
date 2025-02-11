import sys
import random
from collections import Counter

def zeroR(list_of_examples):
    """Returns the most common classification label in the dataset."""
    if len(list_of_examples) < 2:  # If only header exists
        print("Error: No data found in the file.")
        sys.exit(-1)
    
    classifications = [line.strip().split(',')[-1] for line in list_of_examples[1:]]  # Skip header
    most_common = Counter(classifications).most_common(1)[0][0]  # Get most common label
    return most_common

def randR(list_of_examples):
    """Returns a classification randomly based on frequency distribution."""
    if len(list_of_examples) < 2:  # If only header exists
        print("Error: No data found in the file.")
        sys.exit(-1)
    
    classifications = [line.strip().split(',')[-1] for line in list_of_examples[1:]]
    counts = Counter(classifications)
    labels, frequencies = zip(*counts.items())  # Separate labels and their counts
    probabilities = [freq / sum(frequencies) for freq in frequencies]  # Normalize to get probabilities
    return random.choices(labels, probabilities)[0]  # Select based on probability

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python ZeroR.py {-z|-r} file")
        sys.exit(-1)

    classify_type = "-z"  # Default to ZeroR
    if len(sys.argv) == 3:
        classify_type = sys.argv[1]
        if classify_type not in ["-z", "-r"]:
            print("Usage: python ZeroR.py {-z|-r} file")
            sys.exit(-1)

    fname = sys.argv[-1]

    try:
        with open(fname) as f:
            data = f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{fname}' not found.")
        sys.exit(-1)

    if len(data) < 2:  # If file is empty or only contains a header
        print("Error: No data rows found in the file.")
        sys.exit(-1)

    correct_count = 0
    total_count = len(data) - 1  # Exclude header

    if classify_type == "-z":
        prediction = zeroR(data)
        correct_count = sum(1 for line in data[1:] if line.strip().split(',')[-1] == prediction)
    else:
        correct_count = sum(1 for line in data[1:] if line.strip().split(',')[-1] == randR(data))  # Call randR per example

    accuracy = correct_count / total_count
    print(f"Accuracy: {accuracy:.2f}")
