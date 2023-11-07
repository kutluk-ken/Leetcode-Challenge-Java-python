def bfs(n, m, edges, s):
    allNodesEdgeList = [[] for i in range(n)]

    for edg in edges:
        allNodesEdgeList[edg[0]-1].append(edg[1]-1)
        allNodesEdgeList[edg[1]-1].append(edg[0]-1)
        
    visitedNodes=[False]*n
    visitedNodes[s-1]=True

    que = [s-1]

    ret = [-1]*n
    ret[s-1]=0

    while len(que)>0:
        crntNd=que.pop(0)
        nbrsCrntNd = allNodesEdgeList[crntNd]

        for j in range(len(nbrsCrntNd)):
            if not visitedNodes[nbrsCrntNd[j]]:
                visitedNodes[nbrsCrntNd[j]]=True
                que.append(nbrsCrntNd[j])
                ret[nbrsCrntNd[j]]=6+ret[crntNd]
                
    ret.remove(0)
    return ret
