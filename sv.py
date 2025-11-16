import random

class Game:
    def __init__(self, game):
        self.game = game.strip().lower().capitalize()
        self.areas = []
        self.box = []
        self.dupes = []
        f = open("paldea_dex.txt", "r")
        self.pokedex = f.readlines()
        f.close()
        for x in range(len(self.pokedex)):
            self.pokedex[x] = self.pokedex[x][0:len(self.pokedex[x])-1].strip()
        
        self.links = []
        self.links.append([self.pokedex[0],self.pokedex[1],self.pokedex[2]]) # Meowscarada
        self.links.append([self.pokedex[3],self.pokedex[4],self.pokedex[5]]) # Skeledirge
        self.links.append([self.pokedex[6],self.pokedex[7],self.pokedex[8]]) # Quaquaval
        self.links.append([self.pokedex[9],"Oinkologne (Male)","Oinkologne (Female)"]) # Oinkologne
        self.links.append([self.pokedex[11],self.pokedex[12]]) # Spidops
        self.links.append([self.pokedex[13],self.pokedex[14]]) # Lokix
        self.links.append([self.pokedex[15],self.pokedex[16],self.pokedex[17]]) #Jumpluff
        self.links.append([self.pokedex[18],self.pokedex[19],self.pokedex[20]]) #Talonflame
        self.links.append([self.pokedex[21],self.pokedex[22],self.pokedex[23]]) #Pawmot
        self.links.append([self.pokedex[24],self.pokedex[25]]) #Houndoom
        self.links.append([self.pokedex[26],self.pokedex[27]]) #Gumshoos
        self.links.append([self.pokedex[28],self.pokedex[29]]) #Greedent
        self.links.append([self.pokedex[30],self.pokedex[31]]) #Sunflora
        self.links.append([self.pokedex[32],self.pokedex[33]]) #Kricketune
        self.links.append([self.pokedex[34],self.pokedex[35],self.pokedex[36]]) #Vivillon
        self.links.append([self.pokedex[37],self.pokedex[38]]) #Vespiquen
        self.links.append([self.pokedex[39],self.pokedex[40],self.pokedex[41]]) #Corviknight
        self.links.append([self.pokedex[42],self.pokedex[43],self.pokedex[44]]) #Blissey
        self.links.append([self.pokedex[45],self.pokedex[46],self.pokedex[47]]) #Azumarill
        self.links.append([self.pokedex[48],self.pokedex[49]]) #Masquerain
        self.links.append([self.pokedex[50],self.pokedex[51]]) #Floatzel
        self.links.append([self.pokedex[52],self.pokedex[53]]) #Clodsire
        self.links.append([self.pokedex[54],self.pokedex[55]]) #Golduck
        self.links.append([self.pokedex[56],self.pokedex[57]]) #Drednaw
        self.links.append([self.pokedex[58],self.pokedex[59],self.pokedex[60]]) #Wigglytuff
        self.links.append([self.pokedex[61],self.pokedex[62],self.pokedex[63],self.pokedex[64]]) #Gardevoir/Gallade
        self.links.append([self.pokedex[65],self.pokedex[66]]) #Hypno
        self.links.append([self.pokedex[67],self.pokedex[68],self.pokedex[69]]) #Gengar
        self.links.append([self.pokedex[70],self.pokedex[71]]) #Maushold
        self.links.append([self.pokedex[72],self.pokedex[73],self.pokedex[74]]) #Raichu
        self.links.append([self.pokedex[75],self.pokedex[76]]) #Dachsbun
        self.links.append([self.pokedex[77],self.pokedex[78],self.pokedex[79]]) #Slaking
        self.links.append([self.pokedex[80],self.pokedex[81],self.pokedex[82]]) # Tsareena
        self.links.append([self.pokedex[83],self.pokedex[84],self.pokedex[85]]) # Arboliva
        self.links.append([self.pokedex[86],self.pokedex[87]]) # Sudowoodo
        self.links.append(["Rockruff (Standard)", "Rockruff (Own Tempo)","Lycanroc (Midday)","Lycanroc (Midnight)","Lycanroc (Dusk)"]) # Lycanroc
        self.links.append([self.pokedex[90],self.pokedex[91],self.pokedex[92]]) # Coalossal
        self.links.append([self.pokedex[93],self.pokedex[94],self.pokedex[95]]) # Luxray
        self.links.append([self.pokedex[96],self.pokedex[97],self.pokedex[98]]) # Staraptor
        self.links.append(["Oricorio (Pom-Pom Style)","Oricorio (Baile Style)"]) # Oricorio
        self.links.append([self.pokedex[100],self.pokedex[101],self.pokedex[102]]) # Ampharos
        self.links.append([self.pokedex[103],self.pokedex[104]]) # Lilligant
        self.links.append([self.pokedex[105],self.pokedex[106]]) # Breloom
        self.links.append([self.pokedex[107],self.pokedex[108],self.pokedex[109]]) # Appletun
        self.links.append([self.pokedex[110],self.pokedex[111]]) # Grumpig
        self.links.append([self.pokedex[112]]) # Squawkabilly
        self.links.append([self.pokedex[113]+" (Violet)",self.pokedex[114]+" (Violet)"]) # Mismagius
        self.links.append([self.pokedex[115],self.pokedex[116]]) # Hariyama
        self.links.append([self.pokedex[117],self.pokedex[118]]) # Crabominable
        self.links.append([self.pokedex[119],self.pokedex[120]]) # Salazzle
        self.links.append([self.pokedex[121],self.pokedex[122]]) # Donphan
        self.links.append([self.pokedex[123],self.pokedex[124]]) # Copperajah
        self.links.append([self.pokedex[125],self.pokedex[126],self.pokedex[127]]) # Garchomp
        self.links.append([self.pokedex[128],self.pokedex[129],self.pokedex[130]]) # Garganacl
        self.links.append([self.pokedex[131],self.pokedex[132]]) # Pelipper
        self.links.append([self.pokedex[133],self.pokedex[134]]) # Gyarados
        self.links.append([self.pokedex[135],self.pokedex[136]]) # Barraskewda
        self.links.append(["Basculin (Red-Striped)","Basculin (Blue-Striped)"]) # Basculin
        self.links.append([self.pokedex[138]+" (Violet)",self.pokedex[139]+" (Violet)"]) # Swalot
        self.links.append([self.pokedex[140],self.pokedex[141]]) # Persian
        self.links.append([self.pokedex[142]+" (Scarlet)",self.pokedex[143]+" (Scarlet)"]) # Drifblim
        self.links.append([self.pokedex[144],self.pokedex[145],self.pokedex[146]]) # Florges
        self.links.append([self.pokedex[147],self.pokedex[148]]) # Dugtrio
        self.links.append([self.pokedex[149]]) # Torkoal
        self.links.append([self.pokedex[150],self.pokedex[151]]) # Camerupt
        self.links.append([self.pokedex[152],self.pokedex[153]]) # Bronzong
        self.links.append([self.pokedex[154],self.pokedex[155],self.pokedex[156]]) # Haxorus
        self.links.append([self.pokedex[157],self.pokedex[158],self.pokedex[159]]) # Annihilape
        self.links.append([self.pokedex[160],self.pokedex[161]]) # Medicham
        self.links.append([self.pokedex[162],self.pokedex[163]]) # Lucario
        self.links.append([self.pokedex[164],self.pokedex[165]+" (Scarlet)",self.pokedex[166]+" (Violet)"]) # Armarouge / Ceruledge
        self.links.append([self.pokedex[167],self.pokedex[168]]) # Whiscash
        self.links.append([self.pokedex[169],self.pokedex[170]]) # Bellibolt
        self.links.append([self.pokedex[171],self.pokedex[172],self.pokedex[173]]) # Goodra
        self.links.append([self.pokedex[174],self.pokedex[175]]) # Toxicroak
        self.links.append([self.pokedex[176],self.pokedex[177]]) # Kilowattrel
        self.links.append([self.pokedex[178],self.pokedex[179],self.pokedex[180],self.pokedex[181],self.pokedex[182],self.pokedex[183],self.pokedex[184],self.pokedex[185],self.pokedex[186]]) # Eevee
        self.links.append([self.pokedex[187],self.pokedex[188]]) # Dudunsparce
        self.links.append([self.pokedex[189],self.pokedex[190]]) # Sawsbuck
        self.links.append([self.pokedex[191],self.pokedex[192]]) # Farigarif
        self.links.append([self.pokedex[193],self.pokedex[194]]) # Muk
        self.links.append([self.pokedex[195],self.pokedex[196]]) # Mabosstif
        self.links.append([self.pokedex[197],self.pokedex[198]]) # Toxtricity
        self.links.append([self.pokedex[199]]) # Dedenne
        self.links.append([self.pokedex[200]]) # Pachirisu
        self.links.append([self.pokedex[201],self.pokedex[202]]) # Grafaiai
        self.links.append([self.pokedex[203]]) # Stantler
        self.links.append([self.pokedex[204],self.pokedex[205]]) # Amoongus
        self.links.append([self.pokedex[206],self.pokedex[207]]) # Electrode
        self.links.append([self.pokedex[208],self.pokedex[209],self.pokedex[210]]) # Magnezone
        self.links.append([self.pokedex[211]]) # Ditto
        self.links.append([self.pokedex[212],self.pokedex[213]]) # Arcanine
        self.links.append([self.pokedex[214],self.pokedex[215]]) # Ursaring
        self.links.append([self.pokedex[216]]) # Zangoose
        self.links.append([self.pokedex[217]]) # Seviper
        self.links.append([self.pokedex[218],self.pokedex[219]]) # Altaria
        self.links.append([self.pokedex[220],self.pokedex[221]]) # Gogoat
        self.links.append(["Tauros (Combat Breed)", "Tauros (Blaze Breed) (Scarlet)","Tauros (Aqua Breed) (Violet)"]) # Tauros
        self.links.append([self.pokedex[223],self.pokedex[224]]) # Pyroar
        self.links.append([self.pokedex[225]+" (Scarlet)",self.pokedex[226]+" (Scarlet)"]) # Skuntank
        self.links.append([self.pokedex[227],self.pokedex[228]]) # Zoroark
        self.links.append([self.pokedex[229],self.pokedex[230]]) # Weavile
        self.links.append([self.pokedex[231],self.pokedex[232]]) # Honchkrow
        self.links.append([self.pokedex[233],self.pokedex[234],self.pokedex[235]]) # Gothitelle
        self.links.append([self.pokedex[236],self.pokedex[237]]) # Polteageist
        self.links.append([self.pokedex[238]]) # Mimikyu
        self.links.append([self.pokedex[239]]) # Klefki
        self.links.append([self.pokedex[240]]) # Indeedee
        self.links.append([self.pokedex[241],self.pokedex[242]]) # Brambleghast
        self.links.append([self.pokedex[243],self.pokedex[244]]) # Toedscruel
        self.links.append([self.pokedex[245]]) # Tropius
        self.links.append([self.pokedex[246],self.pokedex[247]]) # Lurantis
        self.links.append([self.pokedex[248]]) # Klawf
        self.links.append([self.pokedex[249],self.pokedex[250]]) # Scovillain
        self.links.append([self.pokedex[251],self.pokedex[252]]) # Cacturne
        self.links.append([self.pokedex[253],self.pokedex[254]]) # Rabsca
        self.links.append([self.pokedex[255],self.pokedex[256]]) # Venomoth
        self.links.append([self.pokedex[257],self.pokedex[258]]) # Forretress
        self.links.append([self.pokedex[259],self.pokedex[260]]) # Scizor
        self.links.append([self.pokedex[261]]) # Heracross
        self.links.append([self.pokedex[262],self.pokedex[263]]) # Espathra
        self.links.append([self.pokedex[264],self.pokedex[265]]) # Hippowdon
        self.links.append([self.pokedex[266],self.pokedex[267],self.pokedex[268]]) # Krookodile
        self.links.append([self.pokedex[269],self.pokedex[270]]) # Sandaconda
        self.links.append([self.pokedex[271],self.pokedex[272]]) # Mudsdale
        self.links.append([self.pokedex[273],self.pokedex[274]]) # Volcarona
        self.links.append([self.pokedex[275]+" (Violet)",self.pokedex[276]+" (Violet)",self.pokedex[277]+" (Violet)"]) # Salamence
        self.links.append([self.pokedex[278],self.pokedex[279],self.pokedex[280]]) # Tinkaton
        self.links.append([self.pokedex[281],self.pokedex[282],self.pokedex[283]]) # Hatterene
        self.links.append([self.pokedex[284],self.pokedex[285],self.pokedex[286]]) # Grimmsnarl
        self.links.append([self.pokedex[287],self.pokedex[288]]) # Wugtrio
        self.links.append([self.pokedex[289]]) # Bombirdier
        self.links.append([self.pokedex[290],self.pokedex[291]]) # Palafin
        self.links.append([self.pokedex[292],self.pokedex[293]]) # Revavroom
        self.links.append([self.pokedex[294]]) # Cyclizar
        self.links.append([self.pokedex[295]]) # Orthworm
        self.links.append([self.pokedex[296]]) # Sableye
        self.links.append([self.pokedex[297],self.pokedex[298]]) # Banette
        self.links.append([self.pokedex[299]]) # Falinks
        self.links.append([self.pokedex[300]]) # Hawlucha
        self.links.append([self.pokedex[301]]) # Spiritomb
        self.links.append([self.pokedex[302],self.pokedex[303]]) # Noivern
        self.links.append([self.pokedex[304]+" (Violet)",self.pokedex[305]+" (Violet)",self.pokedex[306]+" (Violet)"]) # Dragapult
        self.links.append([self.pokedex[307],self.pokedex[308]]) # Glimmora
        self.links.append([self.pokedex[309]]) # Rotom
        self.links.append([self.pokedex[310],self.pokedex[311]]) # Houndstone
        self.links.append([self.pokedex[312]+" (Scarlet)"]) # Oranguru
        self.links.append([self.pokedex[313]+" (Violet)"]) # Passimian
        self.links.append([self.pokedex[314]]) # Komala
        self.links.append([self.pokedex[315]+" (Scarlet)",self.pokedex[316]+" (Scarlet)",self.pokedex[317]+" (Scarlet)"]) # Tyranitar
        self.links.append([self.pokedex[318]+" (Scarlet)"]) # Stonjourner
        self.links.append([self.pokedex[319]+" (Violet)"]) # Eiscue
        self.links.append([self.pokedex[320]]) # Pincurchin
        self.links.append([self.pokedex[321],self.pokedex[322]]) # Palossand
        self.links.append([self.pokedex[323],self.pokedex[324],self.pokedex[325]]) # Slowbro / Slowking
        self.links.append([self.pokedex[326],self.pokedex[327]]) # Cloyster
        self.links.append([self.pokedex[330]]) # Qwilfish
        self.links.append([self.pokedex[331]]) # Luvdisc
        self.links.append([self.pokedex[332],self.pokedex[333]]) # Lumineon
        self.links.append([self.pokedex[334]]) # Bruxish
        self.links.append([self.pokedex[335]]) # Alomomola
        self.links.append([self.pokedex[336]+" (Scarlet)",self.pokedex[337]+" (Scarlet)"]) # Dragalge
        self.links.append([self.pokedex[338]+" (Violet)",self.pokedex[339]+" (Violet)"]) # Clawitzer
        self.links.append([self.pokedex[340],self.pokedex[341],self.pokedex[342]]) # Eelektross
        self.links.append([self.pokedex[343],self.pokedex[344]]) # Toxapex
        self.links.append([self.pokedex[345]]) # Flamigo
        self.links.append([self.pokedex[346],self.pokedex[347],self.pokedex[348]]) # Dragonite
        self.links.append([self.pokedex[349],self.pokedex[350]]) # Frosmoth
        self.links.append([self.pokedex[351],self.pokedex[352]]) # Abomasnow
        self.links.append([self.pokedex[353]]) # Delibird
        self.links.append([self.pokedex[354],self.pokedex[355]]) # Beartic
        self.links.append([self.pokedex[356],self.pokedex[357],self.pokedex[358]]) # Glalie / Froslass
        self.links.append([self.pokedex[359]]) # Cryogonal
        self.links.append([self.pokedex[360],self.pokedex[361]])  # Cetitan
        self.links.append([self.pokedex[362],self.pokedex[363]]) # Avalugg
        self.links.append([self.pokedex[364],self.pokedex[365]]) # Braviary
        self.links.append([self.pokedex[366],self.pokedex[367],self.pokedex[368]]) # Kingambit
        self.links.append([self.pokedex[369]+" (Scarlet)",self.pokedex[370]+" (Scarlet)",self.pokedex[371]+" (Scarlet)"]) # Hydreigon
        self.links.append([self.pokedex[372]]) # Veluza
        self.links.append([self.pokedex[373]]) # Dondozo
        self.links.append([self.pokedex[374]]) # Tatsugiri
        self.links.append([self.pokedex[375]+" (Scarlet)"]) # Great Tusk
        self.links.append([self.pokedex[376]+" (Scarlet)"]) # Scream Tail
        self.links.append([self.pokedex[377]+" (Scarlet)"]) # Brute Bonnet 
        self.links.append([self.pokedex[378]+" (Scarlet)"]) # Flutter Mane 
        self.links.append([self.pokedex[379]+" (Scarlet)"]) # Slither Wing 
        self.links.append([self.pokedex[380]+" (Scarlet)"]) # Sandy Shocks 
        self.links.append([self.pokedex[381]+" (Violet)"]) # Iron Treads
        self.links.append([self.pokedex[382]+" (Violet)"]) # Iron Bundle
        self.links.append([self.pokedex[383]+" (Violet)"]) # Iron Hands
        self.links.append([self.pokedex[384]+" (Violet)"]) # Iron Jugulis
        self.links.append([self.pokedex[385]+" (Violet)"]) # Iron Moth
        self.links.append([self.pokedex[386]+" (Violet)"]) # Iron Thorns
        self.links.append([self.pokedex[387],self.pokedex[388],self.pokedex[389]]) # Baxcalibur
        self.links.append([self.pokedex[390],self.pokedex[391]]) # Gholdengo
        self.links.append([self.pokedex[392]]) # Wo-Chien
        self.links.append([self.pokedex[393]]) # Chien-Pao
        self.links.append([self.pokedex[394]]) # Ting-Li
        self.links.append([self.pokedex[395]]) # Chi-Yu
        self.links.append([self.pokedex[396]+" (Scarlet)"]) # Roaring Moon
        self.links.append([self.pokedex[397]+" (Violet)"]) # Iron Valiant
        self.links.append([self.pokedex[398]+" (Scarlet)"]) # Koraidon
        self.links.append([self.pokedex[399]+" (Violet)"]) # Miraidon

    def dupe_out(self):
        found = False
        for boxed_mon in self.box:
            for link in self.links:
                for pkmn in link:
                    if boxed_mon.strip().lower() == pkmn.strip().lower():
                        found = True
                    if found == True:
                        for x in link:
                            self.dupes.append(x)
                        break
                if found == True:
                    found = False
                    break 

    def generate(self, pkmn_set_int, area, time, type, power):
        pkmn_set = {}
        area_chosen = -1
        daypart = ""
        if pkmn_set_int == 1:
            pkmn_set = alphabetical
        elif pkmn_set_int == 0:
            pkmn_set = chronological
        else:
            print("0 = chronological")
            print("1 = alphabetical")
            return None

        if 1 <= area and area <= 30:
            area_chosen = area
        else:
            print("Areas 1-30")
            return None

        if time == 0:
            daypart = "Dawn"
        elif time == 1:
            daypart = "Day"
        elif time == 2:
            daypart = "Dusk"
        elif time == 3:
            daypart = "Night"
        else:
            print("0 = Dawn")
            print("1 = Day")
            print("2 = Dusk")
            print("3 = Night")
            return None
        
        pkmn_set[area_chosen].generate(self.game,daypart,type,power,self.dupes)

    def distribution(self, pkmn_set_int, area, time, type, power):
        pkmn_set = {}
        area_chosen = -1
        daypart = ""
        if pkmn_set_int == 1:
            pkmn_set = alphabetical
        elif pkmn_set_int == 0:
            pkmn_set = chronological
        else:
            print("0 = chronological")
            print("1 = alphabetical")
            return None

        if 1 <= area and area <= 30:
            area_chosen = area
        else:
            print("Areas 1-30")
            return None

        if time == 0:
            daypart = "Dawn"
        elif time == 1:
            daypart = "Day"
        elif time == 2:
            daypart = "Dusk"
        elif time == 3:
            daypart = "Night"
        else:
            print("0 = Dawn")
            print("1 = Day")
            print("2 = Dusk")
            print("3 = Night")
            return None
        
        pkmn_set[area_chosen].distribution(self.game, daypart,type,power,self.dupes)

    def locate(self, pkmn_set_int, pkmn):
        if pkmn_set_int == 1:
            pkmn_set = alphabetical
        elif pkmn_set_int == 0:
            pkmn_set = chronological
        else:
            print("0 = chronological")
            print("1 = alphabetical")
            return None
        
        habitats = []
        for x in range(len(pkmn_set)):
            pkmn_found = False
            dawn_found = False
            day_found = False
            dusk_found = False
            night_found = False
            for k in pkmn_set[x+1].dawn.keys():
                if k.lower().find(pkmn.lower().strip()) != -1:
                    pkmn_found = True
                    break
            if pkmn_found == False:
                continue
            elif pkmn_found == True:
                for k in pkmn_set[x+1].dawn.keys():
                    if k.lower().find(pkmn.lower().strip()) == -1:
                        continue
                    if pkmn_set[x+1].dawn[k] > 0:
                        dawn_found = True
                        break
                for k in pkmn_set[x+1].day.keys():
                    if k.lower().find(pkmn.lower().strip()) == -1:
                        continue
                    if pkmn_set[x+1].day[k] > 0:
                        day_found = True
                        break
                for k in pkmn_set[x+1].dusk.keys():
                    if k.lower().find(pkmn.lower().strip()) == -1:
                        continue
                    if pkmn_set[x+1].dusk[k] > 0:
                        dusk_found = True
                        break
                for k in pkmn_set[x+1].night.keys():
                    if k.lower().find(pkmn.lower().strip()) == -1:
                        continue
                    if pkmn_set[x+1].night[k] > 0:
                        night_found = True
                        break
            if (dawn_found == True) and (day_found == True) and (dusk_found == True) and (night_found == True):
                habitats.append(pkmn_set[x+1].name)
            else:
                string = pkmn_set[x+1].name + " ("
                if dawn_found == True:
                    string = string + "Dawn, "
                if day_found == True:
                    string = string + "Day, "
                if dusk_found == True:
                    string = string + "Dusk, "
                if night_found == True:
                    string = string + "Night, "
                string = string[0:len(string)-2] + ")"
                habitats.append(string)
        if len(habitats) >= 1:
            print("{0} is located in:".format(pkmn))
            for x in habitats:
                print(x)
            
                
            



