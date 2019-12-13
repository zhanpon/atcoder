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
	r, _ := strconv.Atoi(sc.Text())

	fmt.Println(r * r)
}
