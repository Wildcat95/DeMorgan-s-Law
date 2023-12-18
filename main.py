import tkinter as tk
from tkinter import messagebox
import Problem

#  This is the GUI portion, this file acts as the main file.  Its only job is
#  to make a page that calls a new instance of itself "num_pages" amount of times, one new time
#  for each question.  The Problem.py file has 3 classes, one for the
#  question and (correlating answers), an answer class (an int representing the correct answer,
#  and an explanation class

#  All the contents are pulled from text files "questions.txt", "answers.txt", and explanations.txt

#  problem_list is a list of a question, followed by 4 possible answers
problem_list = Problem.fill_problems()

#  correct_answer is a list of 1-4 (inclusively), representing the correct answer
correct_answer = Problem.fill_correct_answers()

#   an array of explanations from explanations.txt
explanation_list = Problem.fill_explanations()

#  num_pages is the number of pages and questions per page, it is
#  only 49 because our problems_list index starts at 0
num_pages = 5
#  num_questions = 1   # number of times that 4 buttons get printed to screen
# Keep num_questions at 1 for now

# Below are some color and font size variables
color_one = 'DarkSlateGray1'
color_two = 'DarkSlateGray2'
color_three = 'DarkSlateGray3'

font_small = 12
font_med = 15
font_big = 24
font_huge = 50


# Create the main tkinter window
root = tk.Tk()
# Defining the size of the window

root.minsize(1000, 500)
#  root.geometry("1000x600"), this was commented out and replaced by root.minsize above

# Defining the bg (background color)
root.configure(bg=color_two)
# Defining the title
root.title("DeMorgans_Questions")

score = 0


def score_check(score_label, rb_icon_var, the_answer, score_before, page_num):
    global score
    #  Problem.radio will compare the passed values, and return true or false
    if Problem.radio(score_label, rb_icon_var, the_answer):
        #  Only increment score if it hasn't already been incremented on this page
        if score == score_before:
            score += 1
            #  This checks if it is time to go to the last page
            #  NOTE: page_num starts at index 0, that's why it is incremented
            if page_num + 1 == num_pages:
                last_page(page_num + 1, score)
                # if not then go to next question
            else:
                create_page(page_num + 1)
    else:
        show_explanation(page_num)
        #  This checks if it is time to go to the last page
        #  NOTE: page_num starts at index 0, that's why it is incremented
        if page_num + 1 == num_pages:
            last_page(page_num + 1, score)
        # if not then go to next question
        else:
            create_page(page_num + 1)


def show_explanation(page_num):
    messagebox.showinfo("Message", explanation_list[page_num].get_reason())


# Define the function to create each page
# this is the gui
def create_page(page_num):
    global score
    # Clear the previous page
    for widget in root.winfo_children():
        widget.destroy()

    # #  print the correct answer, THIS IS FOR TESTING!!!!!
    # correct_label = tk.Label(root, text="Correct answer is {}".format(correct_answer[page_num].check()), bg=color_two)
    # correct_label.pack(side="top")

    #  print the score
    score_label = tk.Label(root, font=('Arial', font_small), text="Score is: {} out of {}".format(score, page_num), bg=color_two)
    score_label.pack(side="top", pady=(0, 20))

    #  print the QUESTION NUMBER
    page_number_label = tk.Label(root, font=font_med, text="Question {}".format(page_num + 1), bg=color_two)
    page_number_label.pack(side="top", pady=(10, 0))

    #  question_label prints the QUESTION to the top of the page
    question_label = tk.Label(root, wraplength=800, font=('Arial', font_med), text=problem_list[page_num].get_question(), bg=color_two)
    question_label.pack(padx=100,  anchor="w", side="top", pady=(20, 10))

##############################################################################

    #  storing the score before any clicks for the page, to prevent multiple increments
    score_before_click = score

    # Creating the radio buttons for the page

    rb_icon_var = tk.IntVar()

    option1 = tk.Radiobutton(root, bg=color_two, wraplength=500,  font=('Arial', font_small), text=problem_list[page_num].get_ans1(), variable=rb_icon_var, value=1)
    option1.pack(padx=(250, 0), pady=(50, 0), anchor="w", side='top')

    option2 = tk.Radiobutton(root, bg=color_two, wraplength=500, font=('Arial', font_small), text=problem_list[page_num].get_ans2(), variable=rb_icon_var, value=2)
    option2.pack(padx=(250, 0), anchor="w", side='top')

    option3 = tk.Radiobutton(root, bg=color_two, wraplength=500, font=('Arial', font_small), text=problem_list[page_num].get_ans3(), variable=rb_icon_var, value=3)
    option3.pack(padx=(250, 0), anchor="w", side='top')

    option4 = tk.Radiobutton(root, bg=color_two, wraplength=500, font=('Arial', font_small), text=problem_list[page_num].get_ans4(), variable=rb_icon_var, value=4)
    option4.pack(padx=(250, 0), pady=(0, 50), anchor="w", side='top')

    # if rb_icon_var.get() == correct_answer[page_num].check():
    #    score1 += 1

    #  Create the "Exit" button
    exit_button = tk.Button(root, text="Exit", command=root.quit, bg='red', font=font_big)
    exit_button.pack(side="left", fill="x", ipady=50, expand=1)

    #  Create the "Next" button
    next_button = tk.Button(root, text="Next", command=lambda: score_check(score_label, rb_icon_var, correct_answer[page_num].check(), score_before_click, page_num) , bg='green2', font=font_big)
    next_button.pack(side="right", fill="x", ipady=50, expand=1)

    # Disable the "Next" button on the last page
    #  if page_num == num_pages:
    #      next_button.configure(text="Next", command=lambda: last_page(page_num, score1), bg='green2', font=font_big)

    #   next_button.config(state="disabled")


#  The gui of the last page
def last_page(page_num, number_of_correct_answers):
    # Clear the previous page
    for widget in root.winfo_children():
        widget.destroy()

    #  This is the math to get a percentage of correct answers
    percentage = round((number_of_correct_answers/page_num) * 100, 2)

    #  The title of the page
    header_label = tk.Label(root, text="Quiz Finished!", font=font_big,  bg=color_two)
    header_label.pack(side="top", pady=50)

    #  The specific details
    info_label = tk.Label(root, text="You got {} out of {} correct".format(number_of_correct_answers, page_num), bg=color_two)
    info_label.pack(side="top",)

    #  The percentage
    percentage_label = tk.Label(root, text="{}%".format(percentage), font=font_big, bg=color_two)
    percentage_label.pack(side="top", pady=50)

    #  reset the score to 0
    global score
    score = 0

    #  Create the "Exit" button
    exit_button = tk.Button(root, text="Exit", command=root.quit, bg='red', font=font_huge)
    exit_button.pack(side="left", fill="x", ipady=50, expand=1)

    #  Create "Try Again" button
    try_again_button = tk.Button(root, text="Try Again", command=lambda: create_page(0), bg='green2', font=font_big)
    try_again_button.pack(side="left", fill="x", ipady=50, expand=1)


# Start at the first page
create_page(0)

# Run the tkinter event loop
root.mainloop()