class Area:
    def __init__(self, name):
        self.name = name
        self.pokemon = []
        self.dawn = {}
        self.day = {}
        self.dusk = {}
        self.night = {}

    def power(self, power):
        upper_bound = 0
        if power == 1:
            upper_bound = 50
        elif power == 2:
            upper_bound = 75
        elif power == 3: 
            upper_bound = 100
        else:
            return False
        
        if random.randint(1,100) <= upper_bound:
            return True
        else:
            return False

    def add(self, name, weight):
        dawn = 0
        day = 0
        dusk = 0
        night = 0
        if weight.find("/") != -1:
            ws = weight.split("/")
            dawn = int(ws[0])
            day = int(ws[1])
            dusk = int(ws[2])
            night = int(ws[3])
        else:
            dawn = int(weight)
            day = int(weight)
            dusk = int(weight)
            night = int(weight)
        if self.f_key(name) == False:
            self.pokemon.append(name)
            self.dawn[name] = dawn
            self.day[name] = day
            self.dusk[name] = dusk
            self.night[name] = night
        else:
            self.dawn[name] = self.dawn[name] + dawn
            self.day[name] = self.day[name] + day
            self.dusk[name] = self.dusk[name] + dusk
            self.night[name] = self.night[name] + night

    def f_key(self, name):
        found = False
        for s in self.pokemon:
            if name.lower().strip() == s.lower().strip():
                found = True
                break
        return found
    
    def f_dupe(self,dupes, name):
        for pkmn in dupes:
            if pkmn.strip().lower() == name.strip().lower():
                return True
        return False

    def distribution(self, game, time, type, power, dupes):
        time = time.lower().strip()
        print("{0} ({1})".format(self.name,time.capitalize()))
        selected = {}
        if time == "dawn":
            selected = self.dawn
        elif time == "day":
            selected = self.day
        elif time == "dusk":
            selected = self.dusk
        elif time == "night":
            selected = self.night

        types = ["Normal","Fighting","Flying","Poison","Ground","Rock","Bug","Ghost","Steel","Fire","Water","Grass","Electric","Psychic","Ice","Dragon","Dark","Fairy"]
        valid_type = False
        for t in types:
            if type.strip().lower() == t.strip().lower():
                valid_type = True
                break
        upper_bound = 0
        if power >= 1 and power <= 3 and valid_type == True:
            if power == 1:
                upper_bound = 0.50
            elif power == 2:
                upper_bound = 0.75
            elif power == 3: 
                upper_bound = 1
        multiplier = (1-upper_bound)

        sum = 0
        keys = selected.keys()
        for k in keys:
            if self.f_dupe(dupes,k.split("_")[0]) == False:
                if game == "Scarlet" and k.find("Violet") == -1:
                    if valid_type == True and upper_bound != 0 and k.find(type) == -1:
                        sum = sum + selected[k]*multiplier
                    else:
                        sum = sum + selected[k]
                elif game == "Violet" and k.find("Scarlet") == -1:
                    if valid_type == True and upper_bound != 0 and k.find(type) == -1:
                        sum = sum + selected[k]*multiplier
                    else:
                        sum = sum + selected[k]
        names = []
        percents = []
        for k in keys:
            if self.f_dupe(dupes,k.split("_")[0]) == False:
                if game == "Scarlet" and k.find("Violet") == -1:
                    n = k.split("_")[0]
                    percent = 0
                    if valid_type == True and upper_bound != 0 and k.find(type) == -1:
                        percent = selected[k]*multiplier/sum
                    else:
                        percent = selected[k]/sum
                    index = -1
                    percent = percent * 10000
                    percent = percent // 1
                    percent = percent / 100
                    if len(percents) == 0:
                        index = 0
                    else:
                        for x in range(len(percents)):
                            if percent >= percents[x]:
                                index = x
                                break
                        if index == -1:
                            index = len(percents)
                    names.insert(index, n)
                    percents.insert(index, percent)
                elif game == "Violet" and k.find("Scarlet") == -1:
                    n = k.split("_")[0]
                    percent = 0
                    if valid_type == True and upper_bound != 0 and k.find(type) == -1:
                        percent = selected[k]*multiplier/sum
                    else:
                        percent = selected[k]/sum
                    index = 0
                    percent = percent * 10000
                    percent = percent // 1
                    percent = percent / 100
                    if len(percents) == 0:
                        continue
                    else:
                        for x in range(len(percents)):
                            if percent >= percents[x]:
                                index = x
                                break
                            index = len(percents)-1
                    names.insert(index, n)
                    percents.insert(index, percent)
        for x in range(len(names)):
            print("{0}: {1}%".format(names[x],percents[x]))        

    def generate(self, game, time, type, power, dupes):
        class Range:
            def __init__(self, name, lower, upper):
                self.name = name
                self.lower = lower
                self.upper = upper

            def enclosed(self, number):
                return (self.lower <= number and number <= self.upper)             
        
        types = ["Normal","Fighting","Flying","Poison","Ground","Rock","Bug","Ghost","Steel","Fire","Water","Grass","Electric","Psychic","Ice","Dragon","Dark","Fairy"]
        valid_type = False
        for t in types:
            if type.strip().lower() == t.strip().lower():
                valid_type = True
                break
        
        power_activated = False
        if valid_type == True:
            power_activated = self.power(power)

        time = time.lower().strip()
        selected = {}
        if time == "dawn":
            selected = self.dawn
        elif time == "day":
            selected = self.day
        elif time == "dusk":
            selected = self.dusk
        elif time == "night":
            selected = self.night
        sum = 0
        keys = selected.keys()
        ranges = []
        for k in keys:
            if self.f_dupe(dupes,k.split("_")[0]) == False:
                if game == "Scarlet" and k.find("Violet") == -1:
                    if power_activated == True and k.find(type) == -1:
                        continue
                    ranges.append(Range(k, sum + 1, sum + selected[k]))
                    sum = sum + selected[k]
                elif game == "Violet" and k.find("Scarlet") == -1:
                    if power_activated == True and k.find(type) == -1:
                        continue
                    ranges.append(Range(k, sum + 1, sum + selected[k]))
                    sum = sum + selected[k]
    
        rng = random.randint(1, sum)
        for r in ranges:
            if r.enclosed(rng):
                n = r.name.split("_")[0]
                if self.f_dupe(dupes,n) == False:
                    if game == "Scarlet" and k.find("Violet") == -1:
                        print("{0}: {1}".format(self.name, n))
                        return r.name
                    elif game == "Violet" and k.find("Scarlet") == -1:
                        print("{0}: {1}".format(self.name, n))
                        return r.name


alfornada_cavern = Area("Alfornada Cavern")
alfornada_cavern.add("Dugtrio_Ground", "20")
alfornada_cavern.add("Umbreon_Dark", "0/0/0/1")
alfornada_cavern.add("Dunsparce_Normal", "5")
alfornada_cavern.add("Larvitar (Scarlet)_Rock_Ground", "10")
alfornada_cavern.add("Pupitar (Scarlet)_Rock_Ground", "10")
alfornada_cavern.add("Hariyama_Fighting", "10")
alfornada_cavern.add("Sableye_Dark_Ghost", "20")
alfornada_cavern.add("Meditite_Fighting_Psychic", "60")
alfornada_cavern.add("Medicham_Fighting_Psychic", "20")
alfornada_cavern.add("Gabite_Dragon_Ground", "10")
alfornada_cavern.add("Deino (Scarlet)_Dark_Dragon", "30")
alfornada_cavern.add("Gumshoos_Normal", "30")
alfornada_cavern.add("Salandit_Poison_Fire", "60")
alfornada_cavern.add("Salazzle_Poison_Fire", "5")
alfornada_cavern.add("Toxtricity_Electric_Poison", "15")
alfornada_cavern.add("Toxtricity_Electric_Poison", "15")
alfornada_cavern.add("Glimmet_Rock_Poison", "1")
alfornada_cavern.add("Bagon (Violet)_Dragon", "10")
alfornada_cavern.add("Shelgon (Violet)_Dragon", "10")

asado_desert = Area("Asado Desert")
asado_desert.add("Dreepy (Violet)_Dragon_Ghost", "5")
asado_desert.add("Murkrow_Dark_Flying", "0/0/40/40")
asado_desert.add("Dunsparce_Normal", "2")
asado_desert.add("Pawmo_Electric_Fighting", "10")
asado_desert.add("Toedscool_Ground_Grass", "2")
asado_desert.add("Phanpy_Ground", "20")
asado_desert.add("Donphan_Ground", "20")
asado_desert.add("Cacnea_Grass", "90")
asado_desert.add("Hippopotas_Ground", "60")
asado_desert.add("Sandile_Ground_Dark", "100")
asado_desert.add("Rufflet_Normal_Flying", "60")
asado_desert.add("Larvesta_Bug_Fire", "5")
asado_desert.add("Silicobra_Ground", "30")
asado_desert.add("Stonjourner (Scarlet)_Rock", "5")
asado_desert.add("Bramblin_Grass_Ghost", "30")
asado_desert.add("Capsakid_Grass", "30")
asado_desert.add("Rellor_Bug", "80")
asado_desert.add("Flittle_Psychic", "40")
asado_desert.add("Orthworm_Steel", "20")
asado_desert.add("Psyduck_Water", "60")
asado_desert.add("Marill_Water_Fairy", "60")
asado_desert.add("Buizel_Water", "20")
asado_desert.add("Chewtle_Water", "10")
asado_desert.add("Drednaw_Water_Rock", "10")
asado_desert.add("Tadbulb_Electric", "50")
asado_desert.add("Makuhita_Fighting", "30")
asado_desert.add("Skiddo_Grass", "50")
asado_desert.add("Yungoos_Normal", "20")
asado_desert.add("Gumshoos_Normal", "30")
asado_desert.add("Lokix_Bug_Dark", "30")
asado_desert.add("Nacli_Rock", "60")
asado_desert.add("Charcadet_Fire", "1")
asado_desert.add("Combee_Bug_Flying", "40")
asado_desert.add("Flabebe_Fairy", "60")
asado_desert.add("Flabebe_Fairy", "60")
asado_desert.add("Flabebe_Fairy", "60")
asado_desert.add("Flabebe_Fairy", "60")
asado_desert.add("Flabebe_Fairy", "6")
asado_desert.add("Floette_Fairy", "55")
asado_desert.add("Floette_Fairy", "55")
asado_desert.add("Floette_Fairy", "55")
asado_desert.add("Floette_Fairy", "55")
asado_desert.add("Floette_Fairy", "3")
asado_desert.add("Gastly_Ghost_Poison", "15")
asado_desert.add("Bronzor_Steel_Psychic", "60")
asado_desert.add("Falinks_Fighting", "40")
asado_desert.add("Stonjourner (Scarlet)_Rock", "15")
asado_desert.add("Tinkatuff_Fairy_Steel", "15")

cabo_poco = Area("Cabo Poco")
cabo_poco.add("Sprigatito_Grass", "33")
cabo_poco.add("Quaxley_Water", "33")
cabo_poco.add("Fuecoco_Fire", "33")

casseroya_lake = Area("Casseroya Lake")
casseroya_lake.add("Mismagius (Violet)_Ghost", "0/0/0/3")
casseroya_lake.add("Swalot (Violet)_Poison", "30")
casseroya_lake.add("Drakloak (Violet)_Dragon_Ghost", "25")
casseroya_lake.add("Drakloak (Violet)_Dragon_Ghost", "5")
casseroya_lake.add("Clawitzer (Violet)_Water", "20")
casseroya_lake.add("Glalie_Ice", "20")
casseroya_lake.add("Bronzong_Steel_Psychic", "20")
casseroya_lake.add("Glaceon_Ice", "1")
casseroya_lake.add("Froslass_Ice", "2")
casseroya_lake.add("Beartic_Ice", "20")
casseroya_lake.add("Frosmoth_Ice_Bug", "10")
casseroya_lake.add("Houndstone_Ghost", "10")
casseroya_lake.add("Cetitan_Ice", "10")
casseroya_lake.add("Golduck_Water", "20")
casseroya_lake.add("Slowpoke_Water_Psychic", "60")
casseroya_lake.add("Slowbro_Water_Psychic", "15")
casseroya_lake.add("Scyther_Bug_Flying", "30")
casseroya_lake.add("Gyarados_Water_Flying", "150")
casseroya_lake.add("Vaporeon_Water", "1")
casseroya_lake.add("Dratini_Dragon", "40")
casseroya_lake.add("Dragonair_Dragon", "10")
casseroya_lake.add("Azumarill_Water_Fairy_Water_Fairy", "30")
casseroya_lake.add("Altaria_Dragon_Flying", "20")
casseroya_lake.add("Tropius_Grass_Flying", "30")
casseroya_lake.add("Staraptor_Normal_Flying", "10/10/10/0")
casseroya_lake.add("Skuntank (Scarlet)_Poison_Dark", "30")
casseroya_lake.add("Toxicroak_Poison_Fighting", "30")
casseroya_lake.add("Sliggoo_Dragon", "50")
casseroya_lake.add("Bergmite_Ice", "150")
casseroya_lake.add("Avalugg_Ice", "100")
casseroya_lake.add("Drednaw_Water_Rock", "20")
casseroya_lake.add("Flamigo_Flying_Fighting", "60")
casseroya_lake.add("Veluza_Water_Psychic", "30")
casseroya_lake.add("Dondozo_Water", "30")
casseroya_lake.add("Tatsugiri_Dragon_Water", "20")
casseroya_lake.add("Tatsugiri_Dragon_Water", "20")
casseroya_lake.add("Tatsugiri_Dragon_Water", "20")
casseroya_lake.add("Golduck_Water", "20")
casseroya_lake.add("Slowpoke_Water_Psychic", "30")
casseroya_lake.add("Slowbro_Water_Psychic", "15")
casseroya_lake.add("Vaporeon_Water", "1")
casseroya_lake.add("Azumarill_Water_Fairy_Water_Fairy", "30")
casseroya_lake.add("Floatzel_Water", "10")
casseroya_lake.add("Toxicroak_Poison_Fighting", "20")
casseroya_lake.add("Bellibolt_Electric", "5")
casseroya_lake.add("Cloyster_Water_Ice", "10")
casseroya_lake.add("Gyarados_Water_Flying", "5")
casseroya_lake.add("Floatzel_Water", "40")
casseroya_lake.add("Skrelp (Scarlet)_Poison_Water", "60")
casseroya_lake.add("Dragalge (Scarlet)_Poison_Water", "20")
casseroya_lake.add("Kilowattrel_Electric_Flying", "30")
casseroya_lake.add("Veluza_Water_Psychic", "20")
casseroya_lake.add("Honchkrow_Dark_Flying", "0/0/20/20")
casseroya_lake.add("Gogoat_Grass", "30")
casseroya_lake.add("Hawlucha_Fighting_Flying", "60")
casseroya_lake.add("Copperajah_Steel", "20")
casseroya_lake.add("Lokix_Bug_Dark", "30")
casseroya_lake.add("Naclstack_Rock", "60")
casseroya_lake.add("Slowpoke_Water_Psychic", "30")
casseroya_lake.add("Slowbro_Water_Psychic", "25")
casseroya_lake.add("Floatzel_Water", "10")
casseroya_lake.add("Gastrodon_Water_Ground", "20")
casseroya_lake.add("Palossand_Ghost_Ground", "20")
casseroya_lake.add("Pincurchin_Electric", "10")
casseroya_lake.add("Naclstack_Rock", "20")
casseroya_lake.add("Kilowattrel_Electric_Flying", "30")
casseroya_lake.add("Wugtrio_Water", "20")
casseroya_lake.add("Bronzong_Steel_Psychic", "20")
casseroya_lake.add("Mabosstiff_Dark", "30")
casseroya_lake.add("Houndstone_Ghost", "5")


dalizapa_passage = Area("Dalizapa Passage")
dalizapa_passage.add("Magneton_Electric_Steel", "20")
dalizapa_passage.add("Haunter_Ghost_Poison", "0/0/0/40")
dalizapa_passage.add("Misdreavus (Violet)_Ghost", "0/0/0/15")
dalizapa_passage.add("Chansey_Normal", "1")
dalizapa_passage.add("Flareon_Fire", "1")
dalizapa_passage.add("Sneasel_Dark_Ice", "60")
dalizapa_passage.add("Ursaring_Normal", "20")
dalizapa_passage.add("Vigoroth_Normal", "20")
dalizapa_passage.add("Grumpig_Psychic", "20")
dalizapa_passage.add("Bagon (Violet)_Dragon", "10")
dalizapa_passage.add("Snorunt_Ice", "10")
dalizapa_passage.add("Drifblim (Scarlet)_Ghost_Flying", "0/0/30/30")
dalizapa_passage.add("Honchkrow_Dark_Flying", "0/0/20/20")
dalizapa_passage.add("Gallade_Psychic_Fighting", "1/1/1/0")
dalizapa_passage.add("Deerling_Normal_Grass", "90")
dalizapa_passage.add("Sawsbuck_Normal_Grass", "60")
dalizapa_passage.add("Axew_Dragon", "60")
dalizapa_passage.add("Cubchoo_Ice", "10")
dalizapa_passage.add("Rufflet_Normal_Flying", "25")
dalizapa_passage.add("Pyroar_Fire_Normal", "30")
dalizapa_passage.add("Pyroar_Fire_Normal", "30")
dalizapa_passage.add("Pyroar_Fire_Normal", "30")
dalizapa_passage.add("Gogoat_Grass", "40")
dalizapa_passage.add("Lycanroc (Midday)_Rock", "20/20/0/0")
dalizapa_passage.add("Lycanroc (Midnight)_Rock", "0/0/0/20")
dalizapa_passage.add("Mudbray_Ground", "60")
dalizapa_passage.add("Mudsdale_Ground", "12")
dalizapa_passage.add("Greedent_Normal", "20")
dalizapa_passage.add("Snom_Ice_Bug", "30")
dalizapa_passage.add("Lokix_Bug_Dark", "20")
dalizapa_passage.add("Pawmo_Electric_Fighting", "15")
dalizapa_passage.add("Scovillain_Grass_Fire", "10")
dalizapa_passage.add("Flittle_Psychic", "60")
dalizapa_passage.add("Espathra_Psychic", "20")
dalizapa_passage.add("Greavard_Ghost", "30")
dalizapa_passage.add("Cetoddle_Ice", "50")
dalizapa_passage.add("Hariyama_Fighting", "15")
dalizapa_passage.add("Grumpig_Psychic", "20")
dalizapa_passage.add("Honchkrow_Dark_Flying", "0/0/20/20")
dalizapa_passage.add("Pyroar_Fire_Normal", "30")
dalizapa_passage.add("Pyroar_Fire_Normal", "30")
dalizapa_passage.add("Pyroar_Fire_Normal", "30")
dalizapa_passage.add("Gogoat_Grass", "30")
dalizapa_passage.add("Gumshoos_Normal", "30")
dalizapa_passage.add("Lokix_Bug_Dark", "30")
dalizapa_passage.add("Naclstack_Rock", "60")
dalizapa_passage.add("Dugtrio_Ground", "20")
dalizapa_passage.add("Umbreon_Dark", "0/0/0/1")
dalizapa_passage.add("Dunsparce_Normal", "5")
dalizapa_passage.add("Larvitar (Scarlet)_Rock_Ground", "10")
dalizapa_passage.add("Hariyama_Fighting", "10")
dalizapa_passage.add("Sableye_Dark_Ghost", "20")
dalizapa_passage.add("Snorunt_Ice", "70")
dalizapa_passage.add("Gabite_Dragon_Ground", "10")
dalizapa_passage.add("Deino (Scarlet)_Dark_Dragon", "30")
dalizapa_passage.add("Gumshoos_Normal", "30")
dalizapa_passage.add("Salandit_Poison_Fire", "60")
dalizapa_passage.add("Salazzle_Poison_Fire", "5")
dalizapa_passage.add("Glimmet_Rock_Poison", "1")
dalizapa_passage.add("Frigibax_Dragon_Ice", "2")
dalizapa_passage.add("Meowth_Normal", "30")
dalizapa_passage.add("Persian_Normal", "30")
dalizapa_passage.add("Chansey_Normal", "1")
dalizapa_passage.add("Scyther_Bug_Flying", "3")
dalizapa_passage.add("Ditto_Normal", "10")
dalizapa_passage.add("Jumpluff_Grass_Flying", "30")
dalizapa_passage.add("Espeon_Psychic", "1/1/1/0")
dalizapa_passage.add("Murkrow_Dark_Flying", "0/0/40/40")
dalizapa_passage.add("Dunsparce_Normal", "2")
dalizapa_passage.add("Vigoroth_Normal", "20")
dalizapa_passage.add("Tropius_Grass_Flying", "10")
dalizapa_passage.add("Staravia_Normal_Flying", "30/30/30/0")
dalizapa_passage.add("Zorua_Dark", "15")
dalizapa_passage.add("Deerling_Normal_Grass", "70")
dalizapa_passage.add("Sawsbuck_Normal_Grass", "10")
dalizapa_passage.add("Fletchinder_Fire_Flying", "30")
dalizapa_passage.add("Oinkologne (Male)_Normal", "20")
dalizapa_passage.add("Oinkologne (Female)_Normal", "20")
dalizapa_passage.add("Pawmo_Electric_Fighting", "10")
dalizapa_passage.add("Mabosstiff_Dark", "20")
dalizapa_passage.add("Toedscool_Ground_Grass", "2")
dalizapa_passage.add("Meowth_Normal", "60")
dalizapa_passage.add("Persian_Normal", "30")
dalizapa_passage.add("Electrode_Electric", "10")
dalizapa_passage.add("Ditto_Normal", "30")
dalizapa_passage.add("Murkrow_Dark_Flying", "0/0/60/60")
dalizapa_passage.add("Drifloon (Scarlet)_Ghost_Flying", "0/0/40/40")
dalizapa_passage.add("Drifblim (Scarlet)_Ghost_Flying", "0/0/20/20")
dalizapa_passage.add("Dedenne_Electric_Fairy", "20")
dalizapa_passage.add("Dachsbun_Fairy", "30")
dalizapa_passage.add("Bombirdier_Flying_Dark", "5")

