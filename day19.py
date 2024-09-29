#OOPS-OBJECTED ORIENTED PROGRAMMING LANGUAGE
#------------------------------------------
#class:-blueprint/protoype to create objects
#it has-- 
 #1.properties-characteristics of class(Attributes)
   #eg:watch-
         #color,brand_name,type,time
 #2.behaviours-actions that can be perform(Methods-functions)
   #eg:watch-
          #display_time,time_adjust

#object:-instance of a class
#it is created from the class blueprint/prototype

# __init__
#constructor method-this function invokes at the creation of an object
#self:-referance to the instance of class

class Watch:
    def __init__(self,brand,color,time):
        self.brand_name=brand#attributes
        self.color=color#attributes
        self.time=time#attributes
    def display_time(self):
        print(f"TIME:{self.time}")
watch_one=Watch("Rolex","Black","12:00 Am")#object creation 
watch_two=Watch("Titan","Silver","9:00 Am")#object creation
watch_one.display_time()


class Watch:
    def __init__(self,brand,color,time):
        self.brand_name=brand#attributes
        self.color=color#attributes
        self.time=time#attributes
    def display_time(self):
        print(f"TIME:{self.time}")
watch_one=Watch("Rolex","Black","12:00 Am")#object creation 
watch_two=Watch("Titan","Silver","9:00 Am")#object creation
watch_three=Watch()'''

