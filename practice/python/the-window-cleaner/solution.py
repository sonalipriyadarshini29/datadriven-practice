def longest_unique_substr(s):
  count = 0
  l = 0
  hashset = set()
  for r in range(len(s)):
    if s[r] in hashset:
      while s[l] != s[r]:
        hashset.remove(s[l])
        l += 1
      l += 1
    else:
      hashset.add(s[r])
    count = max(count, len(hashset))
  return count
