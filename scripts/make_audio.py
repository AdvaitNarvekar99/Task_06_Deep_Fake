from google.cloud import texttospeech
import os

client = texttospeech.TextToSpeechClient()

# --- Script (pulled from src/prompts/street_interview.txt) ---
script = [
    ("JORDAN", "Hey everyone, we're here on the street today talking about a new kind of scam: AI deep fakes in job interviews! It's happening more and more, with scammers using fake videos and voices to get remote jobs."),
    ("JORDAN", "Excuse me, have you heard about deep fake job candidates?"),
    ("ALEX", "Yeah, it's crazy. You can't even trust a video call anymore. My company is worried about it."),
    ("JORDAN", "What would you do if you were in an interview and noticed something was off?"),
    ("ALEX", "I'd probably just end the call. The movements and lip-syncing might not match the audio, and it would feel super creepy."),
    ("JORDAN", "As a hiring manager, how would you make sure you're not interviewing a deep fake?"),
    ("SARAH", "I'd look for red flags like distorted facial features or unnatural eye movements. I might even ask them to wave their hand in front of their face to see if it disrupts the filter."),
    ("JORDAN", "That's a smart strategy. Some companies are also using AI to detect this type of fraud."),
    ("JORDAN", "What do you think is the biggest risk for companies hiring deep fake candidates?"),
    ("MARK", "It's a huge security risk. You could be hiring a malicious actor without knowing it, which could lead to a loss of intellectual property or data."),
    ("JORDAN", "So it's not just about a fake employee, it's about a real threat to the business."),
    ("MARK", "Exactly. It's a significant security threat that requires immediate attention."),
    ("JORDAN", "And that's a wrap! It's clear that deep fakes are a growing concern, but with the right tactics, businesses and job seekers can stay protected.")
]

preferred_voices = {
    "JORDAN": "en-US-Neural2-C",
    "ALEX":   "en-US-Neural2-D",
    "SARAH":  "en-US-Neural2-F",
    "MARK":   "en-US-Neural2-H",
}

# Ensure audio_clips directory exists
os.makedirs("data/audio_clips", exist_ok=True)

def pick_voice(role, available):
    name = preferred_voices[role]
    if name in available:
        return name
    fallbacks = [
        "en-US-Neural2-C","en-US-Neural2-D","en-US-Neural2-F",
        "en-US-Neural2-G","en-US-Neural2-H","en-US-Neural2-I","en-US-Neural2-J",
        "en-US-Standard-C","en-US-Standard-D"
    ]
    for fb in fallbacks:
        if fb in available:
            return fb
    return next(iter(available))

# List available voices
resp = client.list_voices(language_code="en-US")
available = {v.name for v in resp.voices}

for i, (speaker, line) in enumerate(script, start=1):
    try:
        voice_name = pick_voice(speaker, available)
        synthesis_input = texttospeech.SynthesisInput(text=line)
        voice_params = texttospeech.VoiceSelectionParams(language_code="en-US", name=voice_name)
        audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice_params, audio_config=audio_config
        )
        filename = os.path.join("data", "audio_clips", f"{i:02d}_{speaker}.mp3")
        with open(filename, "wb") as out:
            out.write(response.audio_content)
        print(f"Saved {filename} ({voice_name})")
    except Exception as e:
        print(f"Skipped line {i} ({speaker}) due to error: {e}")
