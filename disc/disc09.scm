#lang racket
(require rackunit)
(define expect check-equal?)

; Q1: Perfect Fit
;;; Return whether there are n perfect squares with no repeats that sum to total
(define square (lambda (x) (* x x)))

(define (__fit total n x)
  (cond
    ((= n 0) (= total 0))
    ((or (< n 0) (< total (square x))) #f)
    (else (or (__fit total n (+ x 1)) (__fit (- total (square x)) (- n 1) (+ x 1))))))

(define (fit total n) (__fit total n 1))
;;;; Official Solution
; (define (fit total n)
;   (define (f total n k)
;     (if (and (= n 0) (= total 0))
;       #t
;       (if (< total (* k k))
;         #f
;         (or (f total n (+ k 1)) (f (- total (* k k)) (- n 1) (+ k 1))))))
;   (f total n 1))

;;; Tests
(expect (fit 10 2) #t) ; 1*1 + 3*3
(expect (fit 9 1) #t) ; 3*3
(expect (fit 9 2) #f) ;
(expect (fit 9 3) #f) ; 1*1 + 2*2 + 2*2 doesn't count because of repeated 2*2
(expect (fit 25 1) #t) ; 5*5
(expect (fit 25 2) #t) ; 3*3 + 4*4

; Q2: Nested Lists
; '((a b) c d (e))
; -> + -> c -> d -> +
;    |              |
;    a -> b         e
;;; Using list
(draw (list (list 'a 'b) 'c 'd (list 'e)))
; (expect (list (list 'a 'b) 'c 'd (list 'e)) ((a b) c d (e)))

;;; Using quote
(draw '((a b) c d (e)))
; (expect '((a b) c d (e)) ((a b) c d (e)))
(draw (quote ((a b) c d (e))))
; (expect (quote ((a b) c d (e))) ((a b) c d (e)))

;;; Using cons
(draw (cons (cons 'a (cons 'b nil)) (cons 'c (cons 'd (cons (cons 'e nil) nil)))))
; (expect (cons (cons 'a (cons 'b nil)) (cons 'c (cons 'd (cons (cons 'e nil) nil)))) ((a b) c d (e)))

; Q3: Pair Up
;;; Return a list of pairs containing the elements of s.
; (define (pair-up s)
;   (cond
;     ((null? s) (list s))
;     ((null? (cdr s)) (list s))
;     ((null? (cdr (cdr s))) (list s))
;     ((null? (cdr (cdr (cdr s)))) (list s))
;     (else (cons (list (car s) (car (cdr s))) (pair-up (cdr (cdr s)))))))
;;; Official Solution
(define (pair-up s)
  (cond
    ((<= (length s) 3) (list s))
    (else (cons (list (car s) (car (cdr s))) (pair-up (cdr (cdr s)))))))

;;; Tests
(expect (pair-up nil) (()))
(expect (pair-up '(3)) ((3)))
(expect (pair-up '(3 4)) ((3 4)))
(expect (pair-up '(3 4 5)) ((3 4 5)))
(expect (pair-up '(3 4 5 6 7 8)) ((3 4) (5 6) (7 8)) )
(expect (pair-up '(3 4 5 6 7 8 9)) ((3 4) (5 6) (7 8 9)) )
