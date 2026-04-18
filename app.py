import streamlit as st
import librosa
import numpy as np
import pandas as pd
import altair as alt
from transformers import pipeline

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="VocalSense AI", page_icon="🔊", layout="wide", initial_sidebar_state="expanded")

# --- CUSTOM CSS FOR PREMIUM AESTHETICS ---
st.markdown("""
<style>
    /* Main Background & Fonts */
    .main {
        font-family: 'Inter', sans-serif;
    }
    /* Stylish Title */
    .title-text {
        font-size: 3rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #FF6B6B, #4ECDC4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .subtitle-text {
        font-size: 1.2rem;
        color: #A0AEC0;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_emotion_model():
    return pipeline("audio-classification", model="superb/wav2vec2-base-superb-er")

# --- SIDEBAR COMPONENT ---
with st.sidebar:
    st.markdown("## 🔊 VocalSense AI")
    st.markdown("---")
    st.markdown("### How it works")
    st.markdown("1. Upload any `.wav` or `.mp3` file.")
    st.markdown("2. We convert the audio into mathematical wave features.")
    st.markdown("3. A pre-trained Wav2Vec2 AI model analyzes the variations to predict emotions.")
    st.markdown("---")
    st.caption("Powered by HuggingFace & Streamlit")

# --- MAIN LAYOUT ---
st.markdown('<div class="title-text">VocalSense AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Detect human emotion directly from speech patterns using deep learning.</div>', unsafe_allow_html=True)

# Load model
with st.spinner("Loading AI Engine... (This may take a moment on first launch)"):
    try:
        classifier = load_emotion_model()
    except Exception as e:
        st.error(f"Engine failed to load: {e}")
        st.stop()

# --- UPLOADER ZONE ---
st.markdown("### 🎙️ Audio Input")
uploaded_file = st.file_uploader("Upload an audio clip to analyze", type=["wav", "mp3", "ogg", "flac"], label_visibility="collapsed")

if uploaded_file is not None:
    # Set up layout columns
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown("#### Audio Playback")
        st.audio(uploaded_file)
        
        analyze_clicked = st.button("🚀 Analyze Emotion", use_container_width=True)

    if analyze_clicked:
        with st.spinner("Decoding audio waves & extracting features..."):
            try:
                # Load audio
                uploaded_file.seek(0)
                audio_data, sr = librosa.load(uploaded_file, sr=16000)
                
                with col2:
                    st.markdown("#### Waveform Analysis")
                    # Downsample logic to draw the audio wave cheaply natively in streamlit
                    step = max(1, len(audio_data) // 500)
                    downsampled = audio_data[::step]
                    st.line_chart(downsampled, height=150, color="#4ECDC4")
                
                # Make prediction
                with col1:
                    st.toast("Predicting Emotion...", icon="🧠")
                predictions = classifier(audio_data)
                
                st.markdown("---")
                st.markdown("### 📊 AI Emotion Analysis Results")
                
                # Create a beautiful dataframe for Altair
                df = pd.DataFrame(predictions)
                df['score'] = df['score'] * 100 # percentage
                df['label'] = df['label'].str.capitalize()
                
                # Altair Bar Chart implementation
                chart = alt.Chart(df).mark_bar(cornerRadiusEnd=4).encode(
                    x=alt.X('score:Q', title="Confidence (%)", scale=alt.Scale(domain=[0, 100])),
                    y=alt.Y('label:N', title="", sort="-x"),
                    color=alt.Color('score:Q', scale=alt.Scale(scheme='turbo'), legend=None),
                    tooltip=[alt.Tooltip('label:N', title='Emotion'), alt.Tooltip('score:Q', title='Confidence %', format='.1f')]
                ).properties(height=300)
                
                st.altair_chart(chart, use_container_width=True)
                
                # Winner
                top_emotion = df.iloc[df['score'].idxmax()]
                st.success(f"**Dominant Emotion Detected**: {top_emotion['label']} with {top_emotion['score']:.1f}% confidence. 🎉")

            except Exception as e:
                st.error(f"An error occurred: {e}")
