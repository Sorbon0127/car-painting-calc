from paint_calculator import PaintCalculator

class PaintUI:
    """Интерфейс для работы с калькулятором"""
    
    def __init__(self):
        self.calculator = PaintCalculator()
    
    def display_menu(self):
        """Показывает главное меню"""
        print("\n" + "="*50)
        print("КАЛЬКУЛЯТОР СТОИМОСТИ ОКРАСКИ АВТОМОБИЛЯ")
        print("="*50)
        print("1. Рассчитать стоимость")
        print("2. Показать доступные детали")
        print("3. Показать доступные цвета")
        print("4. Выход")
        print("="*50)
    
    def show_parts(self):
        """Показывает доступные детали"""
        parts = self.calculator.get_available_parts()
        print("\nДоступные детали:")
        for i, part in enumerate(parts, 1):
            print(f"  {i}. {part}")
    
    def show_colors(self):
        """Показывает доступные цвета"""
        colors = self.calculator.get_available_colors()
        print("\nДоступные цвета:")
        for i, color in enumerate(colors, 1):
            print(f"  {i}. {color}")
    
    def calculate_and_display(self):
        """Расчитывает и выводит стоимость"""
        try:
            print("\n--- Расчёт стоимости окраски ---")
            
            self.show_parts()
            part = input("\nВведите название детали: ").strip()
            
            self.show_colors()
            color = input("\nВведите цвет: ").strip()
            
            cost = self.calculator.calculate_cost(part, color)
            
            print(f"\n✓ Стоимость окраски {part} в цвет '{color}': {cost:,.2f} руб.")
        
        except ValueError as e:
            print(f"\n✗ Ошибка: {e}")
    
    def run(self):
        """Главный цикл приложения"""
        while True:
            self.display_menu()
            choice = input("Выберите опцию (1-4): ").strip()
            
            if choice == "1":
                self.calculate_and_display()
            elif choice == "2":
                self.show_parts()
            elif choice == "3":
                self.show_colors()
            elif choice == "4":
                print("\nДо свидания!")
                break
            else:
                print("\n✗ Неверный выбор. Попробуйте снова.")