east_paldean_sea = Area("East Paldean Sea")
east_paldean_sea.add("Clauncher (Violet)_Water", "60")
east_paldean_sea.add("Shellder_Water", "60")
east_paldean_sea.add("Cloyster_Water_Ice", "10")
east_paldean_sea.add("Magikarp_Water", "60")
east_paldean_sea.add("Gyarados_Water_Flying", "5")
east_paldean_sea.add("Qwilfish_Water_Poison", "30")
east_paldean_sea.add("Luvdisc_Water", "60")
east_paldean_sea.add("Buizel_Water", "20")
east_paldean_sea.add("Floatzel_Water", "40")
east_paldean_sea.add("Skrelp (Scarlet)_Poison_Water", "60")
east_paldean_sea.add("Mareanie_Poison_Water", "60")
east_paldean_sea.add("Bruxish_Water_Psychic", "30")
east_paldean_sea.add("Arrokuda_Water", "60")
east_paldean_sea.add("Barraskewda_Water", "20")
east_paldean_sea.add("Finizen_Water", "30")
east_paldean_sea.add("Wattrel_Electric_Flying", "60")
east_paldean_sea.add("Kilowattrel_Electric_Flying", "30")
east_paldean_sea.add("Buizel_Water", "20")
east_paldean_sea.add("Crabrawler_Fighting", "30")
east_paldean_sea.add("Mareanie_Poison_Water", "80")
east_paldean_sea.add("Pincurchin_Electric", "10")
east_paldean_sea.add("Wiglett_Water", "60")
east_paldean_sea.add("Wugtrio_Water", "20")
east_paldean_sea.add("Wattrel_Electric_Flying", "60")
east_paldean_sea.add("Nacli_Rock", "15")
east_paldean_sea.add("Chansey_Normal", "1")
east_paldean_sea.add("Sunflora_Grass", "30/30/30/0")
east_paldean_sea.add("Combee_Bug_Flying", "40")
east_paldean_sea.add("Vivillon_Bug_Flying", "30")
east_paldean_sea.add("Flabebe_Fairy", "60")
east_paldean_sea.add("Flabebe_Fairy", "60")
east_paldean_sea.add("Flabebe_Fairy", "60")
east_paldean_sea.add("Flabebe_Fairy", "60")
east_paldean_sea.add("Flabebe_Fairy", "6")
east_paldean_sea.add("Floette_Fairy", "55")
east_paldean_sea.add("Floette_Fairy", "55")
east_paldean_sea.add("Floette_Fairy", "55")
east_paldean_sea.add("Floette_Fairy", "55")
east_paldean_sea.add("Floette_Fairy", "3")
east_paldean_sea.add("Dolliv_Grass_Normal", "10")

east_province_area_one = Area("East Province (Area One)")
east_province_area_one.add("Tauros (Combat Breed)_Fighting", "40")
east_province_area_one.add("Skiploom_Grass_Flying", "40")
east_province_area_one.add("Murkrow_Dark_Flying", "0/0/40/40")
east_province_area_one.add("Misdreavus (Violet)_Ghost", "0/0/0/15")
east_province_area_one.add("Dunsparce_Normal", "2")
east_province_area_one.add("Dreepy (Violet)_Dragon_Ghost", "5")
east_province_area_one.add("Deerling_Normal_Grass", "70")
east_province_area_one.add("Clauncher (Violet)_Water", "60")
east_province_area_one.add("Litleo_Fire_Normal", "60")
east_province_area_one.add("Steenee_Grass", "10")
east_province_area_one.add("Rookidee_Flying", "30")
east_province_area_one.add("Gulpin (Violet)_Poison", "60")
east_province_area_one.add("Gulpin (Violet)_Poison", "20")
east_province_area_one.add("Corvisquire_Flying", "20")
east_province_area_one.add("Lechonk_Normal", "80")
east_province_area_one.add("Oinkologne (Male)_Normal", "20")
east_province_area_one.add("Oinkologne (Female)_Normal", "20")
east_province_area_one.add("Pawmo_Electric_Fighting", "10")
east_province_area_one.add("Toedscool_Ground_Grass", "2")
east_province_area_one.add("Pikachu_Electric", "10")
east_province_area_one.add("Venonat_Bug_Poison", "40")
east_province_area_one.add("Murkrow_Dark_Flying", "0/0/20/20")
east_province_area_one.add("Pineco_Bug", "60")
east_province_area_one.add("Dunsparce_Normal", "4")
east_province_area_one.add("Teddiursa_Normal", "60")
east_province_area_one.add("Bounsweet_Grass", "60")
east_province_area_one.add("Steenee_Grass", "30")
east_province_area_one.add("Komala_Normal", "30")
east_province_area_one.add("Applin_Grass_Dragon", "10")
east_province_area_one.add("Lechonk_Normal", "60")
east_province_area_one.add("Oinkologne (Male)_Normal", "20")
east_province_area_one.add("Oinkologne (Female)_Normal", "20")
east_province_area_one.add("Spidops_Bug", "30")
east_province_area_one.add("Shroodle_Poison_Normal", "20")
east_province_area_one.add("Charcadet_Fire", "1")
east_province_area_one.add("Toedscool_Ground_Grass", "10")
east_province_area_one.add("Murkrow_Dark_Flying", "0/0/60/60")
east_province_area_one.add("Shuppet_Ghost", "0/0/0/70")
east_province_area_one.add("Drifloon (Scarlet)_Ghost_Flying", "0/0/40/40")
east_province_area_one.add("Oricorio (Baile Style)_Fire_Flying", "40")
east_province_area_one.add("Rookidee_Flying", "30")
east_province_area_one.add("Corvisquire_Flying", "30")
east_province_area_one.add("Tandemaus_Normal", "10")
east_province_area_one.add("Squawkabilly_Normal_Flying", "20")
east_province_area_one.add("Squawkabilly_Normal_Flying", "15")
east_province_area_one.add("Squawkabilly_Normal_Flying", "10")
east_province_area_one.add("Squawkabilly_Normal_Flying", "5")
east_province_area_one.add("Gastly_Ghost_Poison", "0/0/0/50")
east_province_area_one.add("Swablu_Normal_Flying", "70")
east_province_area_one.add("Drifloon (Scarlet)_Ghost_Flying", "0/0/30/30")
east_province_area_one.add("Rufflet_Normal_Flying", "25")
east_province_area_one.add("Litleo_Fire_Normal", "30")
east_province_area_one.add("Skiddo_Grass", "30")
east_province_area_one.add("Rockruff (Standard)_Rock", "40")
east_province_area_one.add("Rockruff (Own Tempo)_Rock", "2")
east_province_area_one.add("Mudbray_Ground", "60")
east_province_area_one.add("Rookidee_Flying", "30")
east_province_area_one.add("Corvisquire_Flying", "30")
east_province_area_one.add("Flittle_Psychic", "60")
east_province_area_one.add("Pawmo_Electric_Fighting", "15")
east_province_area_one.add("Charcadet_Fire", "1")
east_province_area_one.add("Psyduck_Water", "60")
east_province_area_one.add("Slowpoke_Water_Psychic", "30")
east_province_area_one.add("Magikarp_Water", "20")
east_province_area_one.add("Marill_Water_Fairy", "60")
east_province_area_one.add("Buizel_Water", "20")
east_province_area_one.add("Basculin (Red-Striped)_Water", "60")
east_province_area_one.add("Basculin (Blue-Striped)_Water", "60")
east_province_area_one.add("Chewtle_Water", "10")
east_province_area_one.add("Drednaw_Water_Rock", "10")
east_province_area_one.add("Arrokuda_Water", "40")
east_province_area_one.add("Tadbulb_Electric", "50")
east_province_area_one.add("Shellder_Water", "60")
east_province_area_one.add("Magikarp_Water", "60")
east_province_area_one.add("Gyarados_Water_Flying", "5")
east_province_area_one.add("Qwilfish_Water_Poison", "30")
east_province_area_one.add("Luvdisc_Water", "60")
east_province_area_one.add("Buizel_Water", "20")
east_province_area_one.add("Mareanie_Poison_Water", "60")
east_province_area_one.add("Arrokuda_Water", "60")
east_province_area_one.add("Finizen_Water", "30")
east_province_area_one.add("Wattrel_Electric_Flying", "60")
east_province_area_one.add("Makuhita_Fighting", "30")
east_province_area_one.add("Litleo_Fire_Normal", "50")
east_province_area_one.add("Skiddo_Grass", "50")
east_province_area_one.add("Yungoos_Normal", "20")
east_province_area_one.add("Gumshoos_Normal", "30")
east_province_area_one.add("Rookidee_Flying", "30")
east_province_area_one.add("Corvisquire_Flying", "30")
east_province_area_one.add("Nacli_Rock", "60")
east_province_area_one.add("Charcadet_Fire", "1")
east_province_area_one.add("Slowpoke_Water_Psychic", "30")
east_province_area_one.add("Shellder_Water", "60")
east_province_area_one.add("Buizel_Water", "20")
east_province_area_one.add("Shellos_Water_Ground", "60")
east_province_area_one.add("Crabrawler_Fighting", "30")
east_province_area_one.add("Mareanie_Poison_Water", "80")
east_province_area_one.add("Sandygast_Ghost_Ground", "60")
east_province_area_one.add("Pincurchin_Electric", "10")
east_province_area_one.add("Wiglett_Water", "60")
east_province_area_one.add("Wattrel_Electric_Flying", "60")
east_province_area_one.add("Nacli_Rock", "15")

east_province_area_two = Area("East Province (Area Two)")
east_province_area_two.add("Magnemite_Electric_Steel", "50")
east_province_area_two.add("Chansey_Normal", "1")
east_province_area_two.add("Tauros (Combat Breed)_Fighting", "40")
east_province_area_two.add("Tauros (Blaze Breed) (Scarlet)_Fighting_Fire", "3")
east_province_area_two.add("Tauros (Aqua Breed) (Violet)_Fighting_Water", "3")
east_province_area_two.add("Marill_Water_Fairy", "80")
east_province_area_two.add("Clauncher (Violet)_Water", "60")
east_province_area_two.add("Dreepy (Violet)_Dragon_Ghost", "40")
east_province_area_two.add("Skiploom_Grass_Flying", "40")
east_province_area_two.add("Murkrow_Dark_Flying", "0/0/40/40")
east_province_area_two.add("Dunsparce_Normal", "2")
east_province_area_two.add("Deerling_Normal_Grass", "70")
east_province_area_two.add("Rookidee_Flying", "30")
east_province_area_two.add("Corvisquire_Flying", "20")
east_province_area_two.add("Oinkologne (Male)_Normal", "20")
east_province_area_two.add("Oinkologne (Female)_Normal", "20")
east_province_area_two.add("Cyclizar_Dragon_Normal", "15")
east_province_area_two.add("Pawmo_Electric_Fighting", "10")
east_province_area_two.add("Wattrel_Electric_Flying", "110")
east_province_area_two.add("Toedscool_Ground_Grass", "2")
east_province_area_two.add("Venonat_Bug_Poison", "40")
east_province_area_two.add("Murkrow_Dark_Flying", "0/0/20/20")
east_province_area_two.add("Pineco_Bug", "60")
east_province_area_two.add("Dunsparce_Normal", "4")
east_province_area_two.add("Komala_Normal", "30")
east_province_area_two.add("Applin_Grass_Dragon", "10")
east_province_area_two.add("Oinkologne (Male)_Normal", "20")
east_province_area_two.add("Oinkologne (Female)_Normal", "20")
east_province_area_two.add("Spidops_Bug", "30")
east_province_area_two.add("Cyclizar_Dragon_Normal", "15")
east_province_area_two.add("Shroodle_Poison_Normal", "20")
east_province_area_two.add("Charcadet_Fire", "1")
east_province_area_two.add("Toedscool_Ground_Grass", "10")
east_province_area_two.add("Magnemite_Electric_Steel", "20")
east_province_area_two.add("Grimer_Poison", "80")
east_province_area_two.add("Murkrow_Dark_Flying", "0/0/60/60")
east_province_area_two.add("Kirlia_Psychic_Fairy", "50/50/50/0")
east_province_area_two.add("Shuppet_Ghost", "0/0/0/70")
east_province_area_two.add("Drifloon (Scarlet)_Ghost_Flying", "0/0/40/40")
east_province_area_two.add("Rotom_Electric_Ghost", "10")
east_province_area_two.add("Rookidee_Flying", "30")
east_province_area_two.add("Corvisquire_Flying", "30")
east_province_area_two.add("Tandemaus_Normal", "10")
east_province_area_two.add("Squawkabilly_Normal_Flying", "20")
east_province_area_two.add("Squawkabilly_Normal_Flying", "15")
east_province_area_two.add("Squawkabilly_Normal_Flying", "10")
east_province_area_two.add("Squawkabilly_Normal_Flying", "5")
east_province_area_two.add("Psyduck_Water", "60")
east_province_area_two.add("Slowpoke_Water_Psychic", "30")
east_province_area_two.add("Magikarp_Water", "20")
east_province_area_two.add("Marill_Water_Fairy", "60")
east_province_area_two.add("Buizel_Water", "20")
east_province_area_two.add("Basculin (Red-Striped)_Water", "60")
east_province_area_two.add("Basculin (Blue-Striped)_Water", "60")
east_province_area_two.add("Chewtle_Water", "10")
east_province_area_two.add("Drednaw_Water_Rock", "10")
east_province_area_two.add("Arrokuda_Water", "40")
east_province_area_two.add("Tadbulb_Electric", "50")
east_province_area_two.add("Cyclizar_Dragon_Normal", "15")
east_province_area_two.add("Shellder_Water", "60")
east_province_area_two.add("Magikarp_Water", "60")
east_province_area_two.add("Gyarados_Water_Flying", "5")
east_province_area_two.add("Qwilfish_Water_Poison", "30")
east_province_area_two.add("Luvdisc_Water", "60")
east_province_area_two.add("Buizel_Water", "20")
east_province_area_two.add("Mareanie_Poison_Water", "60")
east_province_area_two.add("Arrokuda_Water", "60")
east_province_area_two.add("Finizen_Water", "30")
east_province_area_two.add("Wattrel_Electric_Flying", "60")
east_province_area_two.add("Makuhita_Fighting", "30")
east_province_area_two.add("Skiddo_Grass", "50")
east_province_area_two.add("Yungoos_Normal", "20")
east_province_area_two.add("Gumshoos_Normal", "30")
east_province_area_two.add("Rookidee_Flying", "30")
east_province_area_two.add("Corvisquire_Flying", "30")
east_province_area_two.add("Lokix_Bug_Dark", "30")
east_province_area_two.add("Nacli_Rock", "60")
east_province_area_two.add("Charcadet_Fire", "1")
east_province_area_two.add("Slowpoke_Water_Psychic", "30")
east_province_area_two.add("Shellder_Water", "60")
east_province_area_two.add("Marill_Water_Fairy", "30")
east_province_area_two.add("Buizel_Water", "20")
east_province_area_two.add("Crabrawler_Fighting", "30")
east_province_area_two.add("Mareanie_Poison_Water", "80")
east_province_area_two.add("Sandygast_Ghost_Ground", "60")
east_province_area_two.add("Pincurchin_Electric", "10")
east_province_area_two.add("Wiglett_Water", "60")
east_province_area_two.add("Wattrel_Electric_Flying", "60")
east_province_area_two.add("Nacli_Rock", "15")
east_province_area_two.add("Gastly_Ghost_Poison", "15")
east_province_area_two.add("Bronzor_Steel_Psychic", "60")
east_province_area_two.add("Mimikyu_Ghost_Fairy", "10")
east_province_area_two.add("Tinkatink_Fairy_Steel", "15")
east_province_area_two.add("Tinkatuff_Fairy_Steel", "15")

east_province_area_three = Area("East Province (Area Three)")
east_province_area_three.add("Meowth_Normal", "30")
east_province_area_three.add("Magnemite_Electric_Steel", "50")
east_province_area_three.add("Murkrow_Dark_Flying", "0/0/40/40")
east_province_area_three.add("Dunsparce_Normal", "2")
east_province_area_three.add("Rookidee_Flying", "30")
east_province_area_three.add("Corvisquire_Flying", "20")
east_province_area_three.add("Pawmo_Electric_Fighting", "10")
east_province_area_three.add("Bagon (Violet)_Dragon", "10")
east_province_area_three.add("Bagon (Violet)_Dragon", "3")
east_province_area_three.add("Toedscool_Ground_Grass", "2")
east_province_area_three.add("Clauncher (Violet)_Water", "60")
east_province_area_three.add("Meowth_Normal", "60")
east_province_area_three.add("Magnemite_Electric_Steel", "20")
east_province_area_three.add("Voltorb_Electric", "30")
east_province_area_three.add("Murkrow_Dark_Flying", "0/0/60/60")
east_province_area_three.add("Shuppet_Ghost", "0/0/0/70")
east_province_area_three.add("Misdreavus (Violet)_Ghost", "0/0/0/60")
east_province_area_three.add("Drifloon (Scarlet)_Ghost_Flying", "0/0/40/40")
east_province_area_three.add("Drifblim (Scarlet)_Ghost_Flying", "0/0/20/20")
east_province_area_three.add("Gothita_Psychic", "30")
east_province_area_three.add("Rookidee_Flying", "30")
east_province_area_three.add("Corvisquire_Flying", "30")
east_province_area_three.add("Sinistea_Ghost", "30")
east_province_area_three.add("Dreepy (Violet)_Dragon_Ghost", "15")
east_province_area_three.add("Dreepy (Violet)_Dragon_Ghost", "5")
east_province_area_three.add("Tandemaus_Normal", "10")
east_province_area_three.add("Dachsbun_Fairy", "30")
east_province_area_three.add("Squawkabilly_Normal_Flying", "20")
east_province_area_three.add("Squawkabilly_Normal_Flying", "15")
east_province_area_three.add("Squawkabilly_Normal_Flying", "10")
east_province_area_three.add("Squawkabilly_Normal_Flying", "5")
east_province_area_three.add("Varoom_Steel_Poison", "10")
east_province_area_three.add("Psyduck_Water", "60")
east_province_area_three.add("Magikarp_Water", "60")
east_province_area_three.add("Barboach_Water_Ground", "60")
east_province_area_three.add("Basculin (Red-Striped)_Water", "60")
east_province_area_three.add("Basculin (Blue-Striped)_Water", "60")
east_province_area_three.add("Goomy_Dragon", "40")
east_province_area_three.add("Chewtle_Water", "10")
east_province_area_three.add("Drednaw_Water_Rock", "10")
east_province_area_three.add("Flamigo_Flying_Fighting", "10")
east_province_area_three.add("Clodsire_Poison_Ground", "30")
east_province_area_three.add("Psyduck_Water", "60")
east_province_area_three.add("Magikarp_Water", "20")
east_province_area_three.add("Buizel_Water", "20")
east_province_area_three.add("Floatzel_Water", "10")
east_province_area_three.add("Basculin (Red-Striped)_Water", "60")
east_province_area_three.add("Basculin (Blue-Striped)_Water", "60")
east_province_area_three.add("Pawniard_Dark_Steel", "60")
east_province_area_three.add("Chewtle_Water", "10")
east_province_area_three.add("Drednaw_Water_Rock", "10")
east_province_area_three.add("Arrokuda_Water", "40")
east_province_area_three.add("Barraskewda_Water", "20")
east_province_area_three.add("Tadbulb_Electric", "50")
east_province_area_three.add("Flamigo_Flying_Fighting", "12")
east_province_area_three.add("Shellder_Water", "60")
east_province_area_three.add("Magikarp_Water", "60")
east_province_area_three.add("Gyarados_Water_Flying", "5")
east_province_area_three.add("Qwilfish_Water_Poison", "30")
east_province_area_three.add("Luvdisc_Water", "60")
east_province_area_three.add("Buizel_Water", "20")
east_province_area_three.add("Arrokuda_Water", "60")
east_province_area_three.add("Barraskewda_Water", "20")
east_province_area_three.add("Finizen_Water", "30")
east_province_area_three.add("Wattrel_Electric_Flying", "60")
east_province_area_three.add("Diglett_Ground", "20")
east_province_area_three.add("Dugtrio_Ground", "20")
east_province_area_three.add("Umbreon_Dark", "0/0/0/1")
east_province_area_three.add("Dunsparce_Normal", "5")
east_province_area_three.add("Larvitar (Scarlet)_Rock_Ground", "10")
east_province_area_three.add("Makuhita_Fighting", "20")
east_province_area_three.add("Hariyama_Fighting", "10")
east_province_area_three.add("Sableye_Dark_Ghost", "20")
east_province_area_three.add("Gabite_Dragon_Ground", "10")
east_province_area_three.add("Deino (Scarlet)_Dark_Dragon", "30")
east_province_area_three.add("Yungoos_Normal", "60")
east_province_area_three.add("Gumshoos_Normal", "30")
east_province_area_three.add("Salandit_Poison_Fire", "60")
east_province_area_three.add("Salazzle_Poison_Fire", "5")
east_province_area_three.add("Rolycoly_Rock", "20")
east_province_area_three.add("Charcadet_Fire", "1")
east_province_area_three.add("Glimmet_Rock_Poison", "1")
east_province_area_three.add("Diglett_Ground", "40")
east_province_area_three.add("Dugtrio_Ground", "40")
east_province_area_three.add("Meowth_Normal", "15")
east_province_area_three.add("Growlithe_Fire", "10")
east_province_area_three.add("Gastly_Ghost_Poison", "0/0/0/30")
east_province_area_three.add("Voltorb_Electric", "30")
east_province_area_three.add("Larvitar (Scarlet)_Rock_Ground", "3")
east_province_area_three.add("Makuhita_Fighting", "10")
east_province_area_three.add("Hariyama_Fighting", "40")
east_province_area_three.add("Torkoal_Fire", "10")
east_province_area_three.add("Rufflet_Normal_Flying", "20")
east_province_area_three.add("Rolycoly_Rock", "60")
east_province_area_three.add("Carkol_Rock_Fire", "60")
east_province_area_three.add("Silicobra_Ground", "10")
east_province_area_three.add("Cufant_Steel", "60")
east_province_area_three.add("Bramblin_Grass_Ghost", "60")
east_province_area_three.add("Varoom_Steel_Poison", "15")
east_province_area_three.add("Orthworm_Steel", "30")

