'''
Created on 2014-02-19

@author: Q
'''
import unittest

from queue_circular import CircularQueue
from priority_queue_array import PriorityQueue
from sorted_list_array import SortedList
import random



SIZE = 20
def create_queue(n,datastructure):
    insideList =[]
    for i in range(n):
        number = random.randint(0,SIZE)
        datastructure.insert(number)
        insideList.append(number)

    return insideList

class Test(unittest.TestCase):


    def setUp(self):
        self.empty_queue_circular = CircularQueue(10)
        full_queue_circular = CircularQueue(SIZE)
        values_circular= create_queue(SIZE,full_queue_circular)
        self.full_queue_circular = full_queue_circular
        self.values_circular=values_circular


        #Priority Queue Stuff
        self.empty_queue_priority = PriorityQueue()
        full_queue_priority = PriorityQueue()
        values_priority= create_queue(SIZE,full_queue_priority)
        self.full_queue_priority = full_queue_priority
        values_priority.sort()
        self.values_priority=values_priority


        #Sorted List
        self.empty_sorted_list = SortedList()
        full_sorted_list = SortedList()
        values_sorted_list= create_queue(SIZE,full_sorted_list)
        self.full_sorted_list = full_sorted_list
        values_sorted_list.sort()
        self.values_sorted_list=values_sorted_list



    #Circular

    def testCircularQueueIsEmpty_Empty(self):
        actual = self.empty_queue_circular.is_empty()
        self.assertTrue(actual, "CQ is not empty");
        return

    def testCircularQueueIsEmpty_NotEmpty(self):
        actual = self.full_queue_circular.is_empty()
        self.assertFalse(actual, "CQ is empty")
        return

    def testCircularQueueLen_Empty(self):
        expected = 0
        actual = len(self.empty_queue_circular)
        self.assertEqual(expected, actual, "length is incorrect")
        return

    def testCircularQueueLen_NotEmpty(self):
        actual = len(self.full_queue_circular)
        self.assertEqual(SIZE, actual, "length is incorrect")
        return

    def testCircularQueueIsFull_Empty(self):
        actual = self.empty_queue_circular.is_full()
        self.assertFalse(actual, "CQ is full")
        return

    def testCircularQueueIsFull_Full(self):
        actual = self.full_queue_circular.is_full()
        self.assertTrue(actual, "CQ is not full")
        return

    def testCircularQueuePeek_Empty(self):
        actual = self.empty_queue_circular.peek()
        self.assertIsNone(actual, "peeked is None")
        return

    def testCircularQueuePeek_Full(self):
        expected = self.values_circular[0]
        actual = self.full_queue_circular.peek()
        self.assertEqual(expected,actual);
        return

    def testCircularQueueRemove_Empty(self):
        actual = self.empty_queue_circular.remove()
        self.assertIsNone(actual, "peeked is None")
        return

    def testCircularQueueRemove_Full(self):
        expected = self.values_circular[0]
        actual = self.full_queue_circular.remove()
        self.assertEqual(expected,actual);
        self.assertNotEqual(SIZE, len(self.full_queue_circular))
        return

    def testCircularQueueRemove_FullQueueRemoval(self):
        i=0
        while not self.full_queue_circular.is_empty():
            v = self.full_queue_circular.remove()
            self.assertEqual(self.values_circular[i],v)
            i+=1

        self.assertEqual(0, len(self.full_queue_circular))

    #Priority

    def testPriorityQueueIsEmpty_Empty(self):
        expected = True
        actual = self.empty_queue_priority.is_empty()
        self.assertEqual(expected,actual);
        return

    def testPriorityQueueIsEmpty_NotEmpty(self):
        expected = False
        actual = self.full_queue_priority.is_empty()
        self.assertEqual(expected,actual);
        return

    def testPriorityQueuePeek_Empty(self):
        expected = None
        actual = self.empty_queue_priority.peek()
        self.assertEqual(expected,actual);
        return

    def testPriorityQueuePeek_Full(self):
        expected = self.values_priority[0]
        actual = self.full_queue_priority.peek()
        self.assertEqual(expected,actual);
        return

    def testPriorityQueueRemove_Empty(self):
        expected = None
        actual = self.empty_queue_priority.remove()
        self.assertEqual(expected,actual);
        return

    def testPriorityQueueRemove_Full(self):
        expected = self.values_priority[0]
        actual = self.full_queue_priority.remove()
        self.assertEqual(expected,actual);
        self.assertNotEqual(SIZE, len(self.full_queue_priority))
        return

    def testPriorityQueueRemove_FullQueueRemoval(self):
        i=0
        while not self.full_queue_priority.is_empty():
            v = self.full_queue_priority.remove()
            self.assertEqual(self.values_priority[i],v)
            i+=1

        self.assertEqual(0, len(self.full_queue_priority))

    #Sorted List
    def testSortedList_is_empty_Empty(self):
        expected = True
        actual = self.empty_sorted_list.is_empty()
        self.assertEqual(expected,actual)

        return

    def testSortedList_getitem_Empty(self):
        expected = None
        actual = self.empty_sorted_list[SIZE+1]
        self.assertEqual(expected,actual)
        return

    def testSortedList_index_goodKey_Empty(self):
        expected = -1
        actual = self.empty_sorted_list.index(0)
        self.assertEqual(expected,actual)
        return

    def testSortedList_index_badKey_Empty(self):
        expected = -1
        actual = self.empty_sorted_list.index(30)
        self.assertEqual(expected,actual)
        return

    def testSortedList_min_Empty(self):
        expected = None
        actual = self.empty_sorted_list.min()
        self.assertEqual(expected,actual)
        return

    def testSortedList_max_Empty(self):
        expected = None
        actual = self.empty_sorted_list.max()
        self.assertEqual(expected,actual)
        return

    def testSortedList_contains_goodKey_Empty(self):
        expected = False
        actual = 5 in self.empty_sorted_list
        self.assertEqual(expected,actual)
        return

    def testSortedList_contains_badKey_Empty(self):
        expected = False
        actual = SIZE+1 in self.empty_sorted_list
        self.assertEqual(expected,actual)
        return

    def testSortedList_count_goodKey_Empty(self):
        expected = 0
        actual = self.empty_sorted_list.count(5)
        self.assertEqual(expected,actual)
        return

    def testSortedList_count_badKey_Empty(self):
        expected = 0
        actual = self.empty_sorted_list.count(SIZE+1)
        self.assertEqual(expected,actual)
        return

    def testSortedList_remove_goodKey_Empty(self):
        expected = None
        actual = self.empty_sorted_list.remove(5)
        self.assertEqual(expected,actual)
        return

    def testSortedList_remove_badKey_Empty(self):
        expected = None
        actual = self.empty_sorted_list.remove(SIZE+1)
        self.assertEqual(expected,actual)
        return

    def testSortedList_split_Empty(self):
        test_list=[]
        left_list = []
        right_list = []
        sortedList = SortedList()
        for i in test_list:
            sortedList.insert(i)
            
        left = SortedList()
        right = SortedList()      
        sortedList.split(left, right)
        self.assertEqual(left_list,left._values)
        self.assertEqual(right_list,right._values)

        return

    def testSortedList_copy_Empty(self):
        rhs = SortedList()
        for i in range(10):
            rhs.insert(i)
        self.empty_sorted_list.copy(rhs)

        i=0
        for expected in range(0,10):
            self.assertEqual(expected,self.empty_sorted_list[i])
            i+=1
        return
		
		
	def testSortedList_clean_Empty(self):
        test_list=[]
        sortedList = SortedList()
        for i in test_list:
            sortedList.insert(i)
        sortedList.clean()
        
        clean_list=[]
        
        for expected in clean_list:
            actual = sortedList.remove(expected)
            self.assertEqual(expected, actual)
        return

