#Q1 https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        opmap = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.itruediv}
        stack = []
        for t in tokens:
            if t.isdigit() or t[1:].isdigit():
                stack.append(int(t))
            else:
                a, b = stack.pop(), stack.pop()
                # for case 1/-22, in python it returns -1, here use itruediv to get a float then apply int() to get 0
                stack.append(int(opmap[t](b, a)))
        return stack[0]

    
#Q2 https://leetcode.com/problems/combination-sum-iii/

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.helper([],1,k,n)
        return self.result
    
    def helper(self,path,start,k,target):
        if k == 0 and target == 0:
            self.result.append(path)
            return 
        if k == 0 or target < 0:
            return
        for i in range(start, 10):
            if k-1 < 0:
                break
            self.helper(path + [i], i+1, k-1, target-i)

            
#Q3 https://leetcode.com/problems/bulls-and-cows/

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        a = 0
        b = 0
        x = []
        y = []
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
            else:
                x.append(secret[i])
                y.append(guess[i])
        for i in y:
            if i in x:
                b += 1
                x.remove(i)
        return "{}A{}B".format(a,b)
    
    
    
#Q4 https://leetcode.com/problems/rotate-function/

class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = sum(nums)
        base = 0
        for i in range(n):
            base += i*nums[i]
        x = base
        for i in range(1,n):
            y = base + s - nums[-i]*n
            x = max(x, y)
            base = y
        return x
    

    
#Q5 https://leetcode.com/problems/largest-divisible-subset/

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0: return []
        sol = []
        nums.sort()
        for i in nums:
            sol.append([i])
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]%nums[j] == 0 and len(sol[i]) < len(sol[j]) + 1:
                    sol[i] = sol[j] + [nums[i]]
        return max(sol, key=len)
    
    
    
#Q6 https://leetcode.com/problems/perfect-rectangle/

class Solution:
    def isRectangleCover(self, rectangles):
        
        area = 0
        corners = set()
        a = lambda: (Y-y) * (X-x)
        
        for x, y, X, Y in rectangles:
            area += a()
            corners ^= {(x,y), (x,Y), (X,y), (X,Y)}

        if len(corners) != 4: return False
        x, y = min(corners, key=lambda x: x[0] + x[1])
        X, Y = max(corners, key=lambda x: x[0] + x[1])
        return a() == area
    
#Q7 https://leetcode.com/problems/course-schedule/

class Solution(object):
    def canFinish(self,numCourses, prerequisites):
        hashmap = {i: [] for i in range(numCourses)}

        for prereq in prerequisites:
            hashmap[prereq[0]].append(prereq[1])

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if not hashmap[course]:
                return True
            visited.add(course)
            for prereq in hashmap[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            hashmap[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
    

    
#Q8 https://leetcode.com/problems/most-profitable-path-in-a-tree/

import math
from collections import deque, defaultdict
import sys
sys.setrecursionlimit(10**5) 
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        visited = set()
        self.lvl = 0
        self.sum = 0
        self.max = -math.inf
        def remove_bob_income(src, bob, lvl):
            if src == bob:
                self.lvl = lvl
                amount[bob] = 0
                return True
            visited.add(src)
            for child in graph[src]:
                if child not in visited:
                    ans = remove_bob_income(child, bob, lvl + 1)
                    if ans:
                        if self.lvl & 1 and lvl == (self.lvl + 1)//2:
                            amount[src] //= 2
                        elif lvl > (self.lvl // 2):
                            amount[src] = 0
                        else:
                            self.sum += amount[src]   
                        return True
            return False
        
            visited.remove(src)
        
        def dfs(src, income, visited):
            if len(graph[src]) == 1 and src != 0:
                self.max = max(self.max, income)
                return
            visited.add(src)
            for child in graph[src]:
                if child not in visited:
                    dfs(child, income + amount[child], visited)
            visited.remove(src)
                
        remove_bob_income(0, bob, 1)
        dfs(0, amount[0], set())
        return self.max
    
                         

#Q9 https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, A, B, diff):
        l = SortedList()
        res = 0
        for a,b in zip(A, B):
            res += l.bisect_right(a - b + diff)
            l.add(a - b)
        return res
    
    

#Q10 https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = sorted(nums)
        l = 0
        r = 0
        for i in range(len(nums)):
            if nums[i] != x[i]:
                l = i
                break
        for i in range(len(nums)-1, -1, -1):
            if nums[i] != x[i]:
                r = i+1
                break
        return r-l
    

    
    
#Q11 https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

class Solution:
    def countPaths(self, n, roads):
        G = defaultdict(list)
        for x, y, w in roads:
            G[x].append((y, w))
            G[y].append((x, w))

        dist = [float('inf')] * n
        dist[0] = 0
        cnt = [0]*n
        cnt[0] = 1
        heap = [(0, 0)]

        while heap:
            (min_dist, idx) = heappop(heap)
            if idx == n-1: return cnt[idx] % (10**9 + 7)
            for neib, weight in G[idx]:
                candidate = min_dist + weight
                if candidate == dist[neib]:
                    cnt[neib] += cnt[idx]

                elif candidate < dist[neib]:
                    dist[neib] = candidate
                    heappush(heap, (weight + min_dist, neib))
                    cnt[neib] = cnt[idx]
                    
                    

#Q12 https://leetcode.com/problems/longest-happy-prefix/

class Solution(object):
    def longestPrefix(self, s):
        j = -1
        p = [j]
        for c in s:
            while j >= 0 and s[j] != c:
                j = p[j]
            j += 1
            p.append(j)
        return s[:j]
    
    

#Q13 https://leetcode.com/problems/airplane-seat-assignment-probability/

class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        return 1.0000 if n == 1 else 0.5000

#Q14 https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/

class Solution(object):
    def hcf(self,x,y):
        while(y):
            x, y = y, x % y
        return abs(x)
    def minOperations(self, nums, numsDivide):
        """
        :type nums: List[int]
        :type numsDivide: List[int]
        :rtype: int
        """
        numsDivide.sort()
        gcd = numsDivide[0]
        for i in range(1,len(numsDivide)):
            gcd = self.hcf(numsDivide[i], gcd)
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > gcd:
                return -1
            if gcd%nums[i] == 0:
                return i
        return -1
    
    

#Q15 https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans, lo, cnt = 0, -1, {c : 0 for c in 'abc'}
        for hi, c in enumerate(s):
            cnt[c] += 1
            while all(cnt.values()):
                ans += len(s) - hi
                lo += 1
                cnt[s[lo]] -= 1
        return ans
