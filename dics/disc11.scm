; Q1: Mystery Macro
;;; Figure out what this mystery-macro does. Try to describe what it does by
;;; reading the code and discussing examples as a group.
(define-macro (mystery-macro expr old new)
  (mystery-helper expr old new))

(define (mystery-helper e o n)
  (if (pair? e)
    (cons (mystery-helper (car e) o n) (mystery-helper (cdr e) o n))
    (if (eq? e o) n e)))


; Q2: Multiple Assignment
;;; In Scheme, the expression returned by a macro procedure is evaluated in the
;;; same environment in which the macro was called. Therefore, it's possible to
;;; return a define expression from a macro and have it affect the environment
;;; in which the macro was called. This differs from a regular scheme procedure
;;; that contains a define expression, which would only affect the procedure's
;;; local frame.
;;; In Python, we can bind two names to values in one line as follows:
;;; 
;;; ```py
;;; >>> x, y = 1 + 1, 3  # now x is bound to 2 and y is bound to 3
;;; >>> x, y = y, x      # swap the values of x and y
;;; >>> x
;;; 3
;;; >>> y
;;; 2
;;; ```
;;;
;;; Implement the assign Scheme macro, which takes in two symbols sym1 and sym2
;;; as well as two expressions expr1 and expr2. It should bind sym1 to the value
;;; of expr1 and sym2 to the value of expr2 in the environment from which the
;;; macro was called.
;;; 
;;; ```scheme
;;; scm> (assign x y (+ 1 1) 3)  ; now x is bound to 2 and y is bound to 3
;;; scm> (assign x y y x)        ; swap the values of x and y
;;; scm> x
;;; 3
;;; scm> y
;;; 2
;;; ```
;;;
;;; Make sure that expr2 is evaluated before sym1 is changed.
;;; Assume that expr1 and expr2 do not have side effects
;;; (and so do not contain define or assign expressions).
(define-macro (assign sym1 sym2 expr1 expr2)
  `(begin
     (define ,sym1 ,expr1)
     (define ___ ___)))

;;; Tests
(assign x y (+ 1 1) 3)
(assign x y y x)
(expect x 3)
(expect y 2)

(define z 'x)      ; z is bound to the symbol x
(assign v w 2 z)   ; now v is bound to 2 and w is bound to the symbol x
(assign v w w v)   ; swap the values of v and w
(expect v x)
(expect w 2)


; Q3: Switch
;;; Define the macro switch, which takes in an expression expr and a list of
;;; pairs called cases where the first element of the pair is some number and
;;; the second element is a single expression. switch will evaluate the
;;; expression contained in of cases that corresponds to the number that expr
;;; evaluates to.
;;; 
;;; ```scheme
;;; scm> (switch (+ 1 1) ((1 (print 'a))
;;;                      (2 (print 'b))
;;;                      (3 (print 'c))))
;;; b
;;; ```
;;;
;;; You may assume that the value expr evaluates to is always the first element
;;; of one of the pairs in cases. You can also assume that the first value of
;;; each pair in cases is a number and the second expression does not contain
;;; the symbol val.
;;; Use equal? to check if two numbers are equal.
(define-macro (switch expr cases)
  `(let ((val ,expr))
     ,(cons
        'YOUR-CODE-HERE
        (map (lambda (case) (cons
                              'YOUR-CODE-HERE
                              (cdr case)))
             cases))))
