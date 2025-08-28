# Base Class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = 100  # default battery percentage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"Battery charged to {self.battery}%")

    def __str__(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage"


# Inherited Class
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)
        self.gpu = gpu

    def play_game(self, game):
        if self.battery > 20:
            self.battery -= 20
            print(f"Playing {game} on {self.brand} {self.model} with {self.gpu} GPU 🎮")
        else:
            print("Battery too low! Please charge your phone.")


# Create objects
phone1 = Smartphone("Samsung", "Galaxy S23", 256)
phone2 = GamingSmartphone("Asus", "ROG Phone 6", 512, "Adreno 730")

print(phone1)
phone1.call("123-456-789")
phone1.charge(15)

print(phone2)
phone2.play_game("Genshin Impact")