# Full
    def testSortedList_is_empty_Full(self):
        expected = False
        actual = self.full_sorted_list.is_empty()
        self.assertEqual(expected,actual)

        return

    def testSortedList_getitem_Full(self):
        expected = self.values_sorted_list[2]
        actual = self.full_sorted_list[2]
        self.assertEqual(expected,actual)
        return

    def testSortedList_index_goodKey_Full(self):
        value = self.values_sorted_list[SIZE//2]
        expected = self.values_sorted_list.index(value)
        actual = self.full_sorted_list.index(value)
        self.assertEqual(expected,actual)
        return

    def testSortedList_index_badKey_Full(self):
        expected = -1
        actual = self.full_sorted_list.index(30)
        self.assertEqual(expected,actual)
        return

    def testSortedList_min_Full(self):
        expected = min(self.values_sorted_list)
        actual = self.full_sorted_list.min()
        self.assertEqual(expected,actual)
        return

    def testSortedList_max_Full(self):
        expected = max(self.values_sorted_list)
        actual = self.full_sorted_list.max()
        self.assertEqual(expected,actual)
        return

    def testSortedList_contains_goodKey_Full(self):
        expected = True
        actual = self.values_sorted_list[SIZE//2] in self.full_sorted_list
        self.assertEqual(expected,actual)
        return

    def testSortedList_contains_badKey_Full(self):
        expected = False
        actual = SIZE+1 in self.full_sorted_list
        self.assertEqual(expected,actual)
        return

    def testSortedList_count_goodKey_Full(self):
        value = self.values_sorted_list[SIZE//2]
        expected = self.values_sorted_list.count(value)
        actual = self.full_sorted_list.count(value)
        self.assertEqual(expected,actual)
        return

    def testSortedList_count_badKey_Full(self):
        expected = 0
        actual = self.full_sorted_list.count(SIZE+1)
        self.assertEqual(expected,actual)
        return

    def testSortedList_remove_goodKey_Full(self):
        expected = self.values_sorted_list[0]
        actual = self.full_sorted_list.remove(expected)
        self.assertEqual(expected,actual)
        return

    def testSortedList_remove_badKey_Full(self):
        expected = None
        actual = self.full_sorted_list.remove(SIZE+1)
        self.assertEqual(expected,actual)
        return

    def testSortedList_split_Full(self):
        test_list=[1,3,5,7,9,2,4,6,8,10]
        left_list = [1,3,5,7,9]
        right_list = [2,4,6,8,10]
        sortedList = SortedList()
        for i in test_list:
            sortedList.insert(i)
            
        left = SortedList()
        right = SortedList()      
        sortedList.split(left, right)
        self.assertEqual(left_list,left._values)
        self.assertEqual(right_list,right._values)
        

        return

    def testSortedList_copy_Full(self):
        rhs = SortedList()
        for i in range(10):
            rhs.insert(i)
        self.full_sorted_list.copy(rhs)

        i=0
        for expected in range(0,10):
            self.assertEqual(expected,self.full_sorted_list[i])
            i+=1
        return
		
    def testSortedList_clean_Full(self):
        test_list=[1,1,2,3,5,5,10]
        sortedList = SortedList()
        for i in test_list:
            sortedList.insert(i)
        sortedList.clean()
        
        clean_list=[1,2,3,5,10]
        
        for expected in clean_list:
            actual = sortedList.remove(expected)
            self.assertEqual(expected, actual)
        return







if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
