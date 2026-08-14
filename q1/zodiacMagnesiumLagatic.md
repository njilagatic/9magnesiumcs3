# Chinese Zodiac Locator

## Requirements
a. Ask the user to enter a year of birth.  The baseline year 1900.
b. Validate user input that it should not be earlier than 1900.
c. If the user enters an invalid year then display an appropriate message then stop or abort the program.
d. Otherwise determine the chinese zodiac sign based on the following starting from 1900.  Note: A zodiac sign will recur after each 12 years.
e. CONSIDER only the year of birth.

---

## Python Source Code ('zodiacMagnesiumLagatic.py')

zodiac_signs = [
    "Rat (鼠 / Shǔ)",
    "Ox (牛 / Niú)",
    "Tiger (虎 / Hǔ)",
    "Rabbit (兔 / Tù)",
    "Dragon (龙 / Lóng)",
    "Snake (蛇 / Shé)",
    "Horse (马 / Mǎ)",
    "Goat (羊 / Yáng)",
    "Monkey (猴 / Hóu)",
    "Rooster (鸡 / Jī)",
    "Dog (狗 / Gǒu)",
    "Pig (猪 / Zhū)"
]

base = 1900

birth_year = int(input("Enter your birth year: "))

if birth_year < base:
    print("Invalid Year, it should not be earlier than 1900")
else:
    c = (birth_year - base) % 12
    print(f"Your Chinese Zodiac Sign is: {zodiac_signs[c]}")

---

## Screenshots

![Zodiac Program Output_1](<Screenshot 2026-08-13 231119.png>)
![Zodiac Program Output_2](<Screenshot 2026-08-13 230949.png>)