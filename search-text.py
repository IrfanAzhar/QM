from utils import summingMethod, sum_to_one_digit

# the following script is prepared by Dr Irfan Azhar on 13 October, 2024. Modified on 03 December, 2025
# 1.  modify the arabicLetterMap according to the input file-variable named as "file1" of QM script. here, the type of font
#     used in the input file is important. they must match.
# 2.  "file2" variable is used in conjunction with reading of the QM script. their synchronicity is important
import csv
import os
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
arabicLetterMap ={
"ا":1
,"أ":1
,"إ":1  
,"آ":1
,"ٱ":1 
,"ء":1
,"ب": 2 
,"ج":3
,"د":4 
,"ه":5 
,"و":6 
,"ز":7
,"ح":8
,"ط":9
,"ي":10
,"ى":10
,"ئ":10
,"ك":20 
,"ل":30 
,"م":40 
,"ن":50 
,"س":60 
,"ع":70 
,"ف":80 
,"ص":90 
,"ق":100 
, "ر":200 
,"ش":300 
, "ت":400 
,"ة":400 
,"ث":500 
,"خ":600 
,"ذ":700 
,"ض":800 
,"ظ":900 
,"غ":1000} 
# -------------------------------------------------------------------------------------------------------------------------
  
#arabicLetterMap ={
#"ا":1
#,"أ":1
#,"إ":1  
#,"ب": 2 
#,"ج":3
#,"د":4 
#,"ه":5 
#,"و":6 
#,"ز":7
#,"ح":8
#,"ط":9
#,"ي":10
#,"ى":10
#,"ك":20 
#,"ل":30 
#,"م":40 
#,"ن":50 
#,"س":60 
#,"ع":70 
#,"ف":80 
#,"ص":90 
#,"ق":100 
#, "ر":200 
#,"ش":300 
#, "ت":400 
#,"ة":400 
#,"ث":500 
#,"خ":600 
#,"ذ":700 
#,"ض":800 
#,"ظ":900 
#,"غ":1000} 
## -------------------------------------------------------------------------------------------------------------------------



#for key in arabicLetterMap:
#    print ("\n  letter = ", key, " weight = ", arabicLetterMap[key])
#exit(1)
dictQM_MetaData = {} # this dictionary holds the chapter number and its verses, words and letters
dictQM_QM = {} # this dictionary holds sum of all numerical values in QM
dictQM_SS = {} # this dictionary holds all the chapters and numerical values
dictQM_RR = {} # this dictionary holds all the sections of all the chapters in QM
dictQM_AA = {} # this dictionary holds all the verses of all the chapters in QM
dictQM_WW = {} # this dictionary holds all the words of all the chapters in QM
dictQM_LL = {} # this dictionary holds all the letters of all the chapters in QM
       
#for i in range(len(tasmiahString)):
#    print ("  ", i, "   ",tasmiahString[i])
#exit(1)
count_SS = 0; count_AA = 0; count_WW = 0; count_LL = 0;

count2 = 0;

#-----------------------------------------------------------------------------------------------------------------------
#  --- following line initialises a list of QM chapter numbers which are used as keys

list_SS_Keys = [("SS_" + str(i)) for i in range(115)] # this list contains names of the QM chapters
#print (list_SS_Keys)


#-----------------------------------------------------------------------------------------------------------------------
# in this section we open the file containing text of QM. we tested different files n text

#file1 = open('quran2nd.txt', mode ='r')
#file1 = open('Quran-without-tashkeel.pdf', mode = 'r')
file1 = open('quran-simple-formatted.txt', mode = 'r',  encoding="utf8",)
#file1 = open('quran-simple-clean.txt', mode = 'r',  encoding="utf8",)
#file1 = open('quran-simpleB.sql', mode = 'r', encoding="utf8", errors="ignore")

file1Data = file1.read()
file1.close()
data1Lines = file1Data.split('\n')

#-----------------------------------------------------------------------------------------------------------------------
# in this section we initialize metadata of QM. it contains the chapter numbers, verses-count and word-count

# this file contains the metadata of QM chapters
# Header = ['Chapter Index ', 'Chapter Name ', 'Verses ', 'Words ', 'Chars']

file2 = open('QM_statistics.txt', mode ='r')
file2Data = file2.read()
file2.close()
data2Lines = file2Data.split('\n')

# ---- in the following line we populate the dictionary that contains metadata of QM
dictQM_MetaData = {list_SS_Keys[i]:(data2Lines[i].split('\t')) for i in range(len(list_SS_Keys))}

#-----------------------------------------------------------------------------------------------------------------------
# here we dynamically intialise 114 dictionaries relevant to the chapters of QM

for i in range(115):
    name = "SS_" + str(i)
    name = dict()
    #print (name)

count_AA = len(data1Lines) - 1


