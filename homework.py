class Item:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        node = Item(value)

        if self.is_empty():
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node

        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")

        value = self.first.value
        self.first = self.first.next

        if self.first is None:
            self.last = None

        self.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.first.value

    def __len__(self):
        return self.size

    def __str__(self):
        if self.is_empty():
            return "[]"

        data = []
        current = self.first

        while current:
            data.append(str(current.value))
            current = current.next

        return "[" + " <- ".join(data) + "]"


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, value):
        node = Item(value)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")

        value = self.top.value
        self.top = self.top.next
        self.size -= 1

        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.top.value

    def __len__(self):
        return self.size

    def __str__(self):
        if self.is_empty():
            return "[]"

        data = []
        current = self.top

        while current:
            data.append(str(current.value))
            current = current.next

        return "[" + " -> ".join(data) + "]"


class DItem:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def append_left(self, value):
        node = DItem(value)

        if self.is_empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.size += 1

    def append_right(self, value):
        node = DItem(value)

        if self.is_empty():
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        self.size += 1

    def pop_left(self):
        if self.is_empty():
            raise IndexError("Дек пуст")

        value = self.head.value

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1
        return value

    def pop_right(self):
        if self.is_empty():
            raise IndexError("Дек пуст")

        value = self.tail.value

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1
        return value

    def peek_left(self):
        if self.is_empty():
            raise IndexError("Дек пуст")
        return self.head.value

    def peek_right(self):
        if self.is_empty():
            raise IndexError("Дек пуст")
        return self.tail.value

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        if self.is_empty():
            return "[]"

        result = []
        current = self.head

        while current:
            result.append(str(current.value))
            current = current.next

        return "[ " + " <-> ".join(result) + " ]"

    def __iter__(self):
        current = self.head

        while current:
            yield current.value
            current = current.next

    def reverse(self):
        current = self.tail

        while current:
            yield current.value
            current = current.prev


if __name__ == "__main__":

    print("=" * 40)
    print("ОЧЕРЕДЬ")
    print("=" * 40)

    q = Queue()

    print("Добавляем: 10, 20, 30")
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print(q)
    print("Размер:", len(q))
    print("Первый:", q.peek())

    print("\nУдалили:", q.dequeue())
    print(q)

    print("Удалили:", q.dequeue())
    print(q)

    print("Размер:", len(q))

    print("\n" + "=" * 40)
    print("СТЕК")
    print("=" * 40)

    s = Stack()

    print("Добавляем: 100, 200, 300")
    s.push(100)
    s.push(200)
    s.push(300)

    print(s)
    print("Размер:", len(s))
    print("Вершина:", s.peek())

    print("\nУдалили:", s.pop())
    print(s)

    print("Удалили:", s.pop())
    print(s)

    print("Размер:", len(s))

    print("\n" + "=" * 40)
    print("ПРИМЕРЫ")
    print("=" * 40)

    print("\nFIFO")

    queue_test = Queue()

    for i in range(5):
        queue_test.enqueue(i)
        print(f"Добавили {i}: {queue_test}")

    while not queue_test.is_empty():
        print(f"Извлекли {queue_test.dequeue()}: {queue_test}")

    print("\nLIFO")

    stack_test = Stack()

    for i in range(5):
        stack_test.push(i)
        print(f"Добавили {i}: {stack_test}")

    while not stack_test.is_empty():
        print(f"Извлекли {stack_test.pop()}: {stack_test}")

    print("\n" + "=" * 50)
    print("ДЕК")
    print("=" * 50)

    d = Deque()

    print("\nДобавление:")

    d.append_right(10)
    print(d)

    d.append_right(20)
    print(d)

    d.append_left(5)
    print(d)

    d.append_left(1)
    print(d)

    print("\nРазмер:", len(d))
    print("Слева:", d.peek_left())
    print("Справа:", d.peek_right())

    print("\nУдаление:")

    print("Слева:", d.pop_left())
    print(d)

    print("Справа:", d.pop_right())
    print(d)

    print("Справа:", d.pop_right())
    print(d)

    print("Слева:", d.pop_left())
    print(d)

    print("\nДек как очередь")

    dq_queue = Deque()

    for i in range(5):
        dq_queue.append_right(i)

    print(dq_queue)

    while not dq_queue.is_empty():
        print(f"{dq_queue.pop_left()} -> {dq_queue}")

    print("\nДек как стек")

    dq_stack = Deque()

    for i in range(5):
        dq_stack.append_right(i)

    print(dq_stack)

    while not dq_stack.is_empty():
        print(f"{dq_stack.pop_right()} -> {dq_stack}")

    print("\nПалиндром")

    def palindrome(text):
        temp = Deque()

        for ch in text.lower():
            if ch.isalnum():
                temp.append_right(ch)

        while len(temp) > 1:
            if temp.pop_left() != temp.pop_right():
                return False

        return True

    words = [
        "А роза упала на лапу Азора",
        "racecar",
        "hello",
        "12321",
        "Python"
    ]

    for word in words:
        print(f'"{word}" -> {"Да" if palindrome(word) else "Нет"}')

    print("\nИтераторы")

    demo = Deque()

    for num in [10, 20, 30, 40, 50]:
        demo.append_right(num)

    print(demo)
    print(list(demo))
    print(list(demo.reverse()))

    print("\nОчистка")

    print("До:", demo, len(demo))
    demo.clear()
    print("После:", demo, len(demo))

    print("\nОшибки")

    empty = Deque()

    try:
        empty.pop_left()
    except IndexError as err:
        print(err)

    try:
        empty.pop_right()
    except IndexError as err:
        print(err)