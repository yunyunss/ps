import math

class Astar():
    def __init__(self, nodes: list, connections: list, start: int, end: int):
        self.map = self.converter(nodes=nodes, connections=connections)
        self.nodes = nodes
        self.start = [start] + nodes[start]
        self.end = [end] + nodes[end]
    
    def converter(self, nodes: list, connections: list):
        mapbra = list()
        for i in range(len(nodes)):
            mapket = list()
            for j in range(len(nodes)):
                if [i, j] in connections or [j, i] in connections:
                    mapket.append(1)
                else:
                    mapket.append(0)
            mapbra.append(mapket)
        return mapbra
            
    def heuristic(self, start: list, target: list):
        return math.sqrt((start[0] - target[0]) ** 2 + (start[1] - target[1]) ** 2)

    def getPath(self):
        map = self.map
        nodes = self.nodes
        start = self.start
        end = self.end
        
        curnid = start[0]
        
        openlist = dict()
        closelist = dict()
        
        closelist[curnid] = [nodes[curnid][0], nodes[curnid][1]]
        
        while curnid != end[0]:
            openid = 0
            
            for i in map[curnid]:
                f = 0
                g = 0
                h = 0
                if i == 1 and not openid in openlist and not openid in closelist:
                    try:
                        g = closelist[curnid][3]
                    except:
                        pass
                    g += self.heuristic(nodes[curnid], [nodes[openid][0], nodes[openid][1]])
                    h = self.heuristic([nodes[openid][0], nodes[openid][1]], self.end[1:])
                    f = g + h
                    openlist[openid] = [nodes[openid][0], nodes[openid][1], f, g, h, curnid]
                elif openid in openlist and not openid in closelist:
                    try:
                        g = closelist[curnid][3]
                    except:
                        pass
                    g += self.heuristic(nodes[curnid], [nodes[openid][0], nodes[openid][1]])
                    if openlist[openid][3] > g:
                        h = self.heuristic([nodes[openid][0], nodes[openid][1]], self.end[1:])
                        f = g + h
                        openlist[openid] = [nodes[openid][0], nodes[openid][1], f, g, h, curnid]
                openid += 1
            
            key = 0
            min = -1
            
            for i in openlist.keys():
                if min == -1 or min[2] > openlist[i][2]:
                    key = i
                    min = openlist[i]
            
            closelist[key] = min
            del openlist[key]
            curnid = key
        
        result = list()
        
        for i in closelist:
            try:
                r = [i, closelist[i][5]]
            except:
                r = [i]
            result.append(r)
        
        result.reverse()
        
        p = result[0]
        r = list()
        r.append(result[0][0])
        
        for i in result:
            if p[1] == i[0]:
                r.append(i[0])
                p = i
        r.reverse()
        return r
    
    def arrowcmd(self):
        xy = self.getPath()
        
        result = list()
        
        for i in range(len(xy) - 1):
            xy1 = self.nodes[xy[i]]
            xy2 = self.nodes[xy[i + 1]]
            rightdistance = xy2[0] - xy1[0]
            frontdistance = xy2[1] - xy1[1]
            if abs(rightdistance) < abs(frontdistance):
                if frontdistance < 0:
                    result.append('b')
                else:
                    result.append('f')
            else:
                if rightdistance < 0:
                    result.append('l')
                else:
                    result.append('r')
        return result