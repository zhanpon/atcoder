package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())
	sc.Scan()
	s := sc.Text()

	for _, c := range s {
		fmt.Print(string(rot(c, n)))
	}
	fmt.Println()
}

func rot(r rune, n int) rune {
	return 'A' + (r-'A'+int32(n))%26
}
