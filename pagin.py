# encoding: utf-8
import re

totalpages = 0

def est_lineno(line):
  lineno = len(line.decode("utf-8"))
  print "%d %s" % (lineno, line)
  count = int(lineno/30)
  if lineno % 30 != 0:
    count += 1
  return count

def pagination(fn, outfile, indexfile, threshold = 25):
  pgcount = 0
  chapcount = 0
  chapno = '0'
  secno = '0'

  chapre = re.compile('(第.*?章)(.*)')
  secre = re.compile('第(.*?)节')

  with open(fn, 'rb') as f:
    wordcount = 0
    linecount = 0
    currentlines = []
    for line in f:
      line = line.rstrip().lstrip()
      m = chapre.match(line)
      if m:
        if currentlines:
          writepage(outfile, currentlines, pgcount, chapno, secno)
          currentlines = []
          wordcount = 0
          linecount = 0
        chapno = line
        secno = '0'
        chapcount += 1
        outfile.write('<section class="slide" id="chap%d">\n' % chapcount)
        #outfile.write('<img src="images/decorate.png" width="50px" id="decorator-top"/>\n')
        outfile.write('<div id="decorator-top"><img src="images/decorate.png" width="120px"/></div>\n')
        outfile.write('<div id="decorator-bottom"><img src="images/decorate-bottom.png" width="120px"/></div>\n')
        outfile.write('<h1>%s<br>%s</h1>\n' % (m.group(1),m.group(2)))
        outfile.write('</section>\n')
        indexfile.write('<p><a href="#chap%d">%s</a></p>\n' % (chapcount, chapno))
        continue

      m = secre.match(line)
      if m:
        if currentlines:
          writepage(outfile, currentlines, pgcount, chapno, secno)
          currentlines = []
          wordcount = 0
          linecount = 0
        pgcount = 1
        secno = line
        continue

      if chapno == '0' or secno == '0':
        continue

      wordcount += len(line)
      currentlines.append(line.rstrip())
      linecount += 1
      if linecount > threshold:
        writepage(outfile, currentlines, pgcount, chapno, secno)
        pgcount += 1
        currentlines = []
        wordcount = 0
        linecount = 0
  outfile.close()

def writepage(outfile, lines, pgcount, chapno, secno):
  global totalpages
  outfile.write('<section class="slide" id="pg%d">\n' % totalpages)
  totalpages += 1
  outfile.write('<h2>%s:%s</h2>\n' % (chapno, secno))

  paragraph = ""
  for l in lines:
    if l=="":
      outfile.write('  <p>\n')
      outfile.write('  '+paragraph)
      outfile.write('  </p>\n')
      paragraph = ""
    else:
      paragraph = paragraph + l
  if paragraph != "":
    outfile.write('  <p>\n')
    outfile.write('  '+paragraph)
    outfile.write('  </p>\n')

  outfile.write('</section>\n')

if __name__ == '__main__':
  pagination('novel2.txt', file('novel.html', 'wb'), file('toc.html', 'wb'))
