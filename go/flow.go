package main

import "fmt"

func main() {
	// go 强制了{}的格式 
	// func main()
	// {
	// }
	// 编译不通过

	// 条件
	// 多条件判断，需要括号
	// go自带格式化工具：go fmt flow.go
	var age = 20
	if age >= 18 {
		fmt.Println("adult")
	} else if (age <= 6) {
		fmt.Println("kid")
	} else {
		fmt.Println("teenager")
	}

	// switch
	// 不需要break
	var score = 69
	switch score / 10 {
	case 10:
	case 9:
		fmt.Println("优秀")
	case 8:
		fmt.Println("良好")
	case 7:
		fmt.Println("一般")
	case 6:
		fmt.Println("及格")
	default:
		fmt.Println("不及格")
	}

	// for
	for i := 0; i < 10; i++ {
		fmt.Println(i)
	}

	// 没有while
	// 死循环
	// for {
	// }
}