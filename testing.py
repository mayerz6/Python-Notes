class Dataset:
    
    def __init__(self, *args, **kwargs): 
        self.lang = input("What language?: ")
        self.version = float(input("Version?: "))
        self.skill = input("What is your skill level?: ")
    
    def upgrade(self):
        new_version = input("What version would you like to update to?: ")
        print(f"We have updated the version for {self.lang} from version {self.version} to {new_version}")
        self.version = new_version
        
rec1 = Dataset()
rec1.upgrade()
