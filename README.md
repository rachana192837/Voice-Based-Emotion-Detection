# Voice Based Emotion Detection

A simple and interactive web application that predicts a speaker's emotion from an uploaded audio file using a pre-trained machine learning model.

## Features
- **Interactive UI**: Built with Streamlit for a clean and easy-to-use interface.
- **Audio Processing**: Uses `librosa` to process uploaded audio files (`.wav`, `.mp3`, `.ogg`, `.flac`).
- **AI Emotion Recognition**: Leverages Hugging Face's `transformers` pipeline to run the `superb/wav2vec2-base-superb-er` model, which analyzes speech and predicts emotions (e.g., Happy, Angry, Sad, Neutral).

## Prerequisites
- Python 3.8+ 

## Installation

1. **Clone or Download the Repository** (or navigate to the project directory)
2. **Create a Virtual Environment** 
   ```powershell
   python -m venv venv
   ```
3. **Activate the Virtual Environment**
   - Windows:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
4. **Install Dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application**
   Make sure your virtual environment is activated, then start the Streamlit server:
   ```powershell
   streamlit run app.py
   ```
2. **Access the Web App**
   The application should automatically open in your default browser at `http://localhost:8501`. 
3. **Upload an Audio File**
   Use the file uploader to provide an audio recording and click **Detect Emotion** to view the AI's prediction!

## Note on First Execution
The very first time you click "Detect Emotion", the application will download the pre-trained model weights from Hugging Face. This may take a few moments depending on your internet connection. Subsequent runs will use the cached model and be much faster.
