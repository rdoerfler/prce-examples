import os
from pydub import AudioSegment

# Root of your audiofiles folder
ROOT = "audiofiles"

# Loop through everything under audiofiles
for dirpath, _, filenames in os.walk(ROOT):
    for fname in filenames:
        if fname.endswith(".wav"):
            wav_path = os.path.join(dirpath, fname)
            mp3_path = os.path.splitext(wav_path)[0] + ".mp3"

            try:
                audio = AudioSegment.from_wav(wav_path)
                audio.export(mp3_path, format="mp3", bitrate="320k")
                print(f"✅ Converted: {wav_path} -> {mp3_path}")
            except Exception as e:
                print(f"⚠️ Failed on {wav_path}: {e}")