glaseado_mountain = Area("Glaseado Mountain")
glaseado_mountain.add("Magneton_Electric_Steel", "20")
glaseado_mountain.add("Haunter_Ghost_Poison", "0/0/0/40")
glaseado_mountain.add("Chansey_Normal", "1")
glaseado_mountain.add("Flareon_Fire", "1")
glaseado_mountain.add("Ampharos_Electric", "10")
glaseado_mountain.add("Sneasel_Dark_Ice", "60")
glaseado_mountain.add("Ursaring_Normal", "20")
glaseado_mountain.add("Vigoroth_Normal", "20")
glaseado_mountain.add("Grumpig_Psychic", "20")
glaseado_mountain.add("Altaria_Dragon_Flying", "20")
glaseado_mountain.add("Snorunt_Ice", "10")
glaseado_mountain.add("Misdreavus (Violet)_Ghost", "0/0/0/15")
glaseado_mountain.add("Drifblim (Scarlet)_Ghost_Flying", "0/0/30/30")
glaseado_mountain.add("Honchkrow_Dark_Flying", "0/0/20/20")
glaseado_mountain.add("Gallade_Psychic_Fighting", "1/1/1/0")
glaseado_mountain.add("Deerling_Normal_Grass", "90")
glaseado_mountain.add("Sawsbuck_Normal_Grass", "60")
glaseado_mountain.add("Axew_Dragon", "60")
glaseado_mountain.add("Fraxure_Dragon", "20")
glaseado_mountain.add("Cubchoo_Ice", "10")
glaseado_mountain.add("Rufflet_Normal_Flying", "25")
glaseado_mountain.add("Pyroar_Fire_Normal", "30")
glaseado_mountain.add("Pyroar_Fire_Normal", "30")
glaseado_mountain.add("Pyroar_Fire_Normal", "30")
glaseado_mountain.add("Gogoat_Grass", "40")
glaseado_mountain.add("Lycanroc (Midday)_Rock", "20/20/0/0")
glaseado_mountain.add("Lycanroc (Midnight)_Rock", "0/0/0/20")
glaseado_mountain.add("Mudbray_Ground", "60")
glaseado_mountain.add("Mudsdale_Ground", "12")
glaseado_mountain.add("Greedent_Normal", "20")
glaseado_mountain.add("Snom_Ice_Bug", "30")
glaseado_mountain.add("Lokix_Bug_Dark", "20")
glaseado_mountain.add("Pawmo_Electric_Fighting", "15")
glaseado_mountain.add("Scovillain_Grass_Fire", "10")
glaseado_mountain.add("Flittle_Psychic", "60")
glaseado_mountain.add("Espathra_Psychic", "20")
glaseado_mountain.add("Tinkatuff_Fairy_Steel", "10")
glaseado_mountain.add("Greavard_Ghost", "30")
glaseado_mountain.add("Houndstone_Ghost", "15")
glaseado_mountain.add("Cetoddle_Ice", "50")
glaseado_mountain.add("Magneton_Electric_Steel", "3")
glaseado_mountain.add("Haunter_Ghost_Poison", "0/0/0/50")
glaseado_mountain.add("Sneasel_Dark_Ice", "60")
glaseado_mountain.add("Delibird_Ice_Flying", "10")
glaseado_mountain.add("Snorunt_Ice", "20")
glaseado_mountain.add("Glalie_Ice", "20")
glaseado_mountain.add("Bronzong_Steel_Psychic", "20")
glaseado_mountain.add("Glaceon_Ice", "1")
glaseado_mountain.add("Froslass_Ice", "2")
glaseado_mountain.add("Sawsbuck_Normal_Grass", "30")
glaseado_mountain.add("Cubchoo_Ice", "60")
glaseado_mountain.add("Beartic_Ice", "20")
glaseado_mountain.add("Bergmite_Ice", "60")
glaseado_mountain.add("Avalugg_Ice", "20")
glaseado_mountain.add("Crabrawler_Fighting", "2")
glaseado_mountain.add("Snom_Ice_Bug", "60")
glaseado_mountain.add("Frosmoth_Ice_Bug", "10")
glaseado_mountain.add("Greavard_Ghost", "25")
glaseado_mountain.add("Houndstone_Ghost", "10")
glaseado_mountain.add("Cetoddle_Ice", "60")
glaseado_mountain.add("Frigibax_Dragon_Ice", "1")
glaseado_mountain.add("Hariyama_Fighting", "15")
glaseado_mountain.add("Grumpig_Psychic", "20")
glaseado_mountain.add("Honchkrow_Dark_Flying", "0/0/20/20")
glaseado_mountain.add("Pyroar_Fire_Normal", "30")
glaseado_mountain.add("Pyroar_Fire_Normal", "30")
glaseado_mountain.add("Pyroar_Fire_Normal", "30")
glaseado_mountain.add("Gogoat_Grass", "30")
glaseado_mountain.add("Gumshoos_Normal", "30")
glaseado_mountain.add("Copperajah_Steel", "20")
glaseado_mountain.add("Lokix_Bug_Dark", "30")
glaseado_mountain.add("Naclstack_Rock", "60")
glaseado_mountain.add("Revavroom_Steel_Poison", "20")
glaseado_mountain.add("Haunter_Ghost_Poison", "0/0/0/50")
glaseado_mountain.add("Hypno_Psychic", "20")
glaseado_mountain.add("Bronzong_Steel_Psychic", "20")
glaseado_mountain.add("Mimikyu_Ghost_Fairy", "10")
glaseado_mountain.add("Tinkatuff_Fairy_Steel", "15")
glaseado_mountain.add("Murkrow_Dark_Flying", "0/0/60/60")
glaseado_mountain.add("Delibird_Ice_Flying", "30")
glaseado_mountain.add("Kirlia_Psychic_Fairy", "50/50/50/0")
glaseado_mountain.add("Banette_Ghost", "0/0/0/70")
glaseado_mountain.add("Drifblim (Scarlet)_Ghost_Flying", "0/0/20/20")
glaseado_mountain.add("Snover_Grass_Ice", "50")
glaseado_mountain.add("Klefki_Steel_Fairy", "20")
glaseado_mountain.add("Magneton_Electric_Steel", "20")
glaseado_mountain.add("Chansey_Normal", "1")
glaseado_mountain.add("Flareon_Fire", "1")
glaseado_mountain.add("Sneasel_Dark_Ice", "60")
glaseado_mountain.add("Altaria_Dragon_Flying", "20")
glaseado_mountain.add("Snorunt_Ice", "10")
glaseado_mountain.add("Drifblim (Scarlet)_Ghost_Flying", "0/0/30/30")
glaseado_mountain.add("Honchkrow_Dark_Flying", "0/0/20/20")
glaseado_mountain.add("Gallade_Psychic_Fighting", "1/1/1/0")
glaseado_mountain.add("Deerling_Normal_Grass", "90")
glaseado_mountain.add("Sawsbuck_Normal_Grass", "60")
glaseado_mountain.add("Cubchoo_Ice", "10")
glaseado_mountain.add("Rufflet_Normal_Flying", "25")
glaseado_mountain.add("Gogoat_Grass", "40")
glaseado_mountain.add("Lycanroc (Midday)_Rock", "20/20/0/0")
glaseado_mountain.add("Lycanroc (Midnight)_Rock", "0/0/0/20")
glaseado_mountain.add("Mudbray_Ground", "60")
glaseado_mountain.add("Mudsdale_Ground", "12")
glaseado_mountain.add("Greedent_Normal", "20")
glaseado_mountain.add("Lokix_Bug_Dark", "20")
glaseado_mountain.add("Pawmo_Electric_Fighting", "15")
glaseado_mountain.add("Scovillain_Grass_Fire", "10")
glaseado_mountain.add("Flittle_Psychic", "60")
glaseado_mountain.add("Espathra_Psychic", "20")
glaseado_mountain.add("Greavard_Ghost", "30")
glaseado_mountain.add("Cetoddle_Ice", "50")
glaseado_mountain.add("Magneton_Electric_Steel", "3")
glaseado_mountain.add("Sneasel_Dark_Ice", "60")
glaseado_mountain.add("Delibird_Ice_Flying", "10")
glaseado_mountain.add("Gardevoir_Psychic_Fairy", "10/10/10/0")
glaseado_mountain.add("Snorunt_Ice", "20")
glaseado_mountain.add("Bronzong_Steel_Psychic", "20")
glaseado_mountain.add("Snover_Grass_Ice", "60")
glaseado_mountain.add("Abomasnow_Grass_Ice", "20")
glaseado_mountain.add("Glaceon_Ice", "1")
glaseado_mountain.add("Froslass_Ice", "2")
glaseado_mountain.add("Sawsbuck_Normal_Grass", "30")
glaseado_mountain.add("Cubchoo_Ice", "60")
glaseado_mountain.add("Beartic_Ice", "20")
glaseado_mountain.add("Cryogonal_Ice", "100")
glaseado_mountain.add("Bergmite_Ice", "60")
glaseado_mountain.add("Avalugg_Ice", "20")
glaseado_mountain.add("Crabrawler_Fighting", "2")
glaseado_mountain.add("Greavard_Ghost", "25")
glaseado_mountain.add("Cetoddle_Ice", "60")
glaseado_mountain.add("Frigibax_Dragon_Ice", "1")
glaseado_mountain.add("Psyduck_Water", "60")
glaseado_mountain.add("Golduck_Water", "20")
glaseado_mountain.add("Magikarp_Water", "60")
glaseado_mountain.add("Vaporeon_Water", "1")
glaseado_mountain.add("Whiscash_Water_Ground", "10")
glaseado_mountain.add("Basculin (Red-Striped)_Water", "60")
glaseado_mountain.add("Basculin (Blue-Striped)_Water", "60")
glaseado_mountain.add("Drednaw_Water_Rock", "10")
glaseado_mountain.add("Hattrem_Psychic", "30")
glaseado_mountain.add("Flamigo_Flying_Fighting", "10")
glaseado_mountain.add("Clodsire_Poison_Ground", "30")
glaseado_mountain.add("Psyduck_Water", "60")
glaseado_mountain.add("Golduck_Water", "20")
glaseado_mountain.add("Magikarp_Water", "20")
glaseado_mountain.add("Vaporeon_Water", "1")
glaseado_mountain.add("Floatzel_Water", "10")
glaseado_mountain.add("Basculin (Red-Striped)_Water", "60")
glaseado_mountain.add("Basculin (Blue-Striped)_Water", "60")
glaseado_mountain.add("Drednaw_Water_Rock", "10")
glaseado_mountain.add("Barraskewda_Water", "20")
glaseado_mountain.add("Tadbulb_Electric", "50")
glaseado_mountain.add("Bellibolt_Electric", "5")
glaseado_mountain.add("Flamigo_Flying_Fighting", "12")
glaseado_mountain.add("Shellder_Water", "60")
glaseado_mountain.add("Cloyster_Water_Ice", "10")
glaseado_mountain.add("Magikarp_Water", "60")
glaseado_mountain.add("Gyarados_Water_Flying", "5")
glaseado_mountain.add("Qwilfish_Water_Poison", "30")
glaseado_mountain.add("Floatzel_Water", "40")
glaseado_mountain.add("Skrelp (Scarlet)_Poison_Water", "60")
glaseado_mountain.add("Bergmite_Ice", "60")
glaseado_mountain.add("Avalugg_Ice", "20")
glaseado_mountain.add("Barraskewda_Water", "20")
glaseado_mountain.add("Kilowattrel_Electric_Flying", "30")
glaseado_mountain.add("Finizen_Water", "30")
glaseado_mountain.add("Hariyama_Fighting", "15")
glaseado_mountain.add("Honchkrow_Dark_Flying", "0/0/20/20")
glaseado_mountain.add("Gogoat_Grass", "30")
glaseado_mountain.add("Gumshoos_Normal", "30")
glaseado_mountain.add("Copperajah_Steel", "20")
glaseado_mountain.add("Lokix_Bug_Dark", "30")
glaseado_mountain.add("Naclstack_Rock", "60")
glaseado_mountain.add("Dugtrio_Ground", "20")
glaseado_mountain.add("Umbreon_Dark", "0/0/0/1")
glaseado_mountain.add("Dunsparce_Normal", "5")
glaseado_mountain.add("Larvitar (Scarlet)_Rock_Ground", "10")
glaseado_mountain.add("Hariyama_Fighting", "10")
glaseado_mountain.add("Sableye_Dark_Ghost", "20")
glaseado_mountain.add("Snorunt_Ice", "70")
glaseado_mountain.add("Gabite_Dragon_Ground", "10")
glaseado_mountain.add("Deino (Scarlet)_Dark_Dragon", "30")
glaseado_mountain.add("Gumshoos_Normal", "30")
glaseado_mountain.add("Salandit_Poison_Fire", "60")
glaseado_mountain.add("Salazzle_Poison_Fire", "5")
glaseado_mountain.add("Glimmet_Rock_Poison", "1")
glaseado_mountain.add("Frigibax_Dragon_Ice", "2")
glaseado_mountain.add("Chansey_Normal", "1")
glaseado_mountain.add("Jumpluff_Grass_Flying", "20")
glaseado_mountain.add("Sunflora_Grass", "30/30/30/0")
glaseado_mountain.add("Vespiquen_Bug_Flying", "20")
glaseado_mountain.add("Vivillon_Bug_Flying", "30")
glaseado_mountain.add("Floette_Fairy", "55")
glaseado_mountain.add("Floette_Fairy", "55")
glaseado_mountain.add("Floette_Fairy", "55")
glaseado_mountain.add("Floette_Fairy", "55")
glaseado_mountain.add("Floette_Fairy", "3")
glaseado_mountain.add("Dolliv_Grass_Normal", "10")
glaseado_mountain.add("Hypno_Psychic", "20")
glaseado_mountain.add("Bronzong_Steel_Psychic", "20")
glaseado_mountain.add("Tinkatuff_Fairy_Steel", "15")

great_crater_of_paldea = Area("Great Crater of Paldea")
great_crater_of_paldea.add("Raichu_Electric", "10")
great_crater_of_paldea.add("Venomoth_Bug_Poison", "30")
great_crater_of_paldea.add("Chansey_Normal", "1")
great_crater_of_paldea.add("Jumpluff_Grass_Flying", "30")
great_crater_of_paldea.add("Espeon_Psychic", "1/1/1/0")
great_crater_of_paldea.add("Girafarig_Normal_Psychic", "30")
great_crater_of_paldea.add("Medicham_Fighting_Psychic", "20")
great_crater_of_paldea.add("Braviary_Normal_Flying", "15")
great_crater_of_paldea.add("Floette_Fairy", "15")
great_crater_of_paldea.add("Corviknight_Flying_Steel", "20")
great_crater_of_paldea.add("Frosmoth_Ice_Bug", "5")
great_crater_of_paldea.add("Pawmo_Electric_Fighting", "10")
great_crater_of_paldea.add("Farigiraf_Normal_Psychic", "10")
great_crater_of_paldea.add("Scream Tail (Scarlet)_Fairy_Psychic", "20")
great_crater_of_paldea.add("Slither Wing (Scarlet)_Bug_Fighting", "15")
great_crater_of_paldea.add("Golduck_Water", "20")
great_crater_of_paldea.add("Vaporeon_Water", "1")
great_crater_of_paldea.add("Altaria_Dragon_Flying", "30")
great_crater_of_paldea.add("Floatzel_Water", "10")
great_crater_of_paldea.add("Flamigo_Flying_Fighting", "20")
great_crater_of_paldea.add("Donphan_Ground", "30")
great_crater_of_paldea.add("Honchkrow_Dark_Flying", "0/0/20/20")
great_crater_of_paldea.add("Braviary_Normal_Flying", "15")
great_crater_of_paldea.add("Talonflame_Fire_Flying", "30")
great_crater_of_paldea.add("Gogoat_Grass", "30")
great_crater_of_paldea.add("Hawlucha_Fighting_Flying", "60")
great_crater_of_paldea.add("Lycanroc (Midday)_Rock", "20")
great_crater_of_paldea.add("Copperajah_Steel", "20")
great_crater_of_paldea.add("Lokix_Bug_Dark", "30")
great_crater_of_paldea.add("Naclstack_Rock", "60")
great_crater_of_paldea.add("Garganacl_Rock", "10")
great_crater_of_paldea.add("Sandy Shocks (Scarlet)_Electric_Ground", "15")
great_crater_of_paldea.add("Chansey_Normal", "1")
great_crater_of_paldea.add("Espeon_Psychic", "1/1/1/0")
great_crater_of_paldea.add("Pawmo_Electric_Fighting", "10")
great_crater_of_paldea.add("Golduck_Water", "20")
great_crater_of_paldea.add("Vaporeon_Water", "1")
great_crater_of_paldea.add("Floatzel_Water", "10")
great_crater_of_paldea.add("Dugtrio_Ground", "20")
great_crater_of_paldea.add("Umbreon_Dark", "0/0/0/1")
great_crater_of_paldea.add("Sneasel_Dark_Ice", "50")
great_crater_of_paldea.add("Sableye_Dark_Ghost", "20")
great_crater_of_paldea.add("Gabite_Dragon_Ground", "10")
great_crater_of_paldea.add("Weavile_Dark_Ice", "3")
great_crater_of_paldea.add("Zweilous (Scarlet)_Dark_Dragon", "10")
great_crater_of_paldea.add("Lycanroc (Midday)_Rock", "20")
great_crater_of_paldea.add("Glimmet_Rock_Poison", "1")
great_crater_of_paldea.add("Flutter Mane (Scarlet)_Ghost_Fairy", "15")
great_crater_of_paldea.add("Roaring Moon (Scarlet)_Dragon_Dark", "5")
great_crater_of_paldea.add("Houndstone_Ghost", "5")
great_crater_of_paldea.add("Chansey_Normal", "1")
great_crater_of_paldea.add("Espeon_Psychic", "1/1/1/0")
great_crater_of_paldea.add("Pawmo_Electric_Fighting", "10")
great_crater_of_paldea.add("Dugtrio_Ground", "20")
great_crater_of_paldea.add("Umbreon_Dark", "0/0/0/1")
great_crater_of_paldea.add("Sneasel_Dark_Ice", "50")
great_crater_of_paldea.add("Sableye_Dark_Ghost", "20")
great_crater_of_paldea.add("Gabite_Dragon_Ground", "10")
great_crater_of_paldea.add("Weavile_Dark_Ice", "3")
great_crater_of_paldea.add("Zweilous (Scarlet)_Dark_Dragon", "10")
great_crater_of_paldea.add("Lycanroc (Midnight)_Rock", "20")
great_crater_of_paldea.add("Glimmet_Rock_Poison", "1")
great_crater_of_paldea.add("Flutter Mane (Scarlet)_Ghost_Fairy", "15")
great_crater_of_paldea.add("Chansey_Normal", "1")
great_crater_of_paldea.add("Espeon_Psychic", "1/1/1/0")
great_crater_of_paldea.add("Pawmo_Electric_Fighting", "10")
great_crater_of_paldea.add("Golduck_Water", "20")
great_crater_of_paldea.add("Vaporeon_Water", "1")
great_crater_of_paldea.add("Floatzel_Water", "10")
great_crater_of_paldea.add("Dugtrio_Ground", "20")
great_crater_of_paldea.add("Umbreon_Dark", "0/0/0/1")
great_crater_of_paldea.add("Sneasel_Dark_Ice", "50")
great_crater_of_paldea.add("Sableye_Dark_Ghost", "20")
great_crater_of_paldea.add("Gabite_Dragon_Ground", "10")
great_crater_of_paldea.add("Weavile_Dark_Ice", "3")
great_crater_of_paldea.add("Zweilous (Scarlet)_Dark_Dragon", "10")
great_crater_of_paldea.add("Lycanroc (Midnight)_Rock", "20")
great_crater_of_paldea.add("Glimmet_Rock_Poison", "1")
great_crater_of_paldea.add("Flutter Mane (Scarlet)_Ghost_Fairy", "15")
great_crater_of_paldea.add("Chansey_Normal", "1")
great_crater_of_paldea.add("Espeon_Psychic", "1/1/1/0")
great_crater_of_paldea.add("Pawmo_Electric_Fighting", "10")
great_crater_of_paldea.add("Dugtrio_Ground", "20")
great_crater_of_paldea.add("Umbreon_Dark", "0/0/0/1")
great_crater_of_paldea.add("Sneasel_Dark_Ice", "50")
great_crater_of_paldea.add("Sableye_Dark_Ghost", "20")
great_crater_of_paldea.add("Gabite_Dragon_Ground", "10")
great_crater_of_paldea.add("Weavile_Dark_Ice", "3")
great_crater_of_paldea.add("Deino (Scarlet)_Dark_Dragon", "30")
great_crater_of_paldea.add("Zweilous (Scarlet)_Dark_Dragon", "10")
great_crater_of_paldea.add("Lycanroc (Midnight)_Rock", "20")
great_crater_of_paldea.add("Salazzle_Poison_Fire", "5")
great_crater_of_paldea.add("Glimmet_Rock_Poison", "1")
great_crater_of_paldea.add("Flutter Mane (Scarlet)_Ghost_Fairy", "15")
great_crater_of_paldea.add("Raichu_Electric", "10")
great_crater_of_paldea.add("Venomoth_Bug_Poison", "30")
great_crater_of_paldea.add("Chansey_Normal", "1")
great_crater_of_paldea.add("Espeon_Psychic", "1/1/1/0")
great_crater_of_paldea.add("Girafarig_Normal_Psychic", "30")
great_crater_of_paldea.add("Braviary_Normal_Flying", "15")
great_crater_of_paldea.add("Volcarona_Bug_Fire", "1")
great_crater_of_paldea.add("Floette_Fairy", "15")
great_crater_of_paldea.add("Corviknight_Flying_Steel", "20")
great_crater_of_paldea.add("Pawmo_Electric_Fighting", "10")
great_crater_of_paldea.add("Farigiraf_Normal_Psychic", "10")
great_crater_of_paldea.add("Scream Tail (Scarlet)_Fairy_Psychic", "20")
great_crater_of_paldea.add("Brute Bonnet (Scarlet)_Grass_Dark", "20")
great_crater_of_paldea.add("Golduck_Water", "20")
great_crater_of_paldea.add("Vaporeon_Water", "1")
great_crater_of_paldea.add("Masquerain_Bug_Flying", "30")
great_crater_of_paldea.add("Altaria_Dragon_Flying", "30")
great_crater_of_paldea.add("Floatzel_Water", "10")
great_crater_of_paldea.add("Bisharp_Dark_Steel", "10")
great_crater_of_paldea.add("Bisharp_Dark_Steel", "20")
great_crater_of_paldea.add("Bellibolt_Electric", "30")
great_crater_of_paldea.add("Flamigo_Flying_Fighting", "20")
great_crater_of_paldea.add("Donphan_Ground", "30")
great_crater_of_paldea.add("Camerupt_Fire_Ground", "20")
great_crater_of_paldea.add("Honchkrow_Dark_Flying", "0/0/20/20")
great_crater_of_paldea.add("Braviary_Normal_Flying", "15")
great_crater_of_paldea.add("Talonflame_Fire_Flying", "30")
great_crater_of_paldea.add("Gogoat_Grass", "30")
great_crater_of_paldea.add("Hawlucha_Fighting_Flying", "60")
great_crater_of_paldea.add("Lycanroc (Midnight)_Rock", "20")
great_crater_of_paldea.add("Lokix_Bug_Dark", "30")
great_crater_of_paldea.add("Naclstack_Rock", "60")
great_crater_of_paldea.add("Garganacl_Rock", "10")
great_crater_of_paldea.add("Drakloak (Violet)_Dragon_Ghost", "5")
great_crater_of_paldea.add("Drakloak (Violet)_Dragon_Ghost", "5")
great_crater_of_paldea.add("Drakloak (Violet)_Dragon_Ghost", "5")
great_crater_of_paldea.add("Drakloak (Violet)_Dragon_Ghost", "5")
great_crater_of_paldea.add("Sandy Shocks (Scarlet)_Electric_Ground", "15")
great_crater_of_paldea.add("Iron Thorns (Violet)_Rock_Electric", "15")
great_crater_of_paldea.add("Iron Thorns (Violet)_Rock_Electric", "15")
great_crater_of_paldea.add("Iron Bundle (Violet)_Ice_Water", "20")
great_crater_of_paldea.add("Iron Hands (Violet)_Fighting_Electric", "20")
great_crater_of_paldea.add("Iron Bundle (Violet)_Ice_Water", "20")
great_crater_of_paldea.add("Iron Hands (Violet)_Fighting_Electric", "20")
great_crater_of_paldea.add("Iron Moth (Violet)_Fire_Poison", "15")
great_crater_of_paldea.add("Iron Jugulis (Violet)_Dark_Flying", "15")
great_crater_of_paldea.add("Iron Jugulis (Violet)_Dark_Flying", "15")
great_crater_of_paldea.add("Iron Jugulis (Violet)_Dark_Flying", "15")
great_crater_of_paldea.add("Iron Jugulis (Violet)_Dark_Flying", "15")
great_crater_of_paldea.add("Iron Valiant (Violet)_Fairy_Fighting", "5")
great_crater_of_paldea.add("Dugtrio_Ground", "15")
great_crater_of_paldea.add("Dunsparce_Normal", "20")
great_crater_of_paldea.add("Gabite_Dragon_Ground", "30")
great_crater_of_paldea.add("Zweilous (Scarlet)_Dark_Dragon", "20")
great_crater_of_paldea.add("Drakloak (Violet)_Dragon_Ghost", "20")
great_crater_of_paldea.add("Garganacl_Rock", "20")
great_crater_of_paldea.add("Hypno_Psychic", "20")
great_crater_of_paldea.add("Espathra_Psychic", "5")
great_crater_of_paldea.add("Glimmora_Rock_Poison", "40")
great_crater_of_paldea.add("Dudunsparce_Normal", "2")
great_crater_of_paldea.add("Great Tusk (Scarlet)_Ground_Fighting", "10")
great_crater_of_paldea.add("Scream Tail (Scarlet)_Fairy_Psychic", "20")
great_crater_of_paldea.add("Scream Tail (Scarlet)_Fairy_Psychic", "20")
great_crater_of_paldea.add("Brute Bonnet (Scarlet)_Grass_Dark", "10")
great_crater_of_paldea.add("Flutter Mane (Scarlet)_Ghost_Fairy", "3")
great_crater_of_paldea.add("Iron Treads (Violet)_Ground_Steel", "10")
great_crater_of_paldea.add("Iron Bundle (Violet)_Ice_Water", "20")
great_crater_of_paldea.add("Iron Bundle (Violet)_Ice_Water", "20")
great_crater_of_paldea.add("Iron Hands (Violet)_Fighting_Electric", "10")
great_crater_of_paldea.add("Iron Jugulis (Violet)_Dark_Flying", "3")
great_crater_of_paldea.add("Roaring Moon (Scarlet)_Dragon_Dark", "1")
great_crater_of_paldea.add("Iron Valiant (Violet)_Fairy_Fighting", "1")

