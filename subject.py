from datetime import datetime


class Subject:
    def __init__(self, subject, date):
        self.subject = subject
        self.date = date

    def get_exam_name(self):
        while True:
            self.subject = input("\033[1;36mEnter the subject: \033[0m")

            if self.subject == "":
                print(
                    "\033[1;31mThe Subject Cannot Be Empty. "
                    "Please Enter a Valid Subject.\033[0m"
                )
            elif self.subject.isnumeric():
                print(
                    "\033[1;31mThe Subject Cannot Be A Number. "
                    "Please Enter a Valid Subject.\033[0m"
                )
            else:
                break

    def get_exam_info(self):
        while True:
            self.date = input("\033[1;36mEnter the date (DD-MM-YYYY): \033[0m")
            if self.date == "":
                print(
                    "\033[1;31mThe Exam Date Cannot Be Empty. "
                    "Please Enter a Valid Date.\033[0m"
                )
                continue

            try:
                exam_date = datetime.strptime(self.date, "%d-%m-%Y").date()
            except ValueError:
                print(
                    "\033[1;31mThe Exam Date Must Be In DD-MM-YYYY Format. "
                    "Please Enter a Valid Date.\033[0m"
                )
                continue

            today = datetime.now().date()
            if exam_date < today:
                print(
                    "\033[1;31mThe Exam Has Already Passed. "
                    "Please Enter a Valid Date.\033[0m"
                )
                continue

            try:
                exam_date = datetime.strptime(self.date, "%d-%m-%Y").date()
            except ValueError:
                print(
                    "\033[1;31mThe Exam Date Must Be In DD-MM-YYYY Format. "
                    "Please Enter a Valid Date.\033[0m"
                )
                continue

            today = datetime.now().date()
            if exam_date < today:
                print(
                    "\033[1;31mThe Exam Has Already Passed. "
                    "Please Enter a Valid Date.\033[0m"
                )
                continue

            else:
                print(
                    f"\033[1;32mYour Exam For {self.subject} Is On "
                    f"{self.date}. Good Luck!\033[0m"
                )
                break

        remaining_time = exam_date - datetime.now().date()
        if remaining_time.days > 365:
            print("\033[1;31mYour Exam Is Far Away. Relax!!\033[0m")

        if remaining_time.days < 60:
            print(
                "\033[1;31mYou Have Less Than 60 Days Until Your Exam. "
                "Start Studying!!\033[0m"
            )