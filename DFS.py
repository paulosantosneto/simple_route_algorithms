class City:
    def __init__(self, name):
        self.visited = False
        self.name = name    
        self.near = []
        
    def addNearCity(self, city):
        self.near.append(city)

class Adjacent:
    def __init__(self, city):
        self.city = city    

class Map:
    rio_grande = City('Rio Grande')
    pelotas = City('Pelotas')
    bage = City('Bagé')
    uruguaiana = City('Uruguaiana')
    santa_maria = City('Santa Maria')
    sao_borja = City('São Borja')
    santa_cruz_do_sul = City('Santa Cruz do Sul')
    cruz_alta = City('Cruz Alta')
    passo_fundo = City('Passo Fundo')
    erechim = City('Erechim')
    caxias_do_sul = City('Caxias do Sul')
    porto_alegre = City('Porto Alegre')

    rio_grande.addNearCity(Adjacent(pelotas))

    pelotas.addNearCity(Adjacent(rio_grande))
    pelotas.addNearCity(Adjacent(porto_alegre))
    pelotas.addNearCity(Adjacent(santa_maria))

    bage.addNearCity(Adjacent(uruguaiana))
    bage.addNearCity(Adjacent(santa_maria))
    bage.addNearCity(Adjacent(pelotas))

    uruguaiana.addNearCity(Adjacent(santa_maria))
    uruguaiana.addNearCity(Adjacent(bage))

    santa_maria.addNearCity(Adjacent(sao_borja))
    santa_maria.addNearCity(Adjacent(cruz_alta))
    santa_maria.addNearCity(Adjacent(santa_cruz_do_sul))
    santa_maria.addNearCity(Adjacent(uruguaiana))
    santa_maria.addNearCity(Adjacent(pelotas))
    santa_maria.addNearCity(Adjacent(bage))

    sao_borja.addNearCity(Adjacent(cruz_alta))
    sao_borja.addNearCity(Adjacent(santa_maria))

    santa_cruz_do_sul.addNearCity(Adjacent(passo_fundo))
    santa_cruz_do_sul.addNearCity(Adjacent(porto_alegre))
    santa_cruz_do_sul.addNearCity(Adjacent(santa_maria))

    cruz_alta.addNearCity(Adjacent(sao_borja))
    cruz_alta.addNearCity(Adjacent(santa_maria))
    cruz_alta.addNearCity(Adjacent(passo_fundo))

    passo_fundo.addNearCity(Adjacent(cruz_alta))
    passo_fundo.addNearCity(Adjacent(erechim))
    passo_fundo.addNearCity(Adjacent(caxias_do_sul))

    erechim.addNearCity(Adjacent(passo_fundo))

    caxias_do_sul.addNearCity(Adjacent(passo_fundo))
    caxias_do_sul.addNearCity(Adjacent(porto_alegre))

    porto_alegre.addNearCity(Adjacent(caxias_do_sul))
    porto_alegre.addNearCity(Adjacent(santa_cruz_do_sul))
    porto_alegre.addNearCity(Adjacent(pelotas))
    
class Stack:
    def __init__(self, length):
        self.length = length
        self.cities = [None] * self.length
        self.top = -1

    def push(self, city):
        if not self.full():
            self.top += 1
            self.cities[self.top] = city
        
    def pop(self):
        if not self.empty():
            aux = self.cities[self.top]
            self.top -= 1
            return aux
        return None
      
    def getTop(self):
        return self.cities[self.top]
   
    def empty(self):
        return (self.top == -1)

    def full(self):
        return (self.top == self.length - 1)
 
class DFS:
    def __init__(self, start, goal):
        self.start = start
        self.start.visited = True
        self.goal = goal
        self.stack= Stack(20)
        self.stack.push(start)
        self.found = False

    def search(self):
        print('-----------------------------------')
        top = self.stack.getTop()
        print('City: {}'.format(top.name))
        
        if top == self.goal:
            self.found = True
        else:
            for a in top.near:
                if self.found == False:
                    print('Checking if already visited: {}'.format(a.city.name))
                    if a.city.visited == False:
                        a.city.visited = True
                        self.stack.push(a.city)
                        self.search()
        print('Pop: {}'.format(self.stack.pop().name))
        
def main():
  map = Map()
  dfs = DFS(map.rio_grande, map.erechim)
  dfs.search()

if __name__ == '__main__':
  main()
