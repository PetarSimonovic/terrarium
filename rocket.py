import random
import sparks 

class Rocket:
    
    def __init__(self, display, width, height):
        self.display = display
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.blast_radius = 0
        self.blast_limit = 0
        self.fizzle = 0
        self.sparks = []
        
    def launch(self):
        if (len(self.sparks) == 0):
            self.create_fireworks()
        elif (self.blast_radius > self.blast_limit):
            self.sparks.clear()
        else:
            self.fly_sparks()
    
    def create_fireworks(self):
        self.create_blast_centre()
        self.blast_radius = 0
        self.blast_limit = random.randint(5, 30)
        self.create_sparks()
        # 2 is a magic number radius value in Spark class
        self.fizzle = 2/self.blast_limit

    def create_coordinate(self, range):
        return random.randint(0, range)
        
    def create_blast_centre(self):
        self.x = self.create_coordinate(self.width)
        self.y = self.create_coordinate(round(self.height/2))
    
    def create_sparks(self):
        while (len(self.sparks) < 30):
            for spark in range(30):
                sparks.add_sparks(self.sparks, spark, self.x, self.y)
       
    def fly_sparks(self):
        for spark in self.sparks:
            spark.x = sparks.get_x(self.sparks.index(spark), self.blast_radius, spark.x)
            spark.y = sparks.get_y(self.sparks.index(spark), self.blast_radius, spark.y)
            self.display.set_pen(spark.colour[0], spark.colour[1], spark.colour[2])
            self.display.circle(int(spark.x), int(spark.y), int(spark.r))
            spark.r -= self.fizzle
        self.blast_radius += 1
        


