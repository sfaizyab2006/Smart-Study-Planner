import string
from risk_predict import predict_risk


class Topic:
    def __init__(self, topic=None, hours=0, difficulity="", confidence=""):
        self.topic_name = topic if topic is not None else []
        self.hours = hours
        self.difficulity = difficulity
        self.confidence = confidence
        self.topics = []

    def get_topic_info(self):
        topics = []
        while True:
            try:
                num_topics = int(input("\033[1;36mEnter the number of topics: \033[0m"))
            except ValueError:
                print("\033[1;31mPlease enter a valid number.\033[0m")
                continue

            if num_topics <= 0:
                print(
                    "\033[1;31mThe Number of Topics Cannot Be Negative Or "
                    "Zero. Please Enter a Valid Number.\033[0m"
                )
                continue
            break

        for _ in range(num_topics):
            while True:
                topic_name = input("\033[1;36mEnter the topic name: \033[0m")
                if topic_name == "":
                    print(
                        "\033[1;31mThe Topic Name Cannot Be Empty. "
                        "Please Enter a Valid Topic Name.\033[0m"
                    )
                elif topic_name.isnumeric():
                    print(
                        "\033[1;31mThe Topic Name Cannot Be A Number. "
                        "Please Enter a Valid Topic Name.\033[0m"
                    )
                elif topic_name.upper() in [t[0] for t in topics]:
                    print(
                        "\033[1;31mThe Topic Name Already Exists. "
                        "Please Enter a Unique Topic Name.\033[0m"
                    )
                else:
                    break

            while True:
                try:
                    hours = float(
                        input(
                            "\033[1;36mEnter the number of hours you want to "
                            "spend on this topic: \033[0m"
                        )
                    )
                except ValueError:
                    print("\033[1;31mPlease enter a valid number of hours.\033[0m")
                    continue
                if hours <= 0:
                    print(
                        "\033[1;31mThe Number of Hours Cannot Be Negative "
                        "Or Zero. Please Enter a Valid Number.\033[0m"
                    )

                if hours > 10:
                    print(
                        "\033[1;31mThe Number of Hours Cannot Be More "
                        "Than 10. Please Enter a Valid Number.\033[0m"
                    )
                else:
                    break

            while True:
                try:
                    difficulty = int(
                        input(
                            "\033[1;36mEnter the difficulity level of this "
                            "topic (1-5): \033[0m"
                        )
                    )
                except ValueError:
                    print(
                        "\033[1;31mInvalid input. Please enter a number "
                        "between 1 and 5.\033[0m"
                    )
                    continue
                if difficulty > 5 or difficulty < 1:
                    print(
                        "\033[1;31mInvalid input. Please enter a number "
                        "between 1 and 5.\033[0m"
                    )
                else:
                    break

            while True:
                try:
                    confidence = int(
                        input(
                            "\033[1;36mEnter your confidence level in this "
                            "topic (1-5): \033[0m"
                        )
                    )
                except ValueError:
                    print(
                        "\033[1;31mInvalid input. Please enter a number "
                        "between 1 and 5.\033[0m"
                    )
                    continue
                if confidence > 5 or confidence < 1:
                    print(
                        "\033[1;31mInvalid input. Please enter a number "
                        "between 1 and 5.\033[0m"
                    )
                else:
                    break

            topic_name = topic_name.upper()
            topics.append((topic_name, hours, difficulty, confidence))

        self.topics = topics
        self.topic_name = [t[0] for t in topics]
        return topics

    def display_topics(self, topics=None):
        if topics is None:
            topics = self.topics
        print("\033[1;32mHere Are The Topics You Entered:\033[0m")
        for topic in topics:
            print(
                f"\033[1;36mTopic: {topic[0]}, Hours: {topic[1]}, "
                f"Difficulity: {topic[2]}, Confidence: {topic[3]}\033[0m"
            )

    def priority_score(self):
        if not self.topics:
            print("\033[1;31mNo topics available to rank.\033[0m")
            return

        ranked_topics = []
        for topic_name, hours, difficulty, confidence in self.topics:
            hours_score = min(hours / 10, 1) * 100
            difficulty_score = (difficulty / 5) * 100
            weakness_score = ((6 - confidence) / 5) * 100

            score = (
                hours_score * 0.4
                + difficulty_score * 0.3
                + weakness_score * 0.3
            )
            ranked_topics.append((topic_name, score))

        ranked_topics.sort(key=lambda item: item[1], reverse=True)

        print("\033[1;32m***** PRIORITY RECOMMENDATIONS *****\033[0m")

        for i, (name, score) in enumerate(ranked_topics[:3], 1):
            print(f"{i}. {name} - {score:.2f}%")

        print("\033[1;32mI Recommend You Focus On These Topics In This Order!\033[0m")

    def progress(self, hours, topic_name=None):
        if topic_name is None:
            if not self.topics:
                print("\033[1;31mNo topics available to track.\033[0m")
                return
            topic_name = self.topics[0][0]

        for name, total_hours, _, _ in self.topics:
            if name == topic_name.upper():
                progress_bar = min(hours / total_hours, 1) * 100
                print(
                    f"\033[1;32mYour Progress On {name} Is "
                    f"{progress_bar:.2f}%.\033[0m"
                )
                return

        print(f"\033[1;31mTopic '{topic_name}' was not found.\033[0m")

    def remaining_progress(self, hours, topic_name=None):
        if topic_name is None:
            if not self.topics:
                print("\033[1;31mNo topics available to track.\033[0m")
                return
            topic_name = self.topics[0][0]

        for name, total_hours, _, _ in self.topics:
            if name == topic_name.upper():
                progress_percent = min(hours / total_hours, 1) * 100
                remaining = 100 - progress_percent
                print(
                    f"\033[1;32mYou Have {remaining:.2f}% Remaining "
                    f"Progress On {name}.\033[0m"
                )
                return remaining

        print(f"\033[1;31mTopic '{topic_name}' was not found.\033[0m")

    def reamining_progress(self, hours, topic_name=None):
        return self.remaining_progress(hours, topic_name)

    def additional_topic(self, topics=None):
        if topics is None:
            topics = self.topics

        additional_topics = input(
            "\033[1;36mWould you like to add more topics? (yes/no): \033[0m"
        )
        if additional_topics.lower() == "yes":
            new_topics = self.get_topic_info()
            if topics is None:
                topics = []
            topics.extend(new_topics)
            self.topics = topics
            self.topic_name = [t[0] for t in topics]
            self.display_topics(self.topics)
            return self.topics
        return topics

    def change_topic_info(self):
        user_input = input(
            "\033[1;36mWhat would you like to change? (topic "
            "name/hours/difficulty/confidence/delete a topic): \033[0m"
        )
        if user_input.lower() == "topic name":
            old_name = input("\033[1;36mEnter the old topic name: \033[0m")
            new_name = input("\033[1;36mEnter the new topic name: \033[0m")
            for i, (name, hours, difficulty, confidence) in enumerate(self.topics):
                if name.upper() == old_name.upper():
                    self.topics[i] = (new_name.upper(), hours, difficulty, confidence)
                    print(
                        f"\033[1;32mTopic name changed from {old_name} "
                        f"to {new_name}.\033[0m"
                    )
                    return
            print(f"\033[1;31mTopic '{old_name}' was not found.\033[0m")

        elif user_input.lower() == "hours":
            topic_name = input("\033[1;36mEnter the topic name: \033[0m")
            new_hours = float(
                input("\033[1;36mEnter the new number of hours: \033[0m")
            )
            for i, (name, hours, difficulty, confidence) in enumerate(self.topics):
                if name.upper() == topic_name.upper():
                    self.topics[i] = (name, new_hours, difficulty, confidence)
                    print(
                        f"\033[1;32mHours for {topic_name} changed to "
                        f"{new_hours}.\033[0m"
                    )
                    return
            print(f"\033[1;31mTopic '{topic_name}' was not found.\033[0m")

        elif user_input.lower() == "difficulty":
            new_difficulty = int(
                input(
                    "\033[1;36mEnter the new difficulty level (1-5): \033[0m"
                )
            )
            topic_name = input("\033[1;36mEnter the topic name: \033[0m")
            for i, (name, hours, difficulty, confidence) in enumerate(self.topics):
                if name.upper() == topic_name.uppper():
                    self.topic[i] = (name, hours, new_difficulty, confidence)
                    print(
                        f"\033[1;32mDifficulty for {topic_name} changed to "
                        f"{new_difficulty}.\033[0m"
                    )
                    return
            print(f"\033[1;31mTopic '{topic_name}' was not found.\033[0m")
        elif user_input.lower() == "confidence":
            new_confidence = int(
                input("\033[1;36mEnter the new confidence level (1-5): \033[0m")
            )
            topic_name = input("\033[1;36mEnter the topic name: \033[0m")
            for i, (name, hours, difficulty, confidence) in enumerate(self.topics):
                self.topics[i] = (name, hours, difficulty, new_confidence)
                if name.upper() == topic_name.upper():
                    self.topics[i] = (name, hours, difficulty, new_confidence)
                    print(
                        f"\033[1;32mConfidence for {topic_name} changed to "
                        f"{new_confidence}.\033[0m"
                    )
                    return
            print(f"\033[1;31mTopic '{topic_name}' was not found.\033[0m")

        elif user_input.lower() == "delete":
            del_topic = input(
                "\033[1;36mEnter the topic name you want to delete: \033[0m"
            )
            for i, (name, hours, difficulty, confidence) in enumerate(self.topics):
                if name.upper() == del_topic.upper():
                    del self.topics[i]
                    print(f"\033[1;32mTopic '{del_topic}' has been deleted.\033[0m")
                    return

        else:
            print(
                "\033[1;31mInvalid input. Please enter 'topic name', 'hours', "
                "'difficulty', or 'confidence' or 'delete'.\033[0m"
            )

    def display_topic(self):
        print("\033[1;32mHere Are The Topics You Entered:\033[0m")
        for topic_name in self.topics:
            print(f"\033[1;36mTopic: {topic_name}\033[0m")

    def ai_risk(self):
        print(f"AI Prediction System")
        topic_name = input("Enter The Name Of The Topic: ")
        for name, hours, difficulity, confidence in self.topics:
            if name.upper() == topic_name.upper():
                print(f"Found The Topic {name}")

                while True:
                    try:
                        hours_studied = float(
                            input("How Many Hours Have You Studied: ")
                        )

                        if hours_studied <= 0:
                            print("Hours studied cannot be negative or zero.")

                            continue
                        break
                    except ValueError:
                        print("Enter a Valid Number")

                progress_percent = min(hours_studied / hours, 1) * 100

                prediction = predict_risk(
                    difficulity, confidence, hours, progress_percent
                )

                print(f"AI Risk Prediction: {prediction}")

                if prediction == "High":
                    print("Recommendation: You should give this topic extra attention.")

                elif prediction == "Medium":
                    print("Recommendation: Keep practicing this topic regularly.")

                else:
                    print("Recommendation: This topic currently has low study risk.")

                return

        print(f"Topic {topic_name} was not found`")
