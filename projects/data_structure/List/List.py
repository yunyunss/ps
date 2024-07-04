"""
Linked List를 구현한 python 문서이다.
"""
from Node import node        

def sizeUp(func):
    """
    sizeUp함수는 요소를 추가하는 함수를 실행시킬 때 데코레이터로 사용되어 해당 함수가 실행된 클래스의 size요소를 1 증가시킨다.
    """
    def wrapper(self, *args, **kwargs):
        func(self, *args, **kwargs)
        self.size += 1
    
    return wrapper
def sizeDown(func):
    """
    sizeDown함수는 요소를 삭제하는 함수를 실행시킬 때 데코레이터로 사용되어 해당 함수가 실행된 클래스의 size요소를 1 감소시킨다.
    """
    def wrapper(self, *args, **kwargs):
        func(self, args, kwargs)
        self.size -= 1
    return wrapper

class myList:
    def __init__(self):
        self.head:node = node("head")
        self.size = 0
        self.errors = {"IndexError": [Exception("IndexError: list index out of range")]}
        
    def __str__(self) -> str: # 클래스 속 필드의 값을 string으로 반환
        return f"values: {self.toList()}\nsize: {self.size}"
    
    def toList(self): # 요소들을 List로 반환하는 함수
        return str(self.head).split('\n')[1:-1]
    
    def find(self, index:int, isNode:bool=False) -> any:
        """find함수는 입력받은 위치의 노드 혹은 노드의 value를 반환한다

        Args:
            index (int): 반환할 노드의 위치
            isNode (bool, optional): 노드로 반환할지 노드의 value를 반환할지 정한다. Defaults to False.

        Raises:
            Exception: index의 값이 리스트의 범위를 벗어났을 때 발생한다.

        Returns:
            any: 반환하는 노드의 value
        """
        if self.size <= index:
            raise Exception("리스트의 크기보다 요청된 인덱스의 크기가 클 수 없다.")
        
        result = self.head.getNext()
        for i in range(index):
            result = result.getNext()
        
        if not isNode: # node형으로 반환할지 value를 반환할지 결정
            return result.getValue()
        else:
            return result
        
    @sizeUp
    def append(self, value:any):
        """리스트의 맨 끝에 요소를 추가한다

        Args:
            value (any): 추가할 요소의 value
        """
        if self.size == 0:
            self.head.setNext(node(value))
        else:
            self.head.setNext(self.find(self.size-1, True).setNext(node(value)))
    
    @sizeUp
    def insert(self, index:int, value:node):
        """선택한 위치에 요소를 삽입한다.

        Args:
            index (int): 요소를 삽입할 위치
            value (node): 삽입할 요소

        Raises:
            Exception: index의 값이 리스트의 범위를 벗어났을 때 발생한다.
        """
        if self.size == index:
            self.append(value)
        elif self.size < index:
            raise self.errors["Index"][0]
        
        newNode = node(value).setNext(self.find(index, True))
        newNode = self.find(index-1, True).setNext(newNode) if index != 0 else newNode
        self.head.setNext(newNode)
        
    @sizeDown
    def deleteElement(self, index:int):
        """선택한 위치의 요소를 제거한다.

        Args:
            index (int): 제거한 요소의 위치
        """
        if self.size < index:
            raise self.errors["Index"][0]

if __name__ == "__main__":
    List = myList()
    List.append(3)
    List.append(7)
    List.insert(0, 1)
    print(List.toList())