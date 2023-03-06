from lxml import etree
tree=etree.parse('notes.xml')
root=tree.getroot()
print('Racine:',root.tag)
print("Nombre d'élèves:",len(root))
