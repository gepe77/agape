import openai

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Function to ask OpenAI a question
def ask_openai(question):
    response = openai.chat.Completion.create(
        model="gpt-4",  # Model choice (can be gpt-3.5 or gpt-4)
        messages=[
            {"role": "user", "content": question}  # Send user input as message
        ],
        max_tokens=150,  # Limit the number of tokens in the response
        temperature=0.7,  # Control creativity (0-1)
    )
    
    return response['choices'][0]['message']['content'].strip()  # Extract the response content

# Asking a question
question = input("Tanyakan sesuatu kepada AI: ")
answer = ask_openai(question)

# Displaying the AI response
print("Jawaban AI:", answer)
