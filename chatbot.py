import aiml

# -----------------------------
# AIML Chatbot Setup
# -----------------------------
# Create a new AIML kernel (chatbot engine)
kernel = aiml.Kernel()

# Load the startup AIML file
kernel.learn("aiml_files/std-startup.xml")

# Execute a command to load all AIML files from std-startup.xml
kernel.respond("LOAD AIML B")

print("Chatbot is ready! Type something to start chatting.")
print("Press Ctrl+C to exit.\n")

# -----------------------------
# Chat Loop
# -----------------------------
while True:
    user_input = input("You: ")
    bot_response = kernel.respond(user_input)
    print("Bot:", bot_response)
