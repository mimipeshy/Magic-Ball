import random
import time

responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes-definitely",
             "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes",
             "Signs point to yes", "Reply is hazy", "Ask again later", "Better not tell you now",
             "Cannot predict now", "Concentrate and ask again", "Don't count on it",
             " My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]


def randomization():
    rand_value = random.choice(responses)
    return rand_value


def blank_question():
    response = "Please ask me a question"
    return response


def question():
    response = "Am a genius, ask me anything:"
    return response


def try_again():
    response = "Would you like to ask the Wise One another question? Y/N:"
    return response


def main():
    while True:

        """user can input their question"""
        question = input("Am a genius, ask me anything:")
        if question == '':
            response = blank_question()
            print(response)
        else:
            print("Thinking....")
            time.sleep(2)

            """generate a random response"""
            random_response = randomization()
            print(random_response)

            """prompt user to ask question"""
            user_input = input("Would you like to ask the Wise One another question? Y/N: ")
            if user_input[0].lower() == "n":
                break
    print("Goodbye!!!!It was fun having you")


if __name__ == "__main__":
    print("Welcome to Magic 8 ball")
    main()
