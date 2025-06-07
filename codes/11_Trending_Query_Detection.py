import math
class Query:
    def __init__(self, l, r, idx):
        self.l = l; self.r = r; self.idx = idx
def mos_algorithm(arr, queries):
    block = int(math.sqrt(len(arr)))
    queries.sort(key=lambda q: (q.l//block, q.r))
    curL, curR, distinct = 0, -1, 0
    cnt = {}
    res = [0]*len(queries)
    for q in queries:
        while curR < q.r:  # expand right
            curR += 1
            cnt[arr[curR]] = cnt.get(arr[curR],0) + 1
            if cnt[arr[curR]] == 1:
                distinct += 1
        while curR > q.r:  # shrink right
            cnt[arr[curR]] -= 1
            if cnt[arr[curR]] == 0:
                distinct -= 1
            curR -= 1
        while curL < q.l:  # shrink left
            cnt[arr[curL]] -= 1
            if cnt[arr[curL]] == 0:
                distinct -= 1
            curL += 1
        while curL > q.l:  # expand left
            curL -= 1
            cnt[arr[curL]] = cnt.get(arr[curL],0) + 1
            if cnt[arr[curL]] == 1:
                distinct += 1
        res[q.idx] = distinct
    return res

# Example usage:
views_log = [1,2,1,3,2,1]  # video IDs over time
queries = [Query(0,3,0), Query(2,5,1)]
print(mos_algorithm(views_log, queries))  # distinct counts for each query
