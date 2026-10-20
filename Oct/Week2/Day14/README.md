# Day 14 - Contains Duplicate II
**Topic:** Sliding window + hashmap

## Primary: Contains Duplicate II
**Approach:** Maintain a sliding window of size k using a set. Right
pointer expands the window. When window exceeds size k remove the
leftmost element and move left pointer right. Before adding the new
right element check if it already exists in the window. If yes
duplicate within range k found.

**Time:** O(n) | **Space:** O(k)

**Key difference from Day 2:** Day 2 used a dict storing positions.
Day 14 uses a sliding window set — only elements within distance k
are kept in the set at any time.

## Variants

### Contains Duplicate (Revisited from Day 2 - set membership)
Same as Day 2 primary. Walk through array checking set before adding.
Revisited here to compare approaches — Day 2 was about any duplicate,
Day 14 primary is about duplicate within distance k.

### Longest Continuous Subarray With Absolute Diff <= Limit
Variable sliding window. Expand right. When max minus min in window
exceeds limit shrink from left. Find max and min manually each time
since deque and heapq are forbidden. Returns maximum window size.

### Maximum Number of Vowels in Substring of Given Length
Fixed sliding window of size k. Build first window counting vowels.
Slide one step at a time - add new right character if vowel, remove
old left character if vowel. Track maximum vowel count seen.

### Find All Anagrams in a String
Fixed sliding window of size len(p). Build frequency dicts for p and
first window of s. Slide window comparing dicts at each step. Add
new right char to window count, remove old left char. When dicts
match record starting index.