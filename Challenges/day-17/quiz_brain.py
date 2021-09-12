class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        u_answer = input(f'Q.{self.question_number}: {current_question.text} (True/False): ')
        self.check_answer(u_answer, current_question.answer)

    def check_answer(self, u_answer, q_answer):
        if u_answer.lower() == q_answer.lower():
            self.score += 1
            print(f'That\'s right, {q_answer} is correct.')
        else:
            print(f'You got it wrong.')
            print(f'The correct answer is {q_answer}')
        print(f'Your current score: {self.score}/{self.question_number}\n')
