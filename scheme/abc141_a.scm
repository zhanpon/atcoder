(define (next-weather w)
  (let ([s "Sunny"]
        [c "Cloudy"]
        [r "Rainy"])
    (cond [(equal? w s) c]
          [(equal? w c) r]
          [(equal? w r) s])))

(let ([S (read-line)])
  (print (next-weather S)))
