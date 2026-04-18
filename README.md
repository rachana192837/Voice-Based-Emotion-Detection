# 🔊 VocalSense AI: Voice Emotion Detection

> **Transforming speech into insight.** VocalSense AI is a premium, deep-learning powered web application that analyzes human vocal patterns to detect emotional states in real-time.

---

## ✨ Key Features
- **🎯 Precision Analysis**: Utilizing the `Wav2Vec2` transformer architecture for state-of-the-art speech emotion recognition.
- **📈 Live Waveform Visualization**: Interactive audio wave visualization using `librosa` and Streamlit.
- **📊 Dynamic Data Charting**: Real-time emotion confidence scoring powered by `Altair` interactive charts.
- **🎨 Premium UI/UX**: A modern, responsive interface featuring gradient aesthetics, glassmorphism elements, and intuitive navigation.
- **📂 Versatile File Support**: Process `.wav`, `.mp3`, `.ogg`, and `.flac` audio formats seamlessly.

## 🛠️ Technology Stack
- **Frontend**: [Streamlit](https://streamlit.io/)
- **Core AI**: [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- **Model**: `superb/wav2vec2-base-superb-er`
- **Audio Logic**: [Librosa](https://librosa.org/) & [Numpy](https://numpy.org/)
- **Visuals**: [Altair](https://altair-viz.github.io/) & [Pandas](https://pandas.pydata.org/)

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- [Git](https://git-scm.com/)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/rachana192837/Voice-Based-Emotion-Detection.git
   cd Voice-Based-Emotion-Detection
   ```

2. **Setup Virtual Environment**
   - Windows:
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Usage

1. **Launch the Server**
   ```bash
   streamlit run app.py
   ```
2. **Open in Browser**
   Navigate to `http://localhost:8501` (usually opens automatically).
3. **Analyze**
   Upload an audio file, watch the waveform generate, and click **Analyze Emotion** to see the results.

---

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📄 License
This project is licensed under the MIT License.
