import pandas as pd
import openai

#openai.api

def tag_transcript(transcript, model="gpt-4"):
    chat_completion = openai.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": f" We want to categorize videos based on their topics. Please suggest at most 5 general (not specific) categories in one word for each transcript I give you \n\nTranscript:\n{transcript}\n\nTags:",
            }
        ],
    )
    return chat_completion.choices[0].message.content

df = pd.read_csv('datavideos2.csv')

if len(df.columns) < 6:
    df['Tags'] = ''

tags = []
for tr in df['Transcript']:
    if pd.notna(tr):
        tag = tag_transcript(tr)
        tags.append(tag)
    else:
        tags.append("NaN")
df['Tags'] = tags

df.to_csv('tagged_sheet.csv', index=False)

print("Tagging complete. The updated CSV file has been saved.")