from pydub import AudioSegment

# vowel sound
file1_path = r'C:\Users\aryal\OneDrive\Desktop\voice model\v1\src\Sound\vowel\1.wav'
file2_path = r'C:\Users\aryal\OneDrive\Desktop\voice model\v1\src\Sound\vowel\2.wav'
file3_path = r'C:\Users\aryal\OneDrive\Desktop\voice model\v1\src\Sound\vowel\3.wav'
file4_path = r'C:\Users\aryal\OneDrive\Desktop\voice model\v1\src\Sound\vowel\4.wav'
file5_path = r'C:\Users\aryal\OneDrive\Desktop\voice model\v1\src\Sound\vowel\5.wav'
file6_path = r'C:\Users\aryal\OneDrive\Desktop\voice model\v1\src\Sound\vowel\6.wav'
file7_path = r'C:\Users\aryal\OneDrive\Desktop\voice model\v1\src\Sound\vowel\7.wav'
file8_path = r'C:\Users\aryal\OneDrive\Desktop\voice model\v1\src\Sound\vowel\8.wav'
file9_path = r'C:\Users\aryal\OneDrive\Desktop\voice model\v1\src\Sound\vowel\9.wav'
file10_path = r'C:\Users\aryal\OneDrive\Desktop\voice model\v1\src\Sound\vowel\10.wav'
file11_path = r'C:\Users\aryal\OneDrive\Desktop\voice model\v1\src\Sound\vowel\11.wav'
file12_path = r'C:\Users\aryal\OneDrive\Desktop\voice model\v1\src\Sound\vowel\12.wav'

# consonant sound
file13_path = r'C:\Users\aryal\OneDrive\Desktop\voice model\v1\src\Sound\consonant\1.wav'
file14_path = r'C:\Users\aryal\OneDrive\Desktop\voice model\v1\src\Sound\consonant\2.wav'


# Load the audio files using pydub to ensure consistent length
audio1 = AudioSegment.from_file(file1_path, format="wav")
audio2 = AudioSegment.from_file(file2_path, format="wav")
audio3 = AudioSegment.from_file(file3_path, format="wav")
audio4 = AudioSegment.from_file(file4_path, format="wav")
audio5 = AudioSegment.from_file(file5_path, format="wav")
audio6 = AudioSegment.from_file(file6_path, format="wav")
audio7 = AudioSegment.from_file(file7_path, format="wav")
audio8 = AudioSegment.from_file(file8_path, format="wav")
audio9 = AudioSegment.from_file(file9_path, format="wav")
audio10 = AudioSegment.from_file(file10_path, format="wav")
audio11 = AudioSegment.from_file(file11_path, format="wav")
audio12 = AudioSegment.from_file(file12_path, format="wav")

# consonant sound
audio13 = AudioSegment.from_file(file13_path, format="wav")
audio14 = AudioSegment.from_file(file14_path, format="wav")
