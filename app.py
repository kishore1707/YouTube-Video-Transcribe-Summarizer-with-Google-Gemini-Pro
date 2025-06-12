import streamlit as st
import os
import re
from dotenv import load_dotenv
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import VideoUnavailable, TranscriptsDisabled, NoTranscriptFound
from pytube import YouTube  # For getting video title

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Streamlit UI
st.set_page_config(page_title="YouTube Transcript Summarizer")
st.title("🎥 YouTube Transcript Summarizer")

youtube_url = st.text_input("🔗 Enter YouTube URL")

# Function to extract video ID
def extract_video_id(url):
    match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", url)
    if match:
        return match.group(1)
    return None

# Function to extract transcript
def extract_transcript_details(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry['text'] for entry in transcript])
    except VideoUnavailable:
        return "❌ Error: The video is unavailable or the link is incorrect."
    except TranscriptsDisabled:
        return "❌ Error: Transcripts are disabled for this video."
    except NoTranscriptFound:
        return "❌ Error: No transcript was found for this video."
    except Exception as e:
        return f"❌ Unexpected Error: {str(e)}"

# Function to get YouTube title
def get_video_title(url):
    try:
        yt = YouTube(url)
        return yt.title
    except Exception:
        return "📛 Title not available"

# Function to summarize using Gemini
def generate_gemini_summary(transcript, prompt):
    try:
        model = genai.GenerativeModel(model_name="gemini-pro")
        response = model.generate_content(prompt + transcript)
        return response.text
    except Exception as e:
        return f"❌ Gemini Error: {str(e)}"

# Main logic
if youtube_url:
    video_id = extract_video_id(youtube_url)
    
    if not video_id:
        st.error("❌ Invalid YouTube URL format.")
    else:
        title = get_video_title(youtube_url)
        st.subheader(f"🎬 Title: {title}")

        transcript = extract_transcript_details(video_id)
        st.subheader("📝 Transcript:")
        st.write(transcript)

        if not transcript.startswith("❌"):
            # Add prompt for point-wise summary
            prompt = "Summarize this transcript in clear bullet points:\n"
            summary = generate_gemini_summary(transcript, prompt)
            
            st.subheader("📄 Point-wise Summary:")
            for line in summary.split("\n"):
                if line.strip():
                    st.markdown(f"• {line.strip()}")
