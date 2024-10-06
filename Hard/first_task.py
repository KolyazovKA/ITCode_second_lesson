class Toy():
    def __init__(self, name: str, color: str, toy_type: str):
        self.name = name
        self.color = color
        self.toy_type = toy_type

    def __str__(self) -> str:
        return f"{self.toy_type} - {self.name} (Цвет: {self.color})"


class ToyFactory():
    def create_toy(self, name: str, color: str, toy_type: str) -> Toy:
        self.purchase_materials()
        self.sew()
        self.paint()
        return Toy(name, color, toy_type)

    def purchase_materials(self):
        print("Закупка сырья для игрушки.")

    def sew(self):
        print("Пошив игрушки.")

    def paint(self):
        print("Окраска игрушки.")

if __name__ == "__main__":
    factory = ToyFactory()
    new_toy = factory.create_toy("Медвежонок", "Коричневый", "Животное")
    print(new_toy)
