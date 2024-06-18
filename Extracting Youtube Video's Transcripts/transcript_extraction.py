from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

import pandas as pd
import json as js

#Reading the datavideos.xlsx to extract the transcripts. 
def yt_video_id(link):
    url_data = urlparse(link)
    query = parse_qs(url_data.query)
    vid = query["v"][0]

    return vid

#Extracting transcripts and store them in notepad for each video in a seperate folder
def yt_video_tr(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    transcript_text = ""
    for entry in transcript:
        transcript_text += entry['text'] + " "
    
    return transcript_text.strip()
        
#Save to an Excel file
def save_df_to_csv(df, file_path):
    df.to_csv(file_path)

def main():
    file_path = 'Extracting Youtube Video\'s Transcripts\\datavideos.csv'
    file_path_2 = 'Extracting Youtube Video\'s Transcripts\\datavideos2.csv'
    data_video_df = pd.read_csv(file_path)

    id_list = []
    tr_list = []
    for lnk in data_video_df['Link']:
        vid = yt_video_id(lnk)
        id_list.append(vid)

        tr = yt_video_tr(vid)
        tr_list.append(tr)
        
    
    data_video_df['Video ID'] = id_list
    data_video_df['Transcript'] = tr_list

    save_df_to_csv(data_video_df, file_path_2)

    # print(data_video_df.head())

if __name__ == "__main__":
    main()