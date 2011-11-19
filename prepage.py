# encoding: utf-8
pagewidth = 31

outfile = open('novel2.txt', 'wb')
with open('novel.txt', 'rb') as f:
  for line in f:
    line = line.rstrip().lstrip()
    if len(line) == 0:
      continue
    line = line.decode('utf-8')
    for k in range(0, len(line), pagewidth):
      outfile.write(line[k:pagewidth+k].encode("utf-8"))
      outfile.write('\n')
    outfile.write('\n')

outfile.close()

