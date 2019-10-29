import random






x=' ';

greetings = [ 'hello', 'hi', 'Hi', 'hey!','hey']
greeting_response = [ "sup ranjhna",  "hey!! how can i help you?"]
random_greeting = random.choice(greeting_response)

question = ['How are you?','How are you doing?']
responses = ["I'm good"]
random_response = random.choice(responses)


while True:
	userInput = input(">>>  ")
	if userInput in greetings:
		print(15*x+ random_greeting)
	elif userInput in question:
		print(15*x+ random_response)
	else:
		print("i am not sure if i can answer that")
