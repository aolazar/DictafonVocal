import whisper
import sounddevice as sd
import numpy as np
import subprocess
from scipy.io.wavfile import write
from pynput import keyboard
import threading
import time
import sys

# Setari
model_size = None
if len(sys.argv) > 1:
    model_size = sys.argv[1]
else:
    print("No Whisper model specified. Available models are:")
    for model_name in whisper.available_models():
        print(f"- {model_name}")
    print("\nPlease run the script with a model name, e.g.:")
    print("python3 dictafon.py small")
    sys.exit(1)

samplerate = 16000
output_filename = "/tmp/dictaphone_recording.wav"

recording = False
audio_data = []

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, flush=True)
    if recording:
        audio_data.append(np.frombuffer(indata, dtype=np.int16).copy())

def on_press(key):
    global recording, audio_data
    try:
        if key == keyboard.Key.f12:
            if not recording:
                # Start recording
                print("Recording started (F12 pressed)...")
                recording = True
                audio_data = []  # Clear previous data
            else:
                # Stop recording
                print("Recording stopped (F12 pressed again).")
                recording = False
                # Trigger audio processing in a separate thread to avoid blocking the key listener
                threading.Thread(target=process_audio, args=(list(audio_data),)).start()
                audio_data = [] # Clear the global list immediately after passing a copy
    except AttributeError:
        pass

def process_audio(recorded_audio_blocks):
    if recorded_audio_blocks:
        combined_audio = np.concatenate(recorded_audio_blocks, axis=0)
        write(output_filename, samplerate, combined_audio)  # Save as WAV file
        print(f"Recording saved to {output_filename}")

        # Incarca modelul Whisper
        model = whisper.load_model(model_size)
        text = transcribe_audio(model, output_filename)
        if text:
            print(f"Recognized: {text}")
            subprocess.run(['xdotool', 'type', '--clearmodifiers', text])
    else:
        print("No audio recorded.")

def transcribe_audio(model, audio_path):
    print("Transcribing audio...")
    result = model.transcribe(audio_path, language='ro')
    return result["text"]

def main():
    print(f"Using Whisper model: {model_size}")
    print("Press F12 to start recording. Press F12 again to stop and transcribe.")
    with sd.RawInputStream(samplerate=samplerate, channels=1, dtype='int16', callback=callback):
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        listener.join() # Keep the main thread alive

if __name__ == "__main__":
    main()