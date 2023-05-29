from pytube import YouTube
from summarizer.models import *
from youtube_transcript_api import YouTubeTranscriptApi
import re

############Summary Conversion
def summarize_video(youtube_url,video_id):
    try:
        yt = YouTube(youtube_url)
        video_title = yt.title
        video_transcripts = YouTubeTranscriptApi.get_transcript(video_id)
        transcript=[]
        for index,item in enumerate(video_transcripts):
            transcript.append(item['text'])
            
        video_stream = yt.streams.get_highest_resolution()
        video_path = video_stream.download() 
        cleaned_transcript = ' '.join(transcript) 
        cleaned_transcript = re.sub(r"[^\w\s]", "", cleaned_transcript)
        desired_length = 3
        sentences = cleaned_transcript.split('. ')
        summary = '. '.join(sentences[:desired_length]) 

        return summary
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return None