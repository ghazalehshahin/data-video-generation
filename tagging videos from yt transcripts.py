import pandas as pd
import openai

# Initialize the OpenAI API client
openai.api_key = <insert openai key>

# Function to tag transcript content
def tag_transcript(transcript, model="gpt-4"):
    chat_completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": f"Tag the following transcript with atmost 5 general categories. Output should be comma seperated \n\nTranscript:\n{transcript}\n\nTags:",
            }
        ],
    )
    return chat_completion.choices[0].message.content

# Read the CSV file
df = pd.read_csv('datavideos2.csv')

# Check if the 6th column exists, if not, create it
if len(df.columns) < 6:
    df['Tags'] = ''

# Iterate through each row in the 5th column (transcripts)
for index, row in df.iterrows():
    transcript = row[4]  # 5th column (zero-indexed as 4)
    if pd.notna(transcript):  # Ensure the transcript is not NaN
        tags = tag_transcript(transcript)
        df.at[index, 'Tags'] = tags  # Write tags to the 6th column
        print(index)

# Save the modified CSV file
df.to_csv('tagged_sheet.csv', index=False)

print("Tagging complete. The updated CSV file has been saved.")