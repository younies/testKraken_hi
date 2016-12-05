import re
file1 = open("/Users/youniesmahmoud/Desktop/test_kraken/MiSeq_accuracy2.labels")

lines = file1.read()
file1.close()

lines = lines.split("\n")

for i in range(len(lines)):
        lines[i] = lines[i].split(";")


lines = lines[:-1]


mapper = {
        "S_enterica"    : [  "Salmonella" ,  "enterica"  ] ,
        "K_pneumoniae"  : [  "Klebsiella" , "pneumoniae"  ] ,
        "P_vulgaris"    : [  "Proteus" , "vulgaris"  ] ,
        "S_aureus"      : [   "Staphylococcus" , "aureus" ] ,
        "B_cereus"      : [  "Bacillus" ,  "cereus"  ] ,
        "M_abscessus"   : [  "Mycobacterium" , "abscessus"  ] ,
        "R_sphaeroides" : [  "Rhodobacter" , "sphaeroides"  ] ,
        "V_cholerae"    : [ "Vibrio" , "cholerae"  ] ,
        "C_freundii"    : [  "Citrobacter" , "freundii"  ] ,
        "E_cloacae"     : [  "Enterobacter"  ,  "cloacae"  ] ,

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