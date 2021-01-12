import re
import sys

def readfile(fname):
    with open(fname, 'r') as infile:
        content = infile.readlines()
    return content


def readfile2(fname):
    with open(fname, 'r') as infile:
        content = infile.read()
    return content


def write_html(table,html):

    # type change table list(list) to a string
    str_table = "<table>"
    for r in table:
        str_table+='<tr>'
        for c in r:
            str_table+=c
        str_table+='</tr>'
    #print(str_table)
    str_table+='</table>'
    # remove table in html
    stop = html.find('<table')
    start = html.find('</table>')+len('</table>')
    #print(html[:stop]+html[start:])
    #print(html[stop:start])i
    t = html[stop:start]
    html= html.replace(t,str_table)

    with open('chess2.html','w') as outfile:
        outfile.write(html)



def display_html(board_html):
    # Print HTML for def readfile()
    #for lines in board_html:
    #    print(lines)#.replace('\n',''))

    # Print HTML for def readfile2()
    print(board_html)


def rm_tags(html):
    tag_re = "<[^>]+>"
    
    if type(html) ==str:
        tags = re.findall(tag_re, html)
        for t in range(0,len(tags)):
            html = html.replace(tags[t],'')
    
    elif type(html) == list:
        tags =[]
        tmp = []

        for i in html:
            tags = re.findall(tag_re, i)
            for t in range(0,len(tags)):
                i = i.replace(tags[t], '')
            tmp.append(i)
        html = tmp

    else:
        print('type error')
    return html

    
def get_elements(html,tag):
    elem = []
    ctag = '</' + tag.replace('<','') +'>'

    html = html.replace('\n','')

    #tag = tag.replace('<','').replace('/','').replace('>','')
    #print('tag:', tag)
    #tag_re = "<tr[^/>][^>]*>"
    #print('tag re:',tag_re)
    #tags = re.findall(tag_re,html)
    #for t in tags:
    #    print(t)

    # Get Num Tags
    num_tags = len(re.findall(tag,html))

    start = 0
    end = 0
    for t in range(0, num_tags):
        start = html.find(tag, t+start)
        end = html.find(ctag, t+end)+len(ctag)

        elem.append(html[start:end])


    return elem


#-#-#-#-#-#-#-#-#-
"""-- Main -- """
#-#-#-#-#-#-#-#-#-

# Get HTML Page
fname = 'html_chess.html'
board_html = readfile2(fname)


# Get HTML Table
print('start position of table:', board_html.find('<table>'))

rows = get_elements(board_html,'<tr')


# Could add this to the get_tags function and add an if-statement to check the type of arg1 to test if it's a string or a list. 
# or should I cast rows to a string type?
cnt = 0
for r in rows:
    col = get_elements(r, '<td')
    rows[cnt] = col
    cnt+=1

board = []
for r in rows:
    board.append(rm_tags(r))
#    print(r)


def clear_table(html):
    tag_re = "<[^>]+>"
    cnt=0
    for r in html:
        line = ''
        tags = re.findall(tag_re, r)
        for t in tags:
            line += t
        html[cnt]=line
        cnt+=1
    
    return html


def move_piece(t, p1, p2, d1, d2):
    piece = rm_tags(t[p1][p2])
    d_piece = rm_tags(t[d1][d2])
   
#    print('\n\n\n')
#    print(t)
    print('\npiece:', piece)
    print('destination piece:',d_piece)

    # Removes piece from destination position
    #if d_piece != '':
    #    t[d1][d2].replace(d_piece, '')

    # Get Tags of destination

    # move piece to destination position
    t[d1][d2] = t[d1][d2].replace(d_piece,piece)
    t[p1][p2] = t[p1][p2].replace(piece,d_piece)

    # Note can manipulate this to capture piece by removing piece of p and d_piece of d
    print('d = ', t[d1][d2])
    print('p = ', t[p1][p2])

    return t
"""
print('\n\n')
empty = []
for r in rows:
    empty.append(clear_table(r))

print(empty)
"""

print("\nHEREEEEE!!!!!!! BELOW \n")
table = move_piece(rows,2,3,1,3)
print(table)
write_html(table,board_html)
