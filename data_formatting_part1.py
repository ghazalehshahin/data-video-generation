import pandas as pd

# Function to convert "MM:SS" to seconds
def convert_to_seconds(timestamp):
    if pd.isna(timestamp):
        return 0
    parts = str(timestamp).split(':')
    if len(parts) == 3:
        minutes, seconds, microseconds = parts
        return int(minutes) * 60 + int(seconds)
    else:
        print(f"Unexpected format: {timestamp}")
        return 0

# Load the input file
file_path = 'input_file.xlsx'
input_data = pd.read_excel(file_path)

# Convert 'Setting' and 'Rising-Climax' columns to seconds
input_data['Setting'] = input_data['Setting'].apply(convert_to_seconds)
input_data['Rising-Climax'] = input_data['Rising-Climax'].apply(convert_to_seconds)
print(input_data['Setting'])

# Calculate the duration for Rising/Climax by subtracting Setting duration
input_data['Rising-Climax'] = input_data['Rising-Climax'] - input_data['Setting']
print(input_data['Rising-Climax'])

# Prepare the new DataFrame with the desired columns and format
new_data_list = []
for idx, row in input_data.iterrows():
    new_data_list.append(['', 'Settings', row['Setting'], row['Title'], ''])
    new_data_list.append(['', 'Rising/Climax', row['Rising-Climax'], row['Title'], ''])
    new_data_list.append(['', 'Resolution', 0, row['Title'], ''])  # Placeholder for Resolution

# Convert the list to a DataFrame
new_data = pd.DataFrame(new_data_list, columns=['transcript', 'category', 'duration (in sec)', 'name of video', 'topic'])

# Save the new DataFrame to an Excel file
output_file_path = 'output_file.xlsx'
new_data.to_excel(output_file_path, index=False)

print(f'The processed data has been saved to {output_file_path}')
