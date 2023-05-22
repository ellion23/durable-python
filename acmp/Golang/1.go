package main

import (
	"bufio"
	"os"
)

func main() {
	input := bufio.NewScanner(os.Stdin)
	a := input.Text()
	println(a)
}
