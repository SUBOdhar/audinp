from pydub import AudioSegment
import os

# Database file path
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load the audio files using pydub
audio_files = [
    AudioSegment.from_file(file_path, format="wav")
    for file_path in [
        os.path.join(current_dir, "Sound", "vowel", "1.wav"),
        os.path.join(current_dir, "Sound", "vowel", "2.wav"),
        os.path.join(current_dir, "Sound", "vowel", "3.wav"),
        os.path.join(current_dir, "Sound", "vowel", "4.wav"),
        os.path.join(current_dir, "Sound", "vowel", "5.wav"),
        os.path.join(current_dir, "Sound", "vowel", "6.wav"),
        os.path.join(current_dir, "Sound", "vowel", "7.wav"),
        os.path.join(current_dir, "Sound", "vowel", "8.wav"),
        os.path.join(current_dir, "Sound", "vowel", "9.wav"),
        os.path.join(current_dir, "Sound", "vowel", "10.wav"),
        os.path.join(current_dir, "Sound", "vowel", "11.wav"),
        os.path.join(current_dir, "Sound", "vowel", "12.wav"),
        os.path.join(current_dir, "Sound", "consonant", "1.wav"),
        os.path.join(current_dir, "Sound", "consonant", "2.wav")
    ]
]
