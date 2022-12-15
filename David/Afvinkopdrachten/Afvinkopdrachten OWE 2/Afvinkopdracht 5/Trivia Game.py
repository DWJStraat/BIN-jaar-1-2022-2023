class Question:
    def __init__(self, question, answer, answer1, answer2, answer3, answer4):
        self.question = question
        self.correctAnswer = answer
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4

    def checkAnswer(self, answer):
        if answer == self.correctAnswer:
            return True
        else:
            return False

    def getQuestion(self):
        return self.question


def main():
    questions = [
        Question('What is the music of life?',1,"Silence, my brother", "The sound of the ocean", "The sound of the rain", "The sound of the wind")
    ]
    score = 0
    for question in questions:
        print(question.question)
        print('-'*len(question.question))
        print(f'1:{question.answer1}')
        print(f'2:{question.answer2}')
        print(f'3:{question.answer3}')
        print(f'4:{question.answer4}')
        answer = int(input('Your answer: '))
        if question.checkAnswer(answer):
            score += 1
            print(f'Correct! Your score is {score}')
        else:
            print(f'Incorrect! Your score is {score}')

main()