inlet_grotto = Area("Inlet Grotto")
inlet_grotto.add("Diglett_Ground", "20")
inlet_grotto.add("Houndour_Dark_Fire", "60")
inlet_grotto.add("Yungoos_Normal", "60")


north_paldean_sea = Area("North Paldean Sea")
north_paldean_sea.add("Clauncher (Violet)_Water", "60")
north_paldean_sea.add("Clawitzer (Violet)_Water", "20")
north_paldean_sea.add("Eiscue (Violet)_Ice", "50")
north_paldean_sea.add("Shellder_Water", "60")
north_paldean_sea.add("Cloyster_Water_Ice", "10")
north_paldean_sea.add("Magikarp_Water", "60")
north_paldean_sea.add("Gyarados_Water_Flying", "5")
north_paldean_sea.add("Qwilfish_Water_Poison", "30")
north_paldean_sea.add("Pelipper_Water_Flying", "40")
north_paldean_sea.add("Floatzel_Water", "40")
north_paldean_sea.add("Lumineon_Water", "30")
north_paldean_sea.add("Alomomola_Water", "20")
north_paldean_sea.add("Tynamo_Electric", "60")
north_paldean_sea.add("Eelektrik_Electric", "30")
north_paldean_sea.add("Skrelp (Scarlet)_Poison_Water", "60")
north_paldean_sea.add("Dragalge (Scarlet)_Poison_Water", "20")
north_paldean_sea.add("Bergmite_Ice", "60")
north_paldean_sea.add("Avalugg_Ice", "20")
north_paldean_sea.add("Barraskewda_Water", "20")
north_paldean_sea.add("Finizen_Water", "30")
north_paldean_sea.add("Kilowattrel_Electric_Flying", "30")


north_province_area_one = Area("North Province (Area One)")
north_province_area_one.add("Wigglytuff_Normal_Fairy", "5")
north_province_area_one.add("Haunter_Ghost_Poison", "0/0/0/40")
north_province_area_one.add("Chansey_Normal", "1")
north_province_area_one.add("Flareon_Fire", "1")
north_province_area_one.add("Ampharos_Electric", "10")
north_province_area_one.add("Ursaring_Normal", "20")
north_province_area_one.add("Grumpig_Psychic", "20")
north_province_area_one.add("Altaria_Dragon_Flying", "20")
north_province_area_one.add("Clawitzer (Violet)_Water", "20")
north_province_area_one.add("Eiscue (Violet)_Ice", "50")
north_province_area_one.add("Eiscue (Violet)_Ice", "40")
north_province_area_one.add("Mismagius (Violet)_Ghost", "0/0/0/3")
north_province_area_one.add("Drakloak (Violet)_Dragon_Ghost", "25")
north_province_area_one.add("Drakloak (Violet)_Dragon_Ghost", "5")
north_province_area_one.add("Drifblim (Scarlet)_Ghost_Flying", "0/0/30/30")
north_province_area_one.add("Honchkrow_Dark_Flying", "0/0/20/20")
north_province_area_one.add("Lucario_Fighting_Steel", "3")
north_province_area_one.add("Gallade_Psychic_Fighting", "1/1/1/0")
north_province_area_one.add("Sawsbuck_Normal_Grass", "60")
north_province_area_one.add("Fraxure_Dragon", "20")
north_province_area_one.add("Rufflet_Normal_Flying", "25")
north_province_area_one.add("Gogoat_Grass", "40")
north_province_area_one.add("Hawlucha_Fighting_Flying", "60")
north_province_area_one.add("Lycanroc (Midday)_Rock", "20/20/0/0")
north_province_area_one.add("Lycanroc (Midnight)_Rock", "0/0/0/20")
north_province_area_one.add("Lycanroc (Dusk)_Rock", "0/0/1/0")
north_province_area_one.add("Mudsdale_Ground", "12")
north_province_area_one.add("Indeedee (Male)_Psychic_Normal", "30")
north_province_area_one.add("Indeedee (Female)_Psychic_Normal", "30")
north_province_area_one.add("Lokix_Bug_Dark", "20")
north_province_area_one.add("Pawmo_Electric_Fighting", "15")
north_province_area_one.add("Brambleghast_Grass_Ghost", "1")
north_province_area_one.add("Scovillain_Grass_Fire", "10")
north_province_area_one.add("Espathra_Psychic", "20")
north_province_area_one.add("Tinkatuff_Fairy_Steel", "10")
north_province_area_one.add("Houndstone_Ghost", "15")
north_province_area_one.add("Haunter_Ghost_Poison", "0/0/0/50")
north_province_area_one.add("Glalie_Ice", "20")
north_province_area_one.add("Bronzong_Steel_Psychic", "20")
north_province_area_one.add("Weavile_Dark_Ice", "15")
north_province_area_one.add("Glaceon_Ice", "1")
north_province_area_one.add("Froslass_Ice", "2")
north_province_area_one.add("Sawsbuck_Normal_Grass", "30")
north_province_area_one.add("Beartic_Ice", "20")
north_province_area_one.add("Frosmoth_Ice_Bug", "10")
north_province_area_one.add("Houndstone_Ghost", "10")
north_province_area_one.add("Cetitan_Ice", "10")
north_province_area_one.add("Golduck_Water", "20")
north_province_area_one.add("Vaporeon_Water", "1")
north_province_area_one.add("Dratini_Dragon", "15")
north_province_area_one.add("Altaria_Dragon_Flying", "20")
north_province_area_one.add("Whiscash_Water_Ground", "10")
north_province_area_one.add("Flamigo_Flying_Fighting", "10")
north_province_area_one.add("Clodsire_Poison_Ground", "30")
north_province_area_one.add("Golduck_Water", "20")
north_province_area_one.add("Vaporeon_Water", "1")
north_province_area_one.add("Floatzel_Water", "10")
north_province_area_one.add("Fraxure_Dragon", "5")
north_province_area_one.add("Bellibolt_Electric", "5")
north_province_area_one.add("Cloyster_Water_Ice", "10")
north_province_area_one.add("Gyarados_Water_Flying", "5")
north_province_area_one.add("Floatzel_Water", "40")
north_province_area_one.add("Alomomola_Water", "20")
north_province_area_one.add("Skrelp (Scarlet)_Poison_Water", "60")
north_province_area_one.add("Dragalge (Scarlet)_Poison_Water", "20")
north_province_area_one.add("Kilowattrel_Electric_Flying", "30")
north_province_area_one.add("Primeape_Fighting", "10")
north_province_area_one.add("Grumpig_Psychic", "20")
north_province_area_one.add("Honchkrow_Dark_Flying", "0/0/20/20")
north_province_area_one.add("Lucario_Fighting_Steel", "3")
north_province_area_one.add("Gogoat_Grass", "30")
north_province_area_one.add("Hawlucha_Fighting_Flying", "60")
north_province_area_one.add("Noibat_Flying_Dragon", "10")
north_province_area_one.add("Noivern_Flying_Dragon", "20")
north_province_area_one.add("Copperajah_Steel", "20")
north_province_area_one.add("Lokix_Bug_Dark", "30")
north_province_area_one.add("Naclstack_Rock", "60")
north_province_area_one.add("Revavroom_Steel_Poison", "20")
north_province_area_one.add("Dugtrio_Ground", "20")
north_province_area_one.add("Umbreon_Dark", "0/0/0/1")
north_province_area_one.add("Sableye_Dark_Ghost", "20")
north_province_area_one.add("Gabite_Dragon_Ground", "10")
north_province_area_one.add("Deino (Scarlet)_Dark_Dragon", "30")
north_province_area_one.add("Zweilous (Scarlet)_Dark_Dragon", "10")
north_province_area_one.add("Noibat_Flying_Dragon", "60")
north_province_area_one.add("Noivern_Flying_Dragon", "30")
north_province_area_one.add("Salazzle_Poison_Fire", "5")
north_province_area_one.add("Glimmet_Rock_Poison", "1")
north_province_area_one.add("Floatzel_Water", "10")
north_province_area_one.add("Pincurchin_Electric", "10")
north_province_area_one.add("Naclstack_Rock", "20")
north_province_area_one.add("Kilowattrel_Electric_Flying", "30")
north_province_area_one.add("Wugtrio_Water", "20")
north_province_area_one.add("Chansey_Normal", "1")
north_province_area_one.add("Jumpluff_Grass_Flying", "20")
north_province_area_one.add("Sunflora_Grass", "30/30/30/0")
north_province_area_one.add("Blissey_Normal", "1")
north_province_area_one.add("Vespiquen_Bug_Flying", "20")
north_province_area_one.add("Vivillon_Bug_Flying", "30")
north_province_area_one.add("Floette_Fairy", "55")
north_province_area_one.add("Floette_Fairy", "55")
north_province_area_one.add("Floette_Fairy", "55")
north_province_area_one.add("Floette_Fairy", "55")
north_province_area_one.add("Floette_Fairy", "3")
north_province_area_one.add("Lurantis_Grass", "30")
north_province_area_one.add("Haunter_Ghost_Poison", "0/0/0/50")
north_province_area_one.add("Bronzong_Steel_Psychic", "20")
north_province_area_one.add("Houndstone_Ghost", "5")

north_province_area_two = Area("North Province (Area Two)")
north_province_area_two.add("Mismagius (Violet)_Ghost", "0/0/0/3")
north_province_area_two.add("Drakloak (Violet)_Dragon_Ghost", "25")
north_province_area_two.add("Golduck_Water", "20")
north_province_area_two.add("Scyther_Bug_Flying", "30")
north_province_area_two.add("Vaporeon_Water", "1")
north_province_area_two.add("Passimian (Violet)_Fighting", "15")
north_province_area_two.add("Dratini_Dragon", "15")
north_province_area_two.add("Altaria_Dragon_Flying", "20")
north_province_area_two.add("Arcanine_Fire", "2")
north_province_area_two.add("Houndoom_Dark_Fire", "20")
north_province_area_two.add("Camerupt_Fire_Ground", "20")
north_province_area_two.add("Grumpig_Psychic", "20")
north_province_area_two.add("Luxray_Electric", "10")
north_province_area_two.add("Honchkrow_Dark_Flying", "0/0/20/20")
north_province_area_two.add("Lucario_Fighting_Steel", "3")
north_province_area_two.add("Bisharp_Dark_Steel", "10")
north_province_area_two.add("Bisharp_Dark_Steel", "20")
north_province_area_two.add("Gogoat_Grass", "30")
north_province_area_two.add("Hawlucha_Fighting_Flying", "60")
north_province_area_two.add("Noibat_Flying_Dragon", "10")
north_province_area_two.add("Noivern_Flying_Dragon", "20")
north_province_area_two.add("Copperajah_Steel", "20")
north_province_area_two.add("Lokix_Bug_Dark", "30")
north_province_area_two.add("Naclstack_Rock", "60")
north_province_area_two.add("Dugtrio_Ground", "20")
north_province_area_two.add("Umbreon_Dark", "0/0/0/1")
north_province_area_two.add("Houndoom_Dark_Fire", "20")
north_province_area_two.add("Sableye_Dark_Ghost", "20")
north_province_area_two.add("Gabite_Dragon_Ground", "10")
north_province_area_two.add("Deino (Scarlet)_Dark_Dragon", "30")
north_province_area_two.add("Zweilous (Scarlet)_Dark_Dragon", "10")
north_province_area_two.add("Noibat_Flying_Dragon", "60")
north_province_area_two.add("Noivern_Flying_Dragon", "30")
north_province_area_two.add("Salazzle_Poison_Fire", "5")
north_province_area_two.add("Glimmet_Rock_Poison", "1")
north_province_area_two.add("Chansey_Normal", "1")
north_province_area_two.add("Jumpluff_Grass_Flying", "20")
north_province_area_two.add("Blissey_Normal", "1")
north_province_area_two.add("Vespiquen_Bug_Flying", "20")
north_province_area_two.add("Vivillon_Bug_Flying", "30")
north_province_area_two.add("Floette_Fairy", "55")
north_province_area_two.add("Floette_Fairy", "55")
north_province_area_two.add("Floette_Fairy", "55")
north_province_area_two.add("Floette_Fairy", "55")
north_province_area_two.add("Floette_Fairy", "3")
north_province_area_two.add("Lurantis_Grass", "30")
north_province_area_two.add("Venomoth_Bug_Poison", "0/0/0/20")
north_province_area_two.add("Arcanine_Fire", "2")
north_province_area_two.add("Scyther_Bug_Flying", "50")
north_province_area_two.add("Heracross_Bug_Fighting", "10")
north_province_area_two.add("Ursaring_Normal", "20")
north_province_area_two.add("Kricketune_Bug", "30")
north_province_area_two.add("Luxray_Electric", "40")
north_province_area_two.add("Foongus_Grass_Normal", "15")
north_province_area_two.add("Amoonguss_Grass_Poison", "15")
north_province_area_two.add("Bisharp_Dark_Steel", "15")
north_province_area_two.add("Bisharp_Dark_Steel", "20")
north_province_area_two.add("Oranguru (Scarlet)_Normal_Psychic", "15")
north_province_area_two.add("Falinks_Fighting", "20")
north_province_area_two.add("Spidops_Bug", "20")
north_province_area_two.add("Lokix_Bug_Dark", "60")
north_province_area_two.add("Bronzong_Steel_Psychic", "20")
north_province_area_two.add("Falinks_Fighting", "40")
north_province_area_two.add("Houndstone_Ghost", "5")

