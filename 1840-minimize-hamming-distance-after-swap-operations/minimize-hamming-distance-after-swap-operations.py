class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        
        parent= list(range(len(source)))
        def find(x):
            if parent[x]!=x:
                parent[x]=find (parent[x])
            return parent[x]

        def union(x,y):
            px,py=find(x),find(y)
            if px!=py:
                parent[py]=px

        for a,b in allowedSwaps:
            union(a,b)

        from collections import defaultdict,Counter

        groups = defaultdict(list)
        for i in range(len(source)):
            root=find(i)
            groups[root].append(i)
        res =0
        for i in groups.values():
            count = Counter(source[j] for j in i)
            for j in i:
                if count[target[j]]>0:
                    count[target[j]]-=1
                else :
                    res+=1
 

        return res
