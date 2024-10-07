class Line:
    def __init__(self):
        self.elements = []
        self.current_student = 1
    
    def call_student(self):
        self.current_student += 1
        return self.current_student - 1
    
    def add_student(self, move):
        index = len(self.elements) - move
        self.elements = self.elements[0:index] + [self.call_student()] + self.elements[index:len(self.elements)]

line = Line()

n = int(input())
[line.add_student(i) for i in list(map(int, input().split()))]

print(*line.elements)