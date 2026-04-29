# VocalSense AI: Voice Emotion Detection

> Transforming speech into insight. A deep-learning powered web application that analyzes human vocal patterns to detect emotional states in real-time.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-ff4b4b.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## Overview

VocalSense AI leverages the **Wav2Vec 2.0** transformer architecture to perform real-time speech emotion recognition. The application processes audio files through a pretrained deep learning model and visualizes emotion confidence scores through an interactive, modern web interface.

---

## Features

| Feature | Description |
|---------|-------------|
| **Precision Analysis** | Wav2Vec2-base-superb-er model for state-of-the-art emotion recognition |
| **Live Visualization** | Real-time waveform rendering using Librosa |
| **Dynamic Charts** | Interactive Altair charts displaying emotion confidence scores |
| **Premium UI/UX** | Modern interface with glassmorphism and responsive design |
| **Multi-Format Support** | WAV, MP3, OGG, and FLAC audio formats |

---

## Emotions Detected

The model classifies speech into **7 emotional categories**:

- 😠 **Angry** - Hostile or agitated vocal patterns
- 😃 **Happy** - Joyful, energetic speech
- 😢 **Sad** - Low-energy, melancholic tones
- 😐 **Neutral** - Baseline, emotionless speech
- 😨 **Surprised** - Sudden, elevated pitch patterns
- 🤔 **Disgusted** - Repulsed or contemptuous tones
- 😰 **Fearful** - Anxious, tense vocal qualities

---

## Technology Stack

**Frontend & UI**
- [Streamlit](https://streamlit.io/) - Interactive web interface

**Core AI & ML**
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) - Deep learning framework
- [Wav2Vec2-base-superb-er](https://huggingface.co/superb/wav2vec2-base-superb-er) - Emotion recognition model

**Audio Processing**
- [Librosa](https://librosa.org/) - Audio analysis and feature extraction
- [NumPy](https://numpy.org/) - Numerical operations

**Data & Visualization**
- [Pandas](https://pandas.pydata.org/) - Data manipulation
- [Altair](https://altair-viz.github.io/) - Statistical visualizations

---

## Installation

### Prerequisites

- Python 3.9 or higher
- Git (for cloning the repository)

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/rakshith1928/voice-based-emotion-detector.git
   cd voice-based-emotion-detector
   ```

2. **Create a virtual environment**
   
   Windows (PowerShell):
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
   
   macOS / Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Open in browser**
   
   The application launches automatically at `http://localhost:8501`

3. **Analyze audio**
   - Upload an audio file (WAV, MP3, OGG, or FLAC)
   - View the generated waveform visualization
   - Click **Analyze Emotion** to process the audio
   - Review the emotion confidence scores in the interactive chart

---

## Project Structure

```
voice-based-emotion-detector/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── .gitignore            # Git ignore rules
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Port 8501 already in use | Run `streamlit run app.py --server.port 8502` |
| Model download fails | Check internet connection; model downloads on first run |
| Audio file not loading | Verify file format is WAV, MP3, OGG, or FLAC |
| Slow initial inference | Model loads on first request; subsequent runs are faster |

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- [Hugging Face](https://huggingface.co/) for the Transformers library and model hosting
- [Superb Project](https://huggingface.co/superb) for the pretrained Wav2Vec2 emotion recognition model
- [Streamlit](https://streamlit.io/) for the rapid web application framework

---

## Contact

For questions or feedback, please open an issue on the [GitHub repository](https://github.com/rakshith1928/voice-based-emotion-detector/issues).
