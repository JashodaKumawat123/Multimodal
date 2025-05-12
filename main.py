from router import route_query

print("🧠 Welcome to the Multimodal SMoL-NLP Assistant! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = route_query(user_input)
    print("Assistant:", response)
