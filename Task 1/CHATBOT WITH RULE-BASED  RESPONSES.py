# Define rules and responses
rules = {
    "hello": "Hi there! I'm samson, How can I assist you today?",
    "how are you": "I'm just a chatbot, but I'm here to help! What can I do for you?",
    "bye": "Goodbye! Have a great day!",
    "who made you":" Priyanshu has made me",
    "default":"I'm not sure how to respond to that. Can you please rephrase your question?"
}
def get_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    
    # Check if any of the predefined rules match the user input
    for pattern, response in rules.items():
        if pattern in user_input:
            return response
    
    # If no rule matches, return the default response
    return rules["default"]
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    
    response = get_response(user_input)
    print("Chatbot:", response)
