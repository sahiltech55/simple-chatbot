import random

# Define a list of possible responses to the user's input
responses = {
    "hi": ["Hello!", "Hi there!", "Hi!"],
    "hello": ["Hello!", "Hi there!", "Hi!"],
    "how are you": ["I'm doing well, thank you.", "Not too bad, thanks for asking.", "I'm fine, how are you?"],
    "what is your name": ["My name is Chatbot.", "I'm Chatbot, nice to meet you!"],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!"],
    "bye": ["Goodbye, have a great day!", "See you later!", "Bye!"],
    "what are your interests": ["I'm interested in helping you with whatever you need!", "As a chatbot, I don't have interests like humans do, but I'm always here to chat with you."],
    "do you have any siblings": ["As a chatbot, I don't have siblings like humans do, but I'm here to chat with you!", "No, I don't have any siblings, but I'm here to chat with you!"],
    "what is your favorite color": ["As a chatbot, I don't have a favorite color, but I'm always here to chat with you!", "I don't have a favorite color, but I'm happy to chat with you about yours!"],
    "what do you like to do in your free time": ["As a chatbot, I don't have free time like humans do, but I'm always here to chat with you!", "I don't have free time, but I'm always here to chat with you about whatever you like!"],
    "what is the meaning of life": ["That's a deep question! Many people believe that the meaning of life is to find happiness and fulfillment.", "The meaning of life is different for everyone, and it's up to you to find your own purpose and meaning."],
    "what is your favorite food": ["As a chatbot, I don't eat food, but I'm here to chat with you about your favorite dishes!", "I don't have a favorite food, but I'm happy to hear about yours!"],
    "what is your favorite movie": ["As a chatbot, I don't watch movies, but I'm here to chat with you about your favorite films!", "I don't have a favorite movie, but I'm always interested to hear about your favorites!"],
    "what's your favorite book": ["As an AI language model, I don't have the ability to read books or have personal preferences."],
    "what's the best way to learn a new language": ["The best way to learn a new language is to practice consistently and immerse yourself in the language as much as possible. This could involve taking classes, practicing with native speakers, watching movies or TV shows in the language, and using language-learning apps or software."],
    "what's the most important skill for a successful career": ["One of the most important skills for a successful career is the ability to communicate effectively, both verbally and in writing. Other important skills include problem-solving, teamwork, adaptability, and a strong work ethic."],
    "what's the best way to manage stress": ["The best way to manage stress can vary from person to person, but some effective strategies include exercise, meditation or mindfulness, getting enough sleep, and practicing good self-care habits such as eating healthy and taking breaks when needed. It can also be helpful to identify and address the sources of your stress."],
    "what's your favorite ipl team": ["As a chatbot, I don't have any favorite team in ipl but the team you like is the best."]
}


# Define a function to handle the user's input and generate a response
def respond(input):
    input = input.lower().strip()
    if input in responses:
        return random.choice(responses[input])
    else:
        return "I'm sorry, I didn't understand what you said. Could you please repeat that?"


# Greet the user
print("Hi there! I'm a chatbot. How can I help you today?")

# Keep the chatbot running until the user enters "bye"
while True:
    # Get input from the user
    user_input = input("> ")

    # Check if the user wants to end the conversation
    if user_input.lower() == "bye":
        print(respond(user_input))
        break
            
    # Generate a response based on the user's input
    print(respond(user_input))

    
  



