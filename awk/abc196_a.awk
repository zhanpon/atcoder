NR == 1 { b = $2 }
NR == 2 { c = $1 }
END { print b - c }
