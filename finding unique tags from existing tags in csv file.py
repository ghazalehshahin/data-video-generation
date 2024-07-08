import csv

def extract_unique_tags(csv_filename):
    unique_tags = set()

    # Read the CSV file
    with open(csv_filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 5:  # Ensure the row has at least 6 columns
                tags = row[5].split(',')
                for tag in tags:
                    unique_tags.add(tag.strip())  # Add each tag to the set

    return unique_tags

def write_tags_to_file(tags, output_filename):
    with open(output_filename, mode='w') as file:
        for i, tag in enumerate(sorted(tags), start=1):
            file.write(f"{i}. {tag}\n")

# Define file names
csv_filename = 'tagged_sheet (1).csv'
output_filename = 'unique_tags.txt'

# Extract unique tags from the CSV file
unique_tags = extract_unique_tags(csv_filename)

# Write unique tags to a text file in numbered format
write_tags_to_file(unique_tags, output_filename)

print(f"Unique tags have been written to {output_filename}")