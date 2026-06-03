import ollama

note = 'videos/001.txt'

with open(note, 'r', encoding='utf-8') as file:
  content = file.read()

my_prompt = f'This is a personal note, what is it about? {content}'

response = ollama.generate(model='granite4.1:3b', prompt=my_prompt)
actual_response = response['response']
print(actual_response)
