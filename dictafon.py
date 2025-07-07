import whisper
import sounddevice as sd
import numpy as np
import subprocess
from scipy.io.wavfile import write

# Setari
model_size = "small"  # tiny, base, small, medium, large
samplerate = 16000
duration = 5  # seconds
output_filename = "temp_recording.wav"

def record_audio(duration, samplerate, output_filename):
    print(f"Recording for {duration} seconds...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    write(output_filename, samplerate, recording)  # Save as WAV file
    print(f"Recording saved to {output_filename}")

def transcribe_audio(model, audio_path):
    print("Transcribing audio...")
    result = model.transcribe(audio_path)
    return result["text"]

def main():
    try:
        # Incarca modelul Whisper
        model = whisper.load_model(model_size)

        while True:
            input("Press Enter to start recording, then Ctrl+C to stop...")
            record_audio(duration, samplerate, output_filename)
            text = transcribe_audio(model, output_filename)
            if text:
                print(f"Recognized: {text}")
                subprocess.run(['xdotool', 'type', '--clearmodifiers', text])

    except KeyboardInterrupt:
        print('\nDone')
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()