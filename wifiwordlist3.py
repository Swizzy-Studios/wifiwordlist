import re

#Limiter section. This section is used to provide arbitrary limiters to prevent runaway wordlists
#========================================
#leetlimit is used to prevent the leet speak conversion of passwords over a certain amount of characters
#used in concat()
leetlimit = 5
#extraconcat is used to provde deeper levels of concatenation. 0 = off 1 = on
extraconcat = 1
#additionalcommonnumbers is used to provide additional integers to be added to the commonnumbers list. Separate with commas, accepts ranges denoted with a '-' character
additionalcommonnumbers = ''
#commonnumberseparator enables the ability to separate concatenated words with common numbers  0 = off 1 = on
commonnumberseparator = 0
#specialcharseparator enables the ability to separate concatenated words with special characters 0 = off 1 = on
speccharseparator = 1
#singleseparator enables concatenation of provided arrays separating each element with another, in addition to both
singleseparator = 1
#reversewords enables the reversal of certain words such as the description, businessname and alt business names "company" to "ynapmoc" 0 = off 1 = on
reversewords = 0
#========================================


ssid = input("Please enter the SSID:  ")
bizname = input("Please enter Business Name:  ")
aka = input("Please enter any alternative business names or abbreiviated business names <pharma for pharmaceuticals, including apostrophes, removing 'and', etc>. Separate with commas:  ")
phone = input("Please enter business phone number:  ")
date = input("Please enter the founding date using MM-DD-YYYY. Also accepts MM-YYYY and YYYY:  ")
print("Address information should be supplied using the following format:  ")
print("num=<####>,street=<street address>,town=<township>,zipcode=<zip>,state=<2character state>")
addr = input("Please enter the business address. Shorthand road types will be auto generated:  ")
alttownship = input("Please enter any other or different township names separated by commas:  ")
desc = input("Please enter words describing what the business does, separated by commas:  ")
owner = input("Please enter owner(s)'s name. Separate with Comma if more than 1:  ")
ownerphone = input("Please enter owner's phone:  ")
owneraddr = input("Please enter owner's address:  ")
slogans = input("Please enter any business slogans, separated by commas:  ")
other = input("Please enter other words that could be popular choices for the business or it's owner:  ")

wordlistfile = ssid + '_wordlist.txt'
wlfhandle = open(wordlistfile,'w')
wordlistall = []
leetlist = []
acronym = []
biznameparts = bizname.split(" ")
tempacro = ''
underarr = []

#Create List of Acronyms
#========================================
for word in biznameparts:
    tempacro += word[0].lower()
acronym.append(tempacro)
tempacro = ''
isallupper = 0
for word in biznameparts:
    if word.upper() == word:
        tempacro += word.lower()
        isallupper = 1
    else:
        tempacro += word[0].lower()
if isallupper == 1:
    acronym.append(tempacro)
altbiznames = []
if aka != "":
    altbiznames = aka.split(",")
    for alt in altbiznames:
        tempacro = ''
        words = alt.split(" ")
        for word in words:
            tempacro += word[0].lower()
        acronym.append(tempacro)
        tempacro = ''
        isallupper = 0
        for word in words:
            if word.upper() == word:
                tempacro += word.lower()
                isallupper = 1
            else:
                tempacro += word[0].lower()
        if isallupper == 1:
            acronym.append(tempacro) 
            

#Split Other Provided Lists
#========================================

phoneentries = phone.split(",")
descentries = desc.split(",")
ownerentries = owner.split(",")
sloganentries = slogans.split(",")
otherentries = other.split(",")
ownerphoneentries = ownerphone.split(",")
alttownshipentries = alttownship.split(",")

#Add reverse words to respective lists
#========================================
if reversewords == 1:
    tempreverse = ''
    if aka != '':
        biznametemp = []
        for abn in altbiznames:
            tempreverse = ''
            if len(abn.split(" ")) == 1:
                for c in reversed(abn):
                    tempreverse+=c.lower()
                biznametemp.append(tempreverse)
        altbiznames+=biznametemp
    tempreverse = ''

    if len(acronym) >= 1:
        acrotemp = []
        for acro in acronym:
            tempreverse = ''
            for c in reversed(acro):
                tempreverse+=c.lower()
            acrotemp.append(tempreverse)
        acronym+=acrotemp
    tempreverse = ''
    if phone != '':
        phoneentriestemp = []
        for phoneentry in phoneentries:
            tempreverse = ''
            for c in reversed(phoneentry):
                tempreverse+=c.lower()
            phoneentriestemp.append(tempreverse)
        phoneentries+=phoneentriestemp
    tempreverse = ''
    if desc != '':
        descentriestemp = []
        for descentry in descentries:
            tempreverse = ''
            for c in reversed(descentry):
                tempreverse+=c.lower()
            descentriestemp.append(tempreverse)
        descentries+=descentriestemp
    if slogans != '':
        tempreverse = ''
        sloganentriestemp = []
        for sloganentry in sloganentries:
            tempreverse = ''
            for c in reversed(sloganentry):
                tempreverse+=c.lower()
            sloganentriestemp.append(tempreverse)
        sloganentries+=sloganentriestemp
    if other != '':
        tempreverse = ''
        otherentriestemp = []
        for otherentry in otherentries:
            tempreverse = ''
            for c in reversed(otherentry):
                tempreverse+=c.lower()
            otherentriestemp.append(tempreverse)
        otherentries+=otherentriestemp
    
#Acronymize partial bizname
#========================================
if aka != '':
    tempaltbizname = []
    abnentries = aka.split(',')
    for abnentry in abnentries:
        
        abnparts = abnentry.split(" ")
        if len(abnparts) > 1:
            for part in abnparts:
                tempstring = ''
                for p in abnparts:
                    if part == p:
                        tempstring+=p
                    else:
                        tempstring+=p[0].upper()
                tempaltbizname.append(tempstring)
            print('tempaltbiz')
            print(tempaltbizname)
    altbiznames+=tempaltbizname
    
if len(biznameparts) > 1:
    for biznamepart in biznameparts:
        tempstring = ''
        for bnp in biznameparts:
            if bnp == biznamepart:
                tempstring+=bnp
            else:
                tempstring+=bnp[0].upper()
        print('HERE ' + tempstring)
        altbiznames.append(tempstring)

        
#Collect address parts
#========================================
streetobjects = []
num = street = town = zipcode = state = ''
ownernum = ownerstreet = ownertown = ownerzipcode = ownerstate = ''
if addr != "":
    addrconvert = open('addrconvert.txt','r')
    addrconvertcon = addrconvert.readlines()
    streettypeobj = []

    addressparts = addr.split(",")
    for part in addressparts:
        if 'num' in part:
            numa = part.split("=")
            num = numa[1]
        elif 'street' in part:
            streeta = part.split("=")
            street = streeta[1]
        elif 'town' in part:
            towna = part.split("=")
            town = towna[1]
        elif 'zipcode' in part:
            zipcodea = part.split("=")
            zipcode = zipcodea[1]
        elif 'state' in part:
            statea = part.split("=")
            if len(statea[1]) == 2:
                state = statea[1]
            else:
                state = ''
    streetparts = street.split(" ")
    streettype = streetparts[len(streetparts)-1]
    for line in addrconvertcon:
        linesplit = line.split(",")
        for st in linesplit:
            if streettype.upper() == st.upper():
                for stt in linesplit:
                    if stt.upper() != streettype.upper():
                        streettypeobj.append(stt.lower())
    addrconvert.close()
if owneraddr != "":
    addrconvert = open('addrconvert.txt','r')
    addrconvertcon = addrconvert.readlines()
    ownerstreettypeobj = []
    owneraddressparts = owneraddr.split(",")
    for part in owneraddressparts:
        if 'num' in part:
            ownernuma = part.split("=")
            ownernum = numa[1]
        elif 'street' in part:
            ownerstreeta = part.split("=")
            ownerstreet = streeta[1]
        elif 'town' in part:
            ownertowna = part.split("=")
            ownertown = towna[1]
        elif 'zipcode' in part:
            ownerzipcodea = part.split("=")
            ownerzipcode = zipcodea[1]
        elif 'state' in part:
            ownerstatea = part.split("=")
            if len(ownerstatea[1]) == 2:
                ownerstate = ownerstatea[1]
            else:
                ownerstate = ''
    ownerstreetparts = ownerstreet.split(" ")
    ownerstreettype = ownerstreetparts[len(ownerstreetparts)-1]
    for line in addrconvertcon:
        linesplit = line.split(",")
        for st in linesplit:
            if ownerstreettype.upper() == st.upper():
                for stt in linesplit:
                    if stt.upper() != ownerstreettype.upper():
                        ownerstreettypeobj.append(stt.lower())
addrconvert.close()
print(state) 
#Create Acronym for town
#========================================
townacro = []
tempacro = ''
if town != '':
    townsplit = town.split(" ")
    if len(townsplit) > 1:   
        for word in townsplit:
            tempacro += word[0].lower()
        townacro.append(tempacro)
tempacro = ''
if ownertown != '':
    ownertownsplit = ownertown.split(" ")
    if len(ownertownsplit) > 1:   
        for word in ownertownsplit:
            tempacro += word[0].lower()
        townacro.append(tempacro)        
#Collect date parts
#========================================
months = [['01','january'], ['02','february'], ['03','march'], ['04','april'], ['05','may'], ['06','june'], ['07','july'], ['08','august'], ['09','september'], ['10','october'], ['11','november'], ['12','december']]
yyyy = mmyyyy = ddmmyyyy = mmddyyyy = yy = mmddyy = ddmmyy = mmyy = month = ''
if date != "":
    dateparts = date.split("-")
    if len(dateparts) == 1:
        yyyy = dateparts[0]
        yy = yyyy[2:]
    elif len(dateparts) == 2:
        mm = dateparts[0]
        yyyy = dateparts[1]
        yy = yyyy[2:]
        mmyyyy = mm + yyyy
        mmyy = mm + yy
        month = ''
        for m in months:
            if mm == m[0]:
                month = m[1]
    elif len(dateparts) == 3:
        mm = dateparts[0]
        dd = dateparts[1]
        yyyy = dateparts[2]
        yy = yyyy[2:]
        mmyyyy = mm + yyyy
        mmyy = mm + yy
        ddmmyyyy = dd + mm + yyyy
        mmddyyyy = mm + dd + yyyy
        ddmmyy = dd + mm + yy
        mmddyy = mm + dd + yy
        month = ''
        for m in months:
            if mm == m[0]:
                month = m[1]
#Get phone parts 
#========================================
phone = phone.replace(" ","").replace("-","").replace("(","").replace(")","").replace("#","")
phonefirst3 = phone[:3]
phonelast4 = phone[len(phone)-4:]
phonemid3 = phone[3:6]
ownerphone = ownerphone.replace(" ","").replace("-","").replace("(","").replace(")","").replace("#","")
ownerphonefirst3 = ownerphone[:3]
ownerphonelast4 = ownerphone[len(phone)-4:]
ownerphonemid3 = ownerphone[3:6]

