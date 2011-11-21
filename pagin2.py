# encoding: utf-8

def split_width(lines, pagewidth=30):
  paras = []
  for line in lines:
    line = line.rstrip().lstrip()
    if len(line) == 0:
      continue
    line = line.decode('utf-8')

    para = []
    for k in range(0, len(line), pagewidth):
      para.append(line[k:pagewidth+k].encode('utf-8'))
    paras.append(para)
  return paras

def split_function(paras, func):
  array = []
  content = []
  match = None
  for para in paras:
    new_match = func(para)
    if new_match:
      if match:
        array.append(dict(match=match, content=content))
        content = []
      match = new_match
    else:
      content.append(para)
  return array

def split_chapters(paras):
  chapre = re.compile('第(.*?)章(.*)')
  def chapter_func(para):
    m = chapre.match(para[0])
    if m:
      return (para[0], m.group(1), m.group(2))
    elif para[0]=='引子':
      return (para[0], para[0], "")
    return None
  chapters = split_function(paras, chapter_func)
  return chapters

def split_section(chapter):
  secre = re.compile('第(.*?)节')
  def section_func(para):
    m = secre.match(para[0])
    if m:
      return para[0]
    return None
  sections = split_function(chapter['content'], section_function)
  return sections

slidepages = []
def print_chapters(chapters):
  global slidepages

  for index, chap in enumerate(chapters):
    content = StringIO()
    content.write('<div id="decorator-top"><img src="images/decorate.png" width="120px"/></div>\n')
    content.write('<div id="decorator-bottom"><img src="images/decorate-bottom.png" width="120px"/></div>\n')
    content.write('<h1>%s<br>%s</h1>\n' % (chap['match'][1], chap['match'][2]))
    slidepages.append(dict(id="chap%d" % index, content=content.getvalue()))
    print_sections(chap['content'], chap['match'][0])

def print_sections(sections, chapname):
  global slidepages

  for index, section in enumerate(sections):
    section_name = section['match']



def main():
  with open('novel.txt', 'rb') as f:
    lines = f.read()

  paras = split_width(lines)
  chapters = split_chapters(paras)

  for chap in chapters:
    sections = split_section(chap)
    for sec in sections:
      print_pages(chap, sec)


pagewidth = 31

outfile = open('novel2.txt', 'wb')
with open('novel.txt', 'rb') as f:
  for line in f:

outfile.close()

