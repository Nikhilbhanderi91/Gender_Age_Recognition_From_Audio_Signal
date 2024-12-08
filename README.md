# Speech Recognition and Gender/Age Estimation

This project utilizes Python's `speech_recognition` and `librosa` libraries to:
1. Capture live audio from a microphone.
2. Transcribe the audio into text using Google's Speech Recognition API.
3. Estimate the speaker's gender and approximate age based on the pitch of the audio.

## Features

- **Speech Recognition:** Captures audio from the microphone and converts it into text using Google's API.
- **Gender Estimation:** Analyzes the pitch of the speaker's voice and estimates gender as male, female, or "LGBTQ SUPPORTER" based on the median pitch.
- **Age Estimation:** Uses the detected pitch to estimate the age group of the speaker, ranging from children to older adults.

## Requirements

Make sure you have the following Python libraries installed:

- `speech_recognition`
- `librosa`
- `numpy`

You can install these dependencies using the following command:

```bash
pip install SpeechRecognition librosa numpy
