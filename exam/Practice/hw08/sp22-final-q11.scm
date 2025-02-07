#lang racket
(require rackunit)
(define expect check-equal?)
(define nil '())

; 11. (6.0 points) Beadazzled, The Scheme-quel
; Implement make-necklace, a Scheme procedure that creates a Scheme list where
; each value comes from a given Scheme list of beads, and the beads are
; repeated in order to make a necklace of a given length. For example, if
; make-necklace is called with (~ *) and a length of 3, then the linked list
; will contain ~, then *, then '~'. Here’s a diagram of that list:
; -> ~ -> * -> ~
; See the docstring and doctests for further details on how the function
; should behave.

(define (make-necklace beads length)
  ; Returns a list where each value is taken from the BEADS list,
  ; repeating the values BEADS until the list has reached
  ; LENGTH. You can assume that LENGTH is greater than or equal to 1,
  ; and that there is at least one bead in BEADS.
    (if __________
      __________
      (cons __________
            (make-necklace __________
                           __________))))

; test for racket
(expect (make-necklace '(~ *) 3) '(~ * ~))
(expect (make-necklace '(~ ^) 4) '(~ ^ ~ ^))
(expect (make-necklace '(> 0 <) 9) '(> 0 < > 0 < > 0 <))
; test for cs61a
;(expect (make-necklace '(~ *) 3) (~ * ~))
;(expect (make-necklace '(~ ^) 4) (~ ^ ~ ^))
;(expect (make-necklace '(> 0 <) 9) (> 0 < > 0 < > 0 <))
