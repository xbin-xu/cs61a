(define (ascending? s) 
    (cond
        ((or (null? s) (null? (cdr s))) #t)
        (else (and (<= (car s) (car (cdr s))) (ascending? (cdr s))))))

(define (my-filter pred s) 
    (cond
        ((null? s) nil)
        ((pred (car s)) (cons (car s) (my-filter pred (cdr s))))
        (else (my-filter pred (cdr s)))))

(define (interleave lst1 lst2) 
    (cond
        ((null? lst1) lst2)
        ((null? lst2) lst1)
        (else (cons (car lst1) (interleave lst2 (cdr lst1))))))

(define (no-repeats s)
    (cond
        ((null? s) nil)
        (else (cons (car s) (no-repeats (filter (lambda (x) (not (= x (car s)))) (cdr s)))))))
