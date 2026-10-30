# Day 28 - Number of Recent Calls
**Topic:** Queue sliding time window

## Primary: Number of Recent Calls
**Approach:** Queue stores timestamps of all pings. On each new ping
append timestamp then remove all timestamps older than t-3000 from
the front. Queue length is the count of recent calls.

**Time:** O(1) amortized | **Space:** O(n)

**Edge case I caught:** Pop from front (oldest) not back. Queue is
FIFO so oldest timestamps are always at index 0.

## Variants

### Design Hit Counter (Same sliding window 300 seconds)
Same queue pattern. hit() just appends. getHits() removes timestamps
older than timestamp-300 then returns length.

### Logger Rate Limiter (Hashmap last print time)
Store last printed timestamp per message in dict. Allow print only
if message never printed or last print was 10+ seconds ago.