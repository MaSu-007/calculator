class BMICalculator:
    def __init__(self, height_cm, weight_kg):
        self.height_cm = height_cm / 100
        self.weight = weight_kg

    def calculate_bmi(self):
        if self.height_cm <= 0:
            return None
        bmi = self.weight / (self.height_cm ** 2)
        return round(bmi, 2)

    def interpret_bmi(self, bmi):
        if bmi < 18.5:
            return "გამხდარი"
        elif 18.5 <= bmi < 25:
            return "ნორმა"
        elif 25 <= bmi < 30:
            return "ზედმეტი წონა"
        else:
            return "სიმსუქნე"
