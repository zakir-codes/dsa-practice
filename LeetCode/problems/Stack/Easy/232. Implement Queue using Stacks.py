class MyQueue:
    ## solution 1
    def __init__(self):
        self.input, self.out =[],[]

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.out.pop()

    def peek(self) -> int:
        if not self.out:
            while self.input:
                self.out.append(self.input.pop())
        return self.out[-1]

    def empty(self) -> bool:
        return not self.input and not self.out
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
