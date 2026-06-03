import ollama

video_link = 'https://youtu.be/2RAFDnej5SM&t='
transcript_file = 'videos/004.txt'
transcript_summary_file = 'videos/004_Summary.md'

transcript_summary_file = open(transcript_summary_file, "w", encoding="utf-8") 

# Open the file safely
with open(transcript_file, 'r', encoding='utf-8') as file:
    content = file.read()
    
    # Split by a specific delimiter (e.g., a comma)
    tokens = content.split('--------------------------------------------------')

record_counter = 0
content_to_summarize = ""
document_ids_summarized = ""

for atoken in tokens:
    tokenarr = atoken.split("] ")
    record_counter = record_counter + 1 

    if len(tokenarr) == 2:
        doc_id = transcript_file + tokenarr[0].strip() + "] "
        content_from_this_minute = tokenarr[1]
        
        #Chunk every 10 records. 
        if record_counter % 10 == 0:
          print("Summarizing text of length : " + str(len(content_to_summarize)))
          my_prompt = f'This is a personal note, what is it about? {content_to_summarize}'
          response = ollama.generate(model='granite4.1:3b', prompt=my_prompt)
          actual_response = response['response']
          transcript_summary_file.write("<br /><br />")
          transcript_summary_file.write(video_link + str(record_counter-10) + "m<br />")
          transcript_summary_file.write(actual_response + "<br />")
          # Trying to summarize entire passes of bigger size as we go.
          # The final summary then would encapsulate the entire document. 
          # content_to_summarize = ""       
          document_ids_summarized = ""    
        else:
            content_to_summarize += "\n".join(content_from_this_minute)
            document_ids_summarized = document_ids_summarized + "<br />" + doc_id


#Final Chunk
if len(content_to_summarize) > 0:
  my_prompt = f'This is a personal note, what is it about? {content_to_summarize}'
  response = ollama.generate(model='granite4.1:3b', prompt=my_prompt)
  actual_response = response['response']
  transcript_summary_file.write("<br /><br />")
  transcript_summary_file.write(video_link + str(record_counter-10) + "m<br />")
  transcript_summary_file.write(actual_response + "<br />") 
  
transcript_summary_file.flush()
transcript_summary_file.close()







