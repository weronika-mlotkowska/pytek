# Class performing exam session

class ExamSession(object):
    """docstring for exam session"""

    is_finisehed = False
    answered_questions = []
    loaded_question = None

    def __init__(self, arg):
        self.arg = arg


    def parse_question(self, question=None):
        """
        For now assume that we have already parsed question from the json file
        """

        # ----- MOCK -----
        self.question_id = 0
        self.question_text = "What is good?"
        self.question_type = "multiple"
        self.answers = [["Hot day" , "<correct_ans>", ""],
                        ["Cold night" , "<correct_ans>", ""],
                        ["Cold evening", "<wrong_ans>", ""],
                        ["Warm evening" , "<wrong_ans>", ""]]

        self.loaded_question = {"question_id" : self.question_id,
                                "question_text": self.question_text,
                                "question_type" : self.question_type,
                                "answers": self.answers,
                                "answered_correctly": True}


    def ask_question(self):
        question = self.loaded_question

        if question["question_type"] == "multiple":
            prompt = "Indicate correct answers (type space-separated numbers): "

        # DISPLAY QUESTION
        print(question["question_text"])
        for id, q in enumerate(question["answers"]):
            print(f'{id}: {q[0]}')

        # ASK FOR INDICATING CORRECT ANSWERS
        user_typed = input(prompt)
        #print(f'Answers: {user_typed.split(" ")}')

        # Add user answer to list:
        for id, q in enumerate(question["answers"]):
            if str(id) in user_typed:
                q[2] = "<correct_ans>"
            else:
                q[2] = "<wrong_ans>"

            if  q[1] != q[2]:
                question["answered_correctly"] = False


        print("CORRECT: " + str(question["answered_correctly"]))




if __name__ == "__main__":
    test = ExamSession("duplikat")
    test.parse_question("Parasol")
    test.ask_question()
