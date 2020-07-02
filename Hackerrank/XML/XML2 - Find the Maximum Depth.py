import xml.etree.ElementTree as etree

#Set maxdepth to -1
maxdepth = -1

#Create recursive function to check depth of each child
def depth(elem, level):
    global maxdepth

    if (level == maxdepth):
        maxdepth += 1
    
    for child in elem:
        depth(child, level+1)
    

#Print maxdepth
if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
