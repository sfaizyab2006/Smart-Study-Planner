class Student:
    def __init__(self, name):
        self.name = name

    def get_student_info(self):
        while True:
            self.name = input("\033[1;36mEnter your name: \033[0m")
            if self.name == "":
                print(
                    "\033[1;31mThe Name Cannot Be Empty. "
                    "Please Enter a Valid Name.\033[0m"
                )
            elif self.name.isnumeric():
                print(
                    "\033[1;31mThe Name Cannot Be A Number. "
                    "Please Enter A Valid Name.\033[0m"
                )
            else:
                print(
                    f"\033[1;32mHello {self.name}! "
                    "Welcome to the Smart Study Planner!!\033[0m"
                )
                break