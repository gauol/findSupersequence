from collections import defaultdict # import potrzebnych bibliotek

def dijkSuperstring(originalSeqs): 
  paths = defaultdict(set)
  paths[0] =  { '' }
  while paths:
    minLength = min(paths.keys())
    while paths[minLength]:
      candidate = paths[minLength].pop()
      seqAdded = False
      for seq in originalSeqs:
        if seq in candidate:
          continue
        seqAdded = True
        for i in reversed(range(len(seq)+1)):
          if candidate.endswith(seq[:i]):
            newCandidate = candidate + seq[i:]
            paths[len(newCandidate)].add(newCandidate)
      if not seqAdded:  # nothing added, so all present?
        return candidate
    del paths[minLength]

def getSequences(inputFile):
    seqs = []
    with open(inputFile, "r") as f:
        for line in f:
            if line[0] == '>': continue
            seqs.append("".join(line.split()))
    return seqs

def saveToFile(result, outputFile):
    file = open(outputFile, 'w') 
    file.write(result) 
    file.close() 
    