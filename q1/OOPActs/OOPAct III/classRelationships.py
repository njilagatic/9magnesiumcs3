class MealLog:
    def __init__(self, mealName: str, calories: float, protein_g: float):
        self.mealName = mealName
        self.calories = calories
        self.protein_g = protein_g

    def display_meal(self):
        print(f"    - Meal: {self.mealName} | Calories: {self.calories} kcal | Protein: {self.protein_g}g")


class WorkoutSession:
    def __init__(self, exercise_type: str, duration_minutes: int, calories_burned: float = 0.0, is_completed: bool = False):
        self.exercise_type = exercise_type
        self.duration_minutes = duration_minutes
        self.__calories_burned = calories_burned
        self.__is_completed = is_completed
        self.meals = []  

    def log_calories(self, amount: float):
        if amount > 0:
            self.__calories_burned += amount

    def complete_session(self):
        self.__is_completed = True

    def add_meal_log(self, meal: MealLog):
        self.meals.append(meal)
        print(f"Associated '{meal.mealName}' with {self.exercise_type} session.")

    def display_session_summary(self):
        status = "Completed" if self.__is_completed else "Incomplete"
        print(f"\n[{self.exercise_type}] Duration: {self.duration_minutes} min | Burned: {self.__calories_burned} kcal | Status: {status}")
        print(f"Associated Meals ({len(self.meals)}):")
        if not self.meals:
            print("    No meals logged for this session.")
        else:
            for meal in self.meals:
                meal.display_meal()
                

if __name__ == "__main__":
    print("=== PHASE A: BEFORE RELATIONSHIP ===")
    session = WorkoutSession("Morning Leg Day", 60, 450.0, True)
    meal1 = MealLog("Pre-Workout Banana", 105.0, 1.3)
    meal2 = MealLog("Post-Workout Protein Shake", 280.0, 30.0)
    meal3 = MealLog("Recovery Chicken Rice", 520.0, 45.0)

    session.display_session_summary()

    print("\n=== PHASE B: BUILDING RELATIONSHIP ===")
    session.add_meal_log(meal1)
    session.add_meal_log(meal2)
    session.add_meal_log(meal3)

    print("\n=== PHASE C: AFTER RELATIONSHIP ===")
    session.display_session_summary()