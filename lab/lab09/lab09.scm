; if
; (define (over-or-under num1 num2)
;   (if (= num1 num2)
;       0
;       (if (< num1 num2)
;           -1
;           1)))

; cond
(define (over-or-under num1 num2)
  (cond 
    ((= num1 num2) 0)
    ((< num1 num2) -1)
    (else 1)))

(define (make-adder num)
  (lambda (inc) (+ inc num)))

(define (composed f g)
  (lambda (x) (f (g x))))

; (define (repeat f n)
;   (lambda (x)
;     (if (< n 1)
;         x
;         (f ((repeat f (- n 1)) x)))))

(define (repeat f n)
  (if (< n 1)
      (lambda (x) x)
      (composed f (repeat f (- n 1)))))

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

; (define (gcd a b)
;   (if (zero? b)
;       a
;       (gcd (min a b) (modulo (max a b) (min a b)))))

(define (gcd a b)
  (if (zero? b)
      a
      (gcd b (modulo a b))))
