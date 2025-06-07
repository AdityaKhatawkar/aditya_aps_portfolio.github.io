import bisect

class AdSlot:
    def __init__(self, start, end, revenue):
        self.start = start
        self.end = end
        self.revenue = revenue

def latest_non_conflicting(slots, index):
    # Binary search to find the last ad that doesn't conflict with slot[index]
    lo, hi = 0, index - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if slots[mid].end <= slots[index].start:
            if slots[mid + 1].end <= slots[index].start:
                lo = mid + 1
            else:
                return mid
        else:
            hi = mid - 1
    return -1

def schedule_ads(slots):
    # Sort slots by end time
    slots.sort(key=lambda x: x.end)
    n = len(slots)
    
    # dp[i] stores max revenue including slots[0...i]
    dp = [0] * n
    dp[0] = slots[0].revenue
    for i in range(1, n):
        incl_profit = slots[i].revenue
        l = latest_non_conflicting(slots, i)
        if l != -1:
            incl_profit += dp[l]
        dp[i] = max(incl_profit, dp[i - 1])
    
    return dp[-1]

# Example usage
if __name__ == "__main__":
    ad_slots = [
        AdSlot(0, 3, 20),
        AdSlot(2, 5, 20),
        AdSlot(4, 6, 30),
        AdSlot(6, 9, 25),
        AdSlot(5, 8, 50)
    ]
    
    max_revenue = schedule_ads(ad_slots)
    print("Maximum Revenue from Scheduled Ads:", max_revenue)
