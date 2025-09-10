import google.generativeai as genai

# configure your API key
API_KEY = ""
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

print("Chat with Gemini! Type 'exit' or 'quit' to end the session.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting chat. Goodbye!")
        break
    
    response = chat.send_message(user_input)
    print("Gemini:", response.text)
