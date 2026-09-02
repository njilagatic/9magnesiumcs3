# SG4 - Understanding Classes and Objects
## Workout Session
## This class represents a single fitness activity logged within a personal health application
## Properties
| Property | Data Type | Description |
|---|---|---|
| ExerciseType | string | Name of physical exercise |
| DurationMinutes | int | Total elapsed duration of the workout session in minutes |
| CaloriesBurned | double | Total energy expenditure in kilocalories |
| Completed | boolean | Indicate whether workout session was completed |
## Methods
| Method | Description |
|---|---|| | |

| start_session() | Starts timer tracking and active workout status |
| log_calories() | Updates total energy expenditure during workout |
| complete session() | Sets workout to completed to true and finalizes session stats |
## Class Diagram
![Class Diagram](images/classDiagram.png)
## Design Explanation
### Why did you choose this class?
I selected because personal fitness tracking software relies heavily on modular data structures to capture individual activities. Designing an exercise session provides a clear mapping between daily physical activity and software objects.
### Which property is the most important? Why?
The `Completed property` is the most important due to it's ability to prevent skewing of overall activity analytics as it prevents incomplete or canceled workouts.
### Which method is the most useful? Why?
The `log_calories(quantity: double)` method is the most essential as physical activity happens over time. It enables to quickly update enabled trackers like smartwatches to append active calorie burns continously throughout the workout.