; 7. (12 points) Procedure with Caution
; Definition. A sequential procedure takes a non-negative integer i as an
; argument and returns the ith element of an infinite sequence.
; The ith element of a sequential procedure f is (f i).
; A sequential procedure starts at element 0 (so to get the first element for
; sequential procedure f, you’d call (f 0))


; (a) (4 pt) Implement streamify, which takes a sequential procedure and
; returns a stream containing its elements.
(define (streamify f)
  (define (g n)
    __________________________________________________________)
  ________________________________________)

(streamify (lambda (n) 4)) ; An infinite stream of 4 4 4 4 ...
(streamify (lambda (n) (abs (- n 4)))) ; An infinite stream of 4 3 2 1 0 1 2 3 4 ...


; (b) (5 pt) Implement the Scheme procedure duplicate that returns the first
; duplicate element of a sequential procedure. Assume a duplicate element exists.
; You may call the contains? procedure defined below.
; Your procedure must be tail recurisve in order to receive credit.

(define (contains? s v)
  (cond ((null? s) false)
        ((equal? (car s) v) true)
        (else (contains? (cdr s) v))))

(define (duplicate f)
  (define (helper ____________________________________________________________)
    (if ______________________________________________________________________
      ______________________________________________________________________
      (helper ______________________________________________________________)))
  (helper ____________________________________________________________________))

(duplicate (lambda (n) 4)) ; returns 4, sequence is 4 [4] ...
(duplicate (lambda (n) (abs (- n 4)))) ; returns 1, sequence is 4 3 2 1 0 [1] 2 ...
(duplicate (lambda (n) (remainder (+ n 3) 4))) ; returns 3, sequence is 3 0 1 2 [3] 4 0 ...


; (c) (3 pt) Implement slice, a macro that takes a sequential procedure f and a
; non-negative integer k using the syntax (slice f at k). It returns a new
; sequential procedure whose ith element is element i + k of f.
; You may assume that after we create a slice for f that f will never be reassigned.
(define-macro (slice f at k)
  _______________________________________________________)

(define (f x) (+ x 2)) ; f sequence is 2 3 4 5 6 7 ...
(define g (slice f at 3)) ; g sequence is 5 6 7 ...
(g 2) ; expect 7