import glob
import math
from operator import itemgetter

print('Hello, please enter the documents in the same file directory as the program and run again the program \n')

big_array = [] # lista me tis lekseis olon ton arxeion
array = [] # lista me tis lekseis kathe arxeiou

for filename in glob.glob('*.txt'): #gia na vrethoun ta .txt pou briskontai ston idio fakelo me to .py
    with open(filename, 'r') as f:

        for line in open(filename, 'r'): #gia dimiourgia listas me oles tis lekseis pou exoun ola ta arxeia
            for word in line.split():
                if word not in big_array:
                    big_array.append(word)
big_array.sort() #taksinomisi listas me alfavitiki seira

namelist = glob.glob('*.txt') #lista me ta onomata ton arxeion pou teleionoun se .txt kai einai ston idio fakelo me to .py

print('Are these the documents? ', namelist, '\nyes or no?')
apantisi = str(input())

while apantisi != 'yes':
    print('Try again')
    exit()


try:
    max = int(input('Give me the K number for the TOP-K most similar documents,please: \n')) #ta k zeugaria arxeion ksekinontas me auta pou exoun tin megaliteri omoiotita
except ValueError:
    print("Not a number")
    exit()

while (max > math.factorial(len(namelist))/(2*math.factorial(len(namelist)-2))) or (max == 0): #elegxos gia to an to k einai arithmos mikroteros apo tous sindiasmous ton arxeion pou exo kai megaliteros apo 0
    max = int(input('wrong,try again:'))


globlist = [] #lista pou periexei tis listes me tis sixnotites ton lekseon sta keimena

for filename in namelist:
    with open(filename, 'r') as f:

        wordcount = {} #einai dictionary pou apothikeuei thn sixnothta emfanisis tis kathe lekseis se kathe keimeno, me key tin leksi kai value ton arithmo emfanisis tis, px 'a': 3, diladi i leksi 'a' emfanizetai 3 fores

        for line in open(filename, 'r'):
            for word in line.split():
                for i in big_array:
                    if i not in array: #ftiaxno epimerous listes me lekseis gia kathe arxeio .txt
                        array.append(i)
                    if i not in wordcount: #oses lekseis den uparxoun se kapoio arxeio alla uparxoun stin lista me oles tis lekseis mpainoun me sixnotita 0
                        wordcount[i] = 0

                if word not in wordcount: #gia oses lekseis uparxoun se kathe arxeio metrietai i sixnotita tous
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1

        numbers = [] #lista me oles tis sixnotites ton lekseon
        for key in wordcount:
            numbers.append(wordcount[key])
        globlist.append([numbers[i]  for i in range(len(numbers))]) #bainoun se lista oi listes me tis sixnotites ton lekseon


local_1 = [] #lista gia na kratithei i mia lista me sixnotites lekseon pou tha sigkrithei
local_2 = [] #lista gia na kratithei i deuteri lista me sixnotites lekseon pou tha sigkrithei

dictionary = {} #dictionari pou krataei os key to zeugari ton keimenon kai os value tin omoiotita sinimitonou auton ton dio keimenon


for k in range(0,len(globlist)-1): #perno apo tin lista me tis listes ton sixnotiton ton lekseon kathe mia lista me tis ipolipes gia na vro to esoteriko ginomeno kai to mikos kathe zeugariou
    for p in range(k+1,len(globlist)):
        local_1 = globlist[k]
        local_2 = globlist[p]

        norm_1=0
        for a in range (len(local_1)):
            norm_1 = norm_1+(local_1[a]*local_1[a])#norma1, diladi mikos dianismatos tou protou apo ta dio keimena pou eksetazo kathe fora
        norm_1 = norm_1**0.5 #riza

        norm_2 = 0
        for a in range(len(local_2)):
            norm_2 = norm_2 + (local_2[a] * local_2[a]) #norma2, diladi mikos dianismatos tou deuterou apo ta dio keimena pou eksetazo kathe fora
        norm_2 = norm_2 ** 0.5 #riza

        esot = sum([a * b for a, b in zip(local_1, local_2)]) #esoteriko ginomeno ton 2 keimenon

        cos = esot/(norm_1*norm_2) #ipologismos omoiotitas sinimitonou simfona me ton tipo tis ekfonisis
        dictionary[str(k)+","+str(p)] =cos #prostheto sto key tou dictionary to noumero ton keimenon, diladi to '0,1' gia to 0 keimeno kai 1 gia to 1 keimeno

dictionary = sorted(dictionary.items(), key=itemgetter(1), reverse=True) #taksinomisi tou dictionary me vasi ta values kai ginetai lista me tuples pou periexei to zeugari ton keimenon kai tin iomoiotita simitonou tous

cnt = 1
temp = [] #lista gia na perastoun ta noumera ton keimenon
for tup in dictionary:
    if cnt <= max : #cnt counter pou elegxei an exoun tipothei ola ta TOP-K most similar documents pou zitise o xristis

        temp = tup[0].split(',') #perno apo ta tuples to tup[0]-->dhldadh to proto pou exei to zeugari ton texts files, to zeugari einai xorismeno me ','

        print('The text files are',namelist[int(temp[0])], 'and', namelist[int(temp[1])], '\nwith cos: ', round(tup[1],4), ' or ', round(tup[1]*100,2), '% \n') #zitao apo tin lista me ta onomata ton arxeion na epistrepsei to onoma tou kathe arxeiou apo tin thesi temp[0]--> noumero protou keimenou kai apo tin temp[1]--> noumero deuterou keimenou

    cnt = cnt + 1

f.close()