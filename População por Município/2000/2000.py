
#Para imprimir tabela ou plotar mapa, tirar comentário de um dos últimos dois comandos

import pandas as pd
import geopandas as gpd
import matplotlib

pop00 = pd.read_csv("2000.csv",sep = ";")
pop00["Codmun6"] = pop00["COD_UF"]*10000 + pop00["COD_MN"]

ac = gpd.read_file("shp/ac/12MU500G.shp")
al = gpd.read_file("shp/al/27MU500G.shp")
am = gpd.read_file("shp/am/13MU500G.shp")
ap = gpd.read_file("shp/ap/16MU500G.shp")
ba = gpd.read_file("shp/ba/29MU500G.shp")
ce = gpd.read_file("shp/ce/23MU500G.shp")
df = gpd.read_file("shp/df/53MU500G.shp")
es = gpd.read_file("shp/es/32MU500G.shp")
go = gpd.read_file("shp/go/52MU500G.shp")
ma = gpd.read_file("shp/ma/21MU500G.shp")
mg = gpd.read_file("shp/mg/31MU500G.shp")
ms = gpd.read_file("shp/ms/50MU500G.shp")
mt = gpd.read_file("shp/mt/51MU500G.shp")
pa = gpd.read_file("shp/pa/15MU500G.shp")
pb = gpd.read_file("shp/pb/25MU500G.shp")
pe = gpd.read_file("shp/pe/26MU500G.shp")
pi = gpd.read_file("shp/pi/22MU500G.shp")
pr = gpd.read_file("shp/pr/41MU500G.shp")
rj = gpd.read_file("shp/rj/33MU500G.shp")
rn = gpd.read_file("shp/rn/24MU500G.shp")
ro = gpd.read_file("shp/ro/11MU500G.shp")
rr = gpd.read_file("shp/rr/14MU500G.shp")
rs = gpd.read_file("shp/rs/43MU500G.shp")
sc = gpd.read_file("shp/sc/42MU500G.shp")
se = gpd.read_file("shp/se/28MU500G.shp")
sp = gpd.read_file("shp/sp/35MU500G.shp")
to = gpd.read_file("shp/to/17MU500G.shp")

br00 = ac.append(al)
br00 = br00.append(am)
br00 = br00.append(ap)
br00 = br00.append(ba)
br00 = br00.append(ce)
br00 = br00.append(df)
br00 = br00.append(es)
br00 = br00.append(go)
br00 = br00.append(ma)
br00 = br00.append(mg)
br00 = br00.append(ms)
br00 = br00.append(mt)
br00 = br00.append(pa)
br00 = br00.append(pb)
br00 = br00.append(pe)
br00 = br00.append(pi)
br00 = br00.append(pr)
br00 = br00.append(rj)
br00 = br00.append(rn)
br00 = br00.append(ro)
br00 = br00.append(rr)
br00 = br00.append(rs)
br00 = br00.append(sc)
br00 = br00.append(se)
br00 = br00.append(sp)
br00 = br00.append(to)
br00["GEOCODIGO"] = pd.to_numeric(br00["GEOCODIGO"])

trans_cod = pd.read_csv('cod00.csv', sep = ";")
br00 = br00.merge(trans_cod, on = "GEOCODIGO")

mapa = br00.merge(pop00, on = "Codmun6")

#Ver dados
#print(mapa)

#Plotar
#mapa.plot(column = "POP_ESTIM", figsize = (20,20), legend = True)
