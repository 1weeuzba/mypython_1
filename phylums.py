class Living_orgamism:
    Alive = True
class Phylums(Living_orgamism):
    def porifera(self):
        print("This animal is a porifera. Their characters are::\n")
        characters = [
                "1) Non-motile, multicellular organisms with a hard outer skeleton.",
                "2) Have a porous body.",
                "3) Pores on the bodies create a canal system which helps in the circulation of substances.",
                "4) Not differentiated into head and tail; do not have a well-developed organ or organ system.", 
                "5) Include marine habitat."
        ]
        for i in characters:
            print(i)
    def coelenterata(self):
        print("This animal is a coelenterata. Their characters are::\n")
        characters = [
                "1)Have a hollow body cavity.",
                "2)The body is differentiated into two ends.",
                "3)Includes all aquatic animals.",
                "4)The body is made of two layers of cells: inner and outer linings.",
                "5)Live in colonies (corals) as well as solitary (Sea anemone)."
                ]
        for i in characters:
            print(i)
    def platyhelminthes(self):
        print("This animal is a platyhelminthes. Their characters are::\n")
        characters= [
            "1) Dorsoventrally flattened body.",
            "2) Complex and have differentiated body structure.",
            "3) Tissues are differentiated from three layers of cells and are triploblastic.",
            "4) Do not have a true internal cavity or coelom.",
            "5) Have bilateral symmetry.",
            "6) Either free-living (Planaria) or parasitic (liver flukes)."
            ]
        for i in characters:
            print(i)
    def nemathelminthes(self):
        print("This animal is a nemathelminthes. Their characters are::\n")
        characters = [
            "1) Nematodes have a cylindrical body.",
            "2) Bilaterally symmetrical and triploblastic.",
            "3) Have pseudocoelom, a false body cavity.",
            "4) Parasitic and causes diseases such as elephantiasis, ascariasis."
        ]
        for i in characters:
            print(i)
    def annelida(self):
        print("This animal is an annelida. Their characters are::\n")
        characters=[
            "1) Have a segmented cylindrical body.",
            "2) The body is differentiated into head and tail.",
            "3) Bilaterally symmetrical and triploblastic.",
            "4) Have a true body cavity.",
            "5) Habitat: marine, freshwater and land."
        ]
        for i in range(len(characters)-1):
            print(characters[i])
    def arthropoda(self):
        print("This animal is an arthropoda. Their characters are::\n")
        characters=[
            "1) They are bilaterally symmetrical.",
            "2) Have jointed appendages, exoskeleton and a segmented body.",
            "3) Have well-differentiated organ and organ system.",
            "4) Have an open circulatory system, but do not have differentiated blood vessels."
        ]
        for i in characters:
            print(i)
    def mollusca(self):
        print("This animal is a mollusca. Their characters are::\n")
        characters=[
            "1) Bilaterally symmetrical and triploblastic.",
            "2) Less segmented body.",
            "3) Well-developed organ and organ system.",
            "4) Typically, open circulatory system."
            "5) Limbs are present."
        ]
        for i in characters:
            print(i)
    def echinodermata(self):
        print("This animal is an echinodermata. Their characters are::\n")
        characters=[
            "1) Radial symmetry and triploblastic.",
            "2) Have true coelom.",
            "3) Have hard calcium carbonate skeleton structure.",
            "4) Free-living marine animals."
        ]
        for i in characters:
            print(i)
    def hemichordata(self):
        print("This animal is a hemichordata. Their characters are::\n")
        characters=[
            "1) The body is soft, fragile, and divided into a proboscis.",
            "2) The epidermis is single-layered.",
            "3) It comprises worm-like marine animals with an organ-system level of organization.",
            "4) They have an open circulatory system.",
            "5) They respire through gills since they are marine.",
            "6) They have separate sexes and external fertilization is seen.",
            "7) Development is direct."
        ]
        for i in characters:
            print(i)
    def chordata(self):
        print("This animal is a chordata. Their characters are::\n")
        characters=[
            "1) They are bilaterally symmetrical, triploblastic with an organ-system level of classification.",
            "2) They possess a notochord and a nerve cord.",
            "3) The circulatory system is closed type.",
            "4) Phylum Chordata can be divided into the following sub-phyla:\n\tUrochordata\n\tCephalochordata\n\tVertebrata"
            ]
        for i in characters:
            print(i)
print(Phylums.Alive)
info = Phylums()
match input("Enter the phylum:"):
    case 'chordata':
        info.chordata()
    case 'hemichordata':
        info.hemichordata()
    case 'echinodermata':
        info.echinodermata()
    case 'porifera':
        info.porifera()
    case 'platyhelminthes':
        info.platyhelminthes()
    case 'nemathelminthes':
        info.nemathelminthes()
    case 'coelenterata':
        info.coelenterata()
    case 'annelida':
        info.annelida()
    case 'arthropoda':
        info.arthropoda()
    case 'mollusca':
        info.mollusca()
    case _:
        print("There are only 9 phylums")