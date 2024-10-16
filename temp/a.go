// Terdapat sebuah bilangan bulat B. Buatlah ekspresi untuk memeriksa apakah B merupakan kelipatan 2 dan kelipatan 3. 
// Output true jika B kelipatan 2 dan 3, dan false jika bukan.
package main

import "fmt"

func main() {
	var B int

	// Input nilai B
	fmt.Println("Masukkan bilangan bulat:")
	fmt.Scan(&B)

	// Memeriksa apakah B kelipatan 2 dan 3
	isMultiple := (B % 2 == 0) && (B % 3 == 0) // Memeriksa kelipatan 2 dan 3

	// Output hasil
	fmt.Println(isMultiple)
}
