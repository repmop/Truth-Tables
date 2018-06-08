import string
orToks = ["+","|"]
andToks = ["*","&"]
negToks = ["!","~"]
allowedChars = string.ascii_letters
#allowedChars = allowedChars.replace("a","")
#allowedChars = allowedChars.replace("n","")
#allowedChars = allowedChars.replace("d","")
def stringInsert (source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]
#parse out the set of unique non-operator letters to determine
#what should be varied for our tests.
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

#use textual replacement and eval()
#to determine the expression's output for a given set of inputs.
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
    
#Insert 'and' operators between all operators placed next to each other
#To reflect standard SOP syntax in logic design.
def preProcess(s,varList):
    if (len(s)<=1):
        return s
    insert = "*"
    i=0
    while(i<len(s)-1):
        #print("loop: ",s)
        if (s[i] in varList and s[i+1] in (varList + negToks)):
            s = stringInsert(s,insert,i+1)
            i+=len(insert)
        i+=1
    for c in orToks:
        s = s.replace(c,orToks[0])
    for c in andToks:
        s = s.replace(c,andToks[0])
    for c in negToks:
        s = s.replace(c,negToks[0])
    return s

#Convert a primary expression to a truth table. A truth table
#is a 2D list where the rows consist of each possible combination of the input
#variables, and the columns describe the values used for each evaluation +
#a final column with the output values. Column values are either "0" or "1".
def primToTab(s):
    if s=="":
        return ([],[],"")
    new = s.replace(" ","")
    #print("stripped: ",s)
    varList = getVarsFromPrimExp(new)
    #print("varList: ",varList)
    new = preProcess(new,varList)
    #print("preProcessed: ",new)
    (rows,cols) = dimFromVL(varList)
    tab = [[0]*cols]*rows
    for row in range(rows):
        binStr = bin(row)[2:]
        while(len(binStr)<cols-1):
            binStr = "0" + binStr
        vals = list(binStr)
        out = evalPrimExp(new,varList,vals)
        vals.append(str(out))
        tab[row] = vals
    return (tab,varList,new)

#Convert a tuple returned by primToTab() to a string, consisting of substrings
#of the form (binary number)|(0 or 1), seperated by newlines
#indicating the values for each variable (left of |) used to evaluate the 
#the input expression, and the expression's output value (right of |).
def tabToStr(tup):
    (tab,varList,exp) = tup
    if (exp==""):
        return ""
    rows = len(tab)
    cols = len(tab[0])
    out = "\n"
    for var in varList:
        out += var
    out += "|(" + exp +") \n"
    for row in range(rows):
        for col in range(cols - 1):
            out += tab[row][col]
        out += "|"
        out += tab[row][cols-1] + " \n"
    return out

def orOps():
    orStr=""
    for s in orToks:
        orStr += s
    return orStr
    
def andOps():
    andStr=""
    for s in andToks:
        andStr += s
    return andStr
    
def negOps():
    negStr=""
    for s in negToks:
        negStr += s
    return negStr

    
