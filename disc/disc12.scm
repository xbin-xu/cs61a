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

; (define (up n)
;   (define (helper n result)
;     (if (zero? n) result
;         (helper (quotient n 10)
;                 (let ((first (remainder n 10)))
;                   (cons first (if (null? result) '()
;                                 (if (< first (car result))
;                                   result
;                                   (list result))))))))
;   (helper (quotient n 10) (list (remainder n 10))))
; Official Solution
(define (up n)
  (define (helper n result)
    (if (zero? n) result
        (helper (quotient n 10)
                (let ((first (remainder n 10)))
                  (if (< first (car result)
                    (cons first result)
                    (list first result)
                    ))))))
  (helper (quotient n 10) (list (remainder n 10))))

(up 314152667899)
