import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

from risk_predict import predict_risk


class SmartStudyPlannerGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Smart Study Planner")
        self.root.geometry("1100x700")
        self.root.minsize(900, 600)

        self.student_name = ""
        self.subject_name = ""
        self.exam_date = ""
        self.topics = []

        self.setup_style()
        self.create_layout()
        self.show_dashboard()


    def setup_style(self):
        style = ttk.Style()

        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure(
            "Title.TLabel",
            font=("Segoe UI", 24, "bold")
        )

        style.configure(
            "Subtitle.TLabel",
            font=("Segoe UI", 11)
        )

        style.configure(
            "Card.TFrame",
            relief="solid",
            borderwidth=1
        )

        style.configure(
            "Heading.TLabel",
            font=("Segoe UI", 15, "bold")
        )

        style.configure(
            "Normal.TLabel",
            font=("Segoe UI", 10)
        )

        style.configure(
            "Primary.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=10
        )

        style.configure(
            "Treeview",
            rowheight=32,
            font=("Segoe UI", 10)
        )

        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 10, "bold")
        )


    def create_layout(self):

        self.sidebar = ttk.Frame(self.root, width=220)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        self.main_area = ttk.Frame(self.root)
        self.main_area.pack(
            side="right",
            fill="both",
            expand=True
        )

        title = ttk.Label(
            self.sidebar,
            text="SMART\nSTUDY\nPLANNER",
            font=("Segoe UI", 20, "bold"),
            justify="center"
        )
        title.pack(pady=30)

        self.create_sidebar_button(
            "Dashboard",
            self.show_dashboard
        )

        self.create_sidebar_button(
            "Student",
            self.show_student
        )

        self.create_sidebar_button(
            "Subject",
            self.show_subject
        )

        self.create_sidebar_button(
            "Topics",
            self.show_topics
        )

        self.create_sidebar_button(
            "Priority",
            self.show_priority
        )

        self.create_sidebar_button(
            "Progress",
            self.show_progress
        )

        self.create_sidebar_button(
            "AI Risk",
            self.show_ai_risk
        )

        ttk.Separator(
            self.sidebar,
            orient="horizontal"
        ).pack(fill="x", padx=20, pady=20)

        self.create_sidebar_button(
            "Clear All",
            self.clear_all
        )

    def create_sidebar_button(self, text, command):

        button = ttk.Button(
            self.sidebar,
            text=text,
            command=command
        )

        button.pack(
            fill="x",
            padx=20,
            pady=5
        )


    def clear_page(self):

        for widget in self.main_area.winfo_children():
            widget.destroy()

    def page_title(self, title, subtitle=""):

        ttk.Label(
            self.main_area,
            text=title,
            style="Title.TLabel"
        ).pack(
            anchor="w",
            padx=35,
            pady=(30, 5)
        )

        if subtitle:
            ttk.Label(
                self.main_area,
                text=subtitle,
                style="Subtitle.TLabel"
            ).pack(
                anchor="w",
                padx=35,
                pady=(0, 25)
            )


    def show_dashboard(self):

        self.clear_page()

        self.page_title(
            "Dashboard",
            "Welcome to your Smart Study Planner"
        )

        cards = ttk.Frame(self.main_area)
        cards.pack(
            fill="x",
            padx=35
        )

        self.create_card(
            cards,
            "Student",
            self.student_name if self.student_name else "Not Set",
            0
        )

        self.create_card(
            cards,
            "Subject",
            self.subject_name if self.subject_name else "Not Set",
            1
        )

        self.create_card(
            cards,
            "Topics",
            str(len(self.topics)),
            2
        )

        self.create_card(
            cards,
            "Exam Date",
            self.exam_date if self.exam_date else "Not Set",
            3
        )

        ttk.Label(
            self.main_area,
            text="Quick Actions",
            style="Heading.TLabel"
        ).pack(
            anchor="w",
            padx=35,
            pady=(40, 15)
        )

        actions = ttk.Frame(self.main_area)
        actions.pack(
            fill="x",
            padx=35
        )

        ttk.Button(
            actions,
            text="Add Student Information",
            command=self.show_student
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        ttk.Button(
            actions,
            text="Add Subject",
            command=self.show_subject
        ).grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Button(
            actions,
            text="Manage Topics",
            command=self.show_topics
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=5
        )

        ttk.Button(
            actions,
            text="View Priority",
            command=self.show_priority
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

        ttk.Button(
            actions,
            text="Track Progress",
            command=self.show_progress
        ).grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Button(
            actions,
            text="AI Risk Prediction",
            command=self.show_ai_risk
        ).grid(
            row=1,
            column=2,
            padx=5,
            pady=5
        )

    def create_card(self, parent, title, value, column):

        card = ttk.Frame(
            parent,
            style="Card.TFrame",
            padding=20
        )

        card.grid(
            row=0,
            column=column,
            padx=7,
            sticky="nsew"
        )

        parent.columnconfigure(
            column,
            weight=1
        )

        ttk.Label(
            card,
            text=title,
            font=("Segoe UI", 10)
        ).pack()

        ttk.Label(
            card,
            text=value,
            font=("Segoe UI", 15, "bold")
        ).pack(pady=(8, 0))


    def show_student(self):

        self.clear_page()

        self.page_title(
            "Student Information",
            "Enter your personal information"
        )

        frame = ttk.Frame(
            self.main_area,
            padding=35
        )

        frame.pack(
            anchor="nw"
        )

        ttk.Label(
            frame,
            text="Student Name"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=10
        )

        name_entry = ttk.Entry(
            frame,
            width=40
        )

        name_entry.grid(
            row=0,
            column=1,
            padx=20,
            pady=10
        )

        name_entry.insert(
            0,
            self.student_name
        )

        def save_student():

            name = name_entry.get().strip()

            if not name:
                messagebox.showerror(
                    "Invalid Name",
                    "Student name cannot be empty."
                )
                return

            if name.isnumeric():
                messagebox.showerror(
                    "Invalid Name",
                    "Student name cannot contain only numbers."
                )
                return

            self.student_name = name

            messagebox.showinfo(
                "Success",
                "Student information saved successfully."
            )

            self.show_dashboard()

        ttk.Button(
            frame,
            text="Save Student",
            command=save_student
        ).grid(
            row=1,
            column=1,
            sticky="e",
            pady=20
        )


    def show_subject(self):

        self.clear_page()

        self.page_title(
            "Subject Information",
            "Enter your subject and exam date"
        )

        frame = ttk.Frame(
            self.main_area,
            padding=35
        )

        frame.pack(
            anchor="nw"
        )

        ttk.Label(
            frame,
            text="Subject"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=10
        )

        subject_entry = ttk.Entry(
            frame,
            width=40
        )

        subject_entry.grid(
            row=0,
            column=1,
            padx=20,
            pady=10
        )

        subject_entry.insert(
            0,
            self.subject_name
        )

        ttk.Label(
            frame,
            text="Exam Date (DD-MM-YYYY)"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=10
        )

        date_entry = ttk.Entry(
            frame,
            width=40
        )

        date_entry.grid(
            row=1,
            column=1,
            padx=20,
            pady=10
        )

        date_entry.insert(
            0,
            self.exam_date
        )

        def save_subject():

            subject = subject_entry.get().strip()
            date = date_entry.get().strip()

            if not subject:
                messagebox.showerror(
                    "Invalid Subject",
                    "Subject cannot be empty."
                )
                return

            if subject.isnumeric():
                messagebox.showerror(
                    "Invalid Subject",
                    "Subject cannot contain only numbers."
                )
                return

            try:
                exam_date = datetime.strptime(
                    date,
                    "%d-%m-%Y"
                ).date()

            except ValueError:
                messagebox.showerror(
                    "Invalid Date",
                    "Please enter the date in DD-MM-YYYY format."
                )
                return

            today = datetime.now().date()

            if exam_date < today:
                messagebox.showerror(
                    "Invalid Date",
                    "The exam date cannot be in the past."
                )
                return

            self.subject_name = subject
            self.exam_date = date

            days_until_exam = (exam_date - today).days
            success_message = "Subject information saved successfully."

            if days_until_exam > 365:
                success_message += "\n\nYour Exam Is Far Away. Relax!!"
            elif days_until_exam < 60:
                success_message += (
                    "\n\nYou Have Less Than 60 Days Until Your Exam. "
                    "Start Studying!!"
                )

            messagebox.showinfo(
                "Success",
                success_message
            )

            self.show_dashboard()

        ttk.Button(
            frame,
            text="Save Subject",
            command=save_subject
        ).grid(
            row=2,
            column=1,
            sticky="e",
            pady=20
        )


    def show_topics(self):

        self.clear_page()

        self.page_title(
            "Topics",
            "Add and manage your study topics"
        )

        input_frame = ttk.LabelFrame(
            self.main_area,
            text="Add or Edit Topic",
            padding=20
        )

        input_frame.pack(
            fill="x",
            padx=35,
            pady=10
        )

        ttk.Label(
            input_frame,
            text="Topic Name"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        topic_entry = ttk.Entry(
            input_frame,
            width=22
        )

        topic_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            input_frame,
            text="Hours"
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=5
        )

        hours_entry = ttk.Entry(
            input_frame,
            width=10
        )

        hours_entry.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )

        ttk.Label(
            input_frame,
            text="Difficulty"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

        difficulty_box = ttk.Combobox(
            input_frame,
            values=[1, 2, 3, 4, 5],
            width=7,
            state="readonly"
        )

        difficulty_box.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        difficulty_box.set(3)

        ttk.Label(
            input_frame,
            text="Confidence"
        ).grid(
            row=1,
            column=2,
            padx=5,
            pady=5
        )

        confidence_box = ttk.Combobox(
            input_frame,
            values=[1, 2, 3, 4, 5],
            width=7,
            state="readonly"
        )

        confidence_box.grid(
            row=1,
            column=3,
            padx=5,
            pady=5
        )

        confidence_box.set(3)

        tree_frame = ttk.Frame(
            self.main_area
        )

        tree_frame.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=20
        )

        columns = (
            "Topic",
            "Hours",
            "Difficulty",
            "Confidence"
        )

        tree = ttk.Treeview(
            tree_frame,
            columns=columns,
            show="headings"
        )

        for column in columns:

            tree.heading(
                column,
                text=column
            )

        tree.column(
            "Topic",
            width=250
        )

        tree.column(
            "Hours",
            width=100,
            anchor="center"
        )

        tree.column(
            "Difficulty",
            width=120,
            anchor="center"
        )

        tree.column(
            "Confidence",
            width=120,
            anchor="center"
        )

        tree.pack(
            fill="both",
            expand=True
        )

        editing_topic = None

        def refresh_tree():

            for item in tree.get_children():
                tree.delete(item)

            for topic in self.topics:

                tree.insert(
                    "",
                    "end",
                    values=(
                        topic["name"],
                        topic["hours"],
                        topic["difficulty"],
                        topic["confidence"]
                    )
                )

        def add_topic():

            nonlocal editing_topic

            name = topic_entry.get().strip()

            if not name:
                messagebox.showerror(
                    "Invalid Topic",
                    "Topic name cannot be empty."
                )
                return

            if name.isnumeric():
                messagebox.showerror(
                    "Invalid Topic",
                    "Topic name cannot contain only numbers."
                )
                return

            for topic in self.topics:

                if (
                    topic is not editing_topic
                    and topic["name"].upper() == name.upper()
                ):

                    messagebox.showerror(
                        "Duplicate Topic",
                        "This topic already exists."
                    )

                    return

            try:
                hours = float(
                    hours_entry.get()
                )

            except ValueError:

                messagebox.showerror(
                    "Invalid Hours",
                    "Please enter a valid number."
                )

                return

            if hours <= 0 or hours > 10:

                messagebox.showerror(
                    "Invalid Hours",
                    "Hours must be greater than 0 and no more than 10."
                )

                return

            difficulty = int(
                difficulty_box.get()
            )

            confidence = int(
                confidence_box.get()
            )

            if editing_topic is None:
                self.topics.append(
                    {
                        "name": name.upper(),
                        "hours": hours,
                        "difficulty": difficulty,
                        "confidence": confidence,
                        "studied": 0
                    }
                )
            else:
                editing_topic.update(
                    {
                        "name": name.upper(),
                        "hours": hours,
                        "difficulty": difficulty,
                        "confidence": confidence,
                        "studied": min(editing_topic["studied"], hours)
                    }
                )
                editing_topic = None
                add_button.config(text="Add Topic")

            topic_entry.delete(
                0,
                tk.END
            )

            hours_entry.delete(
                0,
                tk.END
            )

            refresh_tree()

        def edit_topic():

            nonlocal editing_topic

            selected = tree.selection()

            if not selected:
                messagebox.showwarning(
                    "No Selection",
                    "Please select a topic first."
                )
                return

            topic_name = tree.item(selected[0])["values"][0]
            editing_topic = next(
                topic
                for topic in self.topics
                if topic["name"] == topic_name
            )

            topic_entry.delete(0, tk.END)
            topic_entry.insert(0, editing_topic["name"])
            hours_entry.delete(0, tk.END)
            hours_entry.insert(0, str(editing_topic["hours"]))
            difficulty_box.set(editing_topic["difficulty"])
            confidence_box.set(editing_topic["confidence"])
            add_button.config(text="Save Changes")

        def delete_topic():

            nonlocal editing_topic

            selected = tree.selection()

            if not selected:

                messagebox.showwarning(
                    "No Selection",
                    "Please select a topic first."
                )

                return

            item = tree.item(
                selected[0]
            )

            topic_name = item["values"][0]

            self.topics = [
                topic
                for topic in self.topics
                if topic["name"] != topic_name
            ]

            if (
                editing_topic is not None
                and editing_topic["name"] == topic_name
            ):
                editing_topic = None
                add_button.config(text="Add Topic")

                topic_entry.delete(0, tk.END)
                hours_entry.delete(0, tk.END)
                difficulty_box.set(3)
                confidence_box.set(3)

            refresh_tree()

        button_frame = ttk.Frame(
            self.main_area
        )

        button_frame.pack(
            fill="x",
            padx=35,
            pady=(0, 20)
        )

        add_button = ttk.Button(
            button_frame,
            text="Add Topic",
            command=add_topic
        )
        add_button.pack(
            side="left",
            padx=5
        )

        ttk.Button(
            button_frame,
            text="Edit Selected",
            command=edit_topic
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            button_frame,
            text="Delete Selected",
            command=delete_topic
        ).pack(
            side="left",
            padx=5
        )

        refresh_tree()


    def calculate_priority(self):

        ranked_topics = []

        for topic in self.topics:

            hours = topic["hours"]
            difficulty = topic["difficulty"]
            confidence = topic["confidence"]

            hours_score = min(
                hours / 10,
                1
            ) * 100

            difficulty_score = (
                difficulty / 5
            ) * 100

            weakness_score = (
                (6 - confidence) / 5
            ) * 100

            score = (
                hours_score * 0.4
                + difficulty_score * 0.3
                + weakness_score * 0.3
            )

            ranked_topics.append(
                (
                    topic["name"],
                    score
                )
            )

        ranked_topics.sort(
            key=lambda item: item[1],
            reverse=True
        )

        return ranked_topics

    def show_priority(self):

        self.clear_page()

        self.page_title(
            "Study Priority",
            "Topics ranked by your study requirements"
        )

        if not self.topics:

            ttk.Label(
                self.main_area,
                text="No topics available. Add topics first.",
                font=("Segoe UI", 12)
            ).pack(
                pady=50
            )

            return

        ranked_topics = self.calculate_priority()

        tree = ttk.Treeview(
            self.main_area,
            columns=(
                "Rank",
                "Topic",
                "Score"
            ),
            show="headings"
        )

        tree.heading(
            "Rank",
            text="Rank"
        )

        tree.heading(
            "Topic",
            text="Topic"
        )

        tree.heading(
            "Score",
            text="Priority Score"
        )

        tree.column(
            "Rank",
            width=100,
            anchor="center"
        )

        tree.column(
            "Topic",
            width=350
        )

        tree.column(
            "Score",
            width=200,
            anchor="center"
        )

        tree.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=20
        )

        for index, (name, score) in enumerate(
            ranked_topics,
            1
        ):

            tree.insert(
                "",
                "end",
                values=(
                    index,
                    name,
                    f"{score:.2f}%"
                )
            )

        ttk.Label(
            self.main_area,
            text="Higher score = higher study priority",
            font=("Segoe UI", 10)
        ).pack(
            pady=(0, 20)
        )


    def show_progress(self):

        self.clear_page()

        self.page_title(
            "Study Progress",
            "Track how much of each topic you have completed"
        )

        if not self.topics:

            ttk.Label(
                self.main_area,
                text="No topics available. Add topics first.",
                font=("Segoe UI", 12)
            ).pack(
                pady=50
            )

            return

        container = ttk.Frame(
            self.main_area
        )

        container.pack(
            fill="both",
            expand=True,
            padx=35
        )

        for index, topic in enumerate(self.topics):

            frame = ttk.LabelFrame(
                container,
                text=topic["name"],
                padding=15
            )

            frame.pack(
                fill="x",
                pady=8
            )

            progress = min(
                topic["studied"] / topic["hours"],
                1
            ) * 100

            ttk.Label(
                frame,
                text=f"Completed: {progress:.2f}%"
            ).pack(
                anchor="w"
            )

            bar = ttk.Progressbar(
                frame,
                maximum=100,
                value=progress
            )

            bar.pack(
                fill="x",
                pady=10
            )

            ttk.Label(
                frame,
                text=(
                    f"Studied: {topic['studied']} hours / "
                    f"{topic['hours']} hours"
                )
            ).pack(
                anchor="w"
            )

            ttk.Button(
                frame,
                text="Update Progress",
                command=lambda t=topic: self.update_progress(t)
            ).pack(
                anchor="e",
                pady=(10, 0)
            )

    def update_progress(self, topic):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            f"Progress - {topic['name']}"
        )

        window.geometry(
            "400x220"
        )

        ttk.Label(
            window,
            text=topic["name"],
            font=("Segoe UI", 16, "bold")
        ).pack(
            pady=20
        )

        ttk.Label(
            window,
            text="Total hours studied:"
        ).pack()

        entry = ttk.Entry(
            window,
            width=25
        )

        entry.pack(
            pady=10
        )

        entry.insert(
            0,
            str(topic["studied"])
        )

        def save_progress():

            try:
                hours = float(
                    entry.get()
                )

            except ValueError:

                messagebox.showerror(
                    "Invalid Input",
                    "Please enter a valid number.",
                    parent=window
                )

                return

            if hours < 0:

                messagebox.showerror(
                    "Invalid Hours",
                    "Hours cannot be negative.",
                    parent=window
                )

                return

            topic["studied"] = min(
                hours,
                topic["hours"]
            )

            window.destroy()

            self.show_progress()

        ttk.Button(
            window,
            text="Save Progress",
            command=save_progress
        ).pack(
            pady=10
        )


    def show_ai_risk(self):

        self.clear_page()

        self.page_title(
            "AI Study Risk",
            "Use the trained Decision Tree model to predict study risk"
        )

        if not self.topics:

            ttk.Label(
                self.main_area,
                text="No topics available. Add topics first.",
                font=("Segoe UI", 12)
            ).pack(
                pady=50
            )

            return

        frame = ttk.Frame(
            self.main_area,
            padding=35
        )

        frame.pack(
            anchor="nw"
        )

        ttk.Label(
            frame,
            text="Select Topic"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        topic_names = [
            topic["name"]
            for topic in self.topics
        ]

        topic_box = ttk.Combobox(
            frame,
            values=topic_names,
            width=35,
            state="readonly"
        )

        topic_box.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        topic_box.current(0)

        result_frame = ttk.LabelFrame(
            self.main_area,
            text="AI Prediction",
            padding=25
        )

        result_frame.pack(
            fill="x",
            padx=35,
            pady=25
        )

        result_label = ttk.Label(
            result_frame,
            text="No prediction yet.",
            font=("Segoe UI", 16, "bold")
        )

        result_label.pack(
            pady=10
        )

        recommendation_label = ttk.Label(
            result_frame,
            text="",
            font=("Segoe UI", 11)
        )

        recommendation_label.pack(
            pady=10
        )

        def predict():

            selected_name = topic_box.get()

            selected_topic = None

            for topic in self.topics:

                if topic["name"] == selected_name:

                    selected_topic = topic
                    break

            if selected_topic is None:
                return

            progress = min(
                selected_topic["studied"]
                / selected_topic["hours"],
                1
            ) * 100

            prediction = predict_risk(
                selected_topic["difficulty"],
                selected_topic["confidence"],
                selected_topic["hours"],
                progress
            )

            result_label.config(
                text=f"AI Risk Prediction: {prediction}"
            )

            if prediction == "High":

                recommendation_label.config(
                    text=(
                        "Recommendation: Give this topic "
                        "extra attention."
                    )
                )

            elif prediction == "Medium":

                recommendation_label.config(
                    text=(
                        "Recommendation: Keep practicing "
                        "this topic regularly."
                    )
                )

            else:

                recommendation_label.config(
                    text=(
                        "Recommendation: This topic currently "
                        "has low study risk."
                    )
                )

        ttk.Button(
            frame,
            text="Predict Study Risk",
            command=predict
        ).grid(
            row=1,
            column=1,
            sticky="e",
            pady=20
        )


    def clear_all(self):

        answer = messagebox.askyesno(
            "Clear All Data",
            "Are you sure you want to delete all study planner data?"
        )

        if answer:

            self.student_name = ""
            self.subject_name = ""
            self.exam_date = ""
            self.topics = []

            messagebox.showinfo(
                "Data Cleared",
                "All data has been cleared."
            )

            self.show_dashboard()



if __name__ == "__main__":

    root = tk.Tk()

    app = SmartStudyPlannerGUI(root)

    root.mainloop()