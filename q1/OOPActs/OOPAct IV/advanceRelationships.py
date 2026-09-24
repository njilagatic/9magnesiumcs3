class MealLog:
    def __init__(self, mealName: str, calories: float, protein_g: float):
        self.__mealName = mealName
        self.__calories = calories
        self.__protein_g = protein_g

    def get_meal_name(self) -> str:
        return self.__mealName

    def display_meal(self):
        print(f"    - Meal: {self.__mealName} | Calories: {self.__calories} kcal | Protein: {self.__protein_g}g")


class CalorieCalculator:
    def calculate_burn(self, duration_min: int, pace_min_km: float) -> float:
        return duration_min * (30.0 / pace_min_km)


class WorkoutSession:
    def __init__(self, exercise_type: str, duration_minutes: int, calories_burned: float = 0.0, is_completed: bool = False):
        self.exercise_type = exercise_type
        self.duration_minutes = duration_minutes
        self._calories_burned = calories_burned
        self._is_completed = is_completed
        self.meals = []

    def log_calories(self, amount: float):
        if amount > 0:
            self._calories_burned += amount

    def complete_session(self):
        self._is_completed = True

    def add_meal_log(self, meal: MealLog):
        self.meals.append(meal)
        print(f"Associated '{meal.get_meal_name()}' with {self.exercise_type} session.")

    def display_session_summary(self):
        status = "Completed" if self._is_completed else "Incomplete"
        print(f"\n[{self.exercise_type}] Duration: {self.duration_minutes} min | Burned: {self._calories_burned:.1f} kcal | Status: {status}")
        print(f"Associated Meals ({len(self.meals)}):")
        if not self.meals:
            print("    No meals logged for this session.")
        else:
            for meal in self.meals:
                meal.display_meal()


class Cardio(WorkoutSession):
    def __init__(self, exercise_type: str, duration_minutes: int, distance_km: float, pace_min_km: float, calories_burned: float = 0.0, is_completed: bool = False):
        super().__init__(exercise_type, duration_minutes, calories_burned, is_completed)
        self.distance_km = distance_km
        self.pace_min_km = pace_min_km

    def auto_calculate_calories(self, calculator: CalorieCalculator):
        estimated = calculator.calculate_burn(self.duration_minutes, self.pace_min_km)
        self._calories_burned = estimated
        print(f"Calculated calorie burn using external calculator: {estimated:.1f} kcal")

    def display_session_summary(self):
        super().display_session_summary()
        print(f"  [Cardio Details] Distance: {self.distance_km} km | Pace: {self.pace_min_km} min/km")


if __name__ == "__main__":
    print("=== TEST 1: INHERITANCE & DEPENDENCY ===")
    cardio = Cardio("Outdoor Running", 45, 8.0, 5.5)
    calc = CalorieCalculator()

    print(f"Created Cardio instance: {cardio.exercise_type}")
    cardio.auto_calculate_calories(calc)
    cardio.complete_session()

    print("\n=== TEST 2: AGGREGATION ===")
    meal1 = MealLog("Pre-Workout Banana", 105.0, 1.3)
    meal2 = MealLog("Post-Workout Protein Shake", 280.0, 30.0)

    cardio.add_meal_log(meal1)
    cardio.add_meal_log(meal2)

    print("\n=== FINAL SYSTEM OUTPUT ===")
    cardio.display_session_summary()