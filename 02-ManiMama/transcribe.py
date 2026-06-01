import os
import whisper
from datetime import timedelta

def transcribe_with_minute_timestamps(video_path: str, transcript_path: str, model_size: str = "base"):
    if not os.path.exists(video_path):
        print(f"File not found: {video_path}")
        return

    # Load the Whisper model (tiny, base, small, medium, or large)
    print(f"Loading Whisper '{model_size}' model...")
    model = whisper.load_model(model_size)

    # Transcribe the MP4 file
    print("Transcribing video... this may take a while.")
    result = model.transcribe(video_path, verbose=False)
    
    segments = result.get("segments", [])
    
    current_minute = 0
    minute_transcript = []

    print("\n--- Transcription by the Minute ---")
    with open(transcript_path, "w", encoding="utf-8") as text_file:
        for segment in segments:
            start_seconds = segment['start']
            text = segment['text'].strip()

            # Calculate current minute block
            minute_marker = int(start_seconds // 60)

            if minute_marker != current_minute:
                # Print the previous minute's results before moving to the next
                if minute_transcript:
                    print_minute_block(current_minute, minute_transcript, text_file)
                    minute_transcript = []
                current_minute = minute_marker

            minute_transcript.append(text)

        # Print the final remaining chunk
        if minute_transcript:
            print_minute_block(current_minute, minute_transcript, text_file)

def print_minute_block(minute, transcript_list, text_file):
    start_time = timedelta(minutes=minute)
    end_time = timedelta(minutes=minute + 1)
    
    text_file.write(f"\n[{start_time} - {end_time}] ")
    text_file.write(" ".join(transcript_list) + "\n")
    text_file.write("-" * 50)

if __name__ == "__main__":
    # Replace with the path to your local MP4 file
    video_file = r"C:\Venky\LangchainExperiments\02-ManiMama\videos\006.mp4" 
    transcript_path = r"C:\Venky\LangchainExperiments\02-ManiMama\videos\006.txt"
    
    transcribe_with_minute_timestamps(video_file, transcript_path, model_size="medium")