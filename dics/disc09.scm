; Q1: Perfect Fit
;;; Return whether there are n perfect squares with no repeats that sum to total
(define (fit total n) 'YOUR-CODE-HERE)

;;; Tests
(expect (fit 10 2) #t) ; 1*1 + 3*3
(expect (fit 9 1) #t) ; 3*3
(expect (fit 9 2) #f) ;
(expect (fit 9 3) #f) ; 1*1 + 2*2 + 2*2 doesn't count because of repeated 2*2
(expect (fit 25 1) #t) ; 5*5
(expect (fit 25 2) #t) ; 3*3 + 4*4

; Q2: Nested Lists
;;; Using list

;;; Using quote

;;; Using cons


; Q3: Pair Up
;;; Return a list of pairs containing the elements of s.
(define (pair-up s) 'YOUR-CODE-HERE)

;;; Tests
(expect (pair-up '(3 4 5 6 7 8)) ((3 4) (5 6) (7 8)) )
(expect (pair-up '(3 4 5 6 7 8 9)) ((3 4) (5 6) (7 8 9)) )
