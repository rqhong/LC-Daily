class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        visited = set()
        def dfs(k):
            if k in visited:
                return
            visited.add(k)
            for key in rooms[k]:
                dfs(key)
        
        dfs(0)

        return len(visited) == len(rooms) 