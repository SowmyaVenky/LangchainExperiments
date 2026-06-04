import ollama

transcript_file = 'videos/016.txt'
# Open the file safely
with open(transcript_file, 'r', encoding='utf-8') as file:
    text_content = file.read()

response = ollama.chat(model='gemma4:latest', messages=[
    {"role": "system", "content": "You are an expert at text analysis. Summarize and extract the key areas of the provided text."},
    {"role": "user", "content": f"Analyze the following text and outline the key areas, main themes, and important takeaways:\n\n{text_content}"}
])
print(response)