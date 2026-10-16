"""
ダイクストラ法。非負重み付きの無向 or 有向グラフの単一始点最短経路を O(ElogV) で求める。
ある頂点に到達する前の頂点を記録する配列を追加で持つことで最短経路の復元も可能。
有向グラフの場合, グラフの辺を全て反転させてから適用することで単一終点最短経路を求められる（応用例：s → t → s の最短経路）。
"""

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
