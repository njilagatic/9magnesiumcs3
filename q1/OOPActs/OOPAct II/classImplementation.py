class WorkoutSession:
    def __init__(self, exercise_type: str, duration_minutes: int, calories_burned: float = 0.0, is_completed: bool = False):
        self.exercise_type = exercise_type
        self.duration_minutes = duration_minutes
        self.__calories_burned = calories_burned  # Private attribute
        self.__is_completed = is_completed        # Private attribute

    def start_session(self):
        print(f"Started {self.exercise_type} session for {self.duration_minutes} minutes.")

    def log_calories(self, amount: float):
        if amount > 0:
            self.__calories_burned += amount
            print(f"Logged {amount} kcal. Total burned: {self.__calories_burned} kcal.")
        else:
            print("Invalid calorie amount.")

    def complete_session(self):
        self.__is_completed = True
        print(f"Session '{self.exercise_type}' marked as completed.")

    def get_calories_burned(self) -> float:
        return self.__calories_burned

    def is_completed(self) -> bool:
        return self.__is_completed

    def display_info(self):
        print(f"Type: {self.exercise_type} | Duration: {self.duration_minutes} min | "
              f"Calories Burned: {self.__calories_burned} kcal | Completed: {self.__is_completed}")


if __name__ == "__main__":
    print("--- BEFORE ---")
    session1 = WorkoutSession("Morning Run", 30, 0.0, False)
    session2 = WorkoutSession("Evening Cycling", 45, 0.0, False)

    print("Object 1 (session1):")
    session1.display_info()
    print("Object 2 (session2):")
    session2.display_info()

    print("\n--- PERFORMING ACTION ON OBJECT 1 ---")
    session1.log_calories(250.5)
    session1.complete_session()

    print("\n--- AFTER ---")
    print("Object 1 (session1):")
    session1.display_info()
    print("Object 2 (session2):")
    session2.display_info()