"""
Fist the chatbot asks for the user's name and store it 
Then it is ready for any question:
1. If mathmatical question, it uses re.search to handle questions like:
Add/sum of 5 and/to 3, Subtract 5 from 7, Multiply 2 by 4, Divide 8 by 2
Calculate 5 + 3, Calculate 7 - 5, Calculate 2 * 4, Calculate 8 / 2
What is 5 + 3, What is 7 - 5, What is 2 * 4, What is 8 / 2
And according to the format it returns the result

2. If greetings like: hi, hello, thank you, bye

3. If bye, it exits the chat

4. If another question or mathmatical question with another format, it responds: Cannot answer this question, Try another question!

"""

import re

def Handle_mathematical_questions(userInput):
    patterns = [
        r'(?:add|sum of)\s*(\d+\.?\d*)\s*(?:and|to)\s*(\d+\.?\d*)',
        r'(?:subtract)\s*(\d+\.?\d*)\s*(?:from)\s*(\d+\.?\d*)',
        r'(?:multiply| multiplication of)\s*(\d+\.?\d*)\s*(?:by|and)\s*(\d+\.?\d*)',
        r'(?:divide)\s*(\d+\.?\d*)\s*(?:by)\s*(\d+\.?\d*)',
        r'(?:what is|calculate)\s*(\d+\.?\d*)\s*(plus|\+|minus|\-|times|\*|divided by|/)\s*(\d+\.?\d*)'
    ]

    for pattern in patterns:
        found = re.search(pattern, userInput, re.IGNORECASE)

        if found:
            groups = found.groups()
            if len(groups) == 2: #Add/sum of 5 and 3 OR subtracct 7 from 12 ...
                num1, num2 = map(float, groups)
                if "add" in userInput or "sum of" in userInput:
                    return num1 + num2 
                elif "subtract" in userInput:
                    return num2 - num1
                elif "multiply" in userInput or "multiplication of" in userInput:
                    return num1 * num2 
                elif "divide" in userInput:
                    if num2 == 0:
                        return "Cannot divide by zero"
                    else:
                        return num1 / num2
            
            elif len(groups) == 3:
                if groups[1] in '+-*/':
                    num1, op, num2 = float(groups[0]), groups[1], float(groups[2])
                else:
                    num1, op_word, num2 = float(groups[0]), groups[1], float(groups[2])
                    op = {"plus":'+', "minus": '-', "times":'*', "divided by":'/'}.get(op_word)

                if op == '+':
                    return num1 + num2 
                elif op == '-':
                    return num1 - num2 
                elif op == '*':
                    return num1 * num2 
                elif op == '/':
                    if num2 == 0:
                        return "Cannot divide by zero"
                    else:
                        return num1 / num2
    return None


def Chatbot():
    print("Welcome, Please Enter \"bye\" to exit")
    username =input("I am a Mathematical Chatbot! What's your name? \n> ")
    print(f"How can I help you today, {username} ?")

    general_responses = {
        "hi" : f"Hi, How can I help you, {username}?",
        "hello": f"Hello, How can I help you, {username}?",
        "bye": f"Have a nice day, {username}",
        "thank you": f"Welcome, {username}"
    }

    while True:
        userInput = input("> ").lower()

        if "bye" in userInput:
            break

        math_result = Handle_mathematical_questions(userInput)
        if math_result is not None:
            if math_result == "Cannot divide by zero":
                print(math_result)
            else:
                print(f"The result is {round(math_result, 10)}")
            continue
        
        if userInput in general_responses:
            print(general_responses[userInput])
        else:
            print("Cannot answer this question, Try another question!")



Chatbot()

