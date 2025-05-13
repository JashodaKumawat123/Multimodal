# import speech_recognition as sr
# import speech_recognition as sr

# def convert_speech_to_text(audio_path):
#     recognizer = sr.Recognizer()
#     with sr.AudioFile(audio_path) as source:
#         audio = recognizer.record(source)
    
#     try:
#         text = recognizer.recognize_google(audio)
#         return f"Transcription: {text}"
#     except sr.UnknownValueError:
#         return "Sorry, I could not understand the audio."
#     except sr.RequestError as e:
#         return f"Could not request results; {e}"

# # Example usage
# audio_path = r"C:\Users\Jashoda\Downloads\town-10169.wav"
#   # Provide the correct file path
# print(convert_speech_to_text(audio_path))
import speech_recognition as sr
import os

def convert_speech_to_text(audio_path):
    if not os.path.exists(audio_path):
        return f" File not found: {audio_path}"

    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio)
        return f"Transcription: {text}"
    
    except sr.UnknownValueError:
        return " Sorry, I could not understand the audio."
    except sr.RequestError as e:
        return f"Could not request results; {e}"

# Example usage
if __name__ == "__main__":
    audio_path = r"C:\Users\Jashoda\Downloads\town-10169.wav"  # Make sure this path is correct
    print(convert_speech_to_text(audio_path))
