
# 🎤 Speech Recognition App (Python 3.8 Compatible)

This is a simple **Speech Recognition App** built with **Python** and **Streamlit** that allows users to transcribe audio from WAV files using multiple speech recognition APIs.

---

## Features

- Upload **WAV audio files** and transcribe speech to text.
- Select the **speech recognition API** to use:
  - Google Speech Recognition
  - Sphinx (Offline)
  - Wit.ai
  - Bing Speech
- Choose the **language** of the audio for transcription.
- **Pause and Resume** transcription.
- **Save** the transcribed text to a file and download it.

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/speech-recognition-app.git
cd speech-recognition-app
````

2. Create a virtual environment (recommended):

```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Replace API keys in `app.py` if you want to use **Wit.ai** or **Bing Speech**:

```python
WIT_KEY = "YOUR_WIT_AI_KEY"
BING_KEY = "YOUR_BING_API_KEY"
```

---

## Usage

Run the Streamlit app:

```bash
python -m streamlit run app.py
```

1. Upload a WAV file.
2. Select the language.
3. Choose a Speech Recognition API.
4. Pause/Resume if needed.
5. View the transcription.
6. Save or download the transcription.

---

## Requirements

* Python 3.8+
* Streamlit
* SpeechRecognition
* (Optional) PyAudio – if using microphone input in future updates.

---

## Screenshots

*Add screenshots here if you like.*

---

## License

This project is open source under the MIT License.







