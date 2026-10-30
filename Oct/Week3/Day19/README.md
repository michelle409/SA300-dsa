# Day 19 - Isomorphic Strings
**Topic:** Bijective hashmap (two dicts, both directions)

## Primary: Isomorphic Strings
**Approach:** Map s->t and t->s simultaneously. For each position check
if the current mapping is consistent with what was stored. One-way
mapping isn't enough — "foo"→"bar" would pass s->t but fails t->s
because b and a both map to different chars in s.

**Time:** O(n) | **Space:** O(1)

**Edge case I caught:** Need both directions. s->t alone lets two
different chars in s map to the same char in t.

## Variants

### Word Pattern (Same bijection at word level)
Identical logic to primary but maps pattern chars to full words instead
of chars to chars. Split sentence first to get word list.

### Find and Replace Pattern (Check each word against pattern)
Apply the same bijection check as primary to each word in the list.
Collect words that match the pattern. Helper function keeps it clean.

### Buddy Strings (See Day 17)
Already covered.

### Rotate String (See Day 17)
Already covered.

### Groups of Special-Equivalent Strings (Signature by even/odd positions)
Two strings are special-equivalent if you can swap chars at even
positions among themselves and odd positions among themselves to make
them equal. Sort even-indexed and odd-indexed chars separately, join
as signature, count unique signatures.