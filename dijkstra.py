import queue
 
def dijkstra(adj, src):
    dist = [9999999999 for i in range(len(adj))]
    dist[src] = 0
    q = queue.PriorityQueue()
    q.put((0, src))
    while q.qsize() > 0:
        p = q.get()
        cost = p[0]
        here = p[1]
        if dist[here] < cost: continue
        for i in range(len(adj[here])):
            there = adj[here][i][0]
            nextDist = cost + adj[here][i][1]
            if dist[there] > nextDist:
                dist[there] = nextDist
                q.put((nextDist, there))
    return dist