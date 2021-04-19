
from LinkedLists.LinkedList import LinkedList
from Trees.Trie import Trie
from Graphs.Graph import Graph
from Graphs.DirectedGraph import DirectedGraph
from LinkedLists.LRUCache import LRUCache


def runTrie():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"]
    output = ["Not present in trie",
              "Present in trie"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} ---- {}".format("the", t.search("the")))
    print("{} ---- {}".format("these", t.search("these")))
    print("{} ---- {}".format("their", t.search("their")))
    print("{} ---- {}".format("thaw", t.search("thaw")))


def runGraph():
    # g = Graph()
    # g.addEdge('A', 'B')
    # g.addEdge('B', 'F')
    # g.addEdge('G', 'H')
    # g.addEdge('I', 'J')
    # g.addEdge('A', 'C')
    # g.addEdge('C', 'D')
    # g.addEdge('C', 'E')
    # g.addEdge('D', 'E')

    # print(g.dfsCountConnectedComponents())
    # g.removeEdge('A','B')
    # g.removeEdge('A','C')
    # g.removeEdge('C','D')
    # g.removeEdge('C','E')
    # g.removeEdge('D','E')

    g2 = Graph()
    g2.addEdge(0, 1)
    g2.addEdge(0, 2)
    g2.addEdge(1, 3)
    g2.addEdge(2, 3)
    g2.addEdge(3, 4)
    g2.addEdge(4, 5)
    g2.addEdge(4, 6)
    # print(g2.shortestDistance(0))
    print(g2.hasCycles())


def runDirectedGraph():
    g = DirectedGraph()

    # g.addEdge('0', '1')
    g.addEdge('2', '3')
    g.addEdge('3', '4')
    g.addEdge('4', '5')
    g.addEdge('5', '6')
    # g.addEdge('6', '4')

    # print(g.hasCycles())
    g.topologicalSort()


def runLRUCache():
    cache = LRUCache(10)
    items = [12, 23, 34, 45, 56, 10, 50, 10, 10, 12]
    for item in items:
        print('GET: ', item)
        cache.get(item)
        cache.print()
        print('--------------')

def runLinkedListMergeSorted():
    l1 = LinkedList.fromList([4, 5, 6, 7])
    l2 = LinkedList.fromList([1, 2, 3, 10, 12])

    curr = LinkedList.mergeSorted(l1.head, l2.head)

    while curr:
        print(curr.value)
        curr = curr.next

def main():
    runLinkedListMergeSorted()


main()
