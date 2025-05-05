; 8. (4 points) Macros
; The if special form has been removed from scheme.
; Implement an if macro using only and/or:
(define-macro (if condition if-true if-false)
              ; (or (and condition if-true) if-false))
              ; Official Solution
              `(or (and ,condition ,if-true) ,if-false))

; scm> (if #t 1 (/ 1 0))
; 1
; scm> (if #f 1 (/ 1 0))
; Error
