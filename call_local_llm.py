import ollama

response = ollama.chat(model='tinyllama:1.1b', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])

print(response['message']['content'])
