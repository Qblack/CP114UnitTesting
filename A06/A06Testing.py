'''
Created on 2014-03-08

@author: Q
'''
import unittest
from ddt import ddt, data
import random

import functions as palandrome
from deque_linked import Deque 


@ddt
class TestPalindrome(unittest.TestCase):

    @data(["kayak",True],
          ["kayyak",True],
          ["a",True],
          ["aa",True],
          ["Aa",False],
          ["bubbles",False],
          ["",True]
          )
    def test_palandromes(self,pair):
        expected = pair[1]
        actual = palandrome.is_palindrome(pair[0])
        self.assertEqual(expected,actual)
        
class TestDeque(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.m_sut = Deque()
      
    def test__init__(self):        
        self.assertIsNone(self.m_sut._front, "Front is not None")
        self.assertIsNone(self.m_sut._rear, "Rear is not None")
        self.assertEqual(0,self.m_sut._size, "Size is not 0")
    
    def test__len__empty(self):
        actual = len(self.m_sut)
        expected = 0
        self.assertEqual(expected, actual, "Empty list did not work")

    def test__len__insertedInFront(self):
        self.m_sut.insert_front(2)
        actual = len(self.m_sut)
        expected = 1
        self.assertEqual(expected, actual, "InsertedInFront did not set correct length")
    
    def test__len__insertedInRear(self):
        self.m_sut.insert_rear(3)
        actual = len(self.m_sut)
        expected = 1
        self.assertEqual(expected, actual, "Inserted in rear did not set length correctly")
    
    def test_is_empty_empty(self):
        actual = self.m_sut.is_empty()
        self.assertTrue(actual, "Empty does not work on empty")
        return
    
    def test_is_empty_nonEmpty(self):
        self.m_sut.insert_front(5)
        actual = self.m_sut.is_empty()
        self.assertFalse(actual, "Empty does not work on empty")
        return


    def test_insert_front_intoEmpty(self):
        value = random.randint(0,10)
        self.m_sut.insert_front(value)
        self.assertIsNotNone(self.m_sut._rear,"Rear was not set")
        self.assertIsNotNone(self.m_sut._front,"Front was not set")
        self.assertEqual(value,self.m_sut._front._value,"Front value was not correct")
        self.assertEqual(value,self.m_sut._rear._value,"Rear value was not correct")
        actual = self.m_sut.peek_front()
        self.assertEqual(value,actual)
        return
    
    def test_insert_front_intoNonEmpty(self):
        front_value = random.randint(0,10)
        self.m_sut.insert_front(front_value)
        rear_value = random.randint(0,10)
        self.m_sut.insert_front(rear_value)
        self.assertIsNotNone(self.m_sut._rear,"Rear was not set")
        self.assertIsNotNone(self.m_sut._front,"Front was not set")
        
        self.assertEqual(rear_value,self.m_sut._front._value,"Front front_value was not correct")
        self.assertEqual(front_value,self.m_sut._rear._value,"Rear front_value was not correct")
        actual = self.m_sut.peek_front()
        self.assertEqual(rear_value,actual)
        return
    
    def test_insert_rear_intoEmpty(self):
        value = random.randint(0,10)
        self.m_sut.insert_rear(value)
        self.assertIsNotNone(self.m_sut._rear,"Rear was not set")
        self.assertIsNotNone(self.m_sut._front,"Front was not set")
        self.assertEqual(value,self.m_sut._front._value,"Front value was not correct")
        self.assertEqual(value,self.m_sut._rear._value,"Rear value was not correct")
        actual = self.m_sut.peek_front()
        self.assertEqual(value,actual)
        return

    
    def test_insert_rear_intoNonEmpty(self):
        front_value = random.randint(0,10)
        self.m_sut.insert_rear(front_value)
        rear_value = random.randint(0,10)
        self.m_sut.insert_rear(rear_value)

        self.assertIsNotNone(self.m_sut._rear,"Rear was not set")
        self.assertIsNotNone(self.m_sut._front,"Front was not set")
        
        self.assertEqual(front_value,self.m_sut._front._value,"Front rear_value was not correct")
        self.assertEqual(rear_value,self.m_sut._rear._value,"Rear rear_value was not correct")
        actual = self.m_sut.peek_front()
        self.assertEqual(front_value,actual)
        return
    
    def test_remove_front_empty(self):
        actual = self.m_sut.remove_front()
        self.assertIsNone(actual, "Did not return none on empty removal")
        return
    
    def test_remove_rear_empty(self):
        actual = self.m_sut.remove_rear()
        self.assertIsNone(actual, "Did not return none on empty removal")
        return
    
    
    def test_remove_front_non_empty(self):
        value = random.randint(0,10)
        self.m_sut.insert_front(value)
        actual = self.m_sut.remove_front()
        self.assertEqual(value,actual, "Removal did not return the correct value")
        self.assertEqual(0,len(self.m_sut),"Length was not set back to 0")
        
        return
    
    def test_remove_rear_non_empty(self):
        value = random.randint(0,10)
        self.m_sut.insert_rear(value)
        actual = self.m_sut.remove_rear()
        self.assertEqual(value,actual, "Did not return none on empty removal")
        self.assertEqual(0,len(self.m_sut),"Length was not set back to 0")
        return
    
    def test_remove_front_non_empty_multivalues(self):
        values = [0,1,2,3,4,5,6,7,8,9]
        for i in values:
            self.m_sut.insert_front(i)
        for j in range(len(values)-1,-1,-1):
            actual = self.m_sut.remove_front()
            self.assertEqual(values[j],actual, "Did not return correct value") 
        
        self.assertEqual(0,len(self.m_sut),"Length was not set back to 0")
        
        return
    
    def test_remove_rear_non_empty_multivalues(self):
        values = [0,1,2,3,4,5,6,7,8,9]
        for i in values:
            self.m_sut.insert_front(i)
        
        for j in range(len(values)):
            actual = self.m_sut.remove_rear()
            self.assertEqual(values[j],actual, "Did not return correct value")      
        
        self.assertEqual(0,len(self.m_sut),"Length was not set back to 0")
            
        return
    
    def test_peek_front_empty(self):
        self.assertIsNone(self.m_sut.peek_front(),"Peek did not return None")
        return
    
    def test_peek_rear_empty(self):
        self.assertIsNone(self.m_sut.peek_rear(),"Peek did not return None")
        return

    def test_peek_front(self):
        value = random.randint(0,10)
        self.m_sut.insert_front(value)
        actual =self.m_sut.peek_front()
        self.assertEqual(value, actual, "Peek did not return correct value")
        return
    
    def test_peek_rear(self):
        value = random.randint(0,10)
        self.m_sut.insert_front(value)
        actual =self.m_sut.peek_rear()
        self.assertEqual(value, actual, "Peek did not return correct value")
        return



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    