# Langchain Experiments.

The code developed in this repository is mostly created by watching the training videos created by Kris Naik. Here is the video link - https://www.youtube.com/watch?v=rV3HJ4LEZ7k

I have downloaded Ollama and am using locally hosted light weight models to test with. The advantage of doing this is that I get to know the "behind-the-scenes" on how these models work. Also the computer that I am working with does not have any GPU and therefore is seriously limited by the tokens per second it can give when bigger models are used. 

Setting up Ollama is very easy on any OS and there are many videos showing how to do it. 
For the computer I am using I am able to run the granite:4.1 3B parameter model that can support tools and the tinyllama 1.1B models. These are super quick.

For checking what models are running we can execute this command.
<code>
C:\Venky\LangchainExperiments>ollama list
NAME              ID              SIZE      MODIFIED
granite4.1:3b     6fd349357287    2.1 GB    39 minutes ago
tinyllama:1.1b    2644915ede35    637 MB    3 hours ago
gemma4:latest     c6eb396dbd59    9.6 GB    22 hours ago
</code>

Other code links 
https://github.com/krishnaik06/Langchain-V1-Crash-Course


### Run the streamlit application to show a chatbot UI
<code>
(.venv) PS C:\Venky\LangchainExperiments\01-RAGTesting> streamlit run .\app.py
</code>
