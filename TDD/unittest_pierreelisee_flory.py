import sys 
path = "../OOP/"
sys.path.append(path)
import flory_main 
import unittest
import animals as Animals

 #This section tests the flory_main.py file (some parts of the function in the main program)
class AntCreationResults(unittest.TestCase):
    def test_ant_creation(self):
        ''' ant_creation should return an ant named after the input '''
        result=flory_main.ant_creation("test_ant")
        self.assertEqual("test_ant",result.name)

        

class AntCreationBadInput(unittest.TestCase):
    def test_not_string(self):
        ''' ant_creation should fail without a string as input'''
        self.assertRaises(flory_main.NotStringError, flory_main.ant_creation, 0)
        self.assertRaises(flory_main.NotStringError, flory_main.ant_creation, True)
        self.assertRaises(flory_main.NotStringError, flory_main.ant_creation, [])

class BirdCreationBadInput(unittest.TestCase):
    def test_suitable_maxAge(self):
        ''' bird_creation should fail without a positive maxAge for the bird '''
        self.assertRaises(flory_main.InputNotCoherent, flory_main.bird_creation, True, 0, 5, -1, "a")
        self.assertRaises(flory_main.InputNotCoherent, flory_main.bird_creation, True, 0, 5, 0, "a")
    def test_not_bool(self):
        ''' bird_creation should fail if the inputs are bad '''
        self.assertRaises(flory_main.NotBoolError, flory_main.bird_creation, 0,0,5,2,"a")
        self.assertRaises(flory_main.NotBoolError, flory_main.bird_creation, "0",0,5,2,"a")
        self.assertRaises(flory_main.NotBoolError, flory_main.bird_creation, [],0,5,2,"a")

#This section tests the animals.py file (some of the functions in there)
class BirdGetSpeedResults(unittest.TestCase):
    bird1 = Animals.Birds(True, 0, 10)
    bird1.weight = 2
    bird2 = Animals.Birds(True, 0, 10)
    bird2.weight = 7
    bird3 = Animals.Birds(True, 0, 10)
    bird3.weight = 15
    bird4 = Animals.Birds(False, 0, 10)
    bird4.weight = 2
    bird5 = Animals.Birds(True, 0, 10)
    bird5.weight = 23
    bird6 = Animals.Birds(False, 0, 10)
    bird6.weight = 50
    bird7 = Animals.Birds(True, 0, 10)
    bird7.weight = 50
    test_birds=[(bird1,50),(bird2,10),(bird3,5),(bird4,1),(bird5,5),(bird6,1),(bird7,5)]

    def test_bird_getSpeed(self):
        for bird,speed in self.test_birds:
            result = bird.getSpeed()
            self.assertEqual(result,speed)

class InsectGetSpeedResults(unittest.TestCase):
    insect1 = Animals.Insects(7,2)
    insect1.age = 2
    insect2 = Animals.Insects(6,4)
    insect2.age = 4
    insect3 = Animals.Insects(2,10)
    insect3.age = 1
    insect4 = Animals.Insects(10,17)
    insect4.age = 3
    insect5 = Animals.Insects(4,12)
    insect5.age = 2
    test_insects=[(insect1,4), (insect2,16),(insect3,10),(insect4,51),(insect5,24)]

    def test_insect_getSpeed(self):
        for insect,speed in self.test_insects:
            result = insect.getSpeed()
            self.assertEqual(result,speed)


#Launching the tests
unittest.main()
     

