import unittest
import sys
sys.path.insert(0,"..")
from Node import Node
from LinkedList import LinkedList

class LinkedListOperations(unittest.TestCase):

    def setUp(self):
        self.llist = LinkedList()
        self.llist.append(3)
        self.llist.append(4)
        self.llist.append(5)
        self.llist.append(6)
        self.llist.append(7)
        self.llist.append(8)
        self.llist.append(9)

    
    def testAddAnElementAtBeginningOfList(self):
        self.llist.push(1)
        self.assertEqual(self.llist.getListValues(), [1,3,4,5,6,7,8,9])

    def testAddAnElementAtBeginningOgListTwoTimesInARow(self):
        self.llist.push(1)
        self.llist.push(2)
        self.assertEqual(self.llist.getListValues(), [2,1,3,4,5,6,7,8,9])

    def testDeleteTheFirstElement(self):
        self.llist.delete(3)
        self.assertTrue(self.llist.head.data == 4)

    def testDeleteTheFirstElementTwoTimesInARow(self):
        self.llist.delete(3)
        self.llist.delete(4)
        self.assertTrue(self.llist.head.data == 5)

    def testDeleteTheLastElement(self):
        self.llist.delete(9)
        self.assertEqual(self.llist.getListValues(), [3,4,5,6,7,8])

    def testDeleleteAMiddleElement(self):
        self.llist.delete(7)
        self.assertEqual(self.llist.getListValues(), [3,4,5,6,8,9])

    def testDeleleteAfterAnAppend(self):
        self.llist.append(10)
        self.llist.delete(10)
        self.assertEqual(self.llist.getListValues(), [3,4,5,6,7,8,9])

    def testDeleleteAnElementThatIsNotInTheList(self):
        self.llist.delete(23)
        self.assertEqual(self.llist.getListValues(), [3,4,5,6,7,8,9])

    def testReverseList(self):
        self.llist.reverse()
        self.assertEqual(self.llist.getListValues(), [9,8,7,6,5,4,3])

    def testReverseListTwoTimesInARow(self):
        self.llist.reverse()
        self.llist.reverse()
        self.assertEqual(self.llist.getListValues(), [3,4,5,6,7,8,9])

    def testReverseListAfterADelete(self):
        self.llist.delete(3)
        self.llist.reverse()
        self.assertTrue(self.llist.head.data == 9)

    def testGetCount(self):
        count = self.llist.getCount()
        self.assertEqual(count, 7)

    def testGetCountAfterDeletion(self):
        self.llist.delete(3)
        count = self.llist.getCount()
        self.assertEqual(count, 6)

    def testGetCountAfterAppend(self):
        self.llist.append(15)
        count = self.llist.getCount()
        self.assertEqual(count, 8)

    def testSearchItem(self):
        status = self.llist.search(7)
        self.assertTrue(status)

    def testSearchAnItemThatIsNotPresent(self):
        status = self.llist.search(42)
        self.assertFalse(status)

    def testSearchAnItemRightAfterItsAddition(self):
        self.llist.append(42)
        status = self.llist.search(42)
        self.assertTrue(status)

    def testGetListValues(self):
        self.assertEqual(self.llist.getListValues(), [3,4,5,6,7,8,9])


