import unittest
import FiniteAutomata as File

class TestModThree(unittest.TestCase):
                    
        def test_modThree(self):
            for value in range(1000): 
                testValue=bin(value)[2:] #converts test values into binary 
                self.assertEqual(File.modThree(testValue),value%3,"modThree finite automata test 1 failed at "+str(value)+".")

                value=30000000000000
                testValue=bin(value)[2:]
                self.assertEqual(File.modThree(testValue),value%3,"modThree finite automata test 1 failed at "+str(value)+".")

        def test_invalidChar(self):
            for value in "ABCD@!#$%^&*":
                self.assertEqual(File.modThree(value),"string has a non-binary character "+str(value)+'.',"modThree finite automata test 1 failed at "+str(value)+".")

class TestFiniteAutomata(unittest.TestCase):
    
        modThreeTransitions=[[0,"0",0],[0,"1",1],[1,"0",2],[1,"1",0],[2,"0",1],[2,"1",2]]
        modFourTransitions=[[0,"0",0],[0,"1",1],[1,"0",2],[1,"1",3],[2,"0",0],[2,"1",1],[3,"0",2],[3,"1",3]]
        
        def test_modThree(self):
            for value in range(1000): 
                
                testValue=bin(value)[2:] 
                self.assertEqual(File.finiteAutomata([0,1,2],"01",0,[0,1,2],self.modThreeTransitions,testValue),value%3,
                                 "modThree finite automata test 1 failed at "+str(value)+".")

                value=30000000000000
                testValue=bin(value)[2:]
                self.assertEqual(File.finiteAutomata([0,1,2,3],"01",0,[0,1,2,3],self.modThreeTransitions,testValue),value%3,
                                 "modThree finite automata test 2 failed at "+str(value)+".")

        def test_modFour(self):
            for value in range(1000): 
                
                testValue=bin(value)[2:] 
                self.assertEqual(File.finiteAutomata([0,1,2,3],"01",0,[0,1,2,3],self.modFourTransitions,testValue),value%4,
                                 "modFour finite automata test 1 failed at "+str(value)+".")
                
                value=40000000000000
                testValue=bin(value)[2:]
                self.assertEqual(File.finiteAutomata([0,1,2,3],"01",0,[0,1,2,3],self.modFourTransitions,testValue),value%4,
                                 "modFour finite automata test 2 failed at "+str(value)+".")

        def test_invalidChar(self):
            for value in "ABCD@!#$%^&*":
                
                self.assertEqual(File.finiteAutomata([0,1,2],"01",0,[0,1,2],self.modThreeTransitions,"01"+str(value)),"string contains invalid character " +str(value),
                                 "modThree finite automata invalid character test 1 failed at "+str(value)+".")
                                 
                self.assertEqual(File.finiteAutomata([0,1,2,3],"01",0,[0,1,2,3],self.modFourTransitions,"01"+str(value)),"string contains invalid character " +str(value),
                                 "modFour finite automata invalid character test  failed at "+str(value)+".")
                
        def test_invalidInitialState(self):
                self.assertEqual(File.finiteAutomata([0,1,2],"01",10,[0,1,2],self.modThreeTransitions,"0"),"initial state, 10, not in states.",
                                 "modThree finite automata invalid initial state test failed.")
                                 
                self.assertEqual(File.finiteAutomata([0,1,2,3],"01",10,[0,1,2,3],self.modFourTransitions,"0"),"initial state, 10, not in states.",
                                 "modFour finite automata invalid initial state testfailed.")

        def test_invalidAcceptingState(self):
                self.assertEqual(File.finiteAutomata([0,1,2],"01",0,[10],self.modThreeTransitions,"0"),"accepting state, 10, not in states.",
                                 "modThree finite automata invalid accepting state test failed.")
                                 
                self.assertEqual(File.finiteAutomata([0,1,2,3],"01",0,[10],self.modFourTransitions,"0"),"accepting state, 10, not in states.",
                                 "modFour finite automata invalid accepting state test failed.")
                
        def test_invalidTransition(self):
            
                modThreeTransitions=[[0,"0",10],[0,"1",1],[1,"0",2],[1,"1",0],[2,"0",1],[2,"1",2]]
                modFourTransitions=[[0,"0",10],[0,"1",1],[1,"0",2],[1,"1",3],[2,"0",0],[2,"1",1],[3,"0",2],[3,"1",3]]
                
                self.assertEqual(File.finiteAutomata([0,1,2],"01",0,[0,1,2],modThreeTransitions,"0"),"invalid transitions: [[0, '0', 10]]",
                                 "modThree finite automata invalid transition test failed.")
                                 
                self.assertEqual(File.finiteAutomata([0,1,2,3],"01",0,[0,1,2,3],modFourTransitions,"0"),"invalid transitions: [[0, '0', 10]]",
                                 "modFour finite automata invalid transition test failed.")
                
                modThreeTransitions=[[0,"0",10],[0,"1",1],[1,"0",2],[1,"1",0],[2,"0",1],[22,"1",2]]
                modFourTransitions=[[0,"0",10],[0,"1",1],[1,"0",2],[1,"1",3],[2,"0",0],[2,"1",1],[23,"0",2],[3,"1",3]]
                
                self.assertEqual(File.finiteAutomata([0,1,2],"01",0,[0,1,2],modThreeTransitions,"0"),"invalid transitions: [[0, '0', 10], [22, '1', 2]]",
                                 "modThree finite automata invalid transition test failed.")
                                 
                self.assertEqual(File.finiteAutomata([0,1,2,3],"01",0,[0,1,2,3],modFourTransitions,"0"),"invalid transitions: [[0, '0', 10], [23, '0', 2]]",
                                 "modFour finite automata invalid transition test failed.")

        def test_notAcceptingState(self):
                           
                self.assertEqual(File.finiteAutomata([0,1,2],"01",0,[1,2],self.modThreeTransitions,"0"),"not accepting state.",
                                 "modThree finite automata not accepting state test failed.")
                                 
                self.assertEqual(File.finiteAutomata([0,1,2,3],"01",0,[1,2,3],self.modFourTransitions,"0"),"not accepting state.",
                                 "modFour finite automata not accepting state test failed.")

if __name__ == '__main__':
    unittest.main()
