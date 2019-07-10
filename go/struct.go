package main

import "fmt"

// 结构体定义
type Rect struct {
	width, length float64
}

func main() {
	f1()
	f2()
}

// 赋值
func f1() {
	// 内部成员赋值
	var rect Rect
	rect.width = 100
	rect.length = 200
	fmt.Println(rect.width * rect.length)
	// 初始化赋值
	var rect2 = Rect{width: 150, length: 250}
	fmt.Println(rect2.width * rect2.length)
	// 按照顺序赋值
	var rect3 = Rect{175, 275}
	fmt.Println(rect3.width * rect3.length)
}

// 值传递
func f2() {
	var rect = Rect{100, 200}
	fmt.Println(double_area(rect))
	fmt.Println(rect.width, rect.length)
}
func double_area(rect Rect) float64 {
	rect.width *= 2
	rect.length *= 2
	return rect.width * rect.length
}