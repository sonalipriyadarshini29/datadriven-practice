from collections import defaultdict

def hourly_event_counts(logs: list[tuple[str, str]]) -> dict[str, dict[str, int]]:
  output = defaultdict()
  if len(logs)==0:
    return output
  for log in logs:
    logkey = log[0][:13]
    if logkey in output:
      if log[1] in output[logkey]:
        output[logkey][log[1]] += 1
      else:
        output[logkey][log[1]] = 1
    else:
      output[logkey] = defaultdict()
      output[logkey][log[1]] = 1
  return output
      
    