north_province_area_three = Area("North Province (Area Three)")
north_province_area_three.add("Chansey_Normal", "1")
north_province_area_three.add("Jumpluff_Grass_Flying", "30")
north_province_area_three.add("Espeon_Psychic", "1/1/1/0")
north_province_area_three.add("Pawmo_Electric_Fighting", "10")
north_province_area_three.add("Glalie_Ice", "20")
north_province_area_three.add("Bronzong_Steel_Psychic", "20")
north_province_area_three.add("Glaceon_Ice", "1")
north_province_area_three.add("Froslass_Ice", "2")
north_province_area_three.add("Beartic_Ice", "20")
north_province_area_three.add("Frosmoth_Ice_Bug", "10")
north_province_area_three.add("Houndstone_Ghost", "10")
north_province_area_three.add("Cetitan_Ice", "10")
north_province_area_three.add("Golduck_Water", "20")
north_province_area_three.add("Vaporeon_Water", "1")
north_province_area_three.add("Floatzel_Water", "10")
north_province_area_three.add("Barraskewda_Water", "20")
north_province_area_three.add("Bellibolt_Electric", "5")
north_province_area_three.add("Drakloak (Violet)_Dragon_Ghost", "5")
north_province_area_three.add("Flamigo_Flying_Fighting", "12")
north_province_area_three.add("Cloyster_Water_Ice", "10")
north_province_area_three.add("Gyarados_Water_Flying", "5")
north_province_area_three.add("Floatzel_Water", "40")
north_province_area_three.add("Alomomola_Water", "20")
north_province_area_three.add("Clawitzer (Violet)_Water", "20")
north_province_area_three.add("Eiscue (Violet)_Ice", "50")
north_province_area_three.add("Eiscue (Violet)_Ice", "40")
north_province_area_three.add("Skrelp (Scarlet)_Poison_Water", "60")
north_province_area_three.add("Dragalge (Scarlet)_Poison_Water", "20")
north_province_area_three.add("Barraskewda_Water", "20")
north_province_area_three.add("Kilowattrel_Electric_Flying", "30")
north_province_area_three.add("Hariyama_Fighting", "15")
north_province_area_three.add("Honchkrow_Dark_Flying", "0/0/20/20")
north_province_area_three.add("Gogoat_Grass", "30")
north_province_area_three.add("Hawlucha_Fighting_Flying", "60")
north_province_area_three.add("Copperajah_Steel", "20")
north_province_area_three.add("Lokix_Bug_Dark", "30")
north_province_area_three.add("Naclstack_Rock", "60")
north_province_area_three.add("Dugtrio_Ground", "20")
north_province_area_three.add("Umbreon_Dark", "0/0/0/1")
north_province_area_three.add("Hariyama_Fighting", "10")
north_province_area_three.add("Sableye_Dark_Ghost", "20")
north_province_area_three.add("Gabite_Dragon_Ground", "10")
north_province_area_three.add("Deino (Scarlet)_Dark_Dragon", "30")
north_province_area_three.add("Zweilous (Scarlet)_Dark_Dragon", "10")
north_province_area_three.add("Salazzle_Poison_Fire", "5")
north_province_area_three.add("Glimmet_Rock_Poison", "1")
north_province_area_three.add("Floatzel_Water", "10")
north_province_area_three.add("Pincurchin_Electric", "10")
north_province_area_three.add("Wugtrio_Water", "20")
north_province_area_three.add("Kilowattrel_Electric_Flying", "30")
north_province_area_three.add("Naclstack_Rock", "20")
north_province_area_three.add("Chansey_Normal", "1")
north_province_area_three.add("Jumpluff_Grass_Flying", "20")
north_province_area_three.add("Sunflora_Grass", "30/30/30/0")
north_province_area_three.add("Blissey_Normal", "1")
north_province_area_three.add("Vespiquen_Bug_Flying", "20")
north_province_area_three.add("Lilligant_Grass", "5")
north_province_area_three.add("Vivillon_Bug_Flying", "30")
north_province_area_three.add("Floette_Fairy", "55")
north_province_area_three.add("Floette_Fairy", "55")
north_province_area_three.add("Floette_Fairy", "55")
north_province_area_three.add("Floette_Fairy", "55")
north_province_area_three.add("Floette_Fairy", "3")
north_province_area_three.add("Florges_Fairy", "1")
north_province_area_three.add("Florges_Fairy", "1")
north_province_area_three.add("Florges_Fairy", "1")
north_province_area_three.add("Florges_Fairy", "1")
north_province_area_three.add("Florges_Fairy", "1")
north_province_area_three.add("Dedenne_Electric_Fairy", "10")
north_province_area_three.add("Lurantis_Grass", "30")


poco_path = Area("Poco Path")
poco_path.add("Hoppip_Grass_Flying", "60")
poco_path.add("Fletchling_Normal_Flying", "60")
poco_path.add("Scatterbug_Bug", "60")
poco_path.add("Lechonk_Normal", "80")
poco_path.add("Tarountula_Bug", "50")
poco_path.add("Pawmi_Electric", "5")
poco_path.add("Magikarp_Water", "60")
poco_path.add("Wingull_Water_Flying", "80")
poco_path.add("Buizel_Water", "20")
poco_path.add("Arrokuda_Water", "60")
poco_path.add("Wingull_Water_Flying", "60")
poco_path.add("Buizel_Water", "20")


socarrat_trail = Area("Socarrat Trail")
socarrat_trail.add("Raichu_Electric", "5")
socarrat_trail.add("Jolteon_Electric", "1")
socarrat_trail.add("Sudowoodo_Rock", "60")
socarrat_trail.add("Forretress_Bug_Steel", "20")
socarrat_trail.add("Heracross_Bug_Fighting", "30")
socarrat_trail.add("Slaking_Normal", "5")
socarrat_trail.add("Honchkrow_Dark_Flying", "0/0/20/20")
socarrat_trail.add("Skuntank (Scarlet)_Poison_Dark", "20")
socarrat_trail.add("Leafeon_Grass", "1")
socarrat_trail.add("Zoroark_Dark", "10")
socarrat_trail.add("Sawsbuck_Normal_GrassAutumn Form", "50")
socarrat_trail.add("Amoonguss_Grass_Poison", "30")
socarrat_trail.add("Lurantis_Grass", "30")
socarrat_trail.add("Spidops_Bug", "30")
socarrat_trail.add("Mabosstiff_Dark", "20")
socarrat_trail.add("Brambleghast_Grass_Ghost", "1")
socarrat_trail.add("Toedscool_Ground_Grass", "150")
socarrat_trail.add("Toedscruel_Ground_Grass", "40")


south_paldean_sea = Area("South Paldean Sea")
south_paldean_sea.add("Shellder_Water", "60")
south_paldean_sea.add("Magikarp_Water", "60")
south_paldean_sea.add("Gyarados_Water_Flying", "5")
south_paldean_sea.add("Qwilfish_Water_Poison", "30")
south_paldean_sea.add("Wingull_Water_Flying", "80")
south_paldean_sea.add("Clauncher (Violet)_Water", "60")
south_paldean_sea.add("Luvdisc_Water", "60")
south_paldean_sea.add("Buizel_Water", "20")
south_paldean_sea.add("Bruxish_Water_Psychic", "30")
south_paldean_sea.add("Arrokuda_Water", "60")
south_paldean_sea.add("Wattrel_Electric_Flying", "60")
south_paldean_sea.add("Finizen_Water", "30")


south_province_area_one = Area("South Province (Area One)")
south_province_area_one.add("Hoppip_Grass_Flying", "60")
south_province_area_one.add("Happiny_Normal", "1")
south_province_area_one.add("Fletchling_Normal_Flying", "60")
south_province_area_one.add("Scatterbug_Bug", "60")
south_province_area_one.add("Lechonk_Normal", "80")
south_province_area_one.add("Tarountula_Bug", '50')
south_province_area_one.add("Pawmi_Electric", "5")
south_province_area_one.add("Pachirisu_Electric", "10")
south_province_area_one.add("Pichu_Electric", "10")
south_province_area_one.add("Bonsly_Rock", "30")
south_province_area_one.add("Bounsweet_Grass", "60")
south_province_area_one.add("Skwovet_Normal", "50")
south_province_area_one.add("Lechonk_Normal", '60')
south_province_area_one.add("Tarountula_Bug", "60")
south_province_area_one.add("Shroodle_Poison_Normal", "20")
south_province_area_one.add("Igglybuff_Normal_Fairy", "60")
south_province_area_one.add("Ralts_Psychic_Fairy", "5/5/5/0")
south_province_area_one.add("Fidough_Fairy", "50")
south_province_area_one.add("Psyduck_Water", "60")
south_province_area_one.add("Magikarp_Water", "60")
south_province_area_one.add("Wooper_Poison_Ground", "60")
south_province_area_one.add("Surskit_Bug_Water", "60")
south_province_area_one.add("Azurill_Normal_Fairy", "60")
south_province_area_one.add("Chewtle_Water", "10")
south_province_area_one.add("Psyduck_Water", "60")
south_province_area_one.add("Magikarp_Water", "20")
south_province_area_one.add("Surskit_Bug_Water", "60")
south_province_area_one.add("Azurill_Normal_Fairy", "60")
south_province_area_one.add("Buizel_Water", "20")
south_province_area_one.add("Arrokuda_Water", "40")
south_province_area_one.add("Magikarp_Water", "60")
south_province_area_one.add("Wingull_Water_Flying", "80")
south_province_area_one.add("Buizel_Water", "20")
south_province_area_one.add("Arrokuda_Water", "60")
south_province_area_one.add("Wingull_Water_Flying", "60")
south_province_area_one.add("Buizel_Water", "20")
south_province_area_one.add("Sunkern_Grass", "60/60/60/0")
south_province_area_one.add("Combee_Bug_Flying", "40")
south_province_area_one.add("Happiny_Normal", "2")
south_province_area_one.add("Spewpa_Bug", "30")
south_province_area_one.add("Oricorio (Pom-Pom Style)_Electric_Flying", "20")
south_province_area_one.add("Gastly_Ghost_Poison", "15")
south_province_area_one.add("Drowzee_Psychic", "40")


south_province_area_two = Area("South Province (Area Two)")
south_province_area_two.add("Misdreavus (Violet)_Ghost", "0/0/0/15")
south_province_area_two.add("Mareep_Electric", "60")
south_province_area_two.add("Hoppip_Grass_Flying", "60")
south_province_area_two.add("Starly_Normal_Flying", "20/20/20/0")
south_province_area_two.add("Happiny_Normal", "1")
south_province_area_two.add("Fletchling_Normal_Flying", "60")
south_province_area_two.add("Maschiff_Dark", "30")
south_province_area_two.add("Pikachu_Electric", "10")
south_province_area_two.add("Pichu_Electric", "10")
south_province_area_two.add("Bonsly_Rock", "30")
south_province_area_two.add("Bounsweet_Grass", "60")
south_province_area_two.add("Skwovet_Normal", "50")
south_province_area_two.add("Applin_Grass_Dragon", "10")
south_province_area_two.add("Shroodle_Poison_Normal", "20")
south_province_area_two.add("Jigglypuff_Normal_Fairy", "60")
south_province_area_two.add("Igglybuff_Normal_Fairy", "60")
south_province_area_two.add("Fidough_Fairy", "50")
south_province_area_two.add("Gastly_Ghost_Poison", "0/0/0/50")
south_province_area_two.add("Skiddo_Grass", "60")
south_province_area_two.add("Rockruff (Standard)_Rock", "40")
south_province_area_two.add("Rockruff (Own Tempo)_Rock", "2")
south_province_area_two.add("Psyduck_Water", "60")
south_province_area_two.add("Magikarp_Water", "20")
south_province_area_two.add("Azurill_Normal_Fairy", "60")
south_province_area_two.add("Buizel_Water", "20")
south_province_area_two.add("Chewtle_Water", "10")
south_province_area_two.add("Arrokuda_Water", "40")
south_province_area_two.add("Tadbulb_Electric", "50")
south_province_area_two.add("Makuhita_Fighting", "30")
south_province_area_two.add("Yungoos_Normal", "20")
south_province_area_two.add("Nacli_Rock", "60")
south_province_area_two.add("Sunkern_Grass", "60/60/60/0")
south_province_area_two.add("Combee_Bug_Flying", "40")
south_province_area_two.add("Happiny_Normal", "1")
south_province_area_two.add("Flabebe_Fairy", "60")
south_province_area_two.add("Flabebe_Fairy", "60")
south_province_area_two.add("Flabebe_Fairy", "60")
south_province_area_two.add("Flabebe_Fairy", "60")
south_province_area_two.add("Flabebe_Fairy", "6")
south_province_area_two.add("Diglett_Ground", "50")
south_province_area_two.add("Eevee_Normal", "5")
south_province_area_two.add("Mareep_Electric", "30")
south_province_area_two.add("Starly_Normal_Flying", "30/30/30/0")
south_province_area_two.add("Kricketot_Bug", "30")
south_province_area_two.add("Combee_Bug_Flying", "30")
south_province_area_two.add("Skwovet_Normal", "30")
south_province_area_two.add("Smoliv_Grass_Normal", "100")
south_province_area_two.add("Gastly_Ghost_Poison", "15")
south_province_area_two.add("Drowzee_Psychic", "40")
south_province_area_two.add("Bronzor_Steel_Psychic", "60")
south_province_area_two.add("Maschiff_Dark", "50")
south_province_area_two.add("Tinkatink_Fairy_Steel", "15")


south_province_area_three = Area("South Province (Area Three)")
south_province_area_three.add("Murkrow_Dark_Flying", "0/0/40/40")
south_province_area_three.add("Dunsparce_Normal", "2")
south_province_area_three.add("Gulpin (Violet)_Poison", "20")
south_province_area_three.add("Gulpin (Violet)_Poison", "60")
south_province_area_three.add("Happiny_Normal", "1")
south_province_area_three.add("Rookidee_Flying", "30")
south_province_area_three.add("Nymble_Bug", "60")
south_province_area_three.add("Pawmi_Electric", "5")
south_province_area_three.add("Murkrow_Dark_Flying", "0/0/60/60")
south_province_area_three.add("Shuppet_Ghost", "0/0/0/70")
south_province_area_three.add("Drifloon (Scarlet)_Ghost_Flying", "0/0/40/40")
south_province_area_three.add("Oricorio (Baile Style)_Fire_Flying", "40")
south_province_area_three.add("Rookidee_Flying", "30")
south_province_area_three.add("Tandemaus_Normal", "10")
south_province_area_three.add("Squawkabilly_Normal_Flying", "20")
south_province_area_three.add("Squawkabilly_Normal_Flying", "15")
south_province_area_three.add("Squawkabilly_Normal_Flying", "10")
south_province_area_three.add("Squawkabilly_Normal_Flying", "5")
south_province_area_three.add("Growlithe_Fire", "20")
south_province_area_three.add("Makuhita_Fighting", "30")
south_province_area_three.add("Spoink_Psychic", "20")
south_province_area_three.add("Shinx_Electric", "60")
south_province_area_three.add("Skiddo_Grass", "50")
south_province_area_three.add("Yungoos_Normal", "20")
south_province_area_three.add("Rookidee_Flying", "30")
south_province_area_three.add("Pawmi_Electric", "5")
south_province_area_three.add("Nacli_Rock", "60")
south_province_area_three.add("Charcadet_Fire", "1")
south_province_area_three.add("Klawf_Rock", "30")
south_province_area_three.add("Gastly_Ghost_Poison", "15")
south_province_area_three.add("Drowzee_Psychic", "40")
south_province_area_three.add("Bronzor_Steel_Psychic", "60")
south_province_area_three.add("Tinkatink_Fairy_Steel", "15")


south_province_area_four = Area("South Province (Area Four)")
south_province_area_four.add("Murkrow_Dark_Flying", "0/0/40/40")
south_province_area_four.add("Misdreavus (Violet)_Ghost", "0/0/0/15")
south_province_area_four.add("Misdreavus (Violet)_Ghost", "0/0/0/60")
south_province_area_four.add("Dreepy (Violet)_Dragon_Ghost", "5")
south_province_area_four.add("Dunsparce_Normal", "10")
south_province_area_four.add("Starly_Normal_Flying", "20/20/20/0")
south_province_area_four.add("Staravia_Normal_Flying", "30/30/30/0")
south_province_area_four.add("Pachirisu_Electric", "10")
south_province_area_four.add("Dunsparce_Normal", "5")
south_province_area_four.add("Deerling_Normal_Grass", "40")
south_province_area_four.add("Fletchinder_Fire_Flying", "30")
south_province_area_four.add("Toxel_Electric_Poison", "60")
south_province_area_four.add("Lechonk_Normal", "80")
south_province_area_four.add("Tarountula_Bug", "50")
south_province_area_four.add("Pawmo_Electric_Fighting", "10")
south_province_area_four.add("Maschiff_Dark", "30")
south_province_area_four.add("Toedscool_Ground_Grass", "2")
south_province_area_four.add("Pikachu_Electric", "10")
south_province_area_four.add("Murkrow_Dark_Flying", "0/0/20/20")
south_province_area_four.add("Pineco_Bug", "60")
south_province_area_four.add("Dunsparce_Normal", "4")
south_province_area_four.add("Pachirisu_Electric", "40")
south_province_area_four.add("Komala_Normal", "30")
south_province_area_four.add("Applin_Grass_Dragon", "10")
south_province_area_four.add("Lechonk_Normal", "60")
south_province_area_four.add("Tarountula_Bug", "60")
south_province_area_four.add("Charcadet_Fire", "1")
south_province_area_four.add("Shroodle_Poison_Normal", "20")
south_province_area_four.add("Toedscool_Ground_Grass", "10")
south_province_area_four.add("Gastly_Ghost_Poison", "0/0/0/50")
south_province_area_four.add("Phanpy_Ground", "20")
south_province_area_four.add("Meditite_Fighting_Psychic", "60")
south_province_area_four.add("Swablu_Normal_Flying", "70")
south_province_area_four.add("Drifloon (Scarlet)_Ghost_Flying", "0/0/30/30")
south_province_area_four.add("Riolu_Fighting", "20")
south_province_area_four.add("Rufflet_Normal_Flying", "25")
south_province_area_four.add("Skiddo_Grass", "30")
south_province_area_four.add("Rockruff (Standard)_Rock", "40")
south_province_area_four.add("Rockruff (Own Tempo)_Rock", "2")
south_province_area_four.add("Mudbray_Ground", "60")
south_province_area_four.add("Toxel_Electric_Poison", "40")
south_province_area_four.add("Pawmo_Electric_Fighting", "15")
south_province_area_four.add("Charcadet_Fire", "1")
south_province_area_four.add("Lechonk_Normal", "60")
south_province_area_four.add("Psyduck_Water", "60")
south_province_area_four.add("Scyther_Bug_Flying", "30")
south_province_area_four.add("Magikarp_Water", "60")
south_province_area_four.add("Marill_Water_Fairy", "60")
south_province_area_four.add("Wooper_Poison_Ground", "60")
south_province_area_four.add("Dunsparce_Normal", "5")
south_province_area_four.add("Phanpy_Ground", "40")
south_province_area_four.add("Barboach_Water_Ground", "60")
south_province_area_four.add("Basculin (Red-Striped)_Water", "60")
south_province_area_four.add("Basculin (Blue-Striped)_Water", "60")
south_province_area_four.add("Goomy_Dragon", "40")
south_province_area_four.add("Chewtle_Water", "10")
south_province_area_four.add("Hatenna_Psychic", "40")
south_province_area_four.add("Psyduck_Water", "60")
south_province_area_four.add("Magikarp_Water", "20")
south_province_area_four.add("Marill_Water_Fairy", "60")
south_province_area_four.add("Buizel_Water", "20")
south_province_area_four.add("Basculin (Red-Striped)_Water", "60")
south_province_area_four.add("Basculin (Blue-Striped)_Water", "60")
south_province_area_four.add("Chewtle_Water", "10")
south_province_area_four.add("Arrokuda_Water", "40")
south_province_area_four.add("Tadbulb_Electric", "50")
south_province_area_four.add("Shellder_Water", "60")
south_province_area_four.add("Magikarp_Water", "60")
south_province_area_four.add("Gyarados_Water_Flying", "5")
south_province_area_four.add("Qwilfish_Water_Poison", "30")
south_province_area_four.add("Luvdisc_Water", "60")
south_province_area_four.add("Buizel_Water", "20")
south_province_area_four.add("Arrokuda_Water", "60")
south_province_area_four.add("Wattrel_Electric_Flying", "60")
south_province_area_four.add("Finizen_Water", "30")
south_province_area_four.add("Houndour_Dark_Fire", "60")
south_province_area_four.add("Makuhita_Fighting", "30")
south_province_area_four.add("Skiddo_Grass", "50")
south_province_area_four.add("Yungoos_Normal", "20")
south_province_area_four.add("Gumshoos_Normal", "30")
south_province_area_four.add("Nacli_Rock", "60")
south_province_area_four.add("Charcadet_Fire", "1")
south_province_area_four.add("Combee_Bug_Flying", "40")
south_province_area_four.add("Petilil_Grass", "40")
south_province_area_four.add("Spewpa_Bug", "30")
south_province_area_four.add("Flabebe_Fairy", "60")
south_province_area_four.add("Flabebe_Fairy", "60")
south_province_area_four.add("Flabebe_Fairy", "60")
south_province_area_four.add("Flabebe_Fairy", "60")
south_province_area_four.add("Flabebe_Fairy", "6")
south_province_area_four.add("Floette_Fairy", "55")
south_province_area_four.add("Floette_Fairy", "55")
south_province_area_four.add("Floette_Fairy", "55")
south_province_area_four.add("Floette_Fairy", "55")
south_province_area_four.add("Floette_Fairy", "3")
south_province_area_four.add("Gastly_Ghost_Poison", "15")
south_province_area_four.add("Bronzor_Steel_Psychic", "60")
south_province_area_four.add("Maschiff_Dark", "50")
south_province_area_four.add("Tinkatink_Fairy_Steel", "15")


