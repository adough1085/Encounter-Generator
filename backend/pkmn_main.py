from models.game import Game as Game

g = Game("Scarlet")
g.box = ["Crocalor","Clodsire","Gumshoos","Arrokuda","Klawf","Bombirdier", "Magikarp", "Gimmighoul","Azumarill","Oinkologne (Male)","Tauros (Combat Breed)", "Goomy","Basculin (Red-Striped)"]
g.print_box()
g.populate_dupes()
g.distribution("Great Crater of Paldea","Day","Flying",0,True)
g.generate("Great Crater of Paldea",1,"Flying",0,True)
#g.generate(8,1,"Flying",0)
#g.distribution(9,1,"Normal",0)
#g.generate(15,1,"Fairy",1)
g.locate("misdreavus", True)