class node:
    def __init__(self, value:any=None):
        self.value:any = value
        self.next:node = None
    
    def __str__(self): # 자기자신의 value와 next node의 value를 문자열로 반환한다.
        return f"{self.value}\n{self.next}"
    
    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value
        return self
    
    def getNext(self): # next node를 반환한다.
        return self.next
    
    def setNext(self, nextNode): # next node를 설정한다.
        self.next = nextNode
        return self