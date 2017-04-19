class Car:
    def __init__(self, name='General', model='GM', type='saloon'):
        self.name = name
        self.model = model
        self.type = type
        self.speed = 0

        if self.name != 'Porshe' and self.name != 'Koenigsegg':
            self.num_of_doors = 4

        elif self.name == 'Porshe' or self.name == 'Koenigsegg':
            self.num_of_doors = 2

        if self.type == 'trailer':
            self.num_of_wheels = 8

        elif self.type != 'trailer':
            self.num_of_wheels = 4

    def is_saloon(self):
        if self.type == 'saloon':
            return True

        else:
            return False

    def drive(self, gear):
        if self.type == 'trailer':
            self.speed = gear * 11
            return self

        else:
            self.speed = 10 ** gear
            return self