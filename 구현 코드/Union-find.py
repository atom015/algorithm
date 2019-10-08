#재귀함수를 통해 부모노드를 찾고 부모노드를 갱신한다.
def getParent(p,x):
    if p[x] == x:
        return x
    p[x] = getParent(p,p[x])
    return p[x]
#두노드를 비교하고 더작은 부모노드를 두개의노드의 부모노드로 만든다.
def unionParent(p,a,b):
    a = getParent(p,a)
    b = getParent(p,b)
    if a < b:
        p[b] = a
    else:
        p[a] = b
#두 원소가 같은 집합에 포함되어 있는지를 확인한다.
def findParent(p,a,b):
    a = getParent(p,a)
    b = getParent(p,b)
    if a == b:
        return 1
    return 0
