package main

import "fmt"

func main()  {
	// 整型 浮点型
	var i int = 1
	var f float64 = 12
	fmt.Println(i)
	fmt.Println(f)

	// 字符串转义
	// 双引号之间的转义字符会被转义，而``号之间的转义字符保持原样不变
	var a = "hello \n world"
	var b = `hello \n world`
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(len(a))
	fmt.Println(a[1])
	fmt.Println(a + b)

	// 布尔型
	var a1 bool = true
	var b1 bool = false
	fmt.Println(a1 == b1)
	
	// 变量
	var x string = "hello world"
	fmt.Println(x)
	// 直接赋值 会进行类型推断
	var x1 = "hello world"
	fmt.Println(x1)
	// 推断语言类型 无需写var关键字
	// 使用:=方式定义变量的方式只能用在函数内部
	x2 :=10
	fmt.Println(x2)

	// 类型转换
	var x3 float64 = 1.11
	fmt.Println(x3)
	fmt.Println(int(x3))

	fmt.Println(globalVar)

	// 常量
	// :=不能够用来定义常量。因为常量的值是在编译的时候就已经确定的
	const c string = "it is a const"
	fmt.Println(c)

	// 多变量或常量定义
	var (
		am int = 10
		bm float64 = 3.5
		cm bool = true
	)
	const (
		Pi float64 = 3.14
		True bool = true
	)
	fmt.Println(am, bm, cm)
	fmt.Println(Pi, True)
}

// 全局变量
var globalVar string = "this is a global variable"