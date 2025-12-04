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
    
    
    
    

    def calculate_cost(self, part, color):
        """Расчитывает стоимость окраски детали"""
        if not part or not color:
            raise ValueError("Деталь и цвет не должны быть пустыми")
        
        part_lower = part.lower().strip()
        color_lower = color.lower().strip()
        
        if part_lower not in self.PART_COEFFICIENTS:
            available = ", ".join(self.PART_COEFFICIENTS.keys())
            raise ValueError(f"Неизвестная деталь: {part}\nДоступные: {available}")
        
        if color_lower not in self.COLOR_COEFFICIENTS:
            available = ", ".join(self.COLOR_COEFFICIENTS.keys())
            raise ValueError(f"Неизвестный цвет: {color}\nДоступные: {available}")
        
        part_coef = self.PART_COEFFICIENTS[part_lower]
        color_coef = self.COLOR_COEFFICIENTS[color_lower]
        
        cost = self.BASE_COST * part_coef * color_coef
        return cost
    
    def get_available_parts(self):
        """Возвращает список доступных деталей"""
        return list(self.PART_COEFFICIENTS.keys())
    
    def get_available_colors(self):
        """Возвращает список доступных цветов"""
        return list(self.COLOR_COEFFICIENTS.keys())
