import heapq
import collections

class QueueEmpty(Exception):
    pass

class DuplicateKeyError(Exception):
    pass

class Item(object):
    def __init__(self, elm, priority, removed=False):
        self.elm = elm
        self.priority = priority
        self.removed = removed
        
    def __str__(self):
        return "<Item %s priority:%s removed:%s>" % (self.elm, self.priority, self.removed) 

    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

class PriorityQueue(object):
    ''' PriorityQueue with support for removal and __contains__
        Based on heapq.
    '''
        
    def __init__(self):
        self.queue = []
        self.itemdict = {}
    
    def add(self, elm, priority=0):
        """ Add an element 'elm' to to priority queue with priority 'priority' 
            raises DuplicateKeyError if the element is allready present.
        """
        if (elm in self.itemdict and not self.itemdict[elm].removed):
            raise DuplicateKeyError("Item allready present" )
        item = Item(elm, priority)
        heapq.heappush(self.queue, item)
        self.itemdict[elm] = item
    
    def remove(self, elm):
        if (elm not in self.itemdict):
            raise QueueEmpty("element %s not found" % str(elm))
        if (elm == self.queue[0].elm):
            heapq.heappop(self.queue)
            self._cleanup_deleted()
        else:
            self.itemdict[elm].removed = True
        del self.itemdict[elm]

    def _cleanup_deleted(self):
        while (len(self.queue) > 0 and (self.queue[0].removed)):
            heapq.heappop(self.queue)
    
    def get_priority(self, elm):
        if elm not in self.itemdict:
            raise KeyError("not found")
        return self.itemdict[elm].priority
    
    def change_priority(self, elm, new_priority):
        self.remove(elm)
        self.add(elm, new_priority)
                   
    def __contains__(self, elm):
        return ((elm in self.itemdict) and (not self.itemdict[elm].removed))

    def __iter__(self):
        for item in sorted(self.queue):
            if not item.removed:
                yield item.elm, item.priority

    def __len__(self):
        return (len(self.itemdict))

    def _head(self):
        if (len(self) == 0):
            raise QueueEmpty("not element found")
        return self.queue[0]
    
    def peek(self):
        """Returns a tulpe of (elm, pri) containing the element with the lowest priority and its priority.
           Raises QueueEmpty if the Queue is empty.
        """
        head = self._head()
        return (head.elm, head.priority)

    def pop(self):
        """Returns a tulpe of (elm, pri) containing the element with the lowest priority and its priority,
           and removes the element from the priority queue.
           Raises QueueEmpty if the Queue is empty.
        """
        item, priority = self.peek()
        self.remove(item)
        return (item, priority)

    def __str__(self):
        elms_str = ",".join(["(%s,%d)" % (elm, priority) for elm, priority in self])
        return "<PriorityQueue[%s]>" % (elms_str)

    def pop_smaller_than(self, priority):
        """Returns a list of tulpes (pri, elm). The list contains the elements with the priority lower than 'priority'
           and their associated priority.
           The elements are removed from the priority queue.
        """
        result = []
        while (len(self.queue) > 0 and self.peek()[1] < priority):
            result.append(self.pop())
        return (result)


if __name__ == "__main__":
    print Item("a", 2) < Item("fe", 1)