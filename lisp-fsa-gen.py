  
import sys


class FSA:
    def __init__(self):
        self.states =[]
        self.alphabet = []
        self.startState = ""
        self.acceptStates = []
        self.transition = {}
        self.tranString=""
      


    def fillDict(self):
        for state in self.states:
            for alp in self.alphabet:

                try:
                    curr = self.transition[(str(state), alp)]

                
                except KeyError as ke:
                    self.transition[(str(state), alp)] = None
       
        


    def parseString(self,inputString):
        allWords = contents.split(';')
        numStates = int(allWords[0])
        
        alph = allWords[1]
        
        stateTransitions = allWords[2]
        start=allWords[3]
        
        acceptState = allWords[4]
       

        alphabet = []
        startState = ""
        acceptStates = []
        transition = {}
        states = []
        

        for i in range(numStates):
            states.append(i)

        
        self.states = states

       
        alphabet = alph.split(',')
        self.alphabet = alphabet
       

        startState=start
        
        self.startState = startState

        acceptStates = acceptState.split(',')
        
        self.acceptStates = acceptStates
    
        tranString=""

        transitions = stateTransitions.split(',')
       
        
        size = len(transitions)
        for j in range(size):
                 parsedTran= ''.join(filter(str.isalnum,transitions[j]))
                 
                 transition[(parsedTran[0],parsedTran[2])] = parsedTran[1]
                 tranString += "(" + parsedTran[0] +" "+ parsedTran[1] +" " + parsedTran[2]+")"
                 

       
        self.tranString = tranString
        self.transition = transition
        self.fillDict()
        
    

        
    def display(self):
        print(self.alphabet)
        print(self.startState) 
        print(self.acceptStates)
        print(self.transition)

    

    



with open(sys.argv[1]) as f:
    contents = f.read()
   
    fsa = FSA()
    print("Python is Generating Finite State Automata\n")
    
    fsa.parseString(contents)
    f = open("part2.lsp", "w")
    fsaString = "(defun setData() (set 'fsaList '( (stages (" + ' '.join(str(e) for e in fsa.states)+"))(alphabet("+' '.join(str(a) for a in fsa.alphabet)+"))(acceptStates ("+' '.join(str(b) for b in fsa.acceptStates)+"))(startState ("+str(fsa.startState)+"))(transitionStates ("+ fsa.tranString+")))))\n"
    f.write(fsaString)                                                               
    f.write("(defun string-to-list (str) (do* ((stringstream (make-string-input-stream str))(result nil (cons next result))(next (read stringstream nil 'eos) (read stringstream nil 'eos)))((equal next 'eos) (reverse result))))\n")
    f.write("(DEFUN MEMB(X L)(COND ((NULL L)NIL)((ATOM L)NIL)((EQUAL X (CAR L)) T)(T(MEMB X (CDR L)))))\n")
    f.write("(defun itlen (lst) (PROG (sum) (setq sum 0) again(cond((null lst) (return sum))) (setq sum (+ 1 sum)) (setq lst (cdr lst)) (go again)))\n")
    f.write("(defun test (elements)(cond((null elements) (princ '(Program is finished)))  (t  (setq currentChar (car elements))(setq sum (+ 1 sum))(testTrann transitionStates currentState currentChar)(setq result (memb currentChar alphabet))(if (not result)(error currentChar) )(if (and (equal sum stringLength)(memb currentState acceptStates) )(princ '(String is Legal)))(if (and (equal sum stringLength)(not (memb currentState acceptStates)))(princ '(String is Illegal)))(test (cdr elements)) )))\n")
    f.write("(defun testTrann (lst currState currChar) (cond ((null lst) '()) 	(t   	(setq tryState (caar lst)) (setq l (cdr(car lst)))(setq l3(cdr l)) (setq tranChar (car l3))(setq nextState (car l))(if (and (equal tranChar currChar)(equal currState tryState))(setq currentState nextState))(testTrann (cdr lst) currState currChar)) ))\n")
    f.write("(defun assoc (p l) (COND ((null l)	 nil)((atom l)	 nil) ((equal p (caar l))(setq newData (cadar l)))  (t  (assoc p (cdr l))) ))\n")
    f.write("(defun demo()(setData)(assoc 'stages fsaList) (setq stages newData)(assoc 'alphabet fsaList)(setq alphabet newData)(assoc 'acceptStates fsaList)(setq acceptStates newData)(assoc 'startState fsaList)(setq startState (car newData))(assoc 'transitionStates fsaList)(setq transitionStates newData) (setq fp (open 'theString.txt :direction :input)) (setq str (read-line fp))(setq str2 (string-to-list str))(setq testString (car str2))(setq currentState startstate) (setq sum 0)(setq stringLength (itlen testString))(princ 'Processing )(princ testString)(terpri)(test testString)(terpri) )")                


    

    

    