#-----------------------------------------------------------------------------------------------------------------------
# here we initialise the QM text in discrete lines
# data3Lines posed problem and we could not omit error of EOF.
# therefore, we formulated the tempList which is used later

# count_AA as the name suggest holds the total number of lines or verses in the QM text
#  the following section removes the empty lines from the total text

data3Lines = []
i = 0
while i < count_AA:
    #print ("\n the value of i = ", i)
    line1 = data1Lines[i].split('\n')
    line2 = line1[0].split("|")
    line3 = line2[0].split(",")
    data3Lines.append(line2[2])
    #print ("the orig line1 is - ", line1)
    #print ("the 1st split line2 is - ", line2[2])
    #print ("the 2nd split line3 is", line3[0])
    i = i + 1
    if i == 6236: break

# -- in this section we remove the EOF 
tempList = []
for i in range(len(data3Lines)):
   #print (" ",i,"th verse ",data3Lines[i])
   tempList.append(data3Lines[i])

#-----------------------------------------------------------------------------------------------------------------------
# in this section we populate the chapter dicts with their respective verses
verse_count = 0
base = 0
for i in range(len(dictQM_MetaData) - 1):
    #print ("name of the chapter-dict is = ", list_SS_Keys[i+1])
    #print ("the elements in the list are = ", dictQM_MetaData[list_SS_Keys[i+1]])
    #print ("total verses in a chapter is = ", int(dictQM_MetaData[list_SS_Keys[i+1]][2]))
    verse_count = int(dictQM_MetaData[list_SS_Keys[i+1]][2])
    #print ("total verses in a chapter is = ", verse_count)
    list_SS_Keys[i+1] = {k:tempList[base + k] for k in range(verse_count)}
    #print ( " total length of the ", (i + 1)," chapter is  = ",len(list_SS_Keys[i+1]))
    base = base + verse_count
#exit(1)


#-----------------------------------------------------------------------------------------------------------------------
# === in this section we separate 1st verse of each surat from tasmiah, and then we rewrite all 
#        the verses where 0 position holds tasmiah and 1st position holds the 1st verse

tempString1 = ""
tempString2 = ""
chapterIndex = 2

tasmiahString = "بِسْمِ اللَّهِ الرَّحْمَـٰنِ الرَّحِيمِ"

for i in range (113):  # for 114 chapters. we do not touch the 1st chapter
    if chapterIndex == 9:  # this if statement is to cater for Sura-e-Tauba
        chapterIndex = chapterIndex + 1
        continue
    tempString1 = list_SS_Keys[chapterIndex][0]  # this string holds the 1st verse combined with tasmiah
    
#    tempString2 = tempString1[(len(tasmiahString)):-1] # this string holds the 1st verse only
    tempString2 = tempString1[(len(tasmiahString)): -1] # this string holds the 1st verse only
    list_SS_Keys[chapterIndex][0] = tasmiahString
    
    #tempString1 = tasmiahString  # we commented it out and the code worked fine
    
    verseCount = 1
    for k in range (len(list_SS_Keys[chapterIndex]) - 1):
        #print ("  the value of verseCount = ", verseCount)
        tempString1 = list_SS_Keys[chapterIndex][verseCount] + " " # see note-1
        list_SS_Keys[chapterIndex][verseCount] = tempString2
        #print ("  k=", verseCount, "  text =", tempString2)
        tempString2 = tempString1
        verseCount = verseCount + 1

    list_SS_Keys[chapterIndex].update ({verseCount : tempString2})
    chapterIndex = chapterIndex + 1

# note-1
# ===========
## we added this space character here as a solution to our observation where the last word of each chapter
#  got merged with first word of every next chpater. after this addition, things became OK.

#-----------------------------------------------------------------------------------------------------------------------
# --- this section is meant for re-arrangement of Chapter 9 Sura-e-Tauba only.

chapterIndex = 9
verseCount = len(list_SS_Keys[chapterIndex])
tempString1 = list_SS_Keys[chapterIndex][verseCount - 1] + " " # see note-1
tempString2 = " "

for k in range (len(list_SS_Keys[chapterIndex]) - 1):
    #print ("  the vaslue of verseCount = ", verseCount)
#   continue
    list_SS_Keys[chapterIndex][verseCount - 1] = list_SS_Keys[chapterIndex][verseCount - 2] + " "#see note-1
    verseCount = verseCount - 1

list_SS_Keys[chapterIndex][0] = "  " # we make the 0th position = empty string

verseCount = len(list_SS_Keys[chapterIndex]) # we add one more place after the last index
list_SS_Keys[chapterIndex].update ({verseCount : tempString1})

#-----------------------------------------------------------------------------------------------------------------------

# --- the following section is meant for testing purpose only

