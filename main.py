from student import Student
from subject import Subject
from topics import Topic
from risk_predict import predict_risk
import time

stdname = Student("")
stdname.get_student_info()

sub = Subject("", "")
sub.get_exam_name()
sub.get_exam_info()

topic = Topic([], 0, "", "")
topics = topic.get_topic_info()

validation = input(
    "\033[1;36mIs the information you entered correct? (yes/no): \033[0m"
)
if validation.lower() == "no":
    while True:
        try:
            number = int(
                input(
                    "Which information do you want to change? "
                    "(1-Name, 2-Subject, 3-Date, 4-Topics): "
                )
            )
        except ValueError:
            print("\033[1;31mPlease Enter A Valid Number Between 1-4.\033[0m")
            continue

        if number == 1:
            stdname.get_student_info()
            break
        elif number == 2:
            sub.get_exam_name()
            topic.get_topic_info()
            break
        elif number == 3:
            sub.get_exam_info()
            break
        elif number == 4:
            topics = topic.additional_topic(topics)
            user_choice = input(
                "\033[1;36mDo you want to change anything about the topics? "
                "(yes/no): \033[0m"
            )
            if user_choice.lower() == "yes":
                topic.change_topic_info()

            break
        else:
            print("\033[1;31mPlease Enter A Valid Number Between 1-4.\033[0m")
else:
    topic.display_topics()
    priority = input(
        "\033[1;36mDo you want to see the priority of the topics? (yes/no): \033[0m"
    )
    if priority.lower() == "yes":
        topic.priority_score()

progress_check = input(
    "\033[1;36mWould you like to track your progress on the topics you entered? "
    "(yes/no): \033[0m"
)
if progress_check.lower() == "yes":
    for topic_name, _, _, _ in topic.topics:
        try:
            hours = float(
                input(
                    f"\033[1;36mEnter the number of hours you have spent on "
                    f"{topic_name}: \033[0m"
                )
            )
        except ValueError:
            print("\033[1;31mPlease enter a valid number of hours.\033[0m")
            hours = 0

        topic.progress(hours, topic_name)
        topic.reamining_progress(hours, topic_name)

topic.ai_risk()
print(
    "\033[1;32mThank you for using the Smart Study Planner. "
    "Good Luck on your Exam!\033[0m"
)