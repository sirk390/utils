import unittest
from priority_queue import PriorityQueue, QueueEmpty

class TestPriorityQueue(unittest.TestCase):
    def test_PriorityQueue_WhenCreated_IsEmpty(self):
        priority_queue = PriorityQueue()
        
        self.assertEquals(len(priority_queue), 0)
        self.assertFalse(None in priority_queue)
        self.assertFalse("a" in priority_queue)
        self.assertFalse("" in priority_queue)

    def test_PriorityQueue_AddElement_ElementIsAdded(self):
        priority_queue = PriorityQueue()
        
        priority_queue.add("a", 0)
        
        self.assertTrue("a" in priority_queue)

    def test_PriorityQueue_PeekWhenEmpty_RaisesQueueEmpty(self):
        priority_queue = PriorityQueue()        
        
        with self.assertRaises(QueueEmpty):
            priority_queue.peek()
        
    def test_PriorityQueue_Peek_ReturnsElementWithLowestPriority(self):
        priority_queue = PriorityQueue()        
        priority_queue.add("a", 2)
        priority_queue.add("b", 3)
        priority_queue.add("c", 1)
        
        elm, pri = priority_queue.peek()
        self.assertEquals(elm, "c")
        

    def test_PriorityQueue_RemoveElement_ElementIsRemoved(self):
        priority_queue = PriorityQueue()
        priority_queue.add("a")
        
        priority_queue.remove("a")

        self.assertFalse("a" in priority_queue)

    def test_PriorityQueue_RemoveSecondElement_StatesRemaingCorrect(self):
        priority_queue = PriorityQueue()
        priority_queue.add("a", 1)
        priority_queue.add("b", 2)
       
        priority_queue.remove("b")

        self.assertEquals(list(priority_queue), [('a', 1)])
        self.assertEquals(len(priority_queue), 1)

    def test_PriorityQueue_RemoveFirstElement_StatesRemaingCorrect(self):
        priority_queue = PriorityQueue()
        priority_queue.add("a", 1)
        priority_queue.add("b", 2)
       
        priority_queue.remove("a")

        self.assertEquals(list(priority_queue), [('b', 2)])
        self.assertEquals(len(priority_queue), 1)
        
    def test_PriorityQueue_ChangePriorityUsingAddRemoveElement_PeekReturnsLowestElement(self):
        priority_queue = PriorityQueue()        
        priority_queue.add("a", 2)
        priority_queue.add("b", 3)
        priority_queue.add("c", 1)
        priority_queue.add("d", 0)
        priority_queue.remove("c")
        priority_queue.add("c", 4)
        elm, pri = priority_queue.peek()
        self.assertEquals(elm, "d")

    def test_PriorityQueue_NonEmptyQueueToString_ReturnsCorrectString(self):
        priority_queue = PriorityQueue()        
        priority_queue.add("a", 2)
        priority_queue.add("b", 3)
        priority_queue.add("c", 1)
        
        s = str(priority_queue)
        
        self.assertEquals(s, "<PriorityQueue[(c,1),(a,2),(b,3)]>")

    def test_PriorityQueue_GetPriority_ReturnsCorrectPriority(self):
        priority_queue = PriorityQueue()
        priority_queue.add("a", 0)
        priority_queue.add("b", 1)
        
        p_a = priority_queue.get_priority("a")
        p_b = priority_queue.get_priority("b")
        
        self.assertEquals(p_a, 0)
        self.assertEquals(p_b, 1)

    def test_PriorityQueue_OnEmptyQueueGetPriority_RaisesKeyError(self):
        priority_queue = PriorityQueue()
        
        with self.assertRaises(KeyError):
            priority_queue.get_priority("a")

    def test_PriorityQueue_ChangePriority_GetPriorityReturnsNewPriority(self):
        priority_queue = PriorityQueue()
        priority_queue.add("a", 0)
        
        priority_queue.change_priority("a", 5)
        
        p_a = priority_queue.get_priority("a")
        self.assertEquals(p_a, 5)
        
    def test_PriorityQueue_PopSmallerThan_ReturnsThePopedElements(self):
        priority_queue = PriorityQueue()        
        priority_queue.add("a", 2)
        priority_queue.add("b", 3)
        priority_queue.add("c", 1)
        priority_queue.add("d", 0)
        priority_queue.remove("c")
        priority_queue.add("c", 4)
        priority_queue.remove("b")
        priority_queue.add("e", 7)
        priority_queue.add("f", 5)
        priority_queue.add("g", 6)
        priority_queue.add("h", 10)

        l = priority_queue.pop_smaller_than(6)
        
        self.assertEquals(l, [('d', 0), ('a', 2), ('c', 4), ('f', 5)])
        self.assertEquals(list(priority_queue), [('g', 6), ('e', 7), ('h', 10)])

    def test_PriorityQueue_PopAllSmallerThan_LIstIsEmpty(self):
        priority_queue = PriorityQueue()        
        priority_queue.add("a", 2)
        priority_queue.add("b", 1)
        priority_queue.remove("b")

        l = priority_queue.pop_smaller_than(3)
        
        self.assertEquals(list(priority_queue), [])

if __name__ == '__main__':
    unittest.main()
    
