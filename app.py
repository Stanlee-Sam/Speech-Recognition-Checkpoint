import streamlit as st
import speech_recognition as sr
import os

# Available speech recognition APIs
API_OPTIONS = {
    "Google Speech Recognition": "google",
    "Sphinx (Offline)": "sphinx",
    "Wit.ai": "wit",
    "Bing Speech": "bing"
}

# Default keys for APIs
WIT_KEY = "YOUR_WIT_AI_KEY"
BING_KEY = "YOUR_BING_API_KEY"

def main():
    st.title("🎤 Speech Recognition App (Python 3.13 Compatible)")

    # Upload only WAV files
    uploaded_file = st.file_uploader("Upload a WAV audio file", type=["wav"])

    # Language selection
    language = st.selectbox(
        "Select language:",
        ["en-US", "en-GB", "sw", "fr-FR", "de-DE", "es-ES", "ar-SA", "hi-IN"]
    )

    # API selection
    api_choice = st.selectbox("Choose Speech Recognition API:", list(API_OPTIONS.keys()))

    # Pause/Resume state
    if "paused" not in st.session_state:
        st.session_state.paused = False

    st.subheader("Controls")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⏸ Pause"):
            st.session_state.paused = True
    with col2:
        if st.button("▶ Resume"):
            st.session_state.paused = False

    if uploaded_file:
        # Save uploaded WAV file temporarily
        wav_path = "uploaded_audio.wav"
        with open(wav_path, "wb") as f:
            f.write(uploaded_file.read())
        st.success("WAV file uploaded successfully.")

        if not st.session_state.paused:
            st.info("Transcribing audio...")
            text = transcribe_audio(wav_path, API_OPTIONS[api_choice], language)
            st.write("### 📝 Transcription:")
            st.write(text)

            # Option to save transcription
            if st.button("💾 Save Transcription to File"):
                save_text(text)

def transcribe_audio(file_path, api_key, language):
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(file_path) as source:
            audio_data = recognizer.record(source)

        if api_key == "google":
            return recognizer.recognize_google(audio_data, language=language)

        elif api_key == "sphinx":
            return recognizer.recognize_sphinx(audio_data, language=language)

        elif api_key == "wit":
            if WIT_KEY == "YOUR_WIT_AI_KEY":
                return "❌ Wit.ai API key not provided."
            return recognizer.recognize_wit(audio_data, key=WIT_KEY)

        elif api_key == "bing":
            if BING_KEY == "YOUR_BING_API_KEY":
                return "❌ Bing API key not provided."
            return recognizer.recognize_bing(audio_data, key=BING_KEY, language=language)

        else:
            return "❌ Unsupported API selected."

    except sr.UnknownValueError:
        return "❌ Could not understand audio. Please try again."

    except sr.RequestError as e:
        return f"❌ API request failed: {str(e)}"

    except Exception as ex:
        return f"⚠ Unexpected error: {str(ex)}"

def save_text(text):
    filename = "transcription.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    st.success(f"Saved as {filename}")
    st.download_button("⬇ Download File", text, file_name=filename)

if __name__ == "__main__":
    main()
