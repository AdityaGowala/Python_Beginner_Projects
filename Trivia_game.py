# list of questions
# list of their answers
# randomly pick questions 
# ask the user 
# check the answer
# keep track of there score
# tell user his score

import random 

questions = {
    "What is the capital of France?": "paris",
    "How many continents are there on Earth?": "7",
    "What planet is known as the Red Planet?": "mars",
    "Who developed the theory of relativity?": "albert einstein",
    "Which ocean is the largest in the world?": "pacific ocean",
    "Who was the first President of the United States?": "george washington",
    "In which year did World War II end?": "1945",
    "What gas do plants absorb from the atmosphere?": "carbon dioxide",
    "Who directed the movie 'Titanic'?": "james cameron",
    "Which singer is known as the 'King of Pop'?": "michael jackson"
}


def python_trivia_game():
    question_list = list(questions.keys())
    total_questions = 5
    score = 0


    selected_questions = random.sample(question_list , total_questions)
    for idx , question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("Your answer: ").lower().strip()  # lower converts input into lower case & strip removes spaces from front and back
        correct_answer = questions[question].lower()
        if user_answer == correct_answer:
            print("Correct\n")
            score +=1
        else:
            print(f"Wrong !!. The correct answer is {correct_answer}\n")
    print(f"Game Over! Your final score is {score}/{total_questions}")

python_trivia_game()