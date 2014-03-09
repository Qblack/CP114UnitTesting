'''
Created on 2014-03-08

@author: Q
'''
import unittest
import random 

from bst_linked import BST

class TestBST(unittest.TestCase):


    def setUp(self):
        self.m_sut = BST()
        pass

    def testMinIterativeEmpty(self):
        actual = self.m_sut.min_i()
        self.assertIsNone( actual, "Not the correct maximum") 
    
    def testMinIterativeSingleNode(self):
        value = random.randint(0,100)
        self.m_sut.insert(value)
        actual = self.m_sut.min_i()
        self.assertEqual(value, actual, "Not the correct maximum")            
    
    def testMinIterativeFullTree(self):
        values = [41, 53, 76, 7, 59, 19, 92, 47, 43, 1, 13]
        for i in values:
            self.m_sut.insert(i)
        expected = min(values)
        actual = self.m_sut.min_i()
        self.assertEqual(expected, actual, "Not the correct maximum") 
        
    def testMaxRecursiveEmpty(self):
        actual = self.m_sut.max_r()
        self.assertIsNone( actual, "Not the correct maximum") 
    
    def testMaxRecursiveSingleNode(self):
        value = random.randint(0,100)
        self.m_sut.insert(value)
        actual = self.m_sut.max_r()
        self.assertEqual(value, actual, "Not the correct maximum")            
    
    def testMaxRecursiveFullTree(self):
        values = [41, 53, 76, 7, 59, 19, 92, 47, 43, 1, 13]
        for i in values:
            self.m_sut.insert(i)
        expected = max(values)
        actual = self.m_sut.max_r()
        self.assertEqual(expected, actual, "Not the correct maximum")           
        
    def testBST_delete_NoChildren(self):
        values = [41, 53, 76, 7, 59, 19, 92, 47, 43, 1, 13]
        for i in values:
            self.m_sut.insert(i)
        to_delete = 1
        actual = self.m_sut.remove(to_delete)
        self.assertEqual(to_delete, actual, "Did not return correct deleted element")
        return
    
    def testBST_delete_EmptyBst(self):
        values = []
        for i in values:
            self.m_sut.insert(i)
        actual = self.m_sut.remove(1)
        self.assertIsNone( actual, "Did not return correct deleted element")
        return
    
    def testBST_delete_SingleNode(self):
        values = [1]
        for i in values:
            self.m_sut.insert(i)
        to_delete = 1
        actual = self.m_sut.remove(to_delete)
        self.assertEqual( to_delete,actual, "Did not return correct deleted element")
        return
    
    def testBST_delete_RightChild(self):
        values = [1,2]
        for i in values:
            self.m_sut.insert(i)
        to_delete = 1
        actual = self.m_sut.remove(to_delete)
        self.assertEqual( to_delete,actual, "Did not return correct deleted element")
        return
    
    def testBST_delete_LeftChild(self):
        values = [2,1]
        for i in values:
            self.m_sut.insert(i)
        to_delete = 2
        actual = self.m_sut.remove(to_delete)
        self.assertEqual( to_delete,actual, "Did not return correct deleted element")
        return
    
    def testBST_delete_node_one_child(self):
        values = [41, 53, 76, 7, 59, 19, 92, 47, 43, 1, 13]
        for i in values:
            self.m_sut.insert(i)
        to_delete = 19
        actual = self.m_sut.remove(to_delete)
        self.assertEqual(to_delete, actual, "Did not return correct deleted element")

    def testBST_delete_two_children(self):
        values = [41, 53, 76, 7, 59, 19, 92, 47, 43, 1, 13]
        for i in values:
            self.m_sut.insert(i)
        to_delete = 53
        actual = self.m_sut.remove(to_delete)
        self.assertEqual(to_delete, actual, "Did not return correct deleted element")
        return
    
    def testBST_delete_node_node_not_in_Tree(self):
        values = [41, 53, 76, 7, 59, 19, 92, 47, 43, 1, 13]
        for i in values:
            self.m_sut.insert(i)
        to_delete = 99
        actual = self.m_sut.remove(to_delete)
        self.assertIsNone(actual, "Did not return correct deleted element")
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()