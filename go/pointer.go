package main

import "fmt"

func main() {
	f1()
	f2()
	f3()
	f4()
}

// 指针指向变量地址
func f1() {
	var x int
	var x_ptr *int
	x = 10
	x_ptr = &x
	fmt.Println(x)
	fmt.Println(x_ptr)
	fmt.Println(*x_ptr)
	// 输出指针本身地址
	fmt.Println(&x_ptr)
	// 输出指针本身地址指向变量的值 即x的地址 所以*& 相互抵消
	fmt.Println(*&x_ptr)
}

// Go的变量传递都是值传递 通过指针可以引用传递
func f2() {
	var x int = 100
	change(&x)
	fmt.Println(x)
}
// 改变的是地址的值
func change(x *int) {
	*x = 200
}

// new 初始化指针
func f3() {
	x_ptr := new(int)
	set_value(x_ptr)
	// x_ptr指向的地址
    fmt.Println(x_ptr)
    // x_ptr本身的地址
    fmt.Println(&x_ptr)
    // x_ptr指向的地址值
    fmt.Println(*x_ptr)
}
func set_value(x_ptr *int) {
	*x_ptr = 100
}

// 交叉赋值
func f4() {
	x_val := 100
	y_val := 200
	swap(&x_val, &y_val)
	fmt.Println(x_val)
	fmt.Println(y_val)
}
func swap(x, y *int) {
	*x, *y = *y, *x
}