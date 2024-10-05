

class Car():
    def __init__(self, speed: int, color: str, name: str) -> None:
        self.speed = speed
        self.color = color
        self.name = name

    def get_characteristics(self):
        print(f'speed: {self.speed},\ncolor: {self.color},\nname: {self.name}')

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction: str):
        print(f'Машина повернула {direction}')


class TownCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)
        self.is_police = False

class SportCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)
        self.is_police = False

class WorkCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)
        self.is_police = False

class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)
        self.is_police = True
    
    def turn_on_flasher(self):
        print('Включена мигалка')

def test_drive(car):
    print('\n=========================')
    car.get_characteristics()
    car.go()
    car.turn('направо')
    car.turn('налево')
    car.stop()
    print('==========================\n')

if __name__ == '__main__':
    towncar = TownCar(130, 'черный', 'Reno')
    sportcar = SportCar(250, 'красный', 'Ferari')
    workcar = WorkCar(120, 'белый', 'Fiat')
    policecar = PoliceCar(200, 'белый', 'Haval')

    test_drive(towncar)
    test_drive(sportcar)
    test_drive(workcar)
    test_drive(policecar)
    
