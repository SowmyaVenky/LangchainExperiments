import whisper

# Load the model (options: "tiny", "base", "small", "medium", "large")
# "base" balances speed and accuracy well for most tasks
model = whisper.load_model("large")

# Transcribe the audio file
result = model.transcribe(r"C:\Venky\LangchainExperiments\02-ManiMama\videos\005.mp4")

# Write the extracted text to a .txt file
with open(r"C:\Venky\LangchainExperiments\02-ManiMama\videos\005.txt", "w", encoding="utf-8") as text_file:
    text_file.write(result["text"].strip())

