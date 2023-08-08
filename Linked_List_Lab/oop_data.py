from data import train_cars

class Car():
    def __init__(self, ID, color, weight, material):
        self.ID = ID
        self.color = color
        self.weight = weight
        self.material = material
        self.next_train = None

first_ID = 277
first_train = train_cars[str(first_ID)]
train_linked_list = Car(ID=first_ID, color=first_train['color'], weight=first_train['weight'], material=first_train['material'])

ct_oop = train_linked_list
ct = first_train
while ct['next_train']:
    ID = ct['next_train']
    ct = train_cars[ID]
    ct_oop.next_train = Car(ID=ID, color=ct['color'], weight=ct['weight'], material=ct['material'])
    ct_oop = ct_oop.next_train


first_train = train_linked_list