# Animal Shelter Queue
# 2 animals: dog and cat
#--------------------------------------------------
# 'sam'  'fido-Dog'  'spud-Dog**'
#--------------------------------------------------
class AnimalShelter:
    def __init__(self, front=None):
        self.front = front
        self.rear = None

    def enqueue(self, animal):
        # if empty the new is the front and the rear
        if self.is_empty():
            self.front = animal
            self.rear = animal

        # if not empty the animal becomes the new rear
        if not self.is_empty():
            self.rear.next = animal
            self.rear = animal

    # --------------------------------------------------
    #  'fido-Dog' 'spud-Dog**'
    # --------------------------------------------------

    def dequeue(self, pref):
        # Is empty?
        if self.is_empty():
            return 'The animal queue is empty'
        # is there a pref of cat or dog
        if pref != "dog" or pref != "cat":
            return None
        # deque proccess will remove the node from the front of the queue
        # make the next the new front
        temp_front = self.front
        while True:
            if self.front.species == pref and self.front == temp_front:
                return_animal = self.front
                self.front = self.front.next
                return return_animal
            elif self.front.species == pref:
                return_animal = self.front
                self.front = self.front.next

                if self.front == temp_front:
                    return return_animal
                else:
                    while self.front != temp_front:
                        temp = self.front
                        self.front = self.front.next
                        self.enqueue(temp)
                    return return_animal

            if self.front.species != pref:
                temp = self.front
                self.front = self.front.next
                self.enqueue(temp)



        # check if the currnet node is what we are looking for
        # if yes, return the animla
        # if not set a temp_front flag and enqueue



    def is_empty(self):
        # THis returns a boolean
        pass

class Animal:
    def __init__(self, name, species='Dog'):
        self.name = name
        self.species = species
        self.next = None


