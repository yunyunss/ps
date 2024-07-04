from potato import Astar
import hashlib, json, os

with open("MAP.json", 'r') as f:
    map = json.load(f)

nodes = map["nodes"]
connections = map["connections"]

astar = Astar(nodes, connections, 0, 11)

Op = astar.arrowcmd() #받았다.

m = hashlib.sha256() #변환했다.
num1 = 0 #초기화
num2 = len(Op) - 1
#암호화
while num1 <= num2:
    with open("PATH.txt", "w") as f:
        for i in range(num2 + 1):
            m = hashlib.sha256()
            m.update(Op[num1].encode("utf-8"))
            f.write("{0}\n".format(m.hexdigest()))
            num1+=1
    num1+=1

os.system("python3 cherry.py")