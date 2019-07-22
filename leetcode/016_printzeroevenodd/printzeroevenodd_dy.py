import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.tick = 1
        self.hold = True
        self.cond = threading.Condition()

	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            with self.cond:
                self.cond.wait_for(lambda: self.hold)
                printNumber(0)
                self.hold = False
                self.cond.notify_all()



    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(2, self.n+1, 2):
            with self.cond:
                self.cond.wait_for(lambda: self.tick % 2 == 0 and not self.hold)
                printNumber(self.tick)
                self.tick += 1
                self.hold = True
                self.cond.notify_all()


    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(1, self.n+1, 2):
            with self.cond:
                self.cond.wait_for(lambda: self.tick % 2 == 1 and not self.hold)
                printNumber(self.tick)
                self.tick += 1
                self.hold = True
                self.cond.notify_all()

