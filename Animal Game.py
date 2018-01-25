class GameMap:
    def __init__(self,N):
        self.N = N
        self.map = []

    def addAnimal(self):
        for i in range(self.N):
            self.map.append([])
            self.map[i] = ['0'] * self.N
        count = 0
        for x,y in loc_list:
                self.map[x][y] = animal_list[count]
                count += 1

    def printMap(self):
        for row in self.map:
            print ' '.join(row)

class Animal:
    def __init__(self,life,x,y):
        self.life = life
        self.x = x
        self.y = y
        self.store_location()
        self.store_hp()

    def store_location(self):
        loc_list.append([self.x,self.y])

    def store_animal(self,animal):
        animal_list.append(animal)

    def store_hp(self):
        hp_list.append(self.life)

    def moveTo(self,x,y):   #move the animal into particular place
        x_gap = x - self.x
        y_gap = y - self.y
        temp_x = self.x
        temp_y = self.y
        temp_loc = [temp_x, temp_y]
        if temp_loc not in loc_list:
            return

        for i in range(abs(y_gap)):     #move y one by one
            if self.life <= 0:
                self.kill()     #if life < 0, stop looping
                break

            if y_gap < 0:
                temp_y -= 1
                self.life -=1
                temp_loc = [temp_x,temp_y]

            elif y_gap > 0:
                temp_y += 1
                self.life -=1
                temp_loc = [temp_x,temp_y]

            if temp_loc in loc_list:
                self.meet(loc_list.index(temp_loc)) #look for the animal that is met in the location list

        if self.life <= 0:  #stop moving in x location if self.life already <0 after moving in y location
            self.kill()

        else:
            for i in range(abs(x_gap)):     #move x one by one
                if self.life <= 0:
                    self.kill()
                    break

                if x_gap < 0:
                    temp_x -= 1
                    self.life -=1
                    temp_loc = [temp_x,temp_y]

                elif x_gap > 0:
                    temp_x += 1
                    self.life -=1
                    temp_loc = [temp_x,temp_y]

                if temp_loc in loc_list:
                    self.meet(loc_list.index(temp_loc)) #look for the animal that is met in the location list

    def meet(self,index):   #decide if the animal hp should be added or deducted
        this_hp = hp_list[index]
        this_animal = animal_list[index]
        if this_animal == self.typ:
            this_hp += self.life
            hp_list[index] = this_hp
            self.life = this_hp
            self.kill()

        elif this_animal != self.typ:
            host_remaining_hp = this_hp - self.life
            intruder_remaining_hp = self.life - this_hp
            if host_remaining_hp <0:    #kill host
                self.life = intruder_remaining_hp
                animal_list[index] = self.typ
                hp_list[index] = self.life
                self.kill()


            elif intruder_remaining_hp<0:   #kill intruder
                self.kill()
                hp_list[index] = host_remaining_hp

    def kill(self): #kill the intruder
        del animal_list[loc_list.index([self.x,self.y])]
        del hp_list[loc_list.index([self.x,self.y])]
        del loc_list[loc_list.index([self.x,self.y])]

class AnimalA(Animal):
    def __init__(self,life,x,y):
        Animal.__init__(self,life,x,y)
        self.typ = 'A'
        self.store_animal('A')

class AnimalB(Animal):
    def __init__(self,life,x,y):
        Animal.__init__(self,life,x,y)
        self.typ = 'B'
        self.store_animal('B')

class AnimalC(Animal):
    def __init__(self,life,x,y):
        Animal.__init__(self,life,x,y)
        self.typ = 'C'
        self.store_animal('C')

loc_list = []
animal_list = []
hp_list = []

m = GameMap(9)
a1 = AnimalA(10, 2, 2)
a2 = AnimalA(6, 7, 8)
b1 = AnimalB(4, 5, 1)
b2 = AnimalB(3, 0, 6)
c1 = AnimalC(12, 4, 5)
c2 = AnimalC(8, 8, 0)
m.addAnimal()
print 'Initial map'
m.printMap()
print ''
a1.moveTo(5, 1)
a1.moveTo(7,8)
b1.moveTo(2, 3)
c1.moveTo(8, 0)
c2.moveTo(7, 8)
m.addAnimal()
print 'After'
m.printMap()
