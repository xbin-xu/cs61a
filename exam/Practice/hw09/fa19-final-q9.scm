; 9. (3 points) Macro Lens
; Implement partial, a macro that takes a call expression that is missing its
; last operand. A call to partial evaluates to a one-argument procedure that
; takes a value y and returns the result of evaluating call extended to include
; an additional operand y at the end.
;; A macro that creates a procedure from a partial call expression missing
;; the last operand.
;; (define add-two (partial (+ 1 1))) -> (lambda (y) (+ 1 1 y))
;; (add-two 3) -> 5 by evaluating (+ 1 1 3)
;;
;; (define eq-5 (partial (equal? (+ 2 3)))) -> (lambda (y) (equal? (+ 2 3) y))
;; (eq-5 (+ 3 2)) -> #t by evaluating (equal? (+ 2 3) 5)
;;
;; ((partial (append '(1 2))) '(3 4)) -> (1 2 3 4)
(define-macro (partial call)
  `(lambda (y) _________________________________________________________________________ ))

(define add-two (partial (+ 1 1)))
(expect (add-two 3) 5)
(define eq-5 (partial (equal? (+ 2 3))))
(expect (eq-5 (+ 3 2)) #t)
(expect ((partial (append '(1 2))) '(3 4)) (1 2 3 4))