from pydub import AudioSegment
import glob, os

os.makedirs("outputs", exist_ok=True)

files = sorted(glob.glob("data/audio_clips/[0-9][0-9]_*.mp3"))
pause = AudioSegment.silent(duration=600)  # 0.6s pause
final = AudioSegment.silent(duration=0)

for f in files:
    final += AudioSegment.from_file(f) + pause

output_file = "outputs/deepfake_job_interview.mp3"
final.export(output_file, format="mp3")
print(f"Wrote {output_file}")
