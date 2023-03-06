import xml.etree.ElementTree as ET
eleves=['John DOE','Jean DUPONT','Alice MARTIN']
notes=[{'math':[14,13,12],'physique':[12,15],'français':[17,15]},
        {'math':[11,9,12],'physique':[13,15],'français':[12,10]},
        {'math':[8,10,9],'physique':[11,9],'français':[15,16]}]

root = ET.Element("racine")
for e in eleves:
	eleve = ET.Element('eleve')
	eleve.set('name', e)
	root.append(eleve)

	for n in notes:
		for matiere,note in n.items():
			for no in note:
				el = ET.Element('note')
				el.set('matiere', matiere)
				el.text = str(no)
				eleve.append(el)

tree=ET.ElementTree(root)
ET.indent(tree,space='  ',level=0)
tree.write('notes2.xml',encoding='utf-8',xml_declaration=True)