south_province_area_five = Area("South Province (Area Five)")
south_province_area_five.add("Misdreavus (Violet)_Ghost", "0/0/0/15")
south_province_area_five.add("Misdreavus (Violet)_Ghost", "0/0/0/60")
south_province_area_five.add("Mankey_Fighting", "60")
south_province_area_five.add("Skiploom_Grass_Flying", "40")
south_province_area_five.add("Murkrow_Dark_Flying", "0/0/40/40")
south_province_area_five.add("Dunsparce_Normal", "2")
south_province_area_five.add("Stantler_Normal", "20")
south_province_area_five.add("Bagon (Violet)_Dragon", "50")
south_province_area_five.add("Clauncher (Violet)_Water", "60")
south_province_area_five.add("Shroomish_Grass", "30")
south_province_area_five.add("Slakoth_Normal", "10")
south_province_area_five.add("Dreepy (Violet)_Dragon_Ghost", "5")
south_province_area_five.add("Dreepy (Violet)_Dragon_Ghost", "15")
south_province_area_five.add("Dreepy (Violet)_Dragon_Ghost", "20")
south_province_area_five.add("Vigoroth_Normal", "20")
south_province_area_five.add("Zangoose_Normal", "5")
south_province_area_five.add("Seviper_Poison", "15")
south_province_area_five.add("Luxio_Electric", "20")
south_province_area_five.add("Pachirisu_Electric", "10")
south_province_area_five.add("Stunky (Scarlet)_Poison_Dark", "30")
south_province_area_five.add("Deerling_Normal_Grass", "40")
south_province_area_five.add("Fletchinder_Fire_Flying", "30")
south_province_area_five.add("Litleo_Fire_Normal", "60")
south_province_area_five.add("Rookidee_Flying", "30")
south_province_area_five.add("Corvisquire_Flying", "20")
south_province_area_five.add("Lechonk_Normal", "80")
south_province_area_five.add("Oinkologne (Male)_Normal", "20")
south_province_area_five.add("Oinkologne (Female)_Normal", "20")
south_province_area_five.add("Tarountula_Bug", "50")
south_province_area_five.add("Pawmo_Electric_Fighting", "10")
south_province_area_five.add("Toedscool_Ground_Grass", "2")
south_province_area_five.add("Mankey_Fighting", "20")
south_province_area_five.add("Gastly_Ghost_Poison", "0/0/0/50")
south_province_area_five.add("Larvitar (Scarlet)_Rock_Ground", "50")
south_province_area_five.add("Vigoroth_Normal", "20")
south_province_area_five.add("Swablu_Normal_Flying", "70")
south_province_area_five.add("Drifloon (Scarlet)_Ghost_Flying", "0/0/30/30")
south_province_area_five.add("Axew_Dragon", "60")
south_province_area_five.add("Larvitar (Scarlet)_Rock_Ground", "25")
south_province_area_five.add("Litleo_Fire_Normal", "30")
south_province_area_five.add("Skiddo_Grass", "30")
south_province_area_five.add("Rockruff (Standard)_Rock", "40")
south_province_area_five.add("Rockruff (Own Tempo)_Rock", "2")
south_province_area_five.add("Mudbray_Ground", "60")
south_province_area_five.add("Rookidee_Flying", "30")
south_province_area_five.add("Corvisquire_Flying", "30")
south_province_area_five.add("Pawmo_Electric_Fighting", "15")
south_province_area_five.add("Charcadet_Fire", "1")
south_province_area_five.add("Flittle_Psychic", "60")
south_province_area_five.add("Psyduck_Water", "30")
south_province_area_five.add("Wooper_Poison_Ground", "80")
south_province_area_five.add("Croagunk_Poison_Fighting", "60")
south_province_area_five.add("Goomy_Dragon", "60")
south_province_area_five.add("Mudbray_Ground", "15")
south_province_area_five.add("Chewtle_Water", "60")
south_province_area_five.add("Drednaw_Water_Rock", "10")
south_province_area_five.add("Tadbulb_Electric", "70")
south_province_area_five.add("Flamigo_Flying_Fighting", "60")
south_province_area_five.add("Clodsire_Poison_Ground", "40")
south_province_area_five.add("Psyduck_Water", "60")
south_province_area_five.add("Magikarp_Water", "60")
south_province_area_five.add("Marill_Water_Fairy", "60")
south_province_area_five.add("Wooper_Poison_Ground", "60")
south_province_area_five.add("Dunsparce_Normal", "5")
south_province_area_five.add("Surskit_Bug_Water", "60")
south_province_area_five.add("Zangoose_Normal", "40")
south_province_area_five.add("Seviper_Poison", "15")
south_province_area_five.add("Barboach_Water_Ground", "60")
south_province_area_five.add("Stunky (Scarlet)_Poison_Dark", "30")
south_province_area_five.add("Croagunk_Poison_Fighting", "30")
south_province_area_five.add("Basculin (Red-Striped)_Water", "60")
south_province_area_five.add("Basculin (Blue-Striped)_Water", "60")
south_province_area_five.add("Goomy_Dragon", "40")
south_province_area_five.add("Chewtle_Water", "10")
south_province_area_five.add("Psyduck_Water", "60")
south_province_area_five.add("Slowpoke_Water_Psychic", "30")
south_province_area_five.add("Magikarp_Water", "20")
south_province_area_five.add("Marill_Water_Fairy", "60")
south_province_area_five.add("Surskit_Bug_Water", "60")
south_province_area_five.add("Masquerain_Bug_Flying", "20")
south_province_area_five.add("Buizel_Water", "20")
south_province_area_five.add("Croagunk_Poison_Fighting", "20")
south_province_area_five.add("Basculin (Red-Striped)_Water", "60")
south_province_area_five.add("Basculin (Blue-Striped)_Water", "60")
south_province_area_five.add("Axew_Dragon", "20")
south_province_area_five.add("Pawniard_Dark_Steel", "60")
south_province_area_five.add("Chewtle_Water", "10")
south_province_area_five.add("Drednaw_Water_Rock", "10")
south_province_area_five.add("Arrokuda_Water", "40")
south_province_area_five.add("Tadbulb_Electric", "50")
south_province_area_five.add("Shellder_Water", "60")
south_province_area_five.add("Magikarp_Water", "60")
south_province_area_five.add("Gyarados_Water_Flying", "5")
south_province_area_five.add("Qwilfish_Water_Poison", "30")
south_province_area_five.add("Luvdisc_Water", "60")
south_province_area_five.add("Buizel_Water", "20")
south_province_area_five.add("Arrokuda_Water", "60")
south_province_area_five.add("Wattrel_Electric_Flying", "60")
south_province_area_five.add("Finizen_Water", "30")
south_province_area_five.add("Stantler_Normal", "60")
south_province_area_five.add("Makuhita_Fighting", "30")
south_province_area_five.add("Pawniard_Dark_Steel", "30")
south_province_area_five.add("Litleo_Fire_Normal", "50")
south_province_area_five.add("Skiddo_Grass", "50")
south_province_area_five.add("Yungoos_Normal", "20")
south_province_area_five.add("Gumshoos_Normal", "30")
south_province_area_five.add("Rookidee_Flying", "30")
south_province_area_five.add("Corvisquire_Flying", "30")
south_province_area_five.add("Nacli_Rock", "60")
south_province_area_five.add("Charcadet_Fire", "1")
south_province_area_five.add("Slowpoke_Water_Psychic", "30")
south_province_area_five.add("Shellder_Water", "60")
south_province_area_five.add("Buizel_Water", "20")
south_province_area_five.add("Shellos_Water_Ground (East Sea)", "60")
south_province_area_five.add("Crabrawler_Fighting", "30")
south_province_area_five.add("Sandygast_Ghost_Ground", "60")
south_province_area_five.add("Pincurchin_Electric", "10")
south_province_area_five.add("Wiglett_Water", "60")
south_province_area_five.add("Nacli_Rock", "15")
south_province_area_five.add("Wattrel_Electric_Flying", "60")
south_province_area_five.add("Skiploom_Grass_Flying", "20")
south_province_area_five.add("Combee_Bug_Flying", "40")
south_province_area_five.add("Spewpa_Bug", "30")
south_province_area_five.add("Flabebe_Fairy", "60")
south_province_area_five.add("Flabebe_Fairy", "60")
south_province_area_five.add("Flabebe_Fairy", "60")
south_province_area_five.add("Flabebe_Fairy", "60")
south_province_area_five.add("Flabebe_Fairy", "6")
south_province_area_five.add("Floette_Fairy", "55")
south_province_area_five.add("Floette_Fairy", "55")
south_province_area_five.add("Floette_Fairy", "55")
south_province_area_five.add("Floette_Fairy", "55")
south_province_area_five.add("Floette_Fairy", "3")
south_province_area_five.add("Fomantis_Grass", "60")
south_province_area_five.add("Gastly_Ghost_Poison", "15")
south_province_area_five.add("Bronzor_Steel_Psychic", "60")
south_province_area_five.add("Tinkatink_Fairy_Steel", "15")


south_province_area_six = Area("South Province (Area Six)")
south_province_area_six.add("Dreepy (Violet)_Dragon_Ghost", "0/0/0/5")
south_province_area_six.add("Dreepy (Violet)_Dragon_Ghost", "0/0/0/15")
south_province_area_six.add("Misdreavus (Violet)_Ghost", "0/0/0/15")
south_province_area_six.add("Misdreavus (Violet)_Ghost", "0/0/0/60")
south_province_area_six.add("Mismagius (Violet)_Ghost", "0/0/0/3")
south_province_area_six.add("Murkrow_Dark_Flying", "0/0/60/60")
south_province_area_six.add("Banette_Ghost", "0/0/0/70")
south_province_area_six.add("Drifblim (Scarlet)_Ghost_Flying", "0/0/20/20")
south_province_area_six.add("Gothorita_Psychic", "30")
south_province_area_six.add("Gothitelle_Psychic", "1")
south_province_area_six.add("Sylveon_Fairy", "1")
south_province_area_six.add("Klefki_Steel_Fairy", "20")
south_province_area_six.add("Sinistea_Ghost", "30")
south_province_area_six.add("Sinistea_Ghost", "1")
south_province_area_six.add("Dachsbun_Fairy", "30")
south_province_area_six.add("Bombirdier_Flying_Dark", "5")
south_province_area_six.add("Chansey_Normal", "1")
south_province_area_six.add("Flareon_Fire", "1")
south_province_area_six.add("Flaaffy_Electric", "20")
south_province_area_six.add("Ampharos_Electric", "10")
south_province_area_six.add("Donphan_Ground", "10")
south_province_area_six.add("Clauncher (Violet)_Water", "60")
south_province_area_six.add("Clawitzer (Violet)_Water", "20")
south_province_area_six.add("Shelgon (Violet)_Dragon", "10")
south_province_area_six.add("Meditite_Fighting_Psychic", "60")
south_province_area_six.add("Medicham_Fighting_Psychic", "20")
south_province_area_six.add("Altaria_Dragon_Flying", "20")
south_province_area_six.add("Drifblim (Scarlet)_Ghost_Flying", "0/0/30/30")
south_province_area_six.add("Honchkrow_Dark_Flying", "0/0/20/20")
south_province_area_six.add("Gallade_Psychic_Fighting", "1/1/1/0")
south_province_area_six.add("Rufflet_Normal_Flying", "25")
south_province_area_six.add("Gogoat_Grass", "40")
south_province_area_six.add("Lycanroc (Midday)_Rock", "20/20/0/0")
south_province_area_six.add("Lycanroc (Midnight)_Rock", "0/0/0/20")
south_province_area_six.add("Mudsdale_Ground", "12")
south_province_area_six.add("Greedent_Normal", "20")
south_province_area_six.add("Toxtricity_Electric_Poison", "15")
south_province_area_six.add("Toxtricity_Electric_Poison", "15")
south_province_area_six.add("Lokix_Bug_Dark", "20")
south_province_area_six.add("Houndstone_Ghost", "15")
south_province_area_six.add("Flittle_Psychic", "60")
south_province_area_six.add("Espathra_Psychic", "20")
south_province_area_six.add("Scovillain_Grass_Fire", "10")
south_province_area_six.add("Pawmo_Electric_Fighting", "15")
south_province_area_six.add("Bombirdier_Flying_Dark", "10")
south_province_area_six.add("Psyduck_Water", "60")
south_province_area_six.add("Golduck_Water", "20")
south_province_area_six.add("Magikarp_Water", "20")
south_province_area_six.add("Vaporeon_Water", "1")
south_province_area_six.add("Dratini_Dragon", "20")
south_province_area_six.add("Floatzel_Water", "10")
south_province_area_five.add("Basculin (Red-Striped)_Water", "60")
south_province_area_five.add("Basculin (Blue-Striped)_Water", "60")
south_province_area_six.add("Tynamo_Electric", "60")
south_province_area_six.add("Eelektrik_Electric", "30")
south_province_area_six.add("Drednaw_Water_Rock", "10")
south_province_area_six.add("Barraskewda_Water", "20")
south_province_area_six.add("Bellibolt_Electric", "5")
south_province_area_six.add("Flamigo_Flying_Fighting", "12")
south_province_area_six.add("Shellder_Water", "60")
south_province_area_six.add("Cloyster_Water_Ice", "10")
south_province_area_six.add("Magikarp_Water", "60")
south_province_area_six.add("Gyarados_Water_Flying", "5")
south_province_area_six.add("Qwilfish_Water_Poison", "30")
south_province_area_six.add("Floatzel_Water", "40")
south_province_area_six.add("Tynamo_Electric", "60")
south_province_area_six.add("Eelektrik_Electric", "30")
south_province_area_six.add("Skrelp (Scarlet)_Poison_Water", "60")
south_province_area_six.add("Barraskewda_Water", "20")
south_province_area_six.add("Kilowattrel_Electric_Flying", "30")
south_province_area_six.add("Bombirdier_Flying_Dark", "40")
south_province_area_six.add("Finizen_Water", "30")
south_province_area_six.add("Hariyama_Fighting", "15")
south_province_area_six.add("Honchkrow_Dark_Flying", "0/0/20/20")
south_province_area_six.add("Gogoat_Grass", "30")
south_province_area_six.add("Gumshoos_Normal", "30")
south_province_area_six.add("Copperajah_Steel", "20")
south_province_area_six.add("Lokix_Bug_Dark", "30")
south_province_area_six.add("Naclstack_Rock", "60")
south_province_area_six.add("Dugtrio_Ground", "20")
south_province_area_six.add("Umbreon_Dark", "1")
south_province_area_six.add("Dunsparce_Normal", "5")
south_province_area_six.add("Pupitar (Scarlet)_Rock_Ground", "10")
south_province_area_six.add("Hariyama_Fighting", "10")
south_province_area_six.add("Sableye_Dark_Ghost", "20")
south_province_area_six.add("Medicham_Fighting_Psychic", "20")
south_province_area_six.add("Gabite_Dragon_Ground", "10")
south_province_area_six.add("Deino (Scarlet)_Dark_Dragon", "30")
south_province_area_six.add("Salandit_Poison_Fire", "60")
south_province_area_six.add("Salazzle_Poison_Fire", "5")
south_province_area_six.add("Toxtricity_Electric_Poison", "15")
south_province_area_six.add("Toxtricity_Electric_Poison", "15")
south_province_area_six.add("Glimmet_Rock_Poison", "1")
south_province_area_six.add("Chansey_Normal", "1")
south_province_area_six.add("Jumpluff_Grass_Flying", "20")
south_province_area_six.add("Sunflora_Grass", "30/30/30/0")
south_province_area_six.add("Vespiquen_Bug_Flying", "20")
south_province_area_six.add("Lilligant_Grass", "5")
south_province_area_six.add("Vivillon_Bug_Flying", "30")
south_province_area_six.add("Floette_Fairy", "55")
south_province_area_six.add("Floette_Fairy", "55")
south_province_area_six.add("Floette_Fairy", "55")
south_province_area_six.add("Floette_Fairy", "55")
south_province_area_six.add("Floette_Fairy", "3")
south_province_area_six.add("Dolliv_Grass_Normal", "10")
south_province_area_six.add("Hypno_Psychic", "20")
south_province_area_six.add("Bronzong_Steel_Psychic", "20")
south_province_area_six.add("Sinistea_Ghost", "60")
south_province_area_six.add("Tinkatuff_Fairy_Steel", "15")


tagtree_thicket = Area("Tagtree Thicket")
tagtree_thicket.add("Venonat_Bug_Poison", "40")
tagtree_thicket.add("Venomoth_Bug_Poison", "0/0/0/20")
tagtree_thicket.add("Murkrow_Dark_Flying", "0/0/20/20")
tagtree_thicket.add("Dreepy (Violet)_Dragon_Ghost", "5")
tagtree_thicket.add("Dreepy (Violet)_Dragon_Ghost", "15")
tagtree_thicket.add("Misdreavus (Violet)_Ghost", "0/0/0/60")
tagtree_thicket.add("Pineco_Bug", "60")
tagtree_thicket.add("Dunsparce_Normal", "4")
tagtree_thicket.add("Zorua_Dark", "30")
tagtree_thicket.add("Foongus_Grass_Normal", "60")
tagtree_thicket.add("Passimian (Violet)_Fighting", "15")
tagtree_thicket.add("Oranguru (Scarlet)_Normal_Psychic", "15")
tagtree_thicket.add("Komala_Normal", "30")
tagtree_thicket.add("Mimikyu_Ghost_Fairy", "30")
tagtree_thicket.add("Greedent_Normal", "30")
tagtree_thicket.add("Applin_Grass_Dragon", "10")
tagtree_thicket.add("Impidimp_Dark_Fairy", "40")
tagtree_thicket.add("Morgrem_Dark_Fairy", "20")
tagtree_thicket.add("Oinkologne (Male)_Normal", "20")
tagtree_thicket.add("Oinkologne (Female)_Normal", "20")
tagtree_thicket.add("Spidops_Bug", "30")
tagtree_thicket.add("Charcadet_Fire", "1")
tagtree_thicket.add("Shroodle_Poison_Normal", "80")
tagtree_thicket.add("Grafaiai_Poison_Normal", "70")
tagtree_thicket.add("Toedscool_Ground_Grass", "10")
tagtree_thicket.add("Psyduck_Water", "60")
tagtree_thicket.add("Magikarp_Water", "60")
tagtree_thicket.add("Barboach_Water_Ground", "60")
tagtree_thicket.add("Whiscash_Water_Ground", "10")
tagtree_thicket.add("Basculin (Red-Striped)_Water", "60")
tagtree_thicket.add("Basculin (Blue-Striped)_Water", "60")
tagtree_thicket.add("Drednaw_Water_Rock", "10")
tagtree_thicket.add("Clodsire_Poison_Ground", "30")
tagtree_thicket.add("Psyduck_Water", "60")
tagtree_thicket.add("Magikarp_Water", "20")
tagtree_thicket.add("Buizel_Water", "20")
tagtree_thicket.add("Floatzel_Water", "10")
tagtree_thicket.add("Basculin (Red-Striped)_Water", "60")
tagtree_thicket.add("Basculin (Blue-Striped)_Water", "60")
tagtree_thicket.add("Pawniard_Dark_Steel", "60")
tagtree_thicket.add("Chewtle_Water", "10")
tagtree_thicket.add("Drednaw_Water_Rock", "10")
tagtree_thicket.add("Arrokuda_Water", "40")
tagtree_thicket.add("Barraskewda_Water", "20")
tagtree_thicket.add("Tadbulb_Electric", "50")
tagtree_thicket.add("Flamigo_Flying_Fighting", "12")
tagtree_thicket.add("Makuhita_Fighting", "30")
tagtree_thicket.add("Hariyama_Fighting", "15")
tagtree_thicket.add("Pawniard_Dark_Steel", "30")
tagtree_thicket.add("Skiddo_Grass", "50")
tagtree_thicket.add("Gogoat_Grass", "30")
tagtree_thicket.add("Gumshoos_Normal", "30")
tagtree_thicket.add("Lokix_Bug_Dark", "30")
tagtree_thicket.add("Nacli_Rock", "60")
tagtree_thicket.add("Naclstack_Rock", "60")
tagtree_thicket.add("Charcadet_Fire", "1")
tagtree_thicket.add("Chansey_Normal", "1")
tagtree_thicket.add("Sunflora_Grass", "30/30/30/0")
tagtree_thicket.add("Vespiquen_Bug_Flying", "20")
tagtree_thicket.add("Vivillon_Bug_Flying", "30")
tagtree_thicket.add("Floette_Fairy", "55")
tagtree_thicket.add("Floette_Fairy", "55")
tagtree_thicket.add("Floette_Fairy", "55")
tagtree_thicket.add("Floette_Fairy", "55")
tagtree_thicket.add("Floette_Fairy", "3")
tagtree_thicket.add("Fomantis_Grass", "60")
tagtree_thicket.add("Dolliv_Grass_Normal", "10")


west_paldean_sea = Area("West Paldean Sea")
west_paldean_sea.add("Clauncher (Violet)_Water", "60")
west_paldean_sea.add("Clawitzer (Violet)_Water", "20")
west_paldean_sea.add("Shellder_Water", "60")
west_paldean_sea.add("Cloyster_Water_Ice", "10")
west_paldean_sea.add("Magikarp_Water", "60")
west_paldean_sea.add("Gyarados_Water_Flying", "5")
west_paldean_sea.add("Qwilfish_Water_Poison", "30")
west_paldean_sea.add("Wingull_Water_Flying", "80")
west_paldean_sea.add("Pelipper_Water_Flying", "40")
west_paldean_sea.add("Luvdisc_Water", "60")
west_paldean_sea.add("Buizel_Water", "20")
west_paldean_sea.add("Floatzel_Water", "40")
west_paldean_sea.add("Finneon_Water", "60")
west_paldean_sea.add("Lumineon_Water", "30")
west_paldean_sea.add("Tynamo_Electric", "60")
west_paldean_sea.add("Eelektrik_Electric", "30")
west_paldean_sea.add("Skrelp (Scarlet)_Poison_Water", "60")
west_paldean_sea.add("Bruxish_Water_Psychic", "30")
west_paldean_sea.add("Arrokuda_Water", "60")
west_paldean_sea.add("Barraskewda_Water", "20")
west_paldean_sea.add("Veluza_Water_Psychic", "20")
west_paldean_sea.add("Finizen_Water", "30")
west_paldean_sea.add("Wattrel_Electric_Flying", "60")
west_paldean_sea.add("Kilowattrel_Electric_Flying", "30")
west_paldean_sea.add("Bombirdier_Flying_Dark", "40")


