#Alice's graduation party

#algorithm: remove the people who either know >all-5 or <5 

def adjList(vertices, edges):
    graph=dict()
    print("graph blank initialised")
    for i in vertices:
        graph[i]=[]
    print("added keys and empty value pairs")
    for i in edges:
        graph.get(i[0],[]).append(i[1])
    print("graph ready")
    return(graph)

def deletePerson(person,graph,vertices):
    graph[person]=[]
    for i in vertices:
        temp=graph[i]
        try:
            temp.remove(person)
        except:
            continue


def invitees(vertices, graph):
    print("sending invitations!")
    n=len(vertices)
    size=n
    person=0
    iterProgress=True
    while(iterProgress):
        iterProgress=False
        person=0
        while(person<n):
            temp=len(graph[vertices[person]])
            if temp==0:
                person+=1
                continue
            if (temp<5 or temp>size-5):
                #sets the value of key vertices[person] as [] and removes the edge wherever it is present
                deletePerson(vertices[person], graph, vertices)  
                size-=1
                iterProgress=True
            person+=1
    peopleInvited=[]
    for i in vertices:
        if graph[i]!=[]:
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