#for i in range(114):
#    k = 1
#    if i == 8:
#        k = 0
#        print ("  1st verse of ith chapter = ", (i+1), "text = ", list_SS_Keys[i + 1][k])
#        print ("  2nd verse of ith chapter = ", (i+1), "text = ", list_SS_Keys[i + 1][k + 1])
#        continue
#    print ("  1st verse of ith chapter = ", (i+1), "text = ", list_SS_Keys[i + 1][k])
#exit(1)

#for i in range(len(list_SS_Keys[9])):
#    print (" verses of 9th chapter are = ", i, "text = ", list_SS_Keys[9][i])
#exit(1)

#------------------------------------------------------------------------------------------------------------

# --- this section assigns the numerical weights of each letter in each verse of each chapter

#     we look for the space characters in the sequence of letters of a verse and use that character
#     as boundary among the words.

# Legend of Letters' Dictionary is given below

# generic-dict = [key: value]

# dictQM_LL = ["LL_*": [chapter-index, verse-index, word-index, letter-index, arabic-letter-weight, arabic-letter]
# dictQM_WW = ["WW_*": [chapter-index, verse-index, word-index, word-weight, ]
# dictQM_AA = ["AA_*": [chapter-index, verse-index, verse-weight]
# dictQM_SS = ["SS_*": [chapter-index, chapter-weight]
# dictQM_QM = ["QM"  : [QM-weights]

letterIndex  = 0 # this variable is sued to formulate discrete keys for dictQM_LL dictionary
wordIndex    = 0 # this variable is sued to formulate discrete keys for dictQM_WW dictionary
verseIndex   = 0 # this variable is sued to formulate discrete keys for dictQM_VV dictionary
chapterIndex = 0 # this variable is sued to formulate discrete keys for dictQM_SS dictionary

letterKey  = "LL_" + str(letterIndex)    # this key is used for dictQM_LL pairs
wordKey    = "WW_" + str(wordIndex)      # this key is used for dictQM_WW pairs
verseKey   = "AA_" + str(verseIndex)     # this key is used for dictQM_AA pairs
chapterKey = "SS_" + str(chapterIndex)   # this key is used for dictQM_SS pairs

wordWeightSum     = 0 # this variable holds the sum of weights from its constituents letters
verseWeightSum    = 0 # this variable holds the sum of weights from its constituents words
chapterWeightSum  = 0 # this variable holds the sum of weights from its constituents verses
QMWeightSum       = 0 # this variable holds the sum of weights from its constituents chapters

#chapterIndex, we use this counter for the chapters and it starts with a value = 0
#chapterIndex = 112  # we use this duplicate value during testing only. it is not valid for production

validationWeightVariable  = 0 # we are introducing this variable to cross-check the total weight at the end
validationLetterCounter   = 0 # we are introducing this variable to cross-check the total letters # 330,110

noTashkeelString = ""

for i in range(114):
    chapterIndex = chapterIndex + 1   # we initialize the chapter index at start of the loop
                                      # becasue the counting of Chapters starts at 1 in the list
    chapterWeightSum  = 0
    
    for verseCount in range(len(list_SS_Keys[chapterIndex])):
        verseKey   = "AA_" + str(verseIndex)
        #print ("the complete verse is = ", list_SS_Keys[chapterIndex][verseCount])
        
        noTashkeelString = noTashkeelString + '\n'
        for wordCount in range(len(list_SS_Keys[chapterIndex][verseCount])):
            
            #print ("the complete word is = ", list_SS_Keys[chapterIndex][verseCount][wordCount])
                                    
            for key  in (arabicLetterMap):
                if (list_SS_Keys[chapterIndex][verseCount][wordCount] == key):
                    letterKey = "LL_" + str(letterIndex)
                    dictQM_LL[letterKey] = [chapterIndex, verseIndex, wordIndex,letterIndex,
                                      arabicLetterMap[key],
                                      list_SS_Keys[chapterIndex][verseCount][wordCount]]
                                      
                    wordWeightSum    = wordWeightSum    + arabicLetterMap[key]
                    verseWeightSum   = verseWeightSum   + arabicLetterMap[key]
                    chapterWeightSum = chapterWeightSum + arabicLetterMap[key]
                    QMWeightSum      = QMWeightSum      + arabicLetterMap[key]
                    
                    validationWeightVariable = validationWeightVariable + arabicLetterMap[key]
                    validationLetterCounter  = validationLetterCounter  + 1
                    
                    noTashkeelString = noTashkeelString + list_SS_Keys[chapterIndex][verseCount][wordCount]
                    letterIndex = letterIndex + 1
                    
                    #print("    the matched - letter",list_SS_Keys[chapterIndex][verseCount][wordCount] )
                   
                if ((list_SS_Keys[chapterIndex][verseCount][wordCount] == " ") and not(wordWeightSum == 0)): 
                    wordKey    = "WW_" + str(wordIndex)
                    dictQM_WW [wordKey] = [chapterIndex, verseIndex, wordCount, wordWeightSum]
                    wordWeightSum = 0
                    noTashkeelString = noTashkeelString + "-" #list_SS_Keys[chapterIndex][verseCount][wordCount]
                    wordIndex = wordIndex + 1                    
        
        dictQM_AA[verseKey]= [chapterIndex, verseCount, verseWeightSum]
        verseWeightSum = 0
        verseIndex   = verseIndex + 1
    
    chapterKey = "SS_" + str(chapterIndex)
    dictQM_SS [chapterKey] = [chapterIndex, chapterWeightSum]
    chapterWeightSum = 0
                      
    #if chapterIndex == 114: break  # this line is here during testing and it is not valid for production

