; Q3: Increasing Rope
; Definition: A rope in Scheme is a non-empty list containing only numbers
; except for the last element, which may either be a number or a rope.
;
; Implement up, a Scheme procedure that takes a positive integer n.
; It returns a rope containing the digits of n that is the shortest rope in
; which each pair of adjacent numbers in the same list are in increasing order.
;
; Reminder: the quotient procedure performs floor division, like // in Python.
; The remainder procedure is like % in Python.

(define (up n)
  (define (helper n result)
    (if (zero? n) result
        (helper (quotient n 10)
                (let ((first (remainder n 10)))
                  (cons first (if (null? result) '() (list result)))))))
  (helper (quotient n 10) '()))

(expect (up 314152667899) '(3 (1 4 (1 5 (2 6 (6 7 8 9 (9)))))))
