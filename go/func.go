package main

import "fmt"

func main() {
	fmt.Println(sum(1, 2))
	fmt.Println(sum_avg(1, 2))
	fmt.Println(sum_changeable(1, 2, 3, 4, 5))
	fmt.Println(closure(1, 2, 3, 4, 5))
	fmt.Println(recursion(10))

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

// 命名返回值
func sum(a int, b int) (sum int) {
	sum = 0
	sum = a + b
	return
}

// 多个返回值
func sum_avg(a int, b int) (int, float64) {
	sum := 0
	avg := 0.0
	sum = a + b
	avg = float64(sum) / float64(2)
	return sum, avg
}

// 可变参数
func sum_changeable(arr ...int) int {
	sum := 0
	for val := range arr {
		sum += val
	}
	return sum
}

// 闭包
func closure(arr ...int) int {
	var sum = func() int {
		sum := 0
		for val:= range arr {
			sum += val
		}
		return sum
	}
	return sum()
}

// 递归
func recursion(n int) int {
	if n == 1 {
		return n
	} else {
		return n * recursion(n - 1)
	}
}

// 异常
func first() {
    fmt.Println("first func run")
}
func second() {
    fmt.Println("second func run")
}