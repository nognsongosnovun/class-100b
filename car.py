class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelerate(self):
        print("accelerating...")
        "accelerater functionality"

    def change_gear(self,gear_type):
        print("gear_changed")
        "gear related functionality"

audi = Car("A8","orange","audi","190")

print(audi.start())
print(audi.accelerate())

