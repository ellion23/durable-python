package main

import (
	"bufio"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("/home/ellion/ege/07/17.txt")
	if err != nil {
		panic(err)
	}
	var maxsum int16 = 0
	count := 0
	x := 0
	numbers := [10000]int16{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lineStr := scanner.Text()
		num, _ := strconv.Atoi(lineStr)
		numbers[x] = int16(num)
		x++
	}
	defer file.Close()
	for index1, item1 := range numbers[:9998] {

		if maxsum < item1+item1 {
			maxsum = item1 + int16(index1)

		}
	}
	println(count, maxsum)
}