dictQM_QM ["QM"]= [QMWeightSum]

print ("\n  ---  the following lines hold the detail of QM letters and their weights ---")
print ("[LL_*: [chapter-index, verse-index, word-index, letter-index, arabic-letter-weight, arabic-letter]\n")

outputList = ['chapter-index', 'verse-index', 'word-index', 'letter-index', 'arabic-letter-weight', 'arabic-letter', '\n']

tempList = []
print(outputList)


#for key in dictQM_LL:
#    print (dictQM_LL[key][0],',',dictQM_LL[key][1],',',dictQM_LL[key][2],',',dictQM_LL[key][3],',',dictQM_LL[key][4],',',dictQM_LL[key][5])

#print (outputList)


# the following code segment is used to print and save the computed weights in to a text file in Linux shell by the following command:
#  python search-text.py > QM-weight-18-October-2024-1st-version-ver-2.txt



"""

print ("\n  ---  the following lines hold the detail of QM words and their weights ---")
print ("[WW_*: [chapter-index, verse-index, word-index, arabic-word-weight]\n")

for key in dictQM_WW:
#    #print("for WW_key = ", key, "the dictQM_WW value = ", dictQM_WW[key])
    print(dictQM_WW[key])

print ("\n  ---  the following lines hold the detail of QM verses and their weights ---")
print ("[AA_*: [chapter-index, verse-index, arabic-verse-weight]\n")

for key in dictQM_AA:
#    #print("for AA_key = ", key, "the dictQM_AA value = ", dictQM_AA[key])
    print(dictQM_AA[key]); print  (sum_to_one_digit(dictQM_AA[key][2]))

print ("\n  ---  the following lines hold the detail of QM chapters and their weights ---")
print ("[SS_*: [chapter-index, arabic-chapter-weight\n]")

for key in dictQM_SS:
#    #print("for SS_key = ", key, "the dictQM_SS value = ", dictQM_SS[key])
    print(dictQM_SS[key]); print (sum_to_one_digit(dictQM_SS[key][1]))


print ("\n  ---  the following lines hold the detail of QM's' own weight ---")
print ("[QM  : [QM-weights]\n")

print (dictQM_QM); print (sum_to_one_digit(dictQM_QM['QM'][0]))


print ("the total numerical weight of QM = ", dictQM_QM)
print ("the validationWeightVariable is = ", validationWeightVariable)
print ("the validationLetterCounter is = ", validationLetterCounter)

##+++++++
exit(1)
##+++++++

"""

# the following script stores the weights detail in individual .csv files for letters and other categories.

header_LL = ["chapter-counter", "verse-counter", "word-counter", "letter-counter", "arabic-letter-weight"]
header_WW = ["chapter-counter", "verse-counter", "word-counter", "arabic-word-weight"]
header_AA = ["chapter-counter", "verse-counter", "arabic-verse-weight"]
header_SS = ["chapter-counter", "arabic-chpater-weight"]
header_QM = ["QM-weight"]


with open('dictQM_LL_03_Dec_2025.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header_LL)  # Single header
    for item in dictQM_LL:
        writer.writerow(dictQM_LL[item][:len(dictQM_LL[item]) - 1])  # Each string in its own row


with open('dictQM_WW_03_Dec_2025.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header_WW)  # Single header
    for item in dictQM_WW:
        writer.writerow(dictQM_WW[item][:])  # Each string in its own row

with open('dictQM_AA_03_Dec_2025.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header_AA)  # Single header
    for item in dictQM_AA:
        writer.writerow(dictQM_AA[item][:])  # Each string in its own row

with open('dictQM_SS_03_Dec_2025.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header_SS)  # Single header
    for item in dictQM_SS:
        writer.writerow(dictQM_SS[item][:])  # Each string in its own row


with open('dictQM_QM_03_Dec_2025.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header_QM)  # Single header
    for item in dictQM_QM:
        writer.writerow(dictQM_QM[item][:])  # Each string in its own row
