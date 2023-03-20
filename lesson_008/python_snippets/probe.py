from termcolor import cprint, colored


class Road:
    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance
        self.name = f'Трасса "{self.start.name} - {self.end.name}"'

    def __str__(self):
        return f'{self.name}'


class Parking:
    def __init__(self, warehouse):
        self.name = f'Парковка склада {warehouse.name}'
        self.truck = []

    def __str__(self):
        return f'{self.name}'


class Warehouse:
    def __init__(self, name, content=0):
        self.name = name
        self.content = content
        self.road_out = None
        self.queue_in = []
        self.queue_out = []
        self.parking = Parking(self)

    def __str__(self):
        return f'Склад {self.name} груза {self.content}'

    def set_road_out(self, road):
        self.road_out = road

    def truck_arrived(self, truck):
        truck.place = self
        self.queue_in.append(truck)
        cprint(f'{self.name} прибыл грузовик {truck}', color='yellow')

    def get_new_truck(self):
        if self.queue_in:
            truck = self.queue_in.pop(0)
            cprint(f'{truck.model} заехал на склад {self.name}', color='yellow')
            return truck

    def truck_ready(self, truck):
        self.queue_out.append(truck)
        cprint(f'{self.name} грузовик готов {truck.model}', color='magenta')

    def act(self):
        while self.queue_out:
            truck = self.queue_out.pop(0)
            truck.go_to(road=self.road_out)


class Vehicle:
    fuel_rate = 0
    total_fuel = 0

    def __init__(self, model):
        self.model = model
        self.fuel = 0

    def __str__(self):
        return f'{self.model} - топливо {self.fuel}'

    def tank_up(self):
        self.fuel += 1000
        Vehicle.total_fuel += 1000
        cprint(f'{self.model} - заправился', color='blue')

    def act(self):
        if self.fuel < 10:
            self.tank_up()
            return False
        else:
            return True

class Truck(Vehicle):
    fuel_rate = 50
    dead_time = 0

    def __init__(self, model, boody_space=1000):
        super().__init__(model=model)
        self.boody_space = boody_space
        self.cargo = 0
        self.velocity = 100
        self.place = None
        self.distance_to_target = 0

    def __str__(self):
        place_name = 'в нигде'
        if self.place:
            place_name = self.place.name
        res = super().__str__()
        return res + f' груза {self.cargo} находится - {place_name}'

    def ride(self):
        if self.distance_to_target > self.velocity:
            self.distance_to_target -= self.velocity
            cprint(f'{self.model} едет по дороге {self.place.name}, осталось ехать {self.distance_to_target}')
        elif self.distance_to_target <= self.velocity:
            self.place = self.place.end
            self.place.truck_arrived(self)
            cprint(f'{self.model} доехал в {self.place.name}')
        self.fuel -= self.fuel_rate

    def go_to(self, road):
        self.place = road
        self.distance_to_target = road.distance
        cprint(f'{self.model} выехал в путь на трассу к складу {road.end.name}')

    def act(self):
        if super().act():
            if isinstance(self.place, Road):
                self.ride()
            else:
                Truck.dead_time += 1

class OtherTruck(Truck):
    fuel_rate = 100

class AutoLoader(Vehicle):
    fuel_rate = 20
    dead_time = 0

    def __init__(self, model, bucket_capacity=100, warehouse=None, role='loader'):
        super().__init__(model=model)
        self.bucket_capacity = bucket_capacity
        self.warehouse = warehouse
        self.role = role
        self.truck = None

    def __str__(self):
        truck_model = 'никого'
        if self.truck:
            truck_model = self.truck.model
        res = super().__str__()
        return res + f' грузит {truck_model}'

    def act(self):
        if super().act():
            if self.truck is None:
                self.truck = self.warehouse.get_new_truck()
                if self.truck is None:
                    AutoLoader.dead_time += 1
                    cprint(f'На складе {self.warehouse.name} нет грузовиков', color='red')
                else:
                    cprint(f'{self.model} взял в работу {self.truck.model}', color='green')
            elif self.role == 'loader':
                if self.warehouse.content > 0:
                    cprint(f'На складе {self.warehouse.name} {self.model} грузит {self.truck.model}', color='blue')
                    self.load()
                    self.fuel -= self.fuel_rate
                else:
                    cprint(f'{self.warehouse.name} кончился груз.', color='red')
                    if self.truck.cargo > 0:
                        self.warehouse.truck_ready(self.truck)
                    else:
                        cprint(f'{self.model} отправил на паркинг.{self.truck.model}', color='yellow',attrs=['reverse'])
                        self.truck.place = self.warehouse.parking
                        self.warehouse.parking.truck.append(self.truck)
                    self.truck = None

            else:
                self.unload()
                self.fuel -= self.fuel_rate

    def load(self):
        truck_cargo_rest = self.truck.boody_space - self.truck.cargo
        if truck_cargo_rest >= self.bucket_capacity:
            self.warehouse.content -= self.bucket_capacity
            self.truck.cargo += self.bucket_capacity
        else:
            self.warehouse.content -= truck_cargo_rest
            self.truck.cargo += truck_cargo_rest
        if self.truck.cargo == self.truck.boody_space:
            self.warehouse.truck_ready(self.truck)
            self.truck = None

    def unload(self):
        if self.truck.cargo >= self.bucket_capacity:
            self.truck.cargo -= self.bucket_capacity
            self.warehouse.content += self.bucket_capacity
        else:
            self.truck.cargo -= self.truck.cargo
            self.warehouse.content += self.truck.cargo
        if self.truck.cargo == 0:
            self.warehouse.truck_ready(self.truck)
            self.truck = None


TOTAL_CARGO = 100000

moscow = Warehouse(name='Москва', content=TOTAL_CARGO)
piter = Warehouse(name='Питер', content=0)

moscow_piter = Road(start=moscow, end=piter, distance=715)
piter_moscow = Road(start=piter, end=moscow, distance=780)

moscow.set_road_out(moscow_piter)
piter.set_road_out(piter_moscow)

loader_1 = AutoLoader(model='Bobcat', bucket_capacity=1000, warehouse=moscow, role='loader')
loader_2 = AutoLoader(model='Lonking', bucket_capacity=500, warehouse=piter, role='unloader')

trucks = []
for i in range(5):
    truck_in = Truck(model=f'Камаз {i+1}', boody_space=5000)
    trucks.append(truck_in)
    moscow.truck_arrived(truck_in)
for i in range(5):
    truck_in = OtherTruck(model=f'Volvo {i+1}', boody_space=10000)
    trucks.append(truck_in)
    moscow.truck_arrived(truck_in)

hour = 0
while piter.content < TOTAL_CARGO:
    hour += 1
    cprint(f'------------------------------Час {hour}------------------------------', color='red')
    for truck in trucks:
        truck.act()
    loader_1.act()
    loader_2.act()
    moscow.act()
    piter.act()
    for truck in trucks:
        cprint(truck, color='cyan')
    cprint(loader_1, color='cyan')
    cprint(loader_2, color='cyan')
    cprint(moscow, color='cyan')
    cprint(piter, color='cyan')
cprint(f'Всего заправлено горючего - {Vehicle.total_fuel}')
cprint(f'Время простоя погрузчиков - {AutoLoader.dead_time}')
cprint(f'Время простоя грузовиков - {Truck.dead_time}')
