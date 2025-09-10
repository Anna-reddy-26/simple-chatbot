import google.generativeai as genai

# configure your API key
API_KEY = "AIzaSyAoH4UpnMKW8fmKTMZi6JR1M4gAsJIH6Ko"
genai.configure(api_key=API_KEY)

# load the model and start a chat session
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

print("Chat with Gemini! Type 'exit' or 'quit' to end the session.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting chat. Goodbye!")
        break
    
    # send user input to Gemini
    response = chat.send_message(user_input)
    print("Gemini:", response.text)
