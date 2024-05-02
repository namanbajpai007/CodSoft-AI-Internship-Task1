import spacy
class ChatBot:
    def __init__(self):
        #Loading English language model
        self.nlp = spacy.load("en_core_web_sm")
        # Defining rules and responses of the chatbot
        self.rules = {
            "hi": "Hello! How can I assist you today?",
            "hello": "Hi there! What can I do for you?",
            "how are you": "I'm Fantastic , I hope you're doing well!",
            "bye": "Goodbye! Have a great day!"
        }
    #Function to get responses from the chatbot
    def get_response(self, user_input):
        # Processing user input and converting input into lowercase using spaCy
        doc = self.nlp(user_input.lower())
        #Checking for specific user inputs
        if "hi" in user_input.lower() or "hello" in user_input.lower() or "hey" in user_input.lower():
            return "Hello! How can I assist you today?"
        elif "how are you" in user_input.lower():
            return "I'm Fantastic , I hope you're doing well!"
        elif "weather" in user_input.lower():
            return "I'm sorry, I can't provide weather information at the moment."
        elif "what can you do" in user_input.lower():
            return "I'm a simple Rule-based chatbot. You can ask me questions or engage in conversation."
        elif "do you understand me" in user_input.lower():
            return "I'm trying my best to understand you!"
        else:
            # Iterating through tokens to check for matching rules
            for token in doc:
                if token.text in self.rules:
                    return self.rules[token.text]

        #If no rule matches, providing a default response
        return "Sorry, I didn't understand that."
    # Main function to run the chatbot
    def run(self):
        print("Chatbot: Hello! How can I assist you today?")
        while True:
            user_input = input("User: ")  # Getting the user input
            if user_input.lower() == 'exit':
                print("Chatbot: Goodbye! Have a great day!")
                break
            response = self.get_response(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    chatbot = ChatBot()
    chatbot.run()