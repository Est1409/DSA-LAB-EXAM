# for question 1

def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev
def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original List:")
print_list(head)

# test the given example
reversed_head = reverse_linked_list(head)
print("Reversed List:")
print_list(reversed_head)









# for question number 2


def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
# test the given example
nums = [2, 7, 11, 15]
target = 9
print("Indices of the two numbers:", two_sum(nums, target))










# for question number 3 


class CircularQueue:
    def __init__(self, k):
        self.queue = [None] * k
        self.max_size = k
        self.head = self.tail = -1

    def enqueue(self, value):
        if (self.tail + 1) % self.max_size == self.head:
            print("Queue is full")
            return
        if self.head == -1:
            self.head = 0
        self.tail = (self.tail + 1) % self.max_size
        self.queue[self.tail] = value

    def dequeue(self):
        if self.head == -1:
            print("Queue is empty")
            return None
        result = self.queue[self.head]
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.max_size
        return result

    def front(self):
        if self.head == -1:
            return None
        return self.queue[self.head]

    def rear(self):
        if self.tail == -1:
            return None
        return self.queue[self.tail]

    def is_empty(self):
        return self.head == -1
# test the given example

q = CircularQueue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Dequeued item:", q.dequeue())
q.enqueue(4)
print("Front item:", q.front())
print("Rear item:", q.rear())








#for question number 4

def greater_integer(number_list, max_element):
    if max_element in number_list:
        print("The largest number is:", max_element)
    else:
        print("The largest number is not in the list.")
# test the given example
number_list = [1, 2, 3, 4, 5]
greater_integer(number_list, max(number_list))








# for question number 5

def reverse_string(s):
    stack = list(s)
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    return reversed_string
# test the given example
s = "hello"
print("Reversed string:", reverse_string(s))