#Replace characters with 1337 speak. Common will create smaller list, focusing on commonly substituted characters
#========================================
leetlist = []
def leetconvert(word,common):
    global leetlist
    convert = [['a','@','4'],['b','8'],['c','(','[','<'],['d','6'],['e','3'],['f','#'],['g','9'],['h','#'],['i','1','!'],['k','<'],['o','0','()'],['q','9'],['s','5','$'],['t','+'],['w','uu','2u'],['y','?']]
    convertcommon = [['a','@','4'],['e','3'],['i','1','!'],['o','0'],['s','5','$']]
    if common == 1:
        i = 0
        for c in word:
            for letter in convertcommon:
                if c.lower() == letter[0]:
                    for r in letter[1:]:
                        tempword = word[:i] + r + word[i+1:]
                        leetlist.append(tempword)
                        leetconvert(tempword,1)
            i+=1
    elif common == 0:
        i = 0
        for c in word:
            for letter in convert:
                if c.lower() == letter[0]:
                    for r in letter[1:]:
                        tempword = word[:i] + r + word[i+1:]
                        leetlist.append(tempword)
                        leetconvert(tempword,1)
            i+=1

#def filter(word):

#Combine commonly seen combinations of business specific data
#========================================
def concat(wordarr): 
    global underarr
    global leetlimit
    global commonnumberseparator
    global speccharseparator
    global singleseparator
    global commonnumbers
    if commonnumberseparator == 1:
        concatnumbers = []
        global commonnumbers
        global phonelast4
        global phonefirst3
        global phonemid3
        global ownerphonelast4
        global ownerphonefirst3
        global ownerphonemid3
        
        concatnumbers += commonnumbers 
        concatnumbers += phonelast4
        concatnumbers += phonefirst3
        concatnumbers += phonemid3
        concatnumbers += ownerphonelast4
        concatnumbers += ownerphonefirst3
        concatnumbers += ownerphonemid3
    tempwordarr = []
    if speccharseparator == 1:
        specchars = ['-','_','!','@','#','$','%','&','*','?','+',' ']
    convertcommonchars = ['a','e','i','o','s']
    
    tempword = ""
    tempword2 = ""
    for word in wordarr:
        tempword += word
    tempwordarr.append(tempword)
    tempwordarr.append(tempword[0].upper() + tempword[1:].lower())
    tempwordarr.append(tempword.upper())
    tempwordarr.append(tempword.lower())

    tempword = ""
    tempword2 = ""
    for word in wordarr:
        tempword+= word[0].upper() + word[1:]
        tempword2+= word[0].lower() + word[1:]

    tempwordarr.append(tempword)
    tempwordarr.append(tempword2)
    
    for convert in tempwordarr:
        convertcharcounter = 0
        for c in convert:
            if c.lower() in convertcommonchars:
                convertcharcounter += 1
        if convertcharcounter <= leetlimit:
            leetconvert(convert,1)
    if commonnumberseparator == 1:    
        for number in concatnumbers:
            tempword = ""
            tempword2 = ""
            tempword3 = ""
            for word in wordarr:
                tempword += word + number
                tempword2+= word[0].upper() + word[1:] + number
                tempword3+= word[0].lower() + word[1:] + number
            tempword = tempword[:len(tempword) -1]
            tempword2 = tempword2[:len(tempword2) -1]
            tempword3 = tempword3[:len(tempword3) -1]

            tempwordarr.append(tempword)
            tempwordarr.append(tempword2)
            tempwordarr.append(tempword3)
            tempwordarr.append(tempword.upper())
            tempwordarr.append(tempword.lower())
    if speccharseparator == 1:    
        for specchar in specchars:
            tempword = ""
            tempword2 = ""
            tempword3 = ""
            for word in wordarr:
                tempword += word + specchar
                tempword2+= word[0].upper() + word[1:] + specchar
                tempword3+= word[0].lower() + word[1:] + specchar
            tempword = tempword[:len(tempword) -1]
            tempword2 = tempword2[:len(tempword2) -1]
            tempword3 = tempword3[:len(tempword3) -1]

            tempwordarr.append(tempword)
            tempwordarr.append(tempword2)
            tempwordarr.append(tempword3)
            tempwordarr.append(tempword.upper())
            tempwordarr.append(tempword.lower())

    tempwordarr = list(set(tempwordarr))
    
    return tempwordarr
#no leet convert concat, reduces wordlist and increases performance by removing runaway wordlists in certain situations such as concatenating longer words
#change called routine to normal concat() for full effect, will create massive wordlists
def concatnoleet(wordarr):
    global underarr
    global commonnumberseparator
    global speccharseparator
    global singleseparator
    global commonnumbers
    global phonelast4
    global phonefirst3
    global phonemid3
    global ownerphonelast4
    global ownerphonefirst3
    global ownerphonemid3
    if commonnumberseparator == 1:
        concatnumbers = []
        global commonnumbers
        global phonelast4
        global phonefirst3
        global phonemid3
        global ownerphonelast4
        global ownerphonefirst3
        global ownerphonemid3
        concatnumbers += commonnumbers 
        concatnumbers += phonelast4
        concatnumbers += phonefirst3
        concatnumbers += phonemid3
        concatnumbers += ownerphonelast4
        concatnumbers += ownerphonefirst3
        concatnumbers += ownerphonemid3
    tempwordarr = []
    if speccharseparator == 1:
        specchars = ['-','_','!','@','#','$','%','&','*','?','+',' ']
    
    
    tempword = ""
    tempword2 = ""
    for word in wordarr:
        tempword += word
    tempwordarr.append(tempword)
    tempwordarr.append(tempword[0].upper() + tempword[1:].lower())
    tempwordarr.append(tempword.upper())
    tempwordarr.append(tempword.lower())

    tempword = ""
    tempword2 = ""
    for word in wordarr:
        tempword+= word[0].upper() + word[1:]
        tempword2+= word[0].lower() + word[1:]

    tempwordarr.append(tempword)
    tempwordarr.append(tempword2)
    
    if commonnumberseparator == 1:    
        for number in specchars:
            tempword = ""
            tempword2 = ""
            tempword3 = ""
            for word in wordarr:
                tempword += word + number
                tempword2+= word[0].upper() + word[1:] + number
                tempword3+= word[0].lower() + word[1:] + number
            tempword = tempword[:len(tempword) -1]
            tempword2 = tempword2[:len(tempword2) -1]
            tempword3 = tempword3[:len(tempword3) -1]

            tempwordarr.append(tempword)
            tempwordarr.append(tempword2)
            tempwordarr.append(tempword3)
            tempwordarr.append(tempword.upper())
            tempwordarr.append(tempword.lower())
    if speccharseparator == 1:    
        for specchar in specchars:
            tempword = ""
            tempword2 = ""
            tempword3 = ""
            for word in wordarr:
                tempword += word + specchar
                tempword2+= word[0].upper() + word[1:] + specchar
                tempword3+= word[0].lower() + word[1:] + specchar
            tempword = tempword[:len(tempword) -1]
            tempword2 = tempword2[:len(tempword2) -1]
            tempword3 = tempword3[:len(tempword3) -1]

            tempwordarr.append(tempword)
            tempwordarr.append(tempword2)
            tempwordarr.append(tempword3)
            tempwordarr.append(tempword.upper())
            tempwordarr.append(tempword.lower())

    tempwordarr = list(set(tempwordarr))
    
    return tempwordarr       
#Basic word manipulation. Separator character replacement, capitalization substition. For standard input values
#========================================
def wordengine(word):
    global leetlimit
    tempwordarr = []
    convertcommonchars = ['a','e','i','o','s']
    global underarr
    tempwordarr.append(word)
    tempwordarr.append(word.upper())
    tempwordarr.append(word.lower())
    separatorsplit = word.split(" ")
    if (len(word.replace(" ","")) >= 8):
        tempwordarr.append(word.replace(" ",""))
        tempwordarr.append(word[0].upper() + word[1:].replace(" ",""))
        tempwordarr.append(word[0].lower() + word[1:].replace(" ",""))
        tempwordarr.append(word.replace(" ","").lower())
        tempwordarr.append(word.replace(" ","").upper())
        tempwordarr.append(word[0].upper() + word[1:].replace(" ","").lower())
        tempwordarr.append(word[0].lower() + word[1:].replace(" ","").lower())
    else:
        underarr.append(word.replace(" ",""))
        underarr.append(word[0].upper() + word[1:].replace(" ",""))
        underarr.append(word[0].lower() + word[1:].replace(" ",""))
        underarr.append(word.replace(" ","").lower())
        underarr.append(word.replace(" ","").upper())
        underarr.append(word[0].upper() + word[1:].replace(" ","").lower())
        underarr.append(word[0].lower() + word[1:].replace(" ","").lower())
        
    tempwordarr.append(word.replace(" ","-"))
    tempwordarr.append(word.replace(" ","_"))
    tempwordarr.append(word.replace(" ","-").upper())
    tempwordarr.append(word.replace(" ","_").upper())
    tempwordarr.append(word[0].upper() + word[1:])
    tempwordarr.append(word[0].lower() + word[1:])
    tempwordarr.append(word[0].upper() + word[1:].lower())
    tempwordarr.append(word[0].lower() + word[1:].lower())
   
    if len(separatorsplit) > 1:
        tempword = ""
        for part in separatorsplit:
            tempword+= part[0].upper() + part[1:] + " "
        tempwordarr.append(tempword[:len(tempword)-1])
        tempwordarr.append(tempword[:len(tempword)-1].replace(" ","-"))
        tempwordarr.append(tempword[:len(tempword)-1].replace(" ","_"))
        if (len(tempword.replace(" ","")) >= 8):
            tempwordarr.append(tempword[:len(tempword)-1].replace(" ",""))
        else:
            underarr.append(tempword[:len(tempword)-1].replace(" ",""))
        tempword = ""
        for part in separatorsplit:
            tempword+= part[0].lower() + part[1:] + " "
        tempwordarr.append(tempword[:len(tempword)-1])
        tempwordarr.append(tempword[:len(tempword)-1].replace(" ","-"))
        tempwordarr.append(tempword[:len(tempword)-1].replace(" ","_"))
        if (len(tempword.replace(" ","")) >= 8):
            tempwordarr.append(tempword[:len(tempword)-1].replace(" ",""))
        else:
            underarr.append(tempword[:len(tempword)-1].replace(" ",""))
    tempwordarr = list(set(tempwordarr))
    
    for convert in tempwordarr:
        convertcharcounter = 0
        for c in convert:
            if c.lower() in convertcommonchars:
                convertcharcounter += 1
                
        if convertcharcounter <= leetlimit:
            leetconvert(convert,1)

    return tempwordarr
            
        
        
        

#Add inputs if over 8 chars
#========================================
if (len(acronym[0]) >= 1):
    for acro in acronym:
        wordlist = wordengine(acro)
        for w in wordlist:
            if len(w) >=8:
                wordlistall.append(w)
            else:
                underarr.append(w)
            
if (len(ssid) >= 8):
    wordlist = wordengine(ssid)
    for w in wordlist:
        if len(w) >=8:
            wordlistall.append(w)
        else:
            underarr.append(w)
else:
    wordlist = wordengine(ssid)
    for w in wordlist:
        underarr.append(w)

if (len(bizname) >= 8):
    wordlist = wordengine(bizname)
    for w in wordlist:
        if len(w) >=8:
            wordlistall.append(w)
        else:
            underarr.append(w)
    
else:
    wordlist = wordengine(bizname)
    for w in wordlist:
        underarr.append(w)
if phone != '':
    for phoneentry in phoneentries:
        if (len(phoneentry) >= 8):
            wordlist = wordengine(phoneentry)
            for w in wordlist:
                wordlistall.append(w)
        else:
            wordlist = wordengine(phoneentry)
            for w in wordlist:
                underarr.append(w)
if aka != '':      
    for altbizname in altbiznames:
        if (len(altbizname) >= 8):
            wordlist = wordengine(altbizname)
            for w in wordlist:
                if len(w) >=8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
        else:
            wordlist = wordengine(altbizname)
            for w in wordlist:
                underarr.append(w)
if desc != '':
    
    for descentry in descentries:
        if (len(descentry) >= 8):
            wordlist = wordengine(descentry)
            for w in wordlist:
                if len(w) >=8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
        else:
            wordlist = wordengine(descentry)
            for w in wordlist:
                underarr.append(w)
if len(ownerentries[0]) > 0:
    for ownerentry in ownerentries:
        if (len(ownerentry) >= 8):
            wordlist = wordengine(ownerentry)
            for w in wordlist:
                if len(w) >=8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
        else:
            wordlist = wordengine(ownerentry)
            for w in wordlist:
                underarr.append(w)
if len(ownerphoneentries[0]) > 0:
    for ownerphoneentry in ownerphoneentries:
        if (len(ownerphoneentry) >= 8):
            wordlist = wordengine(ownerphoneentry)
            for w in wordlist:
                wordlistall.append(w)
if len(sloganentries[0]) > 0:
    for slogansentry in sloganentries:
        if (len(slogansentry) >= 8):
            wordlist = wordengine(slogansentry)
            for w in wordlist:
                if len(w) >=8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
        else:
            wordlist = wordengine(sloganentry)
            for w in wordlist:
                underarr.append(w)
if len(otherentries[0]) > 0:
    for otherentry in otherentries:
        if (len(otherentry) >= 8):
            wordlist = wordengine(otherentry)
            for w in wordlist:
                if len(w) >=8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
        else:
            wordlist = wordengine(otherentry)
            for w in wordlist:
                underarr.append(w)
if ddmmyyyy != "":            
    wordlistall.append(ddmmyyyy)
    wordlistall.append(mmddyyyy)
if ddmmyy != "":
    underarr.append(ddmmyy)
    underarr.append(mmddyy)
    
print('bizname')
print(bizname)
print('aka')
print(altbiznames)
print('acronym')
print(acronym)




        
#Call concatenate routines based on type of input data. Will also append common words such as WiFi, patterned numbers and special characters
#========================================
#bizname + common words
if bizname != "":
    wordlist = concat([bizname.replace(" ",""),'wi','fi'])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
    
    wordlist = concatnoleet([bizname.replace(" ",""),'wireless'])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w) 
    wordlist = concatnoleet([bizname.replace(" ",""),'staff'])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
    wordlist = concatnoleet([bizname.replace(" ",""),'corporate'])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
    wordlist = concatnoleet([bizname.replace(" ",""),'business'])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w) 
    wordlist = concatnoleet([bizname.replace(" ",""),'employee'])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w) 

#bizname + last 4 phone
if bizname != "" and phonelast4 != "":
    wordlist = concat([bizname.replace(" ",""),phonelast4])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if bizname != "" and phonemid3 != "":
    wordlist = concat([bizname.replace(" ",""),phonemid3])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
#bizname + street number
if bizname != "" and num != "":
    wordlist = concat([bizname.replace(" ",""),num])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
#bizname + zip
if bizname != "" and zipcode != "":
    wordlist = concat([bizname.replace(" ",""),zipcode])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
#bizname + last 4 owner phone
if bizname != "" and ownerphonelast4 != "":
    wordlist = concat([bizname.replace(" ",""),ownerphonelast4])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if bizname != "" and ownerphonemid3 != "":
    wordlist = concat([bizname.replace(" ",""),ownerphonemid3])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
#bizname + owner street number
if bizname != "" and ownernum != "":
    wordlist = concat([bizname.replace(" ",""),ownernum])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
#bizname + owner zip
if bizname != "" and ownerzipcode != "":
    wordlist = concat([bizname.replace(" ",""),ownerzipcode])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
#bizname + first 3 biz phone
if bizname != "" and phonefirst3 != "":
    wordlist = concat([bizname.replace(" ",""),phonefirst3])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
#bizname + township
if bizname != "" and town != "":
    wordlist = concat([bizname.replace(" ",""),town])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if bizname != "" and len(townacro) > 0:
    for ta in townacro:
        wordlist = concat([bizname.replace(" ",""),ta])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#bizname + township + street number
if bizname != "" and town != "" and num != "":
    wordlist = concat([bizname.replace(" ",""),town,num])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if bizname != "" and len(townacro) > 0 and num != "":
    for ta in townacro:
        wordlist = concat([bizname.replace(" ",""),ta,num])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#bizname + street number + township
if bizname != "" and town != "" and num != "":
    wordlist = concat([bizname.replace(" ",""),num,town])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if bizname != "" and len(townacro) > 0 and num != "":
    for ta in townacro:
        wordlist = concat([bizname.replace(" ",""),num,ta])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#bizname + full street
if bizname != "" and town != "" and num != "" and street != "":
    wordlist = concat([bizname.replace(" ",""),num,street.replace(" ",""),town])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
    if len(streettypeobj) > 0:
        wordlist = concat([bizname.replace(" ",""),num,streettypeobj[0],town])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if bizname != "" and len(townacro) > 0 and num != "" and street != "":
    for ta in townacro:
        wordlist = concat([bizname.replace(" ",""),num,street.replace(" ",""),ta])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        if len(streettypeobj) > 0:
            wordlist = concat([bizname.replace(" ",""),num,streettypeobj[0],ta])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#bizname + alt township 
if bizname != "" and alttownship != "":
    for alttown in alttownshipentries:
        wordlist = concat([bizname.replace(" ",""),alttown])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#bizname + alt township + street number
if bizname != "" and alttownship != "" and num != "":
    for alttown in alttownshipentries:
        wordlist = concat([bizname.replace(" ",""),alttown,num])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#bizname + street number + alt township
if bizname != "" and alttownship != "" and num != "":
    for alttown in alttownshipentries:
        wordlist = concat([bizname.replace(" ",""),num,alttown])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#bizname + full street (alt)
if bizname != "" and alttownship != "" and num != "" and street != "":
    for alttown in alttownshipentries:
        wordlist = concat([bizname.replace(" ",""),num,street.replace(" ",""),alttown])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        if len(streettypeobj) > 0:
            wordlist = concat([bizname.replace(" ",""),num,streettypeobj[0],alttown])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#bizname + dates
if bizname != "" and yyyy != "":
    wordlist = concat([bizname.replace(" ",""),yyyy])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if bizname != "" and yy != "":
    wordlist = concat([bizname.replace(" ",""),yy])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if bizname != "" and ddmmyyyy != "":
    wordlist = concat([bizname.replace(" ",""),ddmmyyyy])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if bizname != "" and mmddyyyy != "":
    wordlist = concat([bizname.replace(" ",""),mmddyyyy])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if bizname != "" and mmddyy != "":
    wordlist = concat([bizname.replace(" ",""),mmddyy])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if bizname != "" and ddmmyy != "":
    wordlist = concat([bizname.replace(" ",""),ddmmyy])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if bizname != "" and mmyyyy != "":
    wordlist = concat([bizname.replace(" ",""),mmyyyy])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if bizname != "" and mmyy != "":
    wordlist = concat([bizname.replace(" ",""),mmyy])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if bizname != "" and month != "":
    wordlist = concat([bizname.replace(" ",""),month])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if bizname != "" and month != "" and yyyy != "":
    wordlist = concat([bizname.replace(" ",""),month,yyyy])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if bizname != "" and month != "" and yy != "":
    wordlist = concat([bizname.replace(" ",""),month,yy])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
#ALT
#altbizname + common words

