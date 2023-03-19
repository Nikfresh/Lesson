from termcolor import cprint, colored


class Road:
    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance


class Warehouse:
    def __init__(self, name, content=0):
        self.name = name
        self.content = content
        self.road_out = None
        self.queue_in = []
        self.queue_out = []

    def __str__(self):
        return f'Склад {self.name} груза {self.content}'

    def set_road_out(self, road):
        self.road_out = road

    def truck_arrived(self, truck):
        self.queue_in.append(truck)
        cprint(f'{self.name} прибыл грузовик {truck}', color='yellow')

    def get_new_truck(self):
        if self.queue_in:
            truck = self.queue_in.pop(0)
            cprint(f'{truck.model} заехал на склад {self.name}', color='yellow')
            return truck

    def truck_ready(self, truck):
        self.queue_out.append(truck)
        cprint(f'{self.name} грузовик готов {truck}', color='magenta')

    def act(self):
        while self.queue_out:
            truck = self.queue_out.pop(0)
            truck.go_to(road=self.road_out)


class Vehicle:
    fuel_rate = 0

    def __init__(self, model):
        self.model = model
        self.fuel = 0

    def __str__(self):
        return f'{self.model} - топливо {self.fuel}'

    def tank_up(self):
        self.fuel += 1000
        cprint(f'{self.model} - заправился', color='blue')

    def act(self):
        if self.fuel < 10:
            self.tank_up()
            return False
        else:
            return True


class Truck(Vehicle):
    fuel_rate = 50
    def __init__(self, model, boody_space=1000):
        super().__init__(model=model)
        self.boody_space = boody_space
        self.cargo = 0
        self.velocity = 100
        self.place = None
        self.distance_to_target = 0

    def __str__(self):
        res = super().__str__()
        return res + f' груза {self.cargo}'

    def ride(self):
        if self.distance_to_target > self.velocity:
            self.distance_to_target -= self.velocity
            cprint(f'{self.model} едет по дороге, осталось ехать {self.distance_to_target}')
        elif self.distance_to_target <= self.velocity:
            self.place = self.place.end
            self.place.truck_arrived(self)
            cprint(f'{self.model} доехал в {self.place.name}')
        self.fuel -=self.fuel_rate

    def go_to(self, road):
        self.place = road
        self.distance_to_target = road.distance
        cprint(f'{self.model} выехал в путь на трассу к складу {road.end.name}')

    def act(self):
        if super().act():
            if isinstance(self.place, Road):
                self.ride()



class AutoLoader(Vehicle):
    fuel_rate = 20
    def __init__(self, model, bucket_capacity=100, warehouse=None, role='loader'):
        super().__init__(model=model)
        self.bucket_capacity = bucket_capacity
        self.warehouse = warehouse
        self.role = role
        self.truck = None

    def __str__(self):
        res = super().__str__()
        return res + f' грузит {self.truck}'

    def act(self):
        if super().act():
            if self.truck is None:
                self.truck = self.warehouse.get_new_truck()
            elif self.role == 'loader':
                self.load()
                self.fuel -= self.fuel_rate
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

truck1 = Truck(model='Камаз', boody_space=5000)
truck2 = Truck(model='ГАЗ', boody_space=2000)
truck3 = Truck(model='Урал', boody_space=6000)

moscow.truck_arrived(truck1)
moscow.truck_arrived(truck2)
moscow.truck_arrived(truck3)
hour = 0
while piter.content < TOTAL_CARGO:
    hour += 1
    cprint(f'------------------------------Час {hour}------------------------------', color='red')
    truck1.act()
    truck2.act()
    truck3.act()
    loader_1.act()
    loader_2.act()
    moscow.act()
    piter.act()
    cprint(truck1, color='cyan')
    cprint(truck2, color='cyan')
    cprint(truck3, color='cyan')
    cprint(loader_1, color='cyan')
    cprint(loader_2, color='cyan')
    cprint(moscow, color='cyan')
    cprint(piter, color='cyan')
