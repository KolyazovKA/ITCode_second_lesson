from first_task import Toy

class AnimalToy(Toy):
    def __init__(self, name: str, color: str):
        super().__init__(name, color, "Животное")


class CartoonCharacterToy(Toy):
    def __init__(self, name: str, color: str):
        super().__init__(name, color, "Персонаж мультфильма")


class ToyFactory:
    def create_toy(self, name: str, color: str, toy_type: str) -> Toy:
        self.purchase_materials()
        self.sew()
        self.paint()
        
        if toy_type == "Животное":
            return AnimalToy(name, color)
        elif toy_type == "Персонаж мультфильма":
            return CartoonCharacterToy(name, color)
        else:
            raise ValueError("Неизвестный тип игрушки.")

    def purchase_materials(self):
        print("Закупка сырья для игрушки.")

    def sew(self):
        print("Пошив игрушки.")

    def paint(self):
        print("Окраска игрушки.")


if __name__ == "__main__":
    factory = ToyFactory()
    
    animal_toy = factory.create_toy("Медвежонок", "Коричневый", "Животное")
    print(animal_toy)

    cartoon_toy = factory.create_toy("Супермен", "Красный", "Персонаж мультфильма")
    print(cartoon_toy)
