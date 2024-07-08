import pandas as pd
import json

# Load the updated duration data with transcripts
output_updated_file_path = '/content/output_updated_file.xlsx'
duration_data = pd.read_excel(output_updated_file_path)

# Initialize an empty list to store the JSON objects for each video
videos_json_list = []

# Get the unique video titles in the order they appear in the Excel file
video_titles = duration_data['name of video'].unique()

# Iterate over each video title in the order they appear in the Excel file
for video_title in video_titles:
    video_json = {
        "video_title": video_title,
        "sections": {
            "Settings": {
                "duration": None,
                "context": None
            },
            "rising_climax": {
                "duration": None,
                "context": None
            },
            "resolution": {
                "duration": None,
                "context": None
            }
        }
    }

    # Get the group of rows corresponding to the current video title
    group = duration_data[duration_data['name of video'] == video_title]

    # Iterate over each row in the group to populate the JSON object
    for idx, row in group.iterrows():
        category = row['category']
        duration = row['duration_in_sec']
        transcript = row['transcript']

        if category == 'Settings':
            video_json["sections"]["Settings"]["duration"] = duration
            video_json["sections"]["Settings"]["context"] = transcript
        elif category == 'Rising/Climax':
            video_json["sections"]["rising_climax"]["duration"] = duration
            video_json["sections"]["rising_climax"]["context"] = transcript
        elif category == 'Resolution':
            video_json["sections"]["resolution"]["duration"] = duration
            video_json["sections"]["resolution"]["context"] = transcript

    # Append the video JSON to the list
    videos_json_list.append(video_json)

# Convert the list of JSON objects to a JSON string
videos_json_str = json.dumps(videos_json_list, indent=4)

# Save the JSON string to a file
output_json_file_path = '/content/output_videos.json'
with open(output_json_file_path, 'w') as json_file:
    json_file.write(videos_json_str)

print(f'The JSON data has been saved to {output_json_file_path}')
