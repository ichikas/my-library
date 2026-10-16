"""
有向グラフを O(E + V) で強連結成分分解する。
出力されるリストはトポロジカルソートされている。
"""


def SCC(graph: list[list[int]]) -> list[list[int]]:
    n = len(graph)
    rev_graph = [[] for _ in range(n)]
    for v in range(n):
        for u in graph[v]:
            rev_graph[u].append(v)

    used = [False] * n
    order = []
    for u in range(n):
        if used[u]:
            continue

        s = [u]
        used[u] = True
        while s:
            v = s.pop()
            if v < 0:
                order.append(-v - 1)
                continue

            s.append(-v - 1)
            for nv in graph[v]:
                if used[nv]:
                    continue
                used[nv] = True
                s.append(nv)
    order.reverse()

    res = []
    used = [False] * n
    for u in order:
        if used[u]:
            continue

        s = [u]
        used[u] = True
        grp = []
        while s:
            v = s.pop()
            grp.append(v)
            for nv in rev_graph[v]:
                if used[nv]:
                    continue
                used[nv] = True
                s.append(nv)
        res.append(grp)

    return res
