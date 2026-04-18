import streamlit as st
import librosa
import numpy as np
from transformers import pipeline

# Page config
st.set_page_config(page_title="Voice Emotion Detection", page_icon="🎙️", layout="centered")

@st.cache_resource
def load_emotion_model():
    # Use cache to avoid reloading model on every interaction
    classifier = pipeline("audio-classification", model="superb/wav2vec2-base-superb-er")
    return classifier

# UI
st.title("🎙️ Voice Based Emotion Detection")
st.markdown("Upload an audio file (.wav, .mp3, .ogg) and the application will detect the emotion in the speech.")

# Load model
with st.spinner("Loading speech emotion recognition model..."):
    try:
        classifier = load_emotion_model()
    except Exception as e:
        st.error(f"Failed to load model. Ensure internet connection and dependencies are met. Details: {e}")
        st.stop()

# Audio source selection
uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "ogg", "flac"])

if uploaded_file is not None:
    st.audio(uploaded_file)
    
    if st.button("Detect Emotion"):
        with st.spinner("Analyzing audio..."):
            try:
                # Librosa can load Streamlit's UploadedFile object
                # Re-seek to 0 before reading
                uploaded_file.seek(0)
                audio_data, sr = librosa.load(uploaded_file, sr=16000)
                
                # Make prediction (HuggingFace pipeline expects a numpy array at the model's sampled rate)
                predictions = classifier(audio_data)
                
                st.success("Analysis Complete!")
                st.subheader("Results:")
                
                # Display Results
                for pred in predictions:
                    label = pred['label']
                    score = pred['score']
                    st.write(f"**{label.capitalize()}**: {score:.2%}")
                    st.progress(float(score))
                    
            except Exception as e:
                st.error(f"An error occurred while processing the audio: {e}")
