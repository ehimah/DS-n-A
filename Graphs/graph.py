class Graph:
    def __init__(self) -> None:
        self.adj: dict[str, list[str]] = {}

    def addEdge(self, v1, v2):
        if not v1 in self.adj:
            self.adj[v1] = []

        if not v2 in self.adj:
            self.adj[v2] = []

        self.adj[v1].append(v2)
        self.adj[v2].append(v1)
        return self

    def removeEdge(self, v1, v2):
        if v1 in self.adj:
            if v2 in self.adj[v1]:
                self.adj[v1].remove(v2)

        if v2 in self.adj:
            if v1 in self.adj[v2]:
                self.adj[v2].remove(v1)

    def bfs(self, start: str):
        visited = set[str]()
        q = [start]

        while q:
            curr = q.pop(0)
            if curr in visited:
                continue
            visited.add(curr)
            print(curr)
            neighbours = list(self.adj[curr])
            q.extend(neighbours)

    def bfsDiscon(self):
        visited = set()
        for curr in self.adj.keys():
            if curr in visited:
                continue
            q = [curr]
            while q:
                n = q.pop(0)
                visited.add(n)
                print(n)
                neighbours = self.adj[n]
                for n in neighbours:
                    if n not in visited:
                        q.append(n)
                        visited.add(n)

    def countConnectedComponents(self):
        visited = set()
        count = 0
        for curr in self.adj.keys():
            if curr in visited:
                continue
            count += 1
            q = [curr]
            while q:
                n = q.pop(0)
                visited.add(n)
                # print(n)
                neighbours = self.adj[n]
                for n in neighbours:
                    if n not in visited:
                        q.append(n)
                        visited.add(n)
        return count

    def dfs(self, source):
        visited = set()
        self.dfsHelper(source, visited)

    def dfsCountConnectedComponents(self):
        count = 0
        visited = set()
        for x in self.adj:
            if x not in visited:
                count += 1
                self.dfsHelper(x, visited)
        return count

    def dfsHelper(self, source, visited: set):
        if source in visited:
            return

        print(source)
        visited.add(source)
        neighbours = self.adj[source]
        for n in neighbours:
            if n not in visited:
                self.dfsHelper(n, visited)
        return

    def shortestDistance(self, source):
        visited = set()

        distance = {x: float('inf') for x in self.adj}
        distance[source] = 0

        # BFS
        q = [source]
        visited.add(source)
        while q:
            curr = q.pop(0)
            neighbours = self.adj[curr]

            for u in neighbours:
                if u not in visited:
                    distance[u] = distance[curr] + 1
                    visited.add(u)
                    q.append(u)
        return distance

    def hasCycles(self):
        def helper(adj, source, parent, visited: set):
            if source in visited:
                return

            visited.add(source)
            neighbours = adj[source]
            for n in neighbours:
                if n not in visited:
                    if helper(adj, n, source, visited):
                        return True
                elif n != parent:
                    # we have encountered a previously visited
                    # node that isn't the source (parent) node
                    return True
            return False
        visited = set()
        for n in self.adj:
            if n not in visited:
                if helper(self.adj, n, None, visited):
                    return True
        return False
