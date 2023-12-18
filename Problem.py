# Put the following 2 lines in the client file, make sure "Problem.py"
# and "questions.txt" are in the current working directory

# import Problem
# problem_list = Problem.fill_array()

# Here is an example of a for loop, printing the entire list
# for obj in problem_list:
# print(obj.question, obj.ans1, obj.ans2, obj.ans3, obj.ans4)

# Here is an example of one question (the first one) and its answers, individually returned
# print(problem_list[0].question)
# print(problem_list[0].ans1)
# print(problem_list[0].ans2)
# print(problem_list[0].ans3)
# print(problem_list[0].ans4)

######################################################################


def fill_correct_answers():
    file = open('answers.txt', 'r')  # opening the 'answers.txt' file for reading
    read = file.readlines()
    answer_list = []

    for line in read:
        answer_list.append(Answer(line.strip()))

    return answer_list


def fill_explanations():
    file = open('explanations.txt', 'r')  # opening the 'answers.txt' file for reading
    read = file.readlines()
    explanation_list = []

    for line in read:
        explanation_list.append(Explanation(line.strip()))

    return explanation_list


def fill_problems():
    file = open('questions.txt', 'r')  # opening the file 'questions.txt' for reading, hence the 'r'
    read = file.readlines()
    modified = []
    problem_list = []

    for line in read:
        modified.append(line.strip())

    array_length = len(modified)
    for i in range(0, array_length, 5):
        question = modified[i]
        ans1 = modified[i + 1]
        ans2 = modified[i + 2]
        ans3 = modified[i + 3]
        ans4 = modified[i + 4]
        problem_list.append(Prob(question, ans1, ans2, ans3, ans4))

    return problem_list


class Prob(object):
    def __init__(self, question, ans1, ans2, ans3, ans4):
        self.question = question
        self.ans1 = ans1
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4

    def get_question(self):
        return self.question

    def get_ans1(self):
        return self.ans1

    def get_ans2(self):
        return self.ans2

    def get_ans3(self):
        return self.ans3

    def get_ans4(self):
        return self.ans4

    # Below is the code to print the entire list, for testing purposes
    # for obj n problem_list:
    #    print(obj.question, obj.ans1, obj.ans2, obj.ans3, obj.ans4)
################################################################################

# Below is the score class


def radio(radio_button_icon, rb_icon_var, correct_answer):
    if rb_icon_var.get() == int(correct_answer):
        radio_button_icon.configure(text="you selected: {}, Correct!!!".format(rb_icon_var.get()))
        return bool(True)
    elif rb_icon_var.get() != int(correct_answer):
        radio_button_icon.configure(text="you selected: {}, incorrect.".format(rb_icon_var.get()))
        return bool(False)


class Answer:
    def __init__(self, ans):
        self.answer = ans.strip()

    def check(self):
        return self.answer


class Explanation:
    def __init__(self, exp):
        self.explanation = exp.strip()

    def get_reason(self):
        return self.explanation