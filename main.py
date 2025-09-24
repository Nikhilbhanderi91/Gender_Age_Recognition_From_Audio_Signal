import speech_recognition as sr
import librosa
import numpy as np
import io

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        print("Say something:")
        audio = recognizer.listen(source)
        
        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            return text, audio.get_wav_data()
        except sr.UnknownValueError:
            return "Could not understand audio", None
        except sr.RequestError:
            return "Could not request results", None

def estimate_gender_from_audio(audio_data):
    try:
        audio_buffer = io.BytesIO(audio_data)
        y, sr = librosa.load(audio_buffer, sr=None)
        pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)
        pitches = pitches[magnitudes > np.median(magnitudes)]
        pitches = pitches[(pitches >= 85) & (pitches <= 300)]
        
        if len(pitches) == 0:
            return "No pitch detected"

        pitch_median = np.median(pitches)
        print(f"Detected median pitch: {pitch_median} Hz")
        
        if pitch_median < 235:
            gender = "Male"
        elif 235 <= pitch_median <= 500:
            gender = "Female"
        else:
            gender = "LGBTQ SUPPORTER"
        
        return gender, pitch_median
    
    except Exception as e:
        return f"An error occurred during gender estimation: {e}", None

# def estimate_age_from_audio(pitch_median):
#     if pitch_median < 160:
#         age = "Adult (Approx. 30+)"
#     elif 160 <= pitch_median < 250:
#         age = "Young Adult (Approx. 16-30)"
#     else:
#         age = "Child or Teen (Approx. < 16)"
#     return age
def estimate_age_from_audio(pitch_median):
    if pitch_median < 140:
        age = "Middle-aged or Older Adult (Approx. 40+)"
    elif 140 <= pitch_median < 160:
        age = "Adult (Approx. 30-40)"
    elif 160 <= pitch_median < 180:
        age = "Young Adult (Approx. 20-30)"
    elif 180 <= pitch_median < 200:
        age = "Late Teen (Approx. 16-20)"
    elif 200 <= pitch_median < 220:
        age = "Early Teen (Approx. 13-16)"
    else:
        age = "Child (Approx. < 13)"
    return age




def process_live_audio():
    transcription, audio_data = recognize_speech_from_mic()
    
    if audio_data is None:
        print("No audio captured or an error occurred.")
        return transcription, "N/A", "N/A"
    
    gender, pitch_median = estimate_gender_from_audio(audio_data)
    age = estimate_age_from_audio(pitch_median) if pitch_median else "N/A"
    return transcription, gender, age

# Example usage:
transcription, gender, age = process_live_audio()

print(f"Transcription: {transcription}")
print(f"Estimated Gender: {gender}")
print(f"Estimated Age Range: {age}") 

