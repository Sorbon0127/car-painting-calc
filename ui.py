class PaintCalculator:
    """Калькулятор стоимости окраски деталей автомобиля"""
    
    # Коэффициенты по цветам
    COLOR_COEFFICIENTS = {
        "белый": 1.0,
        "синий": 1.0,
        "жёлтый": 1.1,
        "красный": 1.0,
        "перламутровый": 1.2,
        "серый металлик": 1.3
    }
    
    # Коэффициенты по деталям
    PART_COEFFICIENTS = {
        "капот": 1.0,
        "передняя дверь": 1.2,
        "задняя дверь": 1.1,
        "передний бампер": 1.0,
        "задний бампер": 1.0,
        "крыша": 1.1
    }
    
    BASE_COST = 12000  # Базовая стоимость
    
    def __init__(self):
        pass
    
    
    def calculate_cost(self, part, color, discount=0):
        """
        Расчитывает стоимость окраски детали автомобиля

        Args:
            part (str): Название детали
            color (str): Цвет
            discount (float): Скидка в процентах (0-100)

        Returns:
            float: Стоимость окраски в рублях
        """
        if not 0 <= discount <= 100:
            raise ValueError("Ошибка: Скидка должна быть от 0 до 100 процентов")

        part_lower, color_lower = self.validate_input(part, color)

        part_coef = self.PART_COEFFICIENTS[part_lower]
        color_coef = self.COLOR_COEFFICIENTS[color_lower]

        cost = self.BASE_COST * part_coef * color_coef
        cost = cost * (1 - discount / 100)

        return cost
 
    
    

    def get_available_parts(self):
        """Возвращает список доступных деталей"""
        return list(self.PART_COEFFICIENTS.keys())
    
    def get_available_colors(self):
        """Возвращает список доступных цветов"""
        return list(self.COLOR_COEFFICIENTS.keys())
