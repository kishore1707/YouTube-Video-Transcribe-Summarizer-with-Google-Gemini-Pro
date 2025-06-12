# 🎥 YouTube Transcript Summarizer with Gemini AI

This project is a **Streamlit-based web application** that:
- Extracts **transcripts** from any YouTube video (with subtitles)
- Generates a **clean point-wise summary** using **Google Gemini Pro API**
- Displays the **YouTube video title** and full transcript
- Provides a user-friendly interface for fast summarization

---

## 📌 Features

✅ Input a standard or short YouTube URL  
✅ Automatically extracts the video title and transcript  
✅ Handles errors like unavailable transcripts or invalid links  
✅ Sends transcript to Gemini Pro for summarization  
✅ Displays point-wise bullet summary for better readability  

---

## 🖼️ Demo UI

> `Streamlit` app interface:
- You enter a YouTube URL
- The app shows:
  - 🎬 Title of the video
  - 📝 Transcript (if available)
  - 📄 Gemini-powered point-wise summary

---

## 🔧 Tech Stack

| Tool                  | Purpose                      |
|-----------------------|------------------------------|
| **Streamlit**         | Web-based UI                 |
| **YouTube Transcript API** | Extract subtitles from YouTube |
| **Google Gemini Pro API**  | Generate point-wise summary     |
| **Python**            | App logic, backend handling  |
| **Pytube**            | Get video title from URL     |

---

## 📁 Project Structure

