import streamlit as st

# Set the page title
st.set_page_config(page_title="🎬 YouTube Video Embed", layout="centered")

# Main title
st.title("🎥 Watch a YouTube Video in Streamlit")

# Instructions
st.markdown("Paste a valid YouTube video URL below to watch it directly in the app.")

# Input field for YouTube URL
youtube_url = st.text_input("🔗 Enter YouTube URL", placeholder="e.g. https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# Display the video if URL is entered
if youtube_url:
    try:
        st.video(youtube_url)
    except Exception as e:
        st.error(f"⚠️ Could not load video: {e}")
else:
    st.info("Please enter a YouTube video URL to begin.")
