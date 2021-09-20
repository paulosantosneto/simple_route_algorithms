class City:
    def __init__(self, name, distance):
        self.visited = False
        self.name = name
        self.distance = distance
        self.near = []

    def addNearCity(self, city):
        self.near.append(city)

class Adjacent:
    def __init__(self, city):
        self.city = city


class Map:
    def __init__(self):
        self.matrix = {
            'Rio Grande': [0, 244, 37, 201, 308, 529, 535, 425, 337, 262, 405, 494],
            'Porto Alegre': [238, 0, 220, 311, 254, 489, 286, 229, 97, 122, 278, 286],
            'Pelotas': [37, 220, 0, 174, 271, 482, 506, 368, 288, 206, 249, 438],
            'Erechim': [494, 286, 460, 448, 274, 383, 526, 71, 201, 223, 172, 0],
            'Passo Fundo': [421, 229, 390, 379, 210, 354, 485, 0, 157, 163, 125, 71],
            'São Borja': [529, 489, 482, 349, 242, 0, 162, 354, 473, 366, 234, 383],
            'Santa Cruz do Sul': [262, 122, 228, 240, 134, 266, 449, 163, 137, 0, 165, 233],
            'Santa Maria': [308, 254, 271, 185, 0, 242, 316, 210, 262, 134, 11, 274],
            'Cruz Alta': [405, 278, 368, 303, 188, 234, 360, 125, 243, 165, 0, 172],
            'Uruguaiana': [535, 567, 506, 335, 316, 162, 0, 485, 576, 449, 360, 526],
            'Caxias do Sul': [337, 90, 304, 367, 262, 476, 577, 163, 0, 135, 247, 208],
            'Bagé': [201, 311, 174, 0, 185, 349, 185, 379, 370, 240, 303, 448]
            }

        self.cities = ['Rio Grande', 'Porto Alegre', 'Pelotas', 'Bagé', 'Santa Maria', 'São Borja',
        'Uruguaiana', 'Passo Fundo', 'Caxias do Sul', 'Santa Cruz do Sul', 'Cruz Alta', 'Erechim']

        self.objects = []

    def addCities(self, city):
        for i in range(len(self.cities)):
            self.objects.append(City(self.cities[i], self.matrix[city][i]))


        self.objects[0].addNearCity(Adjacent(self.objects[2]))

        self.objects[2].addNearCity(Adjacent(self.objects[0]))
        self.objects[2].addNearCity(Adjacent(self.objects[1]))
        self.objects[2].addNearCity(Adjacent(self.objects[3]))
        self.objects[2].addNearCity(Adjacent(self.objects[4]))

        self.objects[3].addNearCity(Adjacent(self.objects[6]))
        self.objects[3].addNearCity(Adjacent(self.objects[4]))
        self.objects[3].addNearCity(Adjacent(self.objects[2]))

        self.objects[6].addNearCity(Adjacent(self.objects[4]))
        self.objects[6].addNearCity(Adjacent(self.objects[3]))
        self.objects[6].addNearCity(Adjacent(self.objects[5]))

        self.objects[4].addNearCity(Adjacent(self.objects[5]))
        self.objects[4].addNearCity(Adjacent(self.objects[9]))
        self.objects[4].addNearCity(Adjacent(self.objects[6]))
        self.objects[4].addNearCity(Adjacent(self.objects[2]))
        self.objects[4].addNearCity(Adjacent(self.objects[3]))

        self.objects[5].addNearCity(Adjacent(self.objects[10]))
        self.objects[5].addNearCity(Adjacent(self.objects[4]))
        self.objects[5].addNearCity(Adjacent(self.objects[6]))

        self.objects[9].addNearCity(Adjacent(self.objects[10]))
        self.objects[9].addNearCity(Adjacent(self.objects[2]))
        self.objects[9].addNearCity(Adjacent(self.objects[4]))

        self.objects[10].addNearCity(Adjacent(self.objects[5]))
        self.objects[10].addNearCity(Adjacent(self.objects[7]))
        self.objects[10].addNearCity(Adjacent(self.objects[9]))

        self.objects[7].addNearCity(Adjacent(self.objects[10]))
        self.objects[7].addNearCity(Adjacent(self.objects[11]))
        self.objects[7].addNearCity(Adjacent(self.objects[8]))

        self.objects[11].addNearCity(Adjacent(self.objects[7]))

        self.objects[8].addNearCity(Adjacent(self.objects[7]))
        self.objects[8].addNearCity(Adjacent(self.objects[1]))

        self.objects[1].addNearCity(Adjacent(self.objects[8]))
        self.objects[1].addNearCity(Adjacent(self.objects[2]))

class OrderedVector:

    def __init__(self, length):
        self.numberValues = 0
        self.cities = [None]*length

    def append(self, city):
        if self.numberValues == 0:
            self.cities[0] = city
            self.numberValues = 1
            return

        position = 0
        i = 0
        while i < self.numberValues:
            if city.distance > self.cities[position].distance:
                 position += 1
            i += 1

        for k in range(self.numberValues, position, -1):
             self.cities[k] = self.cities[k -1]

        self.cities[position] = city
        self.numberValues += 1

    def getFirst(self):
        return self.cities[0]

    def print(self):
        for i in range(0, self.numberValues):
            print('{} - {}'.format(self.cities[i].nome, self.cities[i].distance))

class Greedy:
    def __init__(self, goal):
        self.goal = goal
        self.found = False

    def search(self, current):

        current.visited = True

        if current == self.goal:
            print(f'{current.name}')
            self.found = True
        else:
            print(f'{current.name} -> ', end='')
            self.frontier = OrderedVector(len(current.near))
            for a in current.near:


                if a.city.visited == False:
                    a.city.visited = True
                    self.frontier.append(a.city)

            if self.frontier.cities[0] != None:
                self.search(self.frontier.cities[0])

def main():
    map = Map()

    start = input('Enter departure city:')
    while start not in map.matrix:
        start = input('Enter departure city:')
    goal = input('Enter arrival city:')
    while goal not in map.matrix:
        goal = input('Enter arrival city:')

    map.addCities(goal)

    greedy = Greedy(map.objects[map.cities.index(goal)])
    greedy.search(map.objects[map.cities.index(start)])

if __name__ == '__main__':
  main()
