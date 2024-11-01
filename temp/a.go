package main

import (
	"fmt"
)

func main() {
	var huruf rune
	fmt.Scanf("%c", &huruf)
	fmt.Println((huruf >= 'a' && huruf <= 'z' && !(huruf == 'a' || huruf == 'e' || huruf == 'i' || huruf == 'o' || huruf == 'u')))
}
