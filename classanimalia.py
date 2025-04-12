class Animalia:
    p1 = "Porifera"
    p2 = "Cnidaria"
    p3 = "Platyhelminthes"
    p4 = "Nematoda"
    p5 = "Annelida"
    p6 = "Mollusca"
    p7 = "Arthropoda"
    p8 = "Echinodermata"
    p9 = "Chordata"
    phyla = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
    def __init__(self, name, phylum):
        self.name = name
        self.phylum = phylum
        self.kingdom = "Animalia"
print("Sponge is a member of the phylum " , Animalia.phyla[0])
print("Hydra is a member of the phylum " , Animalia.phyla[1])
print("Planaria is a member of the phylum " , Animalia.phyla[2])
print("Roundworm is a member of the phylum " , Animalia.phyla[3])
print("Earthworm is a member of the phylum " , Animalia.phyla[4])
print("Octopus is a member of the phylum " , Animalia.phyla[5])
print("Ant is a member of the phylum " , Animalia.phyla[6])
print("Sea Urchin is a member of the phylum " , Animalia.phyla[7])
print("Human is a member of the phylum " , Animalia.phyla[8])