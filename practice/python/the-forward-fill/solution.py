def forward_fill(values: list) -> list:
  nonNull = None
  result = []
  for i in range(len(values)):
    if values[i]!=None:
      nonNull = values[i]
    result.append(nonNull)
  return result
