import re
file1 = open("/Users/youniesmahmoud/Desktop/test_kraken/HiSeq_accuracy2.labels")

lines = file1.read()
file1.close()

lines = lines.split("\n")

for i in range(len(lines)):
        lines[i] = lines[i].split(";")


lines = lines[:-1]


mapper = {
	"R_sphaeroides" :  ["Rhodobacter" ,"sphaeroides"]    ,
	"S_aureus" :  ["Staphylococcus",  "aureus"]    ,
	"S_pneumoniae" :    ["Streptococcus" , "pneumoniae"]  ,
	"V_cholerae" :     [ "Vibrio" ,  "cholerae"] ,
	"X_axonopodis" :     ["Xanthomonas" , "axonopodis"] ,
	"A_hydrophila" :  ["Aeromonas" , "hydrophila"]    ,
	"B_cereus" :   ["Bacillus" ,  "cereus"]   ,
	"B_fragilis" :   ["Bacteroides" , "fragilis"]   ,
	"M_abscessus" :   ["Mycobacterium" , "abscessus"]   ,
	"P_fermentans" :   ["Pelosinus" , "fermentans"]   ,
}


data = []

species = 0;
genus = 0;
others = 0;

for line in lines:
        m = re.search(r"[a-zA-Z]*_[a-zA-Z]*", line[0])
        m = m.group(0)
        

        mapping = mapper[m];

        if(mapping[0] in line[-1] and mapping[1] in line[-1]):
        	species +=1
        elif(mapping[0] in line[-1] ):
        	genus +=1
        else:
        	others+=1



for d in data:
        print(d)

print (species)
print (genus)
print (others)

print(len(lines))