if len(altbiznames) >= 1:
    for abn in altbiznames:
        wordlist = concat([abn.replace(" ",""),'wi','fi'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        wordlist = concatnoleet([abn.replace(" ",""),'wireless'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w) 
        wordlist = concatnoleet([abn.replace(" ",""),'staff'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        wordlist = concatnoleet([abn.replace(" ",""),'corporate'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        wordlist = concatnoleet([abn.replace(" ",""),'business'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w) 
        wordlist = concatnoleet([abn.replace(" ",""),'employee'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#altbizname + last 4 phone
if ((len(altbiznames) >= 1) and (phonelast4 != "")):
    for abn in altbiznames:
        wordlist = concat([abn.replace(" ",""),phonelast4])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(altbiznames) >= 1) and (phonemid3 != "")):
    for abn in altbiznames:
        wordlist = concat([abn.replace(" ",""),phonemid3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#altbizname + street number
if ((len(altbiznames) >= 1) and (num != "")):
    for abn in altbiznames:
        wordlist = concat([abn.replace(" ",""),num])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#altbizname + zip
if ((len(altbiznames) >= 1) and (zipcode != "")):
    for abn in altbiznames:
        wordlist = concat([abn.replace(" ",""),zipcode])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#altbizname + last 4 owner phone
if ((len(altbiznames) >= 1) and (ownerphonelast4 != "")):
    for abn in altbiznames:
        wordlist = concat([abn.replace(" ",""),ownerphonelast4])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(altbiznames) >= 1) and (ownerphonemid3 != "")):
    for abn in altbiznames:
        wordlist = concat([abn.replace(" ",""),ownerphonemid3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#altbizname + owner street number
if ((len(altbiznames) >= 1) and (ownernum != "")):
    for abn in altbiznames:
        wordlist = concat([abn.replace(" ",""),ownernum])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#altbizname + owner zip
if ((len(altbiznames) >= 1) and (ownerzipcode != "")):
    for abn in altbiznames:
        wordlist = concat([abn.replace(" ",""),ownerzipcode])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#altbizname + first 3 biz phone
if ((len(altbiznames) >= 1) and (phonefirst3 != "")):
    for abn in altbiznames:
        wordlist = concat([abn.replace(" ",""),phonefirst3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#altbizname + township
if ((len(altbiznames) >= 1) and (town != "")):
    for abn in altbiznames:
        wordlist = concat([abn.replace(" ",""),town])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(altbiznames) >= 1) and (len(townacro) > 0 )):
    for ta in townacro:
        for abn in altbiznames:
            wordlist = concat([abn.replace(" ",""),ta])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#altbizname + township + street number
if ((len(altbiznames) >= 1) and (town != "") and (num != "")):
    for abn in altbiznames:
        wordlist = concat([abn.replace(" ",""),town,num])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(altbiznames) >= 1) and (len(townacro) > 0) and (num != "")):
    for ta in townacro:
        for abn in altbiznames:
            wordlist = concat([abn.replace(" ",""),ta,num])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#altbizname + street number + township
if ((len(altbiznames) >= 1) and (town != "") and (num != "")):
    for abn in altbiznames:
        wordlist = concat([abn.replace(" ",""),num,town])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(altbiznames) >= 1) and (len(townacro) > 0) and (num != "")):
    for ta in townacro:
        for abn in altbiznames:
            wordlist = concat([abn.replace(" ",""),num,ta])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#altbizname + full street
if ((len(altbiznames) >= 1) and (town != "") and (num != "") and (street != "")):
    for abn in altbiznames:
        wordlist = concat([abn.replace(" ",""),num,street.replace(" ",""),town])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        if len(streettypeobj) > 0:
            wordlist = concat([abn.replace(" ",""),num,streettypeobj[0],town])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(altbiznames) >= 1) and (len(townacro) > 0) and (num != "") and (street != "")):
    for ta in townacro:
        for abn in altbiznames:
            wordlist = concat([abn.replace(" ",""),num,street.replace(" ",""),ta])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
            if len(streettypeobj) > 0:
                wordlist = concat([abn.replace(" ",""),num,streettypeobj[0],ta])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#altbizname + alt township 
if ((len(altbiznames) >= 1) and (alttownship != "")):
    for abn in altbiznames:
        for alttown in alttownshipentries:
            wordlist = concat([abn.replace(" ",""),alttown])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#altbizname + alt township + street number
if ((len(altbiznames) >= 1) and (alttownship != "") and (num != "")):
    for abn in altbiznames:
        for alttown in alttownshipentries:
            wordlist = concat([abn.replace(" ",""),alttown,num])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#altbizname + street number + alt township
if ((len(altbiznames) >= 1) and (alttownship != "") and (num != "")):
    for abn in altbiznames:
        for alttown in alttownshipentries:
            wordlist = concat([abn.replace(" ",""),num,alttown])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#altbizname + full street (alt)
if ((len(altbiznames) >= 1) and (alttownship != "") and (num != "") and (street != "")):
    for abn in altbiznames:
        for alttown in alttownshipentries:
            wordlist = concat([abn.replace(" ",""),num,street.replace(" ",""),alttown])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
            if len(streettypeobj) > 0:
                wordlist = concat([abn.replace(" ",""),num,streettypeobj[0],alttown])
                for w in wordlist:
                    if len(w) >= 8:
                        wordlistall.append(w)
                    else:
                        underarr.append(w)
#altbizname + dates
if ((len(altbiznames) >= 1) and (yyyy != "")):
    for abn in altbiznames:
        wordlist = concat([abn.replace(" ",""),yyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(altbiznames) >= 1) and (yy != "")):
    for abn in altbiznames:
        wordlist = concat([abn.replace(" ",""),yy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(altbiznames) >= 1) and (ddmmyyyy != "")):
    for abn in altbiznames:
        wordlist = concat([abn.replace(" ",""),ddmmyyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(altbiznames) >= 1) and (mmddyyyy != "")):
    for abn in altbiznames:
        wordlist = concat([abn.replace(" ",""),mmddyyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(altbiznames) >= 1) and (mmddyy != "")):
    for abn in altbiznames:
        wordlist = concat([abn.replace(" ",""),mmddyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(altbiznames) >= 1) and (ddmmyy != "")):
    for abn in altbiznames:
        wordlist = concat([abn.replace(" ",""),ddmmyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(altbiznames) >= 1) and (mmyyyy != "")):
    for abn in altbiznames:
        wordlist = concat([abn.replace(" ",""),mmyyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(altbiznames) >= 1) and (mmyy != "")):
    for abn in altbiznames:
        wordlist = concat([abn.replace(" ",""),mmyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(altbiznames) >= 1) and (month != "")):
    for abn in altbiznames:
        wordlist = concat([abn.replace(" ",""),month])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(altbiznames) >= 1) and (month != "") and (yyyy != "")):
    for abn in altbiznames:
        wordlist = concat([abn.replace(" ",""),month,yyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(altbiznames) >= 1) and (month != "") and (yy != "")):
    for abn in altbiznames:
        wordlist = concat([abn.replace(" ",""),month,yy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#ACRONYMS

if len(acronym) > 0:
    for acro in acronym:
        wordlist = concat([acro.replace(" ",""),'wi','fi'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        wordlist = concatnoleet([acro.replace(" ",""),'wireless'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w) 
        wordlist = concatnoleet([acro.replace(" ",""),'staff'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        wordlist = concatnoleet([acro.replace(" ",""),'corporate'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        wordlist = concatnoleet([acro.replace(" ",""),'business'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        wordlist = concatnoleet([acro.replace(" ",""),'employee'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#acronym + last 4 phone
if ((len(acronym) > 0) and (phonelast4 != "")):
    for acro in acronym:
        wordlist = concat([acro.replace(" ",""),phonelast4])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(acronym) > 0) and (phonemid3 != "")):
    for acro in acronym:
        wordlist = concat([acro.replace(" ",""),phonemid3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#acronym + street number
if ((len(acronym) > 0) and (num != "")):
    for acro in acronym:
        wordlist = concat([acro.replace(" ",""),num])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#acronym + zip
if ((len(acronym) > 0) and (zipcode != "")):
    for acro in acronym:
        wordlist = concat([acro.replace(" ",""),zipcode])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#acronym + last 4 owner phone
if ((len(acronym) > 0) and (ownerphonelast4 != "")):
    for acro in acronym:
        wordlist = concat([acro.replace(" ",""),ownerphonelast4])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(acronym) > 0) and (ownerphonemid3 != "")):
    for acro in acronym:
        wordlist = concat([acro.replace(" ",""),ownerphonemid3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#acronym + owner street number
if ((len(acronym) > 0) and (ownernum != "")):
    for acro in acronym:
        wordlist = concat([acro.replace(" ",""),ownernum])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#acronym + owner zip
if ((len(acronym) > 0) and (ownerzipcode != "")):
    for acro in acronym:
        wordlist = concat([acro.replace(" ",""),ownerzipcode])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#acronym + first 3 biz phone
if ((len(acronym) > 0) and (phonefirst3 != "")):
    for acro in acronym:
        wordlist = concat([acro.replace(" ",""),phonefirst3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#acronym + township
if ((len(acronym) > 0) and (town != "")):
    for acro in acronym:
        wordlist = concat([acro.replace(" ",""),town])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(acronym) > 0) and (len(townacro) > 0)):
    for ta in townacro:
        for acro in acronym:
            wordlist = concat([acro.replace(" ",""),town])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#acronym + township + street number
if ((len(acronym) > 0) and (town != "") and (num != "")):
    for acro in acronym:
        wordlist = concat([acro.replace(" ",""),town,num])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(acronym) > 0) and (len(townacro) > 0) and (num != "")):
    for ta in townacro:
        for acro in acronym:
            wordlist = concat([acro.replace(" ",""),ta,num])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#acronym + street number + township
if ((len(acronym) > 0) and (town != "") and (num != "")):
    for acro in acronym:
        wordlist = concat([acro.replace(" ",""),num,town])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(acronym) > 0) and (len(townacro) > 0) and (num != "")):
    for ta in townacro:
        for acro in acronym:
            wordlist = concat([acro.replace(" ",""),num,ta])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#acronym + full street
if ((len(acronym) > 0) and (town != "") and (num != "") and (street != "")):
    for acro in acronym:
        wordlist = concat([acro.replace(" ",""),num,street.replace(" ",""),town])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        if len(streettypeobj) > 0:
            wordlist = concat([acro.replace(" ",""),num,streettypeobj[0],town])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(acronym) > 0) and (len(townacro) > 0) and (num != "") and (street != "")):
    for ta in townacro:
        for acro in acronym:
            wordlist = concat([acro.replace(" ",""),num,street.replace(" ",""),ta])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
            if len(streettypeobj) > 0:
                wordlist = concat([acro.replace(" ",""),num,streettypeobj[0],ta])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#acronym + alt township 
if ((len(acronym) > 0) and (alttownship != "")):
    for acro in acronym:
        for alttown in alttownshipentries:
            wordlist = concat([acro.replace(" ",""),alttown])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#acronym + alt township + street number
if ((len(acronym) > 0) and (alttownship != "") and (num != "")):
    for acro in acronym:
        for alttown in alttownshipentries:
            wordlist = concat([acro.replace(" ",""),alttown,num])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#acronym + street number + alt township
if ((len(acronym) > 0) and (alttownship != "") and (num != "")):
    for acro in acronym:
        for alttown in alttownshipentries:
            wordlist = concat([acro.replace(" ",""),num,alttown])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#acronym + full street (alt)
if ((len(acronym) > 0) and (alttownship != "") and (num != "") and (street != "")):
    for acro in acronym:
        for alttown in alttownshipentries:
            wordlist = concat([acro.replace(" ",""),num,street.replace(" ",""),alttown])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
            if len(streettypeobj) > 0:
                wordlist = concat([acro.replace(" ",""),num,streettypeobj[0],alttown])
                for w in wordlist:
                    if len(w) >= 8:
                        wordlistall.append(w)
                    else:
                        underarr.append(w)
#acronym + dates
if ((len(acronym) > 0) and (yyyy != "")):
    for acro in acronym:
        wordlist = concat([acro.replace(" ",""),yyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(acronym) > 0) and (yy != "")):
    for acro in acronym:
        wordlist = concat([acro.replace(" ",""),yy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(acronym) > 0) and (ddmmyyyy != "")):
    for acro in acronym:
        wordlist = concat([acro.replace(" ",""),ddmmyyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(acronym) > 0) and (mmddyyyy != "")):
    for acro in acronym:
        wordlist = concat([acro.replace(" ",""),mmddyyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(acronym) > 0) and (ddmmyy != "")):
    for acro in acronym:
        wordlist = concat([acro.replace(" ",""),ddmmyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(acronym) > 0) and (mmddyy != "")):
    for acro in acronym:
        wordlist = concat([acro.replace(" ",""),mmddyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(acronym) > 0) and (mmyyyy != "")):
    for acro in acronym:
        wordlist = concat([acro.replace(" ",""),mmyyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(acronym) > 0) and (mmyy != "")):
    for acro in acronym:
        wordlist = concat([acro.replace(" ",""),mmyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(acronym) > 0) and (month != "")):
    for acro in acronym:
        wordlist = concat([acro.replace(" ",""),month])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(acronym) > 0) and (month != "") and (yyyy != "")):
    for acro in acronym:
        wordlist = concat([acro.replace(" ",""),month,yyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((len(acronym) > 0) and (month != "") and (yy != "")):
    for acro in acronym:
        wordlist = concat([acro.replace(" ",""),month,yy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#acronym separate with pattern number
if (len(acronym) > 0):
    
    for acro in acronym:
        tempstring = ''
        for i in range(1,len(acro)+1):
            tempstring += acro[i-1] + str(i)
        if len(tempstring) >= 8:
            wordlistall.append(tempstring)
        else:
            underarr.append(tempstring)
        if len(tempstring) -1 >= 8:
            wordlistall.append(tempstring[:len(tempstring)-1])
        else:
            underarr.append(tempstring[:len(tempstring)-1])
        tempstring = ''
        for i in range(1,len(acro)+1):
            tempstring += acro[i-1] + str(i)
        if len(tempstring) >= 8:
            wordlistall.append(tempstring)
        else:
            underarr.append(tempstring)
        if len(tempstring) -1 >= 8:
            wordlistall.append(tempstring[:len(tempstring)-1])
        else:
            underarr.append(tempstring[:len(tempstring)-1])

#Descriptions
#desc + common words

if desc != "":
    for descentry in descentries:
        wordlist = concat([descentry.replace(" ",""),'wi','fi'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        wordlist = concatnoleet([descentry.replace(" ",""),'wireless'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w) 
        wordlist = concatnoleet([descentry.replace(" ",""),'staff'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        wordlist = concatnoleet([descentry.replace(" ",""),'corporate'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        wordlist = concatnoleet([descentry.replace(" ",""),'business'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w) 
        wordlist = concatnoleet([descentry.replace(" ",""),'employee'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#desc + last 4 phone
if ((desc != "") and (phonelast4 != "")):
    for descentry in descentries:
        wordlist = concat([descentry.replace(" ",""),phonelast4])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((desc != "") and (phonemid3 != "")):
    for descentry in descentries:
        wordlist = concat([descentry.replace(" ",""),phonemid3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#desc + street number
if ((desc != "") and (num != "")):
    for descentry in descentries:
        wordlist = concat([descentry.replace(" ",""),num])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#desc + zip
if ((desc != "") and (zipcode != "")):
    for descentry in descentries:
        wordlist = concat([descentry.replace(" ",""),zipcode])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#desc + last 4 owner phone
if ((desc != "") and (ownerphonelast4 != "")):
    for descentry in descentries:
        wordlist = concat([descentry.replace(" ",""),ownerphonelast4])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((desc != "") and (ownerphonemid3 != "")):
    for descentry in descentries:
        wordlist = concat([descentry.replace(" ",""),ownerphonemid3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#desc + owner street number
if ((desc != "") and (ownernum != "")):
    for descentry in descentries:
        wordlist = concat([descentry.replace(" ",""),ownernum])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#desc + owner zip
if ((desc != "") and (ownerzipcode != "")):
    for descentry in descentries:
        wordlist = concat([descentry.replace(" ",""),ownerzipcode])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#desc + first 3 biz phone
if ((desc != "") and (phonefirst3 != "")):
    for descentry in descentries:
        wordlist = concat([descentry.replace(" ",""),phonefirst3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#desc + township
if ((desc != "") and (town != "")):
    for descentry in descentries:
        wordlist = concat([descentry.replace(" ",""),town])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((desc != "") and (len(townacro) > 0 )):
    for ta in townacro:
        for descentry in descentries:
            wordlist = concat([descentry.replace(" ",""),ta])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#desc + township + street number
if ((desc != "") and (town != "") and (num != "")):
    for descentry in descentries:
        wordlist = concat([descentry.replace(" ",""),town,num])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((desc != "") and (len(townacro) > 0) and (num != "")):
    for ta in townacro:
        for descentry in descentries:
            wordlist = concat([descentry.replace(" ",""),ta,num])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#desc + street number + township
if ((desc != "") and (town != "") and (num != "")):
    for descentry in descentries:
        wordlist = concat([descentry.replace(" ",""),num,town])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((desc != "") and (len(townacro) > 0) and (num != "")):
    for ta in townacro:
        for descentry in descentries:
            wordlist = concat([descentry.replace(" ",""),num,ta])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#desc + full street
if ((desc != "") and (town != "") and (num != "") and (street != "")):
    for descentry in descentries:
        wordlist = concat([descentry.replace(" ",""),num,street.replace(" ",""),town])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        if len(streettypeobj) > 0:
            wordlist = concat([descentry.replace(" ",""),num,streettypeobj[0],town])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((desc != "") and (len(townacro) > 0) and (num != "") and (street != "")):
    for ta in townacro:
        for descentry in descentries:
            wordlist = concat([descentry.replace(" ",""),num,street.replace(" ",""),ta])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
            if len(streettypeobj) > 0:
                wordlist = concat([descentry.replace(" ",""),num,streettypeobj[0],ta])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#desc + alt township 
if ((desc != "") and (alttownship != "")):
    for descentry in descentries:
        for alttown in alttownshipentries:
            wordlist = concat([descentry.replace(" ",""),alttown])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#desc + alt township + street number
if ((desc != "") and (alttownship != "") and (num != "")):
    for descentry in descentries:
        for alttown in alttownshipentries:
            wordlist = concat([descentry.replace(" ",""),alttown,num])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#desc + street number + alt township
if ((desc != "") and (alttownship != "") and (num != "")):
    for descentry in descentries:
        for alttown in alttownshipentries:
            wordlist = concat([descentry.replace(" ",""),num,alttown])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#desc + full street (alt)
if ((desc != "") and (alttownship != "") and (num != "") and (street != "")):
    for descentry in descentries:
        for alttown in alttownshipentries:
            wordlist = concat([descentry.replace(" ",""),num,street.replace(" ",""),alttown])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
            if len(streettypeobj) > 0:
                wordlist = concat([descentry.replace(" ",""),num,streettypeobj[0],alttown])
                for w in wordlist:
                    if len(w) >= 8:
                        wordlistall.append(w)
                    else:
                        underarr.append(w)
#desc + dates
if ((desc != "") and (yyyy != "")):
    for descentry in descentries:
        wordlist = concat([descentry.replace(" ",""),yyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((desc != "") and (yy != "")):
    for descentry in descentries:
        wordlist = concat([descentry.replace(" ",""),yy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((desc != "") and (ddmmyyyy != "")):
    for descentry in descentries:
        wordlist = concat([descentry.replace(" ",""),ddmmyyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((desc != "") and (mmddyyyy != "")):
    for descentry in descentries:
        wordlist = concat([descentry.replace(" ",""),mmddyyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((desc != "") and (mmddyy != "")):
    for descentry in descentries:
        wordlist = concat([descentry.replace(" ",""),mmddyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((desc != "") and (ddmmyy != "")):
    for descentry in descentries:
        wordlist = concat([descentry.replace(" ",""),ddmmyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((desc != "") and (mmyyyy != "")):
    for descentry in descentries:
        wordlist = concat([descentry.replace(" ",""),mmyyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((desc != "") and (mmyy != "")):
    for descentry in descentries:
        wordlist = concat([descentry.replace(" ",""),mmyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((desc != "") and (month != "")):
    for descentry in descentries:
        wordlist = concat([descentry.replace(" ",""),month])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((desc != "") and (month != "") and (yyyy != "")):
    for descentry in descentries:
        wordlist = concat([descentry.replace(" ",""),month,yyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((desc != "") and (month != "") and (yy != "")):
    for descentry in descentries:
        wordlist = concat([descentry.replace(" ",""),month,yy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w) 

#Other
#other + common words
if other != "":
    for otherentry in otherentries:
        wordlist = concat([otherentry.replace(" ",""),'wi','fi'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        wordlist = concatnoleet([otherentry.replace(" ",""),'wireless'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w) 
        wordlist = concatnoleet([otherentry.replace(" ",""),'staff'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        wordlist = concatnoleet([otherentry.replace(" ",""),'corporate'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        wordlist = concatnoleet([otherentry.replace(" ",""),'business'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w) 
        wordlist = concatnoleet([otherentry.replace(" ",""),'employee'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#other + last 4 phone
if ((other != "") and (phonelast4 != "")):
    for otherentry in otherentries:
        wordlist = concat([otherentry.replace(" ",""),phonelast4])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((other != "") and (phonemid3 != "")):
    for otherentry in otherentries:
        wordlist = concat([otherentry.replace(" ",""),phonemid3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#other + street number
if ((other != "") and (num != "")):
    for otherentry in otherentries:
        wordlist = concat([otherentry.replace(" ",""),num])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#other + zip
if ((other != "") and (zipcode != "")):
    for otherentry in otherentries:
        wordlist = concat([otherentry.replace(" ",""),zipcode])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#other + last 4 owner phone
if ((other != "") and (ownerphonelast4 != "")):
    for otherentry in otherentries:
        wordlist = concat([otherentry.replace(" ",""),ownerphonelast4])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((other != "") and (ownerphonemid3 != "")):
    for otherentry in otherentries:
        wordlist = concat([otherentry.replace(" ",""),ownerphonemid3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#other + owner street number
if ((other != "") and (ownernum != "")):
    for otherentry in otherentries:
        wordlist = concat([otherentry.replace(" ",""),ownernum])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#other + owner zip
if ((other != "") and (ownerzipcode != "")):
    for otherentry in otherentries:
        wordlist = concat([otherentry.replace(" ",""),ownerzipcode])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#other + first 3 biz phone
if ((other != "") and (phonefirst3 != "")):
    for otherentry in otherentries:
        wordlist = concat([otherentry.replace(" ",""),phonefirst3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#other + township
if ((other != "") and (town != "")):
    for otherentry in otherentries:
        wordlist = concat([otherentry.replace(" ",""),town])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((other != "") and (len(townacro) > 0 )):
    for ta in townacro:
        for otherentry in otherentries:
            wordlist = concat([otherentry.replace(" ",""),ta])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#other + township + street number
if ((other != "") and (town != "") and (num != "")):
    for otherentry in otherentries:
        wordlist = concat([otherentry.replace(" ",""),town,num])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((other != "") and (len(townacro) > 0) and (num != "")):
    for ta in townacro:
        for otherentry in otherentries:
            wordlist = concat([otherentry.replace(" ",""),ta,num])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#other + street number + township
if ((other != "") and (town != "") and (num != "")):
    for otherentry in otherentries:
        wordlist = concat([otherentry.replace(" ",""),num,town])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((other != "") and (len(townacro) > 0) and (num != "")):
    for ta in townacro:
        for otherentry in otherentries:
            wordlist = concat([otherentry.replace(" ",""),num,ta])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#other + full street
if ((other != "") and (town != "") and (num != "") and (street != "")):
    for otherentry in otherentries:
        wordlist = concat([otherentry.replace(" ",""),num,street.replace(" ",""),town])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        if len(streettypeobj) > 0:
            wordlist = concat([otherentry.replace(" ",""),num,streettypeobj[0],town])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((other != "") and (len(townacro) > 0) and (num != "") and (street != "")):
    for ta in townacro:
        for otherentry in otherentries:
            wordlist = concat([otherentry.replace(" ",""),num,street.replace(" ",""),ta])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
            if len(streettypeobj) > 0:
                wordlist = concat([otherentry.replace(" ",""),num,streettypeobj[0],ta])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#other + alt township 
if ((other != "") and (alttownship != "")):
    for otherentry in otherentries:
        for alttown in alttownshipentries:
            wordlist = concat([otherentry.replace(" ",""),alttown])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#other + alt township + street number
if ((other != "") and (alttownship != "") and (num != "")):
    for otherentry in otherentries:
        for alttown in alttownshipentries:
            wordlist = concat([otherentry.replace(" ",""),alttown,num])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#other + street number + alt township
if ((other != "") and (alttownship != "") and (num != "")):
    for otherentry in otherentries:
        for alttown in alttownshipentries:
            wordlist = concat([otherentry.replace(" ",""),num,alttown])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
#other + full street (alt)
if ((other != "") and (alttownship != "") and (num != "") and (street != "")):
    for otherentry in otherentries:
        for alttown in alttownshipentries:
            wordlist = concat([otherentry.replace(" ",""),num,street.replace(" ",""),alttown])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
            if len(streettypeobj) > 0:
                wordlist = concat([otherentry.replace(" ",""),num,streettypeobj[0],alttown])
                for w in wordlist:
                    if len(w) >= 8:
                        wordlistall.append(w)
                    else:
                        underarr.append(w)
#other + dates
if ((other != "") and (yyyy != "")):
    for otherentry in otherentries:
        wordlist = concat([otherentry.replace(" ",""),yyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((other != "") and (yy != "")):
    for otherentry in otherentries:
        wordlist = concat([otherentry.replace(" ",""),yy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((other != "") and (ddmmyyyy != "")):
    for otherentry in otherentries:
        wordlist = concat([otherentry.replace(" ",""),ddmmyyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((other != "") and (mmddyyyy != "")):
    for otherentry in otherentries:
        wordlist = concat([otherentry.replace(" ",""),mmddyyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((other != "") and (mmddyy != "")):
    for otherentry in otherentries:
        wordlist = concat([otherentry.replace(" ",""),mmddyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((other != "") and (ddmmyy != "")):
    for otherentry in otherentries:
        wordlist = concat([otherentry.replace(" ",""),ddmmyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((other != "") and (mmyyyy != "")):
    for otherentry in otherentries:
        wordlist = concat([otherentry.replace(" ",""),mmyyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((other != "") and (mmyy != "")):
    for otherentry in otherentries:
        wordlist = concat([otherentry.replace(" ",""),mmyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((other != "") and (month != "")):
    for otherentry in otherentries:
        wordlist = concat([otherentry.replace(" ",""),month])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((other != "") and (month != "") and (yyyy != "")):
    for otherentry in otherentries:
        wordlist = concat([otherentry.replace(" ",""),month,yyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if ((other != "") and (month != "") and (yy != "")):
    for otherentry in otherentries:
        wordlist = concat([otherentry.replace(" ",""),month,yy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)                
#township + common words
if town != "":
    wordlist = concat([town.replace(" ",""),'wi','fi'])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
    wordlist = concatnoleet([town.replace(" ",""),'wireless'])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w) 
    wordlist = concatnoleet([town.replace(" ",""),'staff'])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
    wordlist = concatnoleet([town.replace(" ",""),'corporate'])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
    wordlist = concatnoleet([town.replace(" ",""),'business'])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w) 
    wordlist = concatnoleet([town.replace(" ",""),'employee'])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if len(townacro) > 0:
    for ta in townacro:
        wordlist = concat([ta.replace(" ",""),'wi','fi'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        wordlist = concatnoleet([ta.replace(" ",""),'wireless'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w) 
        wordlist = concatnoleet([ta.replace(" ",""),'staff'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        wordlist = concatnoleet([ta.replace(" ",""),'corporate'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        wordlist = concatnoleet([ta.replace(" ",""),'business'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w) 
        wordlist = concatnoleet([ta.replace(" ",""),'employee'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#alttownship + common words
if alttownship != "":
    for at in alttownshipentries:
        wordlist = concat([at.replace(" ",""),'wi','fi'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        wordlist = concatnoleet([at.replace(" ",""),'wireless'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w) 
        wordlist = concatnoleet([at.replace(" ",""),'staff'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        wordlist = concatnoleet([at.replace(" ",""),'corporate'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        wordlist = concatnoleet([at.replace(" ",""),'business'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w) 
        wordlist = concatnoleet([at.replace(" ",""),'employee'])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#township + last 4 phone
if town != "" and phonelast4 != "":
    wordlist = concat([town.replace(" ",""),phonelast4])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if town != "" and phonemid3 != "":
    wordlist = concat([town.replace(" ",""),phonemid3])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if len(townacro) > 0 and phonelast4 != "":
    for ta in townacro:
        wordlist = concat([ta.replace(" ",""),phonelast4])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if len(townacro) > 0 and phonemid3 != "":
    for ta in townacro:
        wordlist = concat([ta.replace(" ",""),phonemid3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#alttownship + last 4 phone
if alttownship != "" and phonelast4 != "":
    for at in alttownshipentries:
        wordlist = concat([at.replace(" ",""),phonelast4])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if alttownship != "" and phonemid3 != "":
    for at in alttownshipentries:
        wordlist = concat([at.replace(" ",""),phonemid3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#township + last 4 owner phone
if town != "" and ownerphonelast4 != "":
    wordlist = concat([town.replace(" ",""),ownerphonelast4])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if town != "" and ownerphonemid3 != "":
    wordlist = concat([town.replace(" ",""),ownerphonemid3])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if len(townacro) > 0 and ownerphonelast4 != "":
    for ta in townacro:
        wordlist = concat([ta.replace(" ",""),ownerphonelast4])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if len(townacro) > 0 and ownerphonemid3 != "":
    for ta in townacro:
        wordlist = concat([ta.replace(" ",""),ownerphonemid3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#alttownship + last 4 owner phone
if alttownship != "" and ownerphonelast4 != "":
    for at in alttownshipentries:
        wordlist = concat([at.replace(" ",""),ownerphonelast4])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if alttownship != "" and ownerphonemid3 != "":
    for at in alttownshipentries:
        wordlist = concat([at.replace(" ",""),ownerphonemid3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#township + first 3 phone
if town != "" and phonefirst3 != "":
    wordlist = concat([town.replace(" ",""),phonefirst3])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if len(townacro) > 0 and phonefirst3 != "":
    for ta in townacro:
        wordlist = concat([ta.replace(" ",""),phonefirst3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#alttownship + first 3 phone
if alttownship != "" and phonefirst3 != "":
    for at in alttownshipentries:
        wordlist = concat([at.replace(" ",""),phonefirst3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#township + first 3 owner phone
if town != "" and ownerphonefirst3 != "":
    wordlist = concat([town.replace(" ",""),ownerphonefirst3])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if len(townacro) > 0 and ownerphonefirst3 != "":
    for ta in townacro:
        wordlist = concat([ta.replace(" ",""),ownerphonefirst3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#alttownship + first owner phone
if alttownship != "" and ownerphonefirst3 != "":
    for at in alttownshipentries:
        wordlist = concat([at.replace(" ",""),ownerphonefirst3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#township + founding year
if town != "" and yyyy != "":
    wordlist = concat([town.replace(" ",""),yyyy])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if town != "" and yy != "":
    wordlist = concat([town.replace(" ",""),yy])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if len(townacro) > 0 and yyyy != "":
    for ta in townacro:
        wordlist = concat([ta.replace(" ",""),yyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if len(townacro) > 0 and yy != "":
    for ta in townacro:
        wordlist = concat([ta.replace(" ",""),yy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#alttownship + founding year
if alttownship != "" and yyyy != "":
    for at in alttownshipentries:
        wordlist = concat([at.replace(" ",""),yyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if alttownship != "" and yy != "":
    for at in alttownshipentries:
        wordlist = concat([at.replace(" ",""),yy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)

#township + ddmmyyyy
if town != "" and ddmmyyyy != "":
    wordlist = concat([town.replace(" ",""),ddmmyyyy])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if town != "" and mmddyyyy != "":
    wordlist = concat([town.replace(" ",""),mmddyyyy])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if len(townacro) > 0 and ddmmyyyy != "":
    for ta in townacro:
        wordlist = concat([ta.replace(" ",""),ddmmyyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if len(townacro) > 0 and mmddyyyy != "":
    for ta in townacro:
        wordlist = concat([ta.replace(" ",""),mmddyyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#alttownship + ddmmyyyy
if alttownship != "" and ddmmyyyy != "":
    for at in alttownshipentries:
        wordlist = concat([at.replace(" ",""),ddmmyyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if alttownship != "" and mmddyyyy != "":
    for at in alttownshipentries:
        wordlist = concat([at.replace(" ",""),mmddyyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#township + ddmmyy
if town != "" and ddmmyy != "":
    wordlist = concat([town.replace(" ",""),ddmmyy])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if town != "" and mmddyy != "":
    wordlist = concat([town.replace(" ",""),mmddyy])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)              
if len(townacro) > 0 and ddmmyy != "":
    for ta in townacro:
        wordlist = concat([ta.replace(" ",""),ddmmyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if len(townacro) > 0 and mmddyy != "":
    for ta in townacro:
        wordlist = concat([ta.replace(" ",""),mmddyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)                
                
#alttownship + ddmmyy
if alttownship != "" and ddmmyy != "":
    for at in alttownshipentries:
        wordlist = concat([at.replace(" ",""),ddmmyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if alttownship != "" and mmddyy != "":
    for at in alttownshipentries:
        wordlist = concat([at.replace(" ",""),mmddyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#township + mmyy
if town != "" and mmyy != "":
    wordlist = concat([town.replace(" ",""),mmyy])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)              
if len(townacro) > 0 and mmyy != "":
    for ta in townacro:
        wordlist = concat([ta.replace(" ",""),mmyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)                
                
#alttownship + mmyy
if alttownship != "" and mmyy != "":
    for at in alttownshipentries:
        wordlist = concat([at.replace(" ",""),mmyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)                
#full street addr 
if num != "" and street != "" and town != "" and zipcode != "":
    wordlist = concat([num,street.replace(" ",""),town,zipcode])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
    wordlist = concat([num,street.replace(" ",""),town])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
    wordlist = concat([num,street])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
    if len(streettypeobj) > 0:
        for st in streettypeobj:
            wordlist = concat([num,st,town,zipcode])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
            wordlist = concat([num,st,town])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
            wordlist = concat([num,st])
            for w in wordlist:
                if len(w) >= 8:
                    wordlistall.append(w)
                else:
                    underarr.append(w)
if num != "" and street != "" and len(townacro) > 0 and zipcode != "":
    for ta in townacro:
        wordlist = concat([num,street.replace(" ",""),ta,zipcode])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        wordlist = concat([num,street.replace(" ",""),ta])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        wordlist = concat([num,street])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        if len(streettypeobj) > 0:
            for st in streettypeobj:
                wordlist = concat([num,st,ta,zipcode])
                for w in wordlist:
                    if len(w) >= 8:
                        wordlistall.append(w)
                    else:
                        underarr.append(w)
                wordlist = concat([num,st,ta])
                for w in wordlist:
                    if len(w) >= 8:
                        wordlistall.append(w)
                    else:
                        underarr.append(w)
                wordlist = concat([num,st])
                for w in wordlist:
                    if len(w) >= 8:
                        wordlistall.append(w)
                    else:
                        underarr.append(w)
#full street addr (alt)
if num != "" and street != "" and alttownship != "" and zipcode != "":
    for at in alttownshipentries:
        wordlist = concat([num,street.replace(" ",""),at,zipcode])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        wordlist = concat([num,street.replace(" ",""),at])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        wordlist = concat([num,street])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
        if len(streettypeobj) > 0:
            for st in streettypeobj:
                wordlist = concat([num,st,at,zipcode])
                for w in wordlist:
                    if len(w) >= 8:
                        wordlistall.append(w)
                    else:
                        underarr.append(w)
                wordlist = concat([num,st,at])
                for w in wordlist:
                    if len(w) >= 8:
                        wordlistall.append(w)
                    else:
                        underarr.append(w)
          
#street no num + last 4 phone
if street != "" and phonelast4 != "":
    wordlist = concat([street,phonelast4])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if street != "" and phonemid3 != "":
    wordlist = concat([street,phonelast4])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if len(streettypeobj) > 0 and phonelast4 != "":
    for st in streettypeobj:
        wordlist = concat([st,phonelast4])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if len(streettypeobj) > 0 and phonemid3 != "":
    for st in streettypeobj:
        wordlist = concat([st,phonemid3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#street no num + last 4 owner phone
if street != "" and ownerphonelast4 != "":
    wordlist = concat([street,ownerphonelast4])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if street != "" and ownerphonemid3 != "":
    wordlist = concat([street,ownerphonemid3])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if len(streettypeobj) > 0 and ownerphonelast4 != "":
    for st in streettypeobj:
        wordlist = concat([st,ownerphonelast4])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if len(streettypeobj) > 0 and ownerphonemid3 != "":
    for st in streettypeobj:
        wordlist = concat([st,ownerphonemid3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#street no num + first 3 phone
if street != "" and phonefirst3 != "":
    wordlist = concat([street,phonefirst3])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if len(streettypeobj) > 0 and phonefirst3 != "":
    for st in streettypeobj:
        wordlist = concat([st,phonefirst3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#street no num + first 3 owner phone
if street != "" and ownerphonefirst3 != "":
    wordlist = concat([street,ownerphonefirst3])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if len(streettypeobj) > 0 and ownerphonefirst3 != "":
    for st in streettypeobj:
        wordlist = concat([st,ownerphonefirst3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#street no num + founding year
if street != "" and yyyy != "":
    wordlist = concat([street,yyyy])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if len(streettypeobj) > 0 and yyyy != "":
    for st in streettypeobj:
        wordlist = concat([st,yyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#street no num + ddmmyyyy
if street != "" and ddmmyyyy != "":
    wordlist = concat([street,ddmmyyyy])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if len(streettypeobj) > 0 and ddmmyyyy != "":
    for st in streettypeobj:
        wordlist = concat([st,ddmmyyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#street no num + mmyyyy
if street != "" and mmyyyy != "":
    wordlist = concat([street,mmyyyy])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if len(streettypeobj) > 0 and mmyyyy != "":
    for st in streettypeobj:
        wordlist = concat([st,mmyyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#STREET W NUMBER
#street w. num + last 4 phone
if num != "" and street != "" and phonelast4 != "":
    wordlist = concat([num,street.replace(" ",""),phonelast4])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if num != "" and street != "" and phonemid3 != "":
    wordlist = concat([num,street.replace(" ",""),phonemid3])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if num != "" and len(streettypeobj) > 0 and phonelast4 != "":
    for st in streettypeobj:
        wordlist = concat([num,st,phonelast4])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if num != "" and len(streettypeobj) > 0 and phonemid3 != "":
    for st in streettypeobj:
        wordlist = concat([num,st,phonemid3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#street w. num + last 4 owner phone
if num != "" and street != "" and ownerphonelast4 != "":
    wordlist = concat([num,street.replace(" ",""),ownerphonelast4])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if num != "" and street != "" and ownerphonemid3 != "":
    wordlist = concat([num,street.replace(" ",""),ownerphonemid3])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if num != "" and len(streettypeobj) > 0 and ownerphonelast4 != "":
    for st in streettypeobj:
        wordlist = concat([num,st,ownerphonelast4])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
if num != "" and len(streettypeobj) > 0 and ownerphonemid3 != "":
    for st in streettypeobj:
        wordlist = concat([num,st,ownerphonemid3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#street w. num + first 3 phone
if num != "" and street != "" and phonefirst3 != "":
    wordlist = concat([num,street.replace(" ",""),phonefirst3])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if num != "" and len(streettypeobj) > 0 and phonefirst3 != "":
    for st in streettypeobj:
        wordlist = concat([num,st,phonefirst3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#street w. num + first 3 owner phone
if num != "" and street != "" and ownerphonefirst3 != "":
    wordlist = concat([num,street.replace(" ",""),ownerphonefirst3])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if num != "" and len(streettypeobj) > 0 and ownerphonefirst3 != "":
    for st in streettypeobj:
        wordlist = concat([num,st,ownerphonefirst3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#street w. num + founding year
if num != "" and street != "" and yyyy != "":
    wordlist = concat([num,street.replace(" ",""),yyyy])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if num != "" and len(streettypeobj) > 0 and yyyy != "":
    for st in streettypeobj:
        wordlist = concat([num,st,yyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#street w. num + ddmmyyyy
if num != "" and street != "" and ddmmyyyy != "":
    wordlist = concat([num,street.replace(" ",""),ddmmyyyy])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if num != "" and len(streettypeobj) > 0 and ddmmyyyy != "":
    for st in streettypeobj:
        wordlist = concat([num,st,ddmmyyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#street w. num + mmyyyy
if num != "" and street != "" and mmyyyy != "":
    wordlist = concat([num,street.replace(" ",""),mmyyyy])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
if num != "" and len(streettypeobj) > 0 and mmyyyy != "":
    for st in streettypeobj:
        wordlist = concat([num,st,mmyyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#first 3 phone + bizname
if phonefirst3 != "" and bizname != "":
    wordlist = concat([phonefirst3,bizname])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
#first 3 phone + altbizname
if phonefirst3 != "" and aka != "":
    for abn in altbiznames:
    #RIGHT HERE
        wordlist = concat([phonefirst3,abn])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#first 3 phone + acronym
if phonefirst3 != "" and len(acronym) > 0:
    for acro in acronym:
        wordlist = concat([phonefirst3,acro])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#first 3 phone + township
if phonefirst3 != "" and town != "":
    wordlist = concat([phonefirst3,town])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
#first 3 phone + alttownship
if phonefirst3 != "" and alttownship != "":
    for at in alttownshipentries:
        wordlist = concat([phonefirst3,at])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#first 3 phone + street no num
if phonefirst3 != "" and street != "":
    wordlist = concat([phonefirst3,street.replace(" ","")])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
    if len(streettypeobj) > 0:
        wordlist = concat([phonefirst3,num,streettypeobj[0]])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)  
#MID 3
if phonemid3 != "" and bizname != "":
    wordlist = concat([phonemid3,bizname])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
#mid 3 phone + altbizname
if phonemid3 != "" and aka != "":
    for abn in altbiznames:
    #RIGHT HERE
        wordlist = concat([phonemid3,abn])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#mid 3 phone + acronym
if phonemid3 != "" and len(acronym) > 0:
    for acro in acronym:
        wordlist = concat([phonemid3,acro])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#mid 3 phone + township
if phonemid3 != "" and town != "":
    wordlist = concat([phonemid3,town])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
#mid 3 phone + alttownship
if phonemid3 != "" and alttownship != "":
    for at in alttownshipentries:
        wordlist = concat([phonemid3,at])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)
#mid 3 phone + street no num
if phonemid3 != "" and street != "":
    wordlist = concat([phonemid3,street.replace(" ","")])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
    if len(streettypeobj) > 0:
        wordlist = concat([phonemid3,num,streettypeobj[0]])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarr.append(w)                 
#month + year
if month != "" and yyyy != "":
    wordlist = concat([month,yyyy])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)#ssid + common words
if ssid != "":
    wordlist = concat([ssid.replace(" ",""),'wi','fi'])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
    wordlist = concatnoleet([ssid.replace(" ",""),'wireless'])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w) 
    wordlist = concatnoleet([ssid.replace(" ",""),'staff'])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
    wordlist = concatnoleet([ssid.replace(" ",""),'corporate'])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
    wordlist = concatnoleet([ssid.replace(" ",""),'business'])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
    wordlist = concatnoleet([ssid.replace(" ",""),'employee'])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarr.append(w)
leetlist = list(set(leetlist))           
wordlistall = list(set(wordlistall))

for w in wordlistall:
    wlfhandle.write(w + '\n')
for w in leetlist:
    wlfhandle.write(w + '\n')
wlfhandle.close()


commonnumbers = ['1','2','3','4','5','6','7','8','9','0','00','01','02','22','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','69','99','000','101','111','222','333','444','555','666','777','888','999','123','456','789','987','654','321','098','765','432','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024','1234','5678','9876','4321','6969','4444','12345','67890','09876','54321','55555','123456','987654','666666']
commonspec = ['!','#','$','%','^','&','*','?']
#Add other entry to common numbers if int
if len(otherentries) >= 1:
    for otherentry in otherentries:
        allints = re.findall(r'\d+',otherentry)
        if len(allints) == 1 and allints[0] == otherentry:
            commonnumbers.append(otherentry)
undermod = []
#underarr + common words
underarrtemp = []
wordlistall = []
for under in underarr:
    wordlist = concat([under,'wi','fi'])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarrtemp.append(w)
    wordlist = concatnoleet([under,'wireless'])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarrtemp.append(w) 
    wordlist = concatnoleet([under,'staff'])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarrtemp.append(w)
    wordlist = concatnoleet([under,'corporate'])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarrtemp.append(w)
    wordlist = concatnoleet([under,'business'])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarrtemp.append(w)
    wordlist = concatnoleet([under,'employee'])
    for w in wordlist:
        if len(w) >= 8:
            wordlistall.append(w)
        else:
            underarrtemp.append(w)
for under in underarrtemp:
    undermod.append(under)
#underarr + commonnumbers
underarrtemp = []
for under in underarr:
    for commonnumber in commonnumbers:
        word = under + commonnumber
        if len(word) >= 9:
            wordlistall.append(word)
        else:
            underarrtemp.append(word)
for under in underarrtemp:
    undermod.append(under)
#underarr + last 4 phone
if phonelast4 != "":
    underarrtemp = []
    for under in underarrtemp:
        wordlist = concat([under,phonelast4])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarrtemp.append(w)
    for under in underarrtemp:
        undermod.append(under) 
if phonemid3 != "":
    underarrtemp = []
    for under in underarrtemp:
        wordlist = concat([under,phonemid3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarrtemp.append(w)
    for under in underarrtemp:
        undermod.append(under)        
#underarr + street number
if num != "":
    underarrtemp = []
    for under in underarrtemp:
        wordlist = concat([under,num])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarrtemp.append(w)
    for under in underarrtemp:
        undermod.append(under)
#underarr + zip
if zipcode != "":
    underarrtemp = []
    for under in underarrtemp:
        wordlist = concat([under,zipcode])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarrtemp.append(w)
    for under in underarrtemp:
        undermod.append(under)
#underarr + last 4 owner phone
if ownerphonelast4 != "":
    underarrtemp = []
    for under in underarrtemp:
        wordlist = concat([under,ownerphonelast4])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarrtemp.append(w)
    for under in underarrtemp:
        undermod.append(under)
if ownerphonemid3 != "":
    underarrtemp = []
    for under in underarrtemp:
        wordlist = concat([under,ownerphonemid3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarrtemp.append(w)
    for under in underarrtemp:
        undermod.append(under)
#underarr + owner street number
if ownernum != "":
    underarrtemp = []
    for under in underarrtemp:
        wordlist = concat([under,ownernum])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarrtemp.append(w)
    for under in underarrtemp:
        undermod.append(under)
#underarr + owner zip
if ownerzipcode != "":
    underarrtemp = []
    for under in underarrtemp:
        wordlist = concat([under,ownerzipcode])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarrtemp.append(w)
    for under in underarrtemp:
        undermod.append(under)
#underarr + first 3 biz phone
if phonefirst3 != "":
    underarrtemp = []
    for under in underarrtemp:
        wordlist = concat([under,phonefirst3])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarrtemp.append(w)
    for under in underarrtemp:
        undermod.append(under)
#underarr + founding year
if yyyy != "":
    underarrtemp = []
    for under in underarrtemp:
        wordlist = concat([under,yyyy])
        for w in wordlist:
            if len(w) >= 8:
                wordlistall.append(w)
            else:
                underarrtemp.append(w)
    for under in underarrtemp:
        undermod.append(under)

wordlistall = []
leetlist = []
wlfhandle = open(wordlistfile,'a')
#append common word iterations to other words less than 8 characters. If still less than 8, add to second list


wifiword = concat(['wi','fi'])
stateword = []
ownerstateword = []
if state != '':
    stateword.append(state[0].lower() + state[1].lower())
    stateword.append(state[0].lower() + state[1].upper())
    stateword.append(state[0].upper() + state[1].lower())
    stateword.append(state[0].upper() + state[1].upper())
if ownerstate != '':
    ownerstateword.append(ownerstate[0].lower() + ownerstate[1].lower())
    ownerstateword.append(ownerstate[0].lower() + ownerstate[1].upper())
    ownerstateword.append(ownerstate[0].upper() + ownerstate[1].lower())
    ownerstateword.append(ownerstate[0].upper() + ownerstate[1].upper())


othercommonwords = []
others = ['wireless','staff','corporate','business','employee']
undermodcommonwords = []
for pre in others:
    tempcommon = concatnoleet([pre])
    for tempc in tempcommon:
        othercommonwords.append(tempc)
othercommonwords+=wifiword
othercommonwords+=leetlist
if len(stateword) > 0:
    othercommonwords += stateword
if len(ownerstateword) > 0:
    othercommonwords += ownerstateword

for underword in undermod:
    isanycommonpresent = 0
    for commonword in othercommonwords:
        if commonword in underword:
            isanycommonpresent = 1
    if isanycommonpresent == 0:
        for commonword in othercommonwords:
            if len(underword) + len(commonword) >= 8:
                wordlistall.append(underword + commonword)
            else:
                undermodcommonwords.append(underword + commonword)
undermodcommonwords = list(set(undermodcommonwords))
wordlistall = list(set(wordlistall))
for w in wordlistall:
    wlfhandle.write(w + '\n')
#prepend common word iterations to other words less than 8 characters. If still less than 8, add to second list 
wordlistall = []
preundermodcommonwords = []
for underword in undermod:
    isanycommonpresent = 0
    for commonword in othercommonwords:
        if commonword in underword:
            isanycommonpresent = 1
    if isanycommonpresent == 0:
        for commonword in othercommonwords:
            if len(underword) + len(commonword) >= 8:
                wordlistall.append(commonword + underword)
            else:
                preundermodcommonwords.append(commonword + underword)
preundermodcommonwords = list(set(preundermodcommonwords))
wordlistall = list(set(wordlistall))
for w in wordlistall:
    wlfhandle.write(w + '\n') 
#append common numbers to remaining words less than 8 characters. If still less than 8, add to another list
wordlistall = []
undercommonnumbers = []
preundercommonnumbers = []
for underword in undermod:
    tempwords = []
    allints = re.findall(r'\d+',underword)
    isnotspecialsub = 0
    for ints in allints:
        if ints != '1' and ints != '3' and ints != '5':
            isnotspecialsub = 1
    if isnotspecialsub == 0:
        for commonnumber in commonnumbers:
            if len(underword) + len(commonnumber) >= 8:
                wordlistall.append(underword + commonnumber)
            else:
                undercommonnumbers.append(underword + commonnumber)

for underword in undermod:
    tempwords = []
    allints = re.findall(r'\d+',underword)
    isnotspecialsub = 0
    for ints in allints:
        if ints != '1' and ints != '3' and ints != '5':
            isnotspecialsub = 1
    if isnotspecialsub == 0:
        for commonnumber in commonnumbers:
            if len(underword) + len(commonnumber) >= 8:
                wordlistall.append(commonnumber + underword)
            else:
                preundercommonnumbers.append(commonnumber + underword)

for underword in undermodcommonwords:
    tempwords = []
    allints = re.findall(r'\d+',underword)
    isnotspecialsub = 0
    for ints in allints:
        if ints != '1' and ints != '3' and ints != '5':
            isnotspecialsub = 1
    if isnotspecialsub == 0:
        for commonnumber in commonnumbers:
            if len(underword) + len(commonnumber) >= 8:
                wordlistall.append(underword + commonnumber)
            else:
                undercommonnumbers.append(underword + commonnumber)

undercommonnumbers = list(set(undercommonnumbers)) 
preundercommonnumbers = list(set(preundercommonnumbers))               
wordlistall = list(set(wordlistall))
for w in wordlistall:
    wlfhandle.write(w + '\n')
   

#Append special characters to 3 previous lists if still under 8
wordlistall = []
for underword in undermod:
    for specchar in commonspec:
        if len(underword) + 1 >= 8:
            wordlistall.append(underword + specchar)
for underword in undermodcommonwords:
    for specchar in commonspec:
        if len(underword) + 1 >= 8:
            wordlistall.append(underword + specchar)
for underword in undercommonnumbers:
    for specchar in commonspec:
        if len(underword) + 1 >= 8:
            wordlistall.append(underword + specchar)
for underword in preundercommonnumbers:
    for specchar in commonspec:
        if len(underword) + 1 >= 8:
            wordlistall.append(underword + specchar)
for underword in preundermodcommonwords:
    for specchar in commonspec:
        if len(underword) + 1 >= 8:
            wordlistall.append(underword + specchar)
for w in wordlistall:
    wlfhandle.write(w + '\n')
wlfhandle.close()

wlfhandle = open(wordlistfile,'r')
wlflines = wlfhandle.readlines()

wordlistall = []
#append common shortlist if word not present
#ehh


for line in wlflines:
    allints = re.findall(r'\d+',line)
    isnotspecialsub = 0
    line = line.strip()
    line = line.rstrip()
    for ints in allints:
        if ints != '1' and ints != '3' and ints != '5' and ints != '0':
            isnotspecialsub = 1
    if isnotspecialsub == 0:
        #append common number if not in and no other int
        for commonnumber in commonnumbers:
            concatline = line + commonnumber
            wordlistall.append(concatline)
        #append founding year if not in and no other int
        if yyyy != '':
            concatline = line + yyyy
            wordlistall.append(concatline)
        if yy != '':
            concatline = line + yy
            wordlistall.append(concatline)
        #append phone last 4 if not in and no other int
        if phonelast4 != '':
            concatline = line + phonelast4
            wordlistall.append(concatline)
        #append phone mid 3 if not in and no other int
        if phonemid3 != '':
            concatline = line + phonemid3
            wordlistall.append(concatline)
        #append phone first 3 if not in and no other int
        if phonefirst3 != '':
            concatline = line + phonefirst3
            wordlistall.append(concatline)
        #append ownerphone last 4 if not in and no other int
        if ownerphonelast4 != '':
            concatline = line + ownerphonelast4
            wordlistall.append(concatline)
        #append ownerphone mid 3 if not in and no other int
        if ownerphonemid3 != '':
            concatline = line + ownerphonemid3
            wordlistall.append(concatline)
        #append ownerphone first 3 if not in and no other int
        if ownerphonefirst3 != '':
            concatline = line + ownerphonefirst3
            wordlistall.append(concatline)
        #append zipcode if not in and no other int
        if zipcode != '':
            concatline = line + zipcode
            wordlistall.append(concatline)
        #append ownerzipcode if not in and no other int
        if zipcode != '':
            concatline = line + ownerzipcode
            wordlistall.append(concatline)
        #prepend common number if not in and no other int
        for commonnumber in commonnumbers:
            concatline = commonnumber + line
            wordlistall.append(concatline)
        #prepend founding year if not in and no other int
        if yyyy != '':
            concatline = yyyy + line
            wordlistall.append(concatline)
        if yy != '':
            concatline = yy + line
            wordlistall.append(concatline)
        #prepend phone last 4 if not in and no other int
        if phonelast4 != '':
            concatline = phonelast4 + line
            wordlistall.append(concatline)
        #prepend phone first 3 if not in and no other int
        if phonefirst3 != '':
            concatline = phonefirst3 + line
            wordlistall.append(concatline)
        #prepend ownerphone last 4 if not in and no other int
        if ownerphonelast4 != '':
            concatline = ownerphonelast4 + line
            wordlistall.append(concatline)
        #prepend ownerphone first 3 if not in and no other int
        if ownerphonefirst3 != '':
            concatline = ownerphonefirst3 + line
            wordlistall.append(concatline)
        #prepend zipcode if not in and no other int
        if zipcode != '':
            concatline = zipcode + line
            wordlistall.append(concatline)
        #prepend ownerzipcode if not in and no other int
        if zipcode != '':
            concatline = ownerzipcode + line
            wordlistall.append(concatline)
wlfhandle.close()
wlfhandle = open(wordlistfile,'a')
wordlistall = list(set(wordlistall))
for w in wordlistall:
    wlfhandle.write(w + '\n')

#append special characters all
wordlistall = []
for line in wlflines:
    line = line.strip()
    line = line.rstrip()
    if line[len(line) - 1] not in commonspec:
        for specchar in commonspec:
            wordlistall.append(line + specchar)
wordlistall = list(set(wordlistall))
for w in wordlistall:
    wlfhandle.write(w + '\n')
#prepend special characters all
wordlistall = []
for line in wlflines:
    line = line.strip()
    line = line.rstrip()
    if line[0] not in commonspec:
        for specchar in commonspec:
            wordlistall.append(specchar + line)
wordlistall = list(set(wordlistall))
for w in wordlistall:
    wlfhandle.write(w + '\n')
wlfhandle.close()
