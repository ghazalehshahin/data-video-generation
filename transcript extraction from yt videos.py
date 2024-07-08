import pandas as pd
from youtube_transcript_api import YouTubeTranscriptApi
import openpyxl

# Read the spreadsheet to get the list of YouTube video links
input_file = 'video_transcripts.xlsx'  # Replace with your input file name
df = pd.read_excel(input_file)

# Function to extract video ID from a YouTube URL
def get_video_id(url):
    # Handle different URL formats
    if 'youtube.com/watch?v=' in url:
        return url.split('v=')[1].split('&')[0]
    elif 'youtu.be/' in url:
        return url.split('/')[-1].split('?')[0]
    else:
        return None

# Function to create a valid Excel sheet name
def create_valid_sheet_name(base_name, index):
    max_sheet_name_length = 31  # Maximum length for Excel sheet names
    valid_base_name = base_name[:max_sheet_name_length-5]  # Reserve space for index and underscore
    return f"{valid_base_name}_{index+1}"

# Create a new workbook to store the transcripts
output_file = 'output_new.xlsx'

with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    # Loop through each video link and fetch the transcript
    for index, row in df.iterrows():
        video_url = row[2]  # Assuming the links are in the third column
        video_id = get_video_id(video_url)

        if video_id:
            try:
                # Fetch the English transcript
                transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])

                # Prepare the data for the DataFrame
                transcript_data = []
                for i in range(len(transcript)):
                    start_time = transcript[i]['start']
                    end_time = transcript[i+1]['start'] if i < len(transcript) - 1 else start_time+1
                    text = transcript[i]['text']
                    transcript_data.append([start_time, end_time, text])

                # Create a DataFrame with the transcript data
                transcript_df = pd.DataFrame(transcript_data, columns=['Start Time', 'End Time', 'Transcript'])

                # Create a new sheet in the workbook for this video's transcript
                sheet_name = create_valid_sheet_name("Video", index)
                transcript_df.to_excel(writer, sheet_name=sheet_name, index=False)

            except Exception as e:
                print(f"Could not retrieve transcript for video {video_id}: {e}")

print(f"Transcripts have been saved to {output_file}")
