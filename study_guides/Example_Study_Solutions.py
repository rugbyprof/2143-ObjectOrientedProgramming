
def alphanumeric(num):
    num = list(num)
    if len(num) != 9:
        return None
    
    alpha = ['','ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    
    phone = ""
    
    for i in num:
        for chunk in alpha:
            if i in chunk:
                print(alpha.index(chunk))
                phone += str(alpha.index(chunk))
    
    return phone
              
  
def alphanumeric(num):
    num = list(num)
    if len(num) != 9:
        return None
    
    alpha = ['','ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    
    phone = []
    
    for i in num:
        for chunk in alpha:
            if i in chunk:
                print(alpha.index(chunk))
                phone.append(alpha.index(chunk))
    
    return ''.join([str(i) for i in phone])
    
def guessAnswer(low,high,answer):
    guesses = 0
    for i in range(low,high+1):
        if answer == i:
            return guesses + 1
        guesses += 1

    
  
def guessAnswer2(low,high,answer,guesses=1):
    
    start = (low + high) // 2
    
    print(start,low,high)
    if answer == start:
        return guesses
    elif answer > start:
        return guessAnswer2(start+1,high,answer,guesses+1)
    else:
        return guessAnswer2(low,start-1,answer,guesses+1)

class wordDictonary(object):
    def __init__(self):
        self.words = {}
        f = open('words.txt', 'r')
        for line in f:
            word,definition = line.split(':')
            definition = definition.strip("\n")
            
            if not word in self.words:
                self.words[word] = []
            
            self.words[word].append(definition)

                

    def printDictionary(self):
        for k in self.words:
            print(k,self.words[k])
  
if __name__=='__main__':
    #print(alphanumeric('ABCFFGZMX'))

    # L = ['a','b','c','d','e']
    # print(L.index('c'))
    
    # print(guessAnswer(1,10923140192340,1923874))
    # print(guessAnswer2(1,10923140192340,1923874))   
    d = wordDictonary()
    d.printDictionary()
  
