import string
orToks = ["+","|","||"]
andToks = ["*","&"]
negToks = ["~","!","¬"]
allowedChars = string.ascii_letters
allowedChars = allowedChars.replace("a","")
allowedChars = allowedChars.replace("n","")
allowedChars = allowedChars.replace("d","")
def stringInsert (source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]

def getVarsFromPrimExp(s):
    vars = set()
    for c in s:
        if c not in (orToks + andToks + negToks + ["(",")"]):
            if c not in allowedChars:
                raise Exception("Invalid character entered: " + c)
            vars.add(c)
    out = list(vars)
    out.sort()
    return out
    
def dimFromVL(varList):
    cols = len(varList)
    rows = 2**(cols)
    return (rows,cols + 1)
    
def evalPrimExp(s,varList,vals):
    for i in range(len(varList)):
        s = s.replace(varList[i],vals[i])
    for orTok in orToks:
        s = s.replace(orTok," or ")
    for andTok in andToks:
        s = s.replace(andTok," and ")
    for negTok in negToks:
        s = s.replace(negTok," not ")
    #print(s)
    try:
        out = 1 if (eval(s)) else 0
    except:
        raise Exception("Parse Error!")
    return out
    

def preProcess(s,varList):
    if (len(s)<=1):
        return s
    insert = " and "
    i=0
    while(i<len(s)-1):
        #print("loop: ",s)
        if (s[i] in varList and s[i+1] in (varList + negToks)):
            s = stringInsert(s,insert,i+1)
            i+=len(insert)
        i+=1
    return s

def primToTab(s):
    s = s.replace(" ","")
    #print("stripped: ",s)
    varList = getVarsFromPrimExp(s)
    #print("varList: ",varList)
    s = preProcess(s,varList)
    #print("preProcessed: ",s)
    (rows,cols) = dimFromVL(varList)
    tab = [[0]*cols]*rows
    for row in range(rows):
        binStr = bin(row)[2:]
        while(len(binStr)<cols-1):
            binStr = "0" + binStr
        vals = list(binStr)
        out = evalPrimExp(s,varList,vals)
        vals.append(str(out))
        tab[row] = vals
    return (tab,varList,s)

def tabToStr(tup):
    (tab,varList,exp) = tup
    rows = len(tab)
    cols = len(tab[0])
    out = ""
    for var in varList:
        out += var
    out += "|(" + exp +")\n"
    for row in range(rows):
        for col in range(cols - 1):
            out += tab[row][col]
        out += "|"
        out += tab[row][cols-1] + "\n"
    return out


    
    
print(tabToStr(primToTab("g | ~(hj | k)")))

        
    
    
            
        
    


    