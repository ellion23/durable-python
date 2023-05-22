package main

import (
	"bufio"
	"os"
	"strconv"
)

var d int16 = 160

func main() {
	file, err := os.Open("/home/ellion/heh/in.txt")
	if err != nil {
		panic(err)
	}
	var maxsum int16 = 0
	count := 0
	x := 0
	numbers := [30000]int16{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lineStr := scanner.Text()
		num, _ := strconv.Atoi(lineStr)
		numbers[x] = int16(num)
		x++
	}
	defer file.Close()
	for index1, item1 := range numbers[:29999] {
		for _, item2 := range numbers[index1+1 : 30000] {
			if ((item1 % d) != (item2 % d)) && ((item1%7 == 0) || (item2%7 == 0)) {
				count++
				if maxsum < item1+item2 {
					maxsum = item1 + item2
				}
			}
		}
	}
	println(count, maxsum)
}
