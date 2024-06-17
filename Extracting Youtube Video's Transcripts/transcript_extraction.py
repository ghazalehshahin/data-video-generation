from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

import pandas as pd

#Reading the datavideos.xlsx to extract the transcripts. 
def yt_video_id(file_path):
    data_video_df = pd.read_csv(file_path)

    id_list = []
    for lnk in data_video_df['Link']:
        url_data = urlparse(lnk)
        query = parse_qs(url_data.query)
        vid = query["v"][0]
        id_list.append(vid)
    
    data_video_df['Video ID'] = id_list
    return data_video_df

def main():
    df = yt_video_id('Extracting Youtube Video\'s Transcripts\\datavideos.csv')
    print(df.head())


if __name__ == "__main__":
    main()