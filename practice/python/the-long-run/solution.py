def run_length_encoding(s: str):
  result = ""
  pointer, i = 0, 0
  s = s+'.'
  while i<len(s)-1:
    while s[pointer]==s[i]:
      i += 1
    result += s[i-1]
    result += str(i-pointer)
    pointer = i
  return result
