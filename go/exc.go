package main

import "fmt"

func main() {
	// defer 在函数运行结束的时候运行一段代码或调用一个清理函数
	second()
	defer first()
	// panic用来触发异常，而recover用来终止异常并且返回传递给panic的值
	defer func() {
		msg := recover()
		fmt.Println(msg)
	}()
	fmt.Println("I am walking and singing...")
	panic("It starts to rain cats and dogs")
}

// 异常
func first() {
    fmt.Println("first func run")
}
func second() {
    fmt.Println("second func run")
}