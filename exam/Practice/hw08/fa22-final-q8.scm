#lang racket
(require rackunit)
(define expect check-equal?)
(define nil '())

; 8. (6.0 points) A Parentheses Scheme
; In a fit of Scheme-induced rage, you’ve decided that all internal
; parentheses must be eliminated! Implement the procedure remove-parens that
; takes as input a Scheme list and returns that list with all internal
; parentheses removed.

;;; > (remove-parens '(((1) 2 3) 4 5 (6 (7)) (8 10)))
;;; (1 2 3 4 5 6 7 8 10)
;;; > (remove-parens '(((a) b (c) ()) (d) e (f (((g)))) (h i)))
;;; (a b c d e f g h i)

(define (remove-parens s)
  (cond
    ((null? s) nil)
    (__(a)__ __(b)__)
    (else __(c)__)))

; test for racket
(expect (remove-parens '(((1) 2 3) 4 5 (6 (7)) (8 10))) '(1 2 3 4 5 6 7 8 10))
(expect (remove-parens '(((a) b (c) ()) (d) e (f (((g)))) (h i))) '(a b c d e f g h i))
; test for cs61a scheme
;(expect (remove-parens '(((1) 2 3) 4 5 (6 (7)) (8 10))) (1 2 3 4 5 6 7 8 10))
;(expect (remove-parens '(((a) b (c) ()) (d) e (f (((g)))) (h i))) (a b c d e f g h i))

