from pythonds.graphs import Graph
def buildGraph():
    d = {}
    g = Graph()
    wfile = open("test","r")
    text = wfile.readline()
    for line in text:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 == word2:
                    g.addEdge(word1,word2)
    wfile.close()
    return g
