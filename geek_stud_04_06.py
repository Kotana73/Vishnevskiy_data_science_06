class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} started'

    def stop(self):
        return f'{self.name} was stopped'

    def turn_right(self):
        return f'{self.name} turned right'

    def turn_left(self):
        return f'{self.name} turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} was {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} was higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} was {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} which was higher that is allowed for the work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


porsche = SportCar(100, 'Red', 'Porsche', False)
lincoln = TownCar(30, 'Blue', 'Lincoln', False)
gazel = WorkCar(70, 'Pink', 'Gazel', True)
ford = PoliceCar(110, 'White',  'Ford', True)
print(gazel.turn_left())
print(f'When {lincoln.turn_right()}, the {porsche.stop()}')
print(f'{gazel.go()} with speed about {gazel.show_speed()}')
print(f'{gazel.name} is {gazel.color}')
print(f'Is {porsche.name} a police car? {porsche.is_police}')
print(f'Is {gazel.name}  a police car? {gazel.is_police}')
print(porsche.show_speed())
print(lincoln.show_speed())
print(ford.police())
print(ford.show_speed())
