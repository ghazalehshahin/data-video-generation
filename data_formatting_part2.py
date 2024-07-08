import pandas as pd

# Load the duration data
duration_file_path = '/content/output_file.xlsx'
duration_data = pd.read_excel(duration_file_path)

# Load the transcript data
transcript_file_path = '/content/output_new.xlsx'
transcript_data = pd.read_excel(transcript_file_path, sheet_name=None)

# Function to extract video number from sheet name
def extract_video_number(sheet_name):
    return int(sheet_name.split('_')[1])

# Function to aggregate transcripts for a specific duration
def aggregate_transcripts(df, duration_start, duration_end):
    relevant_transcripts = df[(df['Start Time'] < duration_end) & (df['End Time'] > duration_start)]
    aggregated_transcript = " ".join(relevant_transcripts['Transcript'])
    return aggregated_transcript

# Initialize a dictionary to store the aggregated transcripts
transcripts_dict = {'Settings': [], 'Rising/Climax': [], 'Resolution': []}

# Process each video sheet
variable = []
for sheet_name, sheet_data in transcript_data.items():
    print("sheet_name ", f"{sheet_name}")
    # Extract video number from sheet name
    video_number = extract_video_number(sheet_name)

    # Get the corresponding rows in the duration data
    iterator = len(variable)

    # Extract durations
    settings_duration = duration_data['duration_in_sec'][3*iterator]
    rising_climax_duration = duration_data['duration_in_sec'][3*iterator+1]
    total_duration = settings_duration + rising_climax_duration

    # Calculate the duration for the Resolution
    end_time = sheet_data['End Time'].max()
    resolution_duration = end_time - total_duration

    variable.append(video_number)

    # Aggregate transcripts for each category
    transcripts_dict['Settings'].append(aggregate_transcripts(sheet_data, 0, settings_duration))
    transcripts_dict['Rising/Climax'].append(aggregate_transcripts(sheet_data, settings_duration, total_duration))
    transcripts_dict['Resolution'].append(aggregate_transcripts(sheet_data, total_duration, end_time))

    # Update the duration data for Resolution
    duration_data.loc[3*iterator+2, 'duration_in_sec'] = resolution_duration

print(transcripts_dict)

# Add the aggregated transcripts back to the duration data and add the video number column
for idx, row in duration_data.iterrows():
    category = row['category']
    if transcripts_dict[category]:
        duration_data.at[idx, 'transcript'] = transcripts_dict[category].pop(0)
    else:
        duration_data.at[idx, 'transcript'] = ""

# Save the updated DataFrame to a new Excel file
output_updated_file_path = '/content/output_updated_file.xlsx'
duration_data.to_excel(output_updated_file_path, index=False)

print(f'The updated data with transcripts has been saved to {output_updated_file_path}')
