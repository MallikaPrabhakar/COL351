#Alice's graduation party

#algorithm: remove the people who either know >all-5 or <5

from sortedcontainers import sortedset

def adjList(vertices, edges):
    graph=dict()
    print("graph blank initialised")
    for i in vertices:
        graph[i]=[]
    print("added keys and empty value pairs")
    for i in edges:
        graph.get(i[0],{}).add(i[1])
        graph.get(i[1],{}).add(i[0])
    print("graph ready")
    return(graph)

def deletePerson(person,graph,vertices):
    for neighbour in graph[person]:
        graph[neighbour].remove(person)
        if len(graph[neighbour]) == 0:
            del graph[neighbour]
    del graph[person]


def invitees(vertices, graph):
    print("sending invitations!")
    n=len(vertices)
    size=n
    person=0
    iterProgress=True
    while(iterProgress):
        iterProgress=False
    peopleInvited=[]
    for i in vertices:
        peopleInvited.append(i)
    print("Only",len(peopleInvited), "called, remaining were not suitable")
    print(peopleInvited)

def dining():
    print("i don't get paid enough for this")

def getVertices(n):
    string=input().strip()
    vertices=list(map(int,string.split()))
    if (len(vertices)!=n):
        print("wrong input but ok")
    else:
        print("vertices ready!")
    return vertices

def getEdges(m):
    edges=[]
    for i in range(m):
        temp=list(map(int,input().split()))
        edges.append(temp)
    if (len(edges)!=m):
        print("I did something wrong oops")
    else:
        print("edges ready!")
    return edges

n,m=tuple(map(int,input().split()))
vertices=getVertices(n)
edges=getEdges(m)
graph=adjList(vertices, edges)
invitees(vertices,graph)
dining()
