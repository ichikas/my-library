from heapq import heappush, heappop


def dijkstra(graph: list, start: int) -> list:
    INF = 10**18
    pq = []
    cur = [INF] * len(graph)
    cur[start] = 0
    heappush(pq, (cur[start], start))
    while pq:
        min_cost, pos = heappop(pq)
        if cur[pos] < min_cost:
            continue
        for nv, nc in graph[pos]:
            if cur[nv] > cur[pos] + nc:
                cur[nv] = cur[pos] + nc
                heappush(pq, (cur[nv], nv))
    return cur
