import google.generativeai as genai

# Add your API key here
genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-pro")

print("SmartAssist AI Chatbot (type 'exit' to stop)")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    response = model.generate_content(user_input)
    print("AI:", response.text)
