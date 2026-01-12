class ComputerSpecification():
    def __init__(self,processor,ram):
        self.processor = processor
        self.ram = ram

computer1 = ComputerSpecification("intel i5","16gb")
del computer1           #this del statement id deleting the call computer1

print(computer1.processor,computer1.ram)