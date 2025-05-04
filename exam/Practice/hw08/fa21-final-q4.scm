#lang racket
(require rackunit)
(define expect check-equal?)
(define nil '())

; 4. (15.0 points) Spice
; Definition. A repeated call is a nested call expression in which each
; subexpression is either a number, a symbol, or a call with exactly one
; operand. For example, (((f 2) 3) 4) is a repeated call.
; Reminder. In Scheme, the call expression (f 2) is a 2-element list
; containing the symbol f and the number 2. Therefore, one expression can
; evaluate to another expression. For example, the expression (list 'f 2)
; evaluates to (f 2).

;; (a) (4.0 points)
; Implement repeated-call, a procedure that takes an operator expression and a
; list of operand expressions. It returns a repeated call for the operator and
; operands. If operands is nil, the result is the operator expression.
;;; Construct a repeated call expression from an operator and a list of operands.
;;;
;;; scm> (repeated-call 'f '(2 3 4))
;;; (((f 2) 3) 4)
;;; scm> (repeated-call '(f 2) '(3 4))
;;; (((f 2) 3) 4)
;;; scm> (repeated-call 'f nil)
;;; f

(define (repeated-call operator operands)
  (if (null? operands)
    operator
    (repeated-call (list operator (car operands)) (cdr operands))))

; test for racket
(expect (repeated-call 'f '(2 3 4)) '(((f 2) 3) 4))
(expect (repeated-call '(f 2) '(3 4)) '(((f 2) 3) 4))
(expect (repeated-call 'f nil) 'f)
; test for cs61a scheme
; (expect (repeated-call 'f '(2 3 4)) (((f 2) 3) 4))
; (expect (repeated-call '(f 2) '(3 4)) (((f 2) 3) 4))
; (expect (repeated-call 'f nil) f)

;; (b) (4.0 points)
; Complete the implementation of curry, a higher-order procedure that is
; called repeatedly on a non-negative integer num-args and then a procedure f.
; It returns a curried version of f that, when called repeatedly num-args times,
; returns the result of applying f to those arguments. Assume that f can take
; num-args arguments.
; As a special case, ((curry 0) f) calls f on no arguments, which is
; equivalent to evaluating (f).
; Hint: The built-in apply procedure takes a procedure f and a list of
; arguments s and applies f to the elements of s. For example,
; • (apply + '(1 2 3)) is equivalent to (+ 1 2 3) and evaluates to 6.
; • (apply + '()) is equivalent to (+) and evaluates to 0.
;;; Return a curried version of f that can be called repeatedly num-args times.
;;;
;;; scm> (((((curry 3) +) 4) 5) 6)      ; (+ 4 5 6) evaluates to 15
;;; 15
;;; scm> ((curry 0) +)                  ; (+) evaluates to 0
;;; 0
;;; scm> (((curry 1) +) 3)              ; (+ 3) evaluates to 3
;;; 3
;;; scm> (((((curry 3) list) 4) 5) 6)   ; (list 4 5 6) evaluates to (4 5 6)
;;; (4 5 6)

(define (curry num-args)
  (lambda (f)
    (curry-helper num-args
                  (lambda (s)
                    ; (displayln f)
                    ; (displayln s)
                    (apply f s)))))

;;; curry-helper's argument g is a one-argument procedure that takes a list.
;;;
;;; scm> ((((curry-helper 3 cdr) 5) 6) 7) ; (cdr '(5 6 7)) => (6 7)
;;; (6 7)

(define (curry-helper num-args g)
  ; (displayln num-args)
  ; (displayln g)
  (if (= num-args 0)
    (cond
      ((not (list? g)) (g nil))
      (else
        (let ((operator (car g))
              (operands (car (cdr g))))
          ; (displayln operator)
          ; (displayln operands)
          (operator operands))))
    (lambda (x) (curry-helper (- num-args 1)
                              (cond
                                ((not (list? g)) (list g (list x)))
                                (else
                                  (let ((operator (car g))
                                        (operands (car (cdr g))))
                                    (define new_operands (append operands (list x)))
                                    ; (displayln operator)
                                    ; (displayln operands)
                                    ; (displayln new_operands)
                                    (list operator new_operands))))))))

; test for racket
(expect (((((curry 3) +) 4) 5) 6) 15)
(expect ((curry 0) +) 0)
(expect (((curry 1) +) 3) 3)
(expect (((((curry 3) list) 4) 5) 6) '(4 5 6))
(expect ((((curry-helper 3 cdr) 5) 6) 7) '(6 7))
; test for cs61a scheme
; (expect (((((curry 3) +) 4) 5) 6) 15)
; (expect ((curry 0) +) 0)
; (expect (((curry 1) +) 3) 3)
; (expect (((((curry 3) list) 4) 5) 6) (4 5 6))
; (expect ((((curry-helper 3 cdr) 5) 6) 7) (6 7))

;; (c) (7.0 points)
; Implement one-arg, which takes a Scheme expression s.
; It returns a call expression that would evaluate to the same value as s
; (calling the same procedures), but which uses curry to ensure that all call
; expressions have exactly one operand. Call expressions that already have one
; operand are unchanged.
; • Assume s contains only numbers, symbols, and call expressions; no special
; forms.
; • Assume that each operator (first sub-expression) of a call expression in s
; is a symbol (such as +).
; • Assume that each operand of a call expression in s is either a number or
; another call expression.
;;; Take a (possibly nested) call expression s and return
;;; an equivalent expression in which all calls have one argument.
;;;
;;; scm> (one-arg '(abs 3)) ; (abs 3) already takes just 1 argument
;;; (abs 3)
;;; scm> (+ 4 5 6)
;;; 15
;;; scm> (one-arg '(+ 4 5 6))
;;; (((((curry 3) +) 4) 5) 6)
;;; scm> (eval (one-arg '(+ 4 5 6))); Same value as (+ 4 5 6)
;;; 15
;;; scm> (one-arg '(+ (- 4) (*) (* 5 6)))
;;; (((((curry 3) +) (- 4)) ((curry 0) *)) ((((curry 2) *) 5) 6))

(define (one-arg s)
  (if (number? s) s
    (let ((num-args (- (length s) 1)))
      (if (= num-args 1)
        (list (car s) (one-arg (car (cdr s))))
        (repeated-call (list (list 'curry num-args) (car s))
                       (map one-arg (cdr s)))))))

; test for racket
(expect (one-arg '(abs 3)) '(abs 3))
(expect (one-arg '(+ 4 5 6)) '(((((curry 3) +) 4) 5) 6))
(expect (eval (one-arg '(+ 4 5 6))) 15)
(expect (one-arg '(+ (- 4) (*) (* 5 6))) '(((((curry 3) +) (- 4)) ((curry 0) *)) ((((curry 2) *) 5) 6)))
; test for cs61a scheme
; (expect (one-arg '(abs 3)) (abs 3))
; (expect (one-arg '(+ 4 5 6)) (((((curry 3) +) 4) 5) 6))
; (expect (eval (one-arg '(+ 4 5 6))) 15)
; (expect (one-arg '(+ (- 4) (*) (* 5 6))) (((((curry 3) +) (- 4)) ((curry 0) *)) ((((curry 2) *) 5) 6)))
