from network import Network 

n = Network()
message = n.connect()

while True:
    print(f"\n{message}\n")
    message_to_send = input("Message: ")
    # print("\n")
    message = n.send(message_to_send)
    if message == "quit":
        n.send("quit")
        print("\nEnding the chat...goodbye!")
        break