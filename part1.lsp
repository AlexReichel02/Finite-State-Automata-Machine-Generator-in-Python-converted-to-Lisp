
(DEFUN MEMB (X L)
    (COND ((NULL L)	 NIL)
        ((ATOM L)	 NIL)
        ((EQUAL X (CAR L)) T)
        (T  (MEMB X (CDR L)))
    )
)

(defun itlen (lst)
	
        (PROG (sum)
	(setq sum 0)
	
     again
	(cond 
            ((null lst) (return sum))
         )
	
	
	(setq sum (+ 1 sum))
        (setq lst (cdr lst))
     (go again)
))



(defun test (elements)
	
   
    (cond
        
	((null elements) (princ "\n Program is finished, have a good day")) 
	
        (t  
	(setq currentChar (car elements))
	(setq sum (+ 1 sum))


	   (princ "Current char in string: ")(print currentChar)
	    
	   (testTrann transitionStates currentState currentChar)
	   (princ "Char is currently in: ")(print currentState)
	   
 	    
        (setq result (memb currentChar alphabet))
	(if (not result) (error "\nChar is illegal\n"))

	    
	(if (and (equal sum stringLength)(memb currentState acceptStates) )(princ "String is Legal"))
	(if (and (equal sum stringLength)(not (memb currentState acceptStates)))(princ "String is Illegal"))
	    

            (test (cdr elements))
        )
	
	
    )
)


(defun testTrann (lst currState currChar) 
	(cond
        ((null lst) '()) 
       	(t 
       	(setq tryState (caar lst))
	(setq l (cdr(car lst)))(setq l3(cdr l))
	(setq tranChar (car l3))
	(setq nextState (car l))


	(if (and (equal tranChar currChar)(equal currState tryState))(setq currentState nextState))
	

	(testTrann (cdr lst) currState currChar)
        )

    )

)

(defun setData() 
	(set 'fsaList '( (stages (0 1 2 3 4))(alphabet (x y z a))(acceptStates (1 3))(startState (0))
(transitionStates ((0 0 x)(0 1 y)(1 2 x)(2 2 x)(2 3 y)(3 3 x)(3 4 z)(4 4 x)(4 1 a))))
)
) 


(defun assoc (p l)
    (COND ((null l)	 nil)
        ((atom l)	 nil)
        ((equal p (caar l))(setq newData (cadar l)))
        (t  (assoc p (cdr l)))
    )
)

(defun demo()

	(setData)
   	(assoc 'stages fsaList)
	(setq stages newData)

	(assoc 'alphabet fsaList)
	(setq alphabet newData)

	(assoc 'acceptStates fsaList)
	(setq acceptStates newData)
	
	(assoc 'startState fsaList)
	(setq startState (car newData))
	
	(assoc 'transitionStates fsaList)
	(setq transitionStates newData)
   

  (setq fp (open "theString.txt" :direction :input)) 
  (setq testString (read fp "done"))
  (setq currentState startstate)
  (setq sum 0)
  (setq stringLength (itlen testString))
  (princ "Processing: ")(print testString)
  (test testString)
		
 
)

