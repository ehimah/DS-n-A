class DirectedGraph:
    def __init__(self):
        self.adj: dict[str, list] = {}
        self.indegs: dict[str, int] = {}

    def addEdge(self, v1: str, v2: str):
        if not v1 in self.adj:
            self.adj[v1] = []

        self.adj[v1].append(v2)
        self.indegs[v1] = self.indegs.get(v1, 0)
        self.indegs[v2] = self.indegs.get(v2, 0) + 1

    def hasCycles(self):
        def dfsHelper(adj: dict[str, list], source: str, visited: set, callStack: set):
            neighbours = adj[source]
            visited.add(source)
            callStack.add(source)
            for n in neighbours:
                # if it's not visited and has neighbours
                if n in callStack:
                    return True
                elif n not in visited and n in adj:
                    if dfsHelper(adj, n, visited, callStack):
                        return True
            return False

        visited = set()
        for n in self.adj:
            if n not in visited:
                if dfsHelper(self.adj, n, visited, set()):
                    return True
        return False

    def topologicalSort(self):
        '''
        store indegrees of every vertex
        create a q and all all zero indeg item to queue
        while q is not empty

        '''
        # get all items with zero indegrees
        q = [x for x in self.indegs.keys() if self.indegs[x] == 0]
        while q:
            n = q.pop(0)
            # visit here
            print(n)

            if n in self.adj:
                neighbours = self.adj[n]
                for x in neighbours:
                    indeg = self.indegs[x]
                    self.indegs[x] = indeg - 1
                    if indeg == 1:
                        # append this because indeg will become zero in next line
                        q.append(x)
