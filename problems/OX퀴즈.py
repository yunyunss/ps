class counter:
    all_score = []
    
    def __init__(self, report):
        self.score = 0
        self.grade(report)
        self.regist(self.score)
    
    def grade(self, report):
        temp = 0
        for i, v in enumerate(list(report)):
            if v == 'O':
                temp += 1
            elif v == 'X':
                self.score += int(temp * (1 + temp) / 2)
                temp = 0
        self.score += int(temp * (1 + temp) / 2)
                
    @classmethod
    def regist(cls, score):
        cls.all_score.append(score)

n = int(input())

for i in range(n):
    counter(input())
    
for i in counter.all_score:
    print(i)