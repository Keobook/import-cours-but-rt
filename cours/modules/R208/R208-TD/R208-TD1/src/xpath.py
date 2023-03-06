from lxml import etree
tree=etree.parse('notes.xml')
root=tree.getroot()
print('Racine:',root.tag)
print("Nombre d'élèves:",len(root))
# Q1
n=tree.xpath("/resultats/eleve[1]/note")
for x in n:
  print(f"Notes de {x.get('matiere')}: {x.text}")
# Q2
moy = tree.xpath("sum(//note) div count(//note)")
print(f"Moyenne générale: {moy:.4g}")
# Q3
e = tree.xpath("//eleve")
for x in e:
  print(f"Eleve {x.get('prenom')} {x.get('nom')}:")
  mat = set(x.xpath("./note/@matiere"))
  for m in mat:
    moy = x.xpath(f"sum(./note[@matiere='{m}']) div count(./note[@matiere='{m}'])")
    print(f"  Moyenne de {m}: {moy:.4f}")