west_province_area_one = Area("West Province (Area One)")
west_province_area_one.add("Mankey_Fighting", "20")
west_province_area_one.add("Gastly_Ghost_Poison", "0/0/0/50")
west_province_area_one.add("Bagon (Violet)_Dragon", "10")
west_province_area_one.add("Misdreavus (Violet)_Ghost", "0/0/0/15")
west_province_area_one.add("Phanpy_Ground", "20")
west_province_area_one.add("Numel_Fire_Ground", "60")
west_province_area_one.add("Swablu_Normal_Flying", "70")
west_province_area_one.add("Drifloon (Scarlet)_Ghost_Flying", "0/0/30/30")
west_province_area_one.add("Skiddo_Grass", "30")
west_province_area_one.add("Rockruff (Standard)_Rock", "40")
west_province_area_one.add("Rockruff (Own Tempo)_Rock", "2")
west_province_area_one.add("Mudbray_Ground", "60")
west_province_area_one.add("Nymble_Bug", "30")
west_province_area_one.add("Pawmo_Electric_Fighting", "15")
west_province_area_one.add("Charcadet_Fire", "1")
west_province_area_one.add("Capsakid_Grass", "30")
west_province_area_one.add("Flittle_Psychic", "60")
west_province_area_one.add("Bombirdier_Flying_Dark", "10")
west_province_area_one.add("Psyduck_Water", "60")
west_province_area_one.add("Magikarp_Water", "20")
west_province_area_one.add("Buizel_Water", "20")
west_province_area_one.add("Basculin (Red-Striped)_Water", "60")
west_province_area_one.add("Basculin (Blue-Striped)_Water", "60")
west_province_area_one.add("Chewtle_Water", "10")
west_province_area_one.add("Arrokuda_Water", "40")
west_province_area_one.add("Tadbulb_Electric", "50")
west_province_area_one.add("Shellder_Water", "60")
west_province_area_one.add("Magikarp_Water", "60")
west_province_area_one.add("Gyarados_Water_Flying", "5")
west_province_area_one.add("Qwilfish_Water_Poison", "30")
west_province_area_one.add("Wingull_Water_Flying", "80")
west_province_area_one.add("Luvdisc_Water", "60")
west_province_area_one.add("Buizel_Water", "20")
west_province_area_one.add("Arrokuda_Water", "60")
west_province_area_one.add("Wattrel_Electric_Flying", "60")
west_province_area_one.add("Bombirdier_Flying_Dark", "40")
west_province_area_one.add("Finizen_Water", "30")
west_province_area_one.add("Makuhita_Fighting", "30")
west_province_area_one.add("Skiddo_Grass", "50")
west_province_area_one.add("Yungoos_Normal", "20")
west_province_area_one.add("Gumshoos_Normal", "30")
west_province_area_one.add("Nacli_Rock", "60")
west_province_area_one.add("Charcadet_Fire", "1")
west_province_area_one.add("Diglett_Ground", "20")
west_province_area_one.add("Dunsparce_Normal", "5")
west_province_area_one.add("Larvitar (Scarlet)_Rock_Ground", "10")
west_province_area_one.add("Makuhita_Fighting", "20")
west_province_area_one.add("Sableye_Dark_Ghost", "20")
west_province_area_one.add("Gible_Dragon_Ground", "15")
west_province_area_one.add("Yungoos_Normal", "60")
west_province_area_one.add("Gumshoos_Normal", "30")
west_province_area_one.add("Salandit_Poison_Fire", "60")
west_province_area_one.add("Charcadet_Fire", "1")
west_province_area_one.add("Wingull_Water_Flying", "60")
west_province_area_one.add("Buizel_Water", "20")
west_province_area_one.add("Crabrawler_Fighting", "30")
west_province_area_one.add("Wiglett_Water", "60")
west_province_area_one.add("Wattrel_Electric_Flying", "60")
west_province_area_one.add("Nacli_Rock", "15")
west_province_area_one.add("Combee_Bug_Flying", "40")
west_province_area_one.add("Happiny_Normal", "1")
west_province_area_one.add("Petilil_Grass", "40")
west_province_area_one.add("Flabebe_Fairy", "60")
west_province_area_one.add("Flabebe_Fairy", "60")
west_province_area_one.add("Flabebe_Fairy", "60")
west_province_area_one.add("Flabebe_Fairy", "60")
west_province_area_one.add("Flabebe_Fairy", "6")
west_province_area_one.add("Floette_Fairy", "55")
west_province_area_one.add("Floette_Fairy", "55")
west_province_area_one.add("Floette_Fairy", "55")
west_province_area_one.add("Floette_Fairy", "55")
west_province_area_one.add("Floette_Fairy", "3")
west_province_area_one.add("Gastly_Ghost_Poison", "15")
west_province_area_one.add("Bronzor_Steel_Psychic", "60")
west_province_area_one.add("Falinks_Fighting", "40")
west_province_area_one.add("Tinkatink_Fairy_Steel", "15")


west_province_area_two = Area("West Province (Area Two)")
west_province_area_two.add("Meowth_Normal", "30")
west_province_area_two.add("Chansey_Normal", "1")
west_province_area_two.add("Tauros (Combat Breed)_Fighting", "40")
west_province_area_two.add("Tauros (Blaze Breed) (Scarlet)_Fighting_Fire", "3")
west_province_area_two.add("Tauros (Aqua Breed) (Violet)_Fighting_Water", "3")
west_province_area_two.add("Dreepy (Violet)_Dragon_Ghost", "5")
west_province_area_two.add("Clauncher (Violet)_Water", "60")
west_province_area_two.add("Bagon (Violet)_Dragon", "10")
west_province_area_two.add("Ditto_Normal", "10")
west_province_area_two.add("Flaaffy_Electric", "30")
west_province_area_two.add("Murkrow_Dark_Flying", "0/0/40/40")
west_province_area_two.add("Girafarig_Normal_Psychic", "50")
west_province_area_two.add("Dunsparce_Normal", "2")
west_province_area_two.add("Donphan_Ground", "30")
west_province_area_two.add("Staravia_Normal_Flying", "30/30/30/0")
west_province_area_two.add("Stunky (Scarlet)_Poison_Dark", "30")
west_province_area_two.add("Deerling_Normal_Grass", "70")
west_province_area_two.add("Oinkologne (Male)_Normal", "20")
west_province_area_two.add("Oinkologne (Female)_Normal", "20")
west_province_area_two.add("Pawmo_Electric_Fighting", "10")
west_province_area_two.add("Maschiff_Dark", "30")
west_province_area_two.add("Toedscool_Ground_Grass", "2")
west_province_area_two.add("Cyclizar_Dragon_Normal", "15")
west_province_area_two.add("Meowth_Normal", "60")
west_province_area_two.add("Grimer_Poison", "80")
west_province_area_two.add("Ditto_Normal", "30")
west_province_area_two.add("Murkrow_Dark_Flying", "0/0/60/60")
west_province_area_two.add("Kirlia_Psychic_Fairy", "50/50/50/0")
west_province_area_two.add("Drifloon (Scarlet)_Ghost_Flying", "0/0/40/40")
west_province_area_two.add("Drifblim (Scarlet)_Ghost_Flying", "0/0/20/20")
west_province_area_two.add("Rotom_Electric_Ghost", "10")
west_province_area_two.add("Tandemaus_Normal", "10")
west_province_area_two.add("Varoom_Steel_Poison", "10")
west_province_area_two.add("Psyduck_Water", "60")
west_province_area_two.add("Slowpoke_Water_Psychic", "30")
west_province_area_two.add("Magikarp_Water", "20")
west_province_area_two.add("Marill_Water_Fairy", "60")
west_province_area_two.add("Azumarill_Water_Fairy_Water_Fairy", "30")
west_province_area_two.add("Buizel_Water", "20")
west_province_area_two.add("Floatzel_Water", "10")
west_province_area_two.add("Croagunk_Poison_Fighting", "20")
west_province_area_two.add("Basculin (Red-Striped)_Water", "60")
west_province_area_two.add("Basculin (Blue-Striped)_Water", "60")
west_province_area_two.add("Chewtle_Water", "10")
west_province_area_two.add("Drednaw_Water_Rock", "10")
west_province_area_two.add("Arrokuda_Water", "40")
west_province_area_two.add("Barraskewda_Water", "20")
west_province_area_two.add("Tadbulb_Electric", "50")
west_province_area_two.add("Cyclizar_Dragon_Normal", "15")
west_province_area_two.add("Flamigo_Flying_Fighting", "12")
west_province_area_two.add("Shellder_Water", "60")
west_province_area_two.add("Magikarp_Water", "60")
west_province_area_two.add("Gyarados_Water_Flying", "5")
west_province_area_two.add("Qwilfish_Water_Poison", "30")
west_province_area_two.add("Wingull_Water_Flying", "80")
west_province_area_two.add("Buizel_Water", "20")
west_province_area_two.add("Floatzel_Water", "40")
west_province_area_two.add("Arrokuda_Water", "60")
west_province_area_two.add("Barraskewda_Water", "20")
west_province_area_two.add("Wattrel_Electric_Flying", "60")
west_province_area_two.add("Kilowattrel_Electric_Flying", "30")
west_province_area_two.add("Finizen_Water", "30")
west_province_area_two.add("Makuhita_Fighting", "30")
west_province_area_two.add("Hariyama_Fighting", "15")
west_province_area_two.add("Skiddo_Grass", "50")
west_province_area_two.add("Yungoos_Normal", "20")
west_province_area_two.add("Gumshoos_Normal", "30")
west_province_area_two.add("Lokix_Bug_Dark", "30")
west_province_area_two.add("Nacli_Rock", "60")
west_province_area_two.add("Charcadet_Fire", "1")
west_province_area_two.add("Slowpoke_Water_Psychic", "30")
west_province_area_two.add("Wingull_Water_Flying", "60")
west_province_area_two.add("Buizel_Water", "20")
west_province_area_two.add("Floatzel_Water", "10")
west_province_area_two.add("Shellos_Water_Ground", "60")
west_province_area_two.add("Crabrawler_Fighting", "30")
west_province_area_two.add("Sandygast_Ghost_Ground", "60")
west_province_area_two.add("Pincurchin_Electric", "10")
west_province_area_two.add("Wattrel_Electric_Flying", "60")
west_province_area_two.add("Kilowattrel_Electric_Flying", "30")
west_province_area_two.add("Nacli_Rock", "15")
west_province_area_two.add("Wiglett_Water", "60")
west_province_area_two.add("Wugtrio_Water", "20")
west_province_area_two.add("Diglett_Ground", "20")
west_province_area_two.add("Dugtrio_Ground", "20")
west_province_area_two.add("Dunsparce_Normal", "5")
west_province_area_two.add("Larvitar (Scarlet)_Rock_Ground", "10")
west_province_area_two.add("Makuhita_Fighting", "20")
west_province_area_two.add("Hariyama_Fighting", "10")
west_province_area_two.add("Sableye_Dark_Ghost", "20")
west_province_area_two.add("Meditite_Fighting_Psychic", "60")
west_province_area_two.add("Gible_Dragon_Ground", "15")
west_province_area_two.add("Noibat_Flying_Dragon", "70")
west_province_area_two.add("Yungoos_Normal", "60")
west_province_area_two.add("Gumshoos_Normal", "30")
west_province_area_two.add("Salandit_Poison_Fire", "60")
west_province_area_two.add("Charcadet_Fire", "1")
west_province_area_two.add("Glimmet_Rock_Poison", "1")

west_province_area_three = Area("West Province (Area Three)")
west_province_area_three.add("Misdreavus_Ghost", "60")
west_province_area_three.add("Dreepy_Dragon_Ghost", "15")
west_province_area_three.add("Dreepy_Dragon_Ghost", "5")
west_province_area_three.add("Meowth_Normal", "30")
west_province_area_three.add("Persian_Normal", "30")
west_province_area_three.add("Chansey_Normal", "1")
west_province_area_three.add("Scyther_Bug_Flying", "3")
west_province_area_three.add("Ditto_Normal", "10")
west_province_area_three.add("Jumpluff_Grass_Flying", "30")
west_province_area_three.add("Espeon_Psychic", "1/1/1/0")
west_province_area_three.add("Murkrow_Dark_Flying", "0/0/40/40")
west_province_area_three.add("Dunsparce_Normal", "2")
west_province_area_three.add("Shroomish_Grass", "30")
west_province_area_three.add("Vigoroth_Normal", "20")
west_province_area_three.add("Tropius_Grass_Flying", "10")
west_province_area_three.add("Staravia_Normal_Flying", "30/30/30/0")
west_province_area_three.add("Pachirisu_Electric", "10")
west_province_area_three.add("Zorua_Dark", "15")
west_province_area_three.add("Deerling_Normal_Grass", "70")
west_province_area_three.add("Sawsbuck_Normal_Grass", "10")
west_province_area_three.add("Fletchinder_Fire_Flying", "30")
west_province_area_three.add("Oinkologne (Male)_Normal", "20")
west_province_area_three.add("Oinkologne (Female)_Normal", "20")
west_province_area_three.add("Pawmo_Electric_Fighting", "10")
west_province_area_three.add("Maschiff_Dark", "30")
west_province_area_three.add("Mabosstiff_Dark", "20")
west_province_area_three.add("Toedscool_Ground_Grass", "2")
west_province_area_three.add("Lilligant_Grass", "1")
west_province_area_three.add("Pikachu_Electric", "10")
west_province_area_three.add("Primeape_Fighting", "20")
west_province_area_three.add("Scyther_Bug_Flying", "5")
west_province_area_three.add("Jolteon_Electric", "1")
west_province_area_three.add("Sudowoodo_Rock", "60")
west_province_area_three.add("Murkrow_Dark_Flying", "0/0/20/20")
west_province_area_three.add("Pineco_Bug", "60")
west_province_area_three.add("Dunsparce_Normal", "4")
west_province_area_three.add("Shroomish_Grass", "60")
west_province_area_three.add("Breloom_Grass_Fighting", "30")
west_province_area_three.add("Tropius_Grass_Flying", "30")
west_province_area_three.add("Pachirisu_Electric", "40")
west_province_area_three.add("Honchkrow_Dark_Flying", "0/0/20/20")
west_province_area_three.add("Leafeon_Grass", "1")
west_province_area_three.add("Zorua_Dark", "30")
west_province_area_three.add("Sawsbuck_Normal_Grass", "50")
west_province_area_three.add("Foongus_Grass_Normal", "60")
west_province_area_three.add("Komala_Normal", "30")
west_province_area_three.add("Greedent_Normal", "30")
west_province_area_three.add("Applin_Grass_Dragon", "10")
west_province_area_three.add("Oinkologne (Male)_Normal", "20")
west_province_area_three.add("Oinkologne (Female)_Normal", "20")
west_province_area_three.add("Spidops_Bug", "30")
west_province_area_three.add("Charcadet_Fire", "1")
west_province_area_three.add("Mabosstiff_Dark", "20")
west_province_area_three.add("Shroodle_Poison_Normal", "20")
west_province_area_three.add("Toedscool_Ground_Grass", "10")
west_province_area_three.add("Jigglypuff_Normal_Fairy", "60")
west_province_area_three.add("Meowth_Normal", "60")
west_province_area_three.add("Persian_Normal", "30")
west_province_area_three.add("Voltorb_Electric", "30")
west_province_area_three.add("Electrode_Electric", "10")
west_province_area_three.add("Ditto_Normal", "30")
west_province_area_three.add("Eevee_Normal", "10")
west_province_area_three.add("Murkrow_Dark_Flying", "0/0/60/60")
west_province_area_three.add("Drifloon (Scarlet)_Ghost_Flying", "0/0/40/40")
west_province_area_three.add("Drifblim (Scarlet)_Ghost_Flying", "0/0/20/20")
west_province_area_three.add("Dedenne_Electric_Fairy", "20")
west_province_area_three.add("Tandemaus_Normal", "10")
west_province_area_three.add("Dachsbun_Fairy", "30")
west_province_area_three.add("Bombirdier_Flying_Dark", "5")
west_province_area_three.add("Psyduck_Water", "60")
west_province_area_three.add("Scyther_Bug_Flying", "30")
west_province_area_three.add("Magikarp_Water", "60")
west_province_area_three.add("Azumarill_Water_Fairy_Water_Fairy", "30")
west_province_area_three.add("Dunsparce_Normal", "5")
west_province_area_three.add("Barboach_Water_Ground", "60")
west_province_area_three.add("Whiscash_Water_Ground", "10")
west_province_area_three.add("Tropius_Grass_Flying", "30")
west_province_area_three.add("Basculin (Red-Striped)_Water", "60")
west_province_area_three.add("Basculin (Blue-Striped)_Water", "60")
west_province_area_three.add("Goomy_Dragon", "40")
west_province_area_three.add("Drednaw_Water_Rock", "10")
west_province_area_three.add("Hatenna_Psychic", "40")
west_province_area_three.add("Flamigo_Flying_Fighting", "10")
west_province_area_three.add("Clodsire_Poison_Ground", "30")
west_province_area_three.add("Psyduck_Water", "60")
west_province_area_three.add("Golduck_Water", "20")
west_province_area_three.add("Magikarp_Water", "20")
west_province_area_three.add("Vaporeon_Water", "1")
west_province_area_three.add("Azumarill_Water_Fairy_Water_Fairy", "30")
west_province_area_three.add("Floatzel_Water", "10")
west_province_area_three.add("Basculin (Red-Striped)_Water", "60")
west_province_area_three.add("Basculin (Blue-Striped)_Water", "60")
west_province_area_three.add("Drednaw_Water_Rock", "10")
west_province_area_three.add("Barraskewda_Water", "20")
west_province_area_three.add("Tadbulb_Electric", "50")
west_province_area_three.add("Bellibolt_Electric", "5")
west_province_area_three.add("Flamigo_Flying_Fighting", "12")
west_province_area_three.add("Primeape_Fighting", "10")
west_province_area_three.add("Hariyama_Fighting", "15")
west_province_area_three.add("Honchkrow_Dark_Flying", "0/0/20/20")
west_province_area_three.add("Skiddo_Grass", "50")
west_province_area_three.add("Gogoat_Grass", "30")
west_province_area_three.add("Gumshoos_Normal", "30")
west_province_area_three.add("Lokix_Bug_Dark", "30")
west_province_area_three.add("Nacli_Rock", "60")
west_province_area_three.add("Naclstack_Rock", "60")
west_province_area_three.add("Charcadet_Fire", "1")
west_province_area_three.add("Hypno_Psychic", "20")
west_province_area_three.add("Bronzong_Steel_Psychic", "20")
west_province_area_three.add("Mabosstiff_Dark", "30")
west_province_area_three.add("Tinkatuff_Fairy_Steel", "15")
west_province_area_three.add("Greavard_Ghost", "40")

"""
 1 = Alfornada Cavern
 2 = Asado Desert
 3 = Casseroya Lake
 4 = Dalizapa Passage
 5 = East Paldean Sea
 6 = East Province (Area One)
 7 = East Province (Area Two)
 8 = East Province (Area Three)
 9 = Glaseado Mountain
10 = Great Crater of Paldea
11 = Inlet Grotto
12 = North Paldean Sea
13 = North Province (Area One)
14 = North Province (Area Two)
15 = North Province (Area Three)
16 = Poco Path
17 = Socarrat Trail
18 = South Paldean Sea
19 = South Province (Area One)
20 = South Province (Area Two)
21 = South Province (Area Three)
22 = South Province (Area Four)
23 = South Province (Area Five)
24 = South Province (Area Six)
25 = Tagtree Thicket
26 = West Paldean Sea
27 = West Province (Area One)
28 = West Province (Area Two)
29 = West Province (Area Three)
"""
alphabetical = {}
alphabetical[1] = alfornada_cavern
alphabetical[2] = asado_desert
alphabetical[3] = cabo_poco
alphabetical[4] = casseroya_lake
alphabetical[5] = dalizapa_passage
alphabetical[6] = east_paldean_sea
alphabetical[7] = east_province_area_one
alphabetical[8] = east_province_area_two
alphabetical[9] = east_province_area_three
alphabetical[10] = glaseado_mountain
alphabetical[11] = great_crater_of_paldea
alphabetical[12] = inlet_grotto
alphabetical[13] = north_paldean_sea
alphabetical[14] = north_province_area_one
alphabetical[15] = north_province_area_two
alphabetical[16] = north_province_area_three
alphabetical[17] = poco_path
alphabetical[18] = socarrat_trail
alphabetical[19] = south_paldean_sea
alphabetical[20] = south_province_area_one
alphabetical[21] = south_province_area_two
alphabetical[22] = south_province_area_three
alphabetical[23] = south_province_area_four
alphabetical[24] = south_province_area_five
alphabetical[25] = south_province_area_six
alphabetical[26] = tagtree_thicket
alphabetical[27] = west_paldean_sea
alphabetical[28] = west_province_area_one
alphabetical[29] = west_province_area_two
alphabetical[30] = west_province_area_three
"""
 3 = Cabo Poco
16 = Poco Path
11 = Inlet Grotto
19 = South Province (Area One)
20 = South Province (Area Two)
21 = South Province (Area Three)
27 = West Province (Area One)
18 = South Paldean Sea
22 = South Province (Area Four)
23 = South Province (Area Five)
 6 = East Province (Area One)
 7 = East Province (Area Two)
 8 = East Province (Area Three)
 2 = Asado Desert
25 = Tagtree Thicket
28 = West Province (Area Two)
29 = West Province (Area Three)
 5 = East Paldean Sea
26 = West Paldean Sea
 9 = Glaseado Mountain
 1 = Alfornada Cavern
24 = South Province (Area Six)
15 = North Province (Area Three)
14 = North Province (Area Two)
13 = North Province (Area One)
12 = North Paldean Sea
 3 = Casseroya Lake
17 = Socarrat Trail
 4 = Dalizapa Passage
10 = Great Crater of Paldea
"""
chronological = {}
chronological[1] = cabo_poco
chronological[2] = poco_path
chronological[3] = inlet_grotto
chronological[4] = south_province_area_one
chronological[5] = south_province_area_two
chronological[6] = south_province_area_three
chronological[7] = west_province_area_one
chronological[8] = south_paldean_sea
chronological[9] = south_province_area_four
chronological[10] = south_province_area_five
chronological[11] = east_province_area_one
chronological[12] = east_province_area_two
chronological[13] = east_province_area_three
chronological[14] = west_province_area_two
chronological[15] = tagtree_thicket
chronological[16] = west_province_area_three
chronological[17] = east_paldean_sea
chronological[18] = west_paldean_sea
chronological[19] = dalizapa_passage
chronological[20] = glaseado_mountain
chronological[21] = alfornada_cavern
chronological[22] = south_province_area_six
chronological[23] = asado_desert
chronological[24] = north_province_area_three
chronological[25] = north_province_area_two
chronological[26] = north_province_area_one
chronological[27] = north_paldean_sea
chronological[28] = casseroya_lake
chronological[29] = socarrat_trail
chronological[30] = great_crater_of_paldea

g = Game("Scarlet")
g.box = ["Crocalor","Oinkologne (Male)","Clodsire","Gumshoos","Arrokuda","Klawf","Bombirdier", "Gyarados", "Gimmighoul","Goomy", "Tauros (Combat Breed)", "Basculin (Red-Striped)","Floette", "Azumarill","Jigglypuff"]
g.dupe_out()
#g.distribution(0,8,1,"Flying",0)
#g.generate(0,8,1,"Flying",0)
#g.distribution(0,9,1,"Normal",0)
g.generate(0,19,3,"Normal",1)
#g.generate(0,10,1,"Dragon",1)
#g.locate(0, "Dratini")