import pandas as pd
from moviepy.editor import VideoFileClip
from datetime import datetime

# Function to convert time string to seconds
def time_to_seconds(time_str):
    time_obj = datetime.strptime(str(time_str), "%H:%M:%S")
    return time_obj.hour * 60 + time_obj.minute

# Read the Excel file
df = pd.read_excel('Coding-Videos-Freytags-Pyramid.xlsx')

# Iterate over each row
for index, row in df.iterrows():
    start_time_str = row[0]  # Assuming start time is in the first column
    end_time_str = row[1]    # Assuming end time is in the second column

    # Convert time strings to seconds
    start_time = time_to_seconds(start_time_str)
    end_time = time_to_seconds(end_time_str)

    # Create subclip
    clip = VideoFileClip("sample_video.mp4").subclip(start_time, end_time)

    # Do something with the subclip, like saving it
    clip.write_videofile(f"subclip_{index}.mp4")

    # Close the clip to free up resources
    clip.close()