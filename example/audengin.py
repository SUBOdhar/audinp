from audsrc import *
import os

# Database file path
current_dir = os.path.dirname(os.path.abspath(__file__))
Temp_file_path = os.path.join(current_dir, "temp", "temp.wav")
combined_audio = 0.000
for i in range(14):
    combined_audio = combined_audio+audio_files[i]
# Make sure both audio clips have the same length
combined_audio.export(Temp_file_path, format="wav")
