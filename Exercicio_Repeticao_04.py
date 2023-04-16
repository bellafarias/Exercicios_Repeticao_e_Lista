PovoA = 80000
PovoA_taxa = 0.03
PovoB = 200000
PovoB_taxa = 0.015
anos = 0

while PovoA < PovoB:
    anos = anos +1
    PovoA = PovoA * (PovoA_taxa +1)
    PovoB = PovoB * (PovoB_taxa +1)
print("Serão necessários",anos, "anos para que a população a Ultrapasse a população B")