# Problem: implement a circular queue, where the last and first elements of
# its array are treated as continuous

class CircularQueue:
    def __init__(self, limit=10):
        self.queue = []
        self.limit = limit
        self.front = None
        self.back = None
        self.size = 0

    def is_empty(self):
        return self.size <= 0

    def clear_queue(self):
        self.queue = []
        self.front = self.back
        self.size = 0

    def enqueue(self, item):
        if self.size >= self.limit:
            print('**Queue overflow**')
            return
        else:
            self.queue.append(item)

        if self.front is None:
            self.front = self.back = self.size
            self.size += 1
        else:
            self.back = self.size
            self.size += 1
            print('Current queue:', self.queue)

    def dequeue(self):
        if self.size <= 0:
            print('**Queue is empty**')
            return
        else:
            print(f'"{self.queue.pop(0)}" dequeued successfully!')
            self.size -= 1
        if self.size == 0:
            self.front = self.back = None
        else:
            self.back = self.size - 1
            print('Current queue:', self.queue)

    def print(self):
        print(self.queue)


queue = CircularQueue(limit=5)
queue.enqueue(4)
queue.enqueue(3)

queue.print()

queue.dequeue()
queue.enqueue(6)
queue.dequeue()
queue.dequeue()

# dequeue from emty queue:
queue.dequeue()

# try to add to full queue:
for i in range(1, 7):
    queue.enqueue(i)
