package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	line := scanner.Text()
	abc := strings.Fields(line)

	var sum int
	for _, s := range abc {
		x, _ := strconv.Atoi(s)
		sum += x
	}

	if sum <= 21 {
		fmt.Println("win")
	} else {
		fmt.Print("bust")
	}
}
