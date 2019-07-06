package main

import "fmt"

func main()  {
	// 数组
	var a = [5]int {1, 2, 3, 4, 5}
	a[3] = 33
	for elem := range a {
		fmt.Println(elem)
	}

	// 不显示指定数组长度
	// 果将数组元素定义在不同行上面，那么最后一个元素后面必须跟上}或者,
	var week = [...]string {
		"Monday",
		"Tuesday",
		"Wednesday"}
	// 可以使用下划线(_)来忽略返回值
	for _, day := range week {
		fmt.Println(day)
	}
	for index, day := range week {
		fmt.Println(index, day)
	}

	// 切片 Slice
	// 切片有容量(capacity)和长度(length)两个属性
	var s = make([]float64, 5)
	fmt.Println("Capcity:", cap(s), "Length:", len(s))
	var s2 = make([]float64, 5, 10)
	fmt.Println("Capcity:", cap(s2), "Length:", len(s2))

	for i := 0; i < len(s); i++ {
        s[i] = float64(i)
    }
	fmt.Println(s)
	
	// 数组切片赋值，采用[low_index:high_index]的方式获取数值切片
	var arr1 = [5]int {1, 2, 3, 4, 5}
	var s11 = arr1[2:3]
	var s12 = arr1[:3]
	var s13 = arr1[2:]
	var s14 = arr1[:]
	fmt.Println(s11, s12, s13, s14)

	for i := 0; i < len(s2); i++ {
        s2[i] = float64(i)
    }
	// 切片长度可变
	s2 = append(s2, 5, 6, 7, 8)
	fmt.Println(s2)
	fmt.Println("Capacity:", cap(s2), "Length:", len(s2))
	
	// Go在默认的情况下，如果追加的元素超过了容量大小，Go会自动地重新为切片分配容量，容量大小为原来的两倍
	s2 = append(s2, 9, 10, 11, 12)
	fmt.Println(s2)
	fmt.Println("Capacity:", cap(s2), "Length:", len(s2))

	// 拷贝切片 slice1的元素拷贝到slice2
	slice1 := []int{1, 2, 3, 4, 5, 6}
    slice2 := make([]int, 5, 10)
    copy(slice2, slice1)
    fmt.Println(slice1)
	fmt.Println(slice2)
	
	// 字典 Map
	// 初始化数据
	var m = map[string]string {
		"A": "Apple",
		"B": "Banana",
		"O": "Orange",
		"P": "Pear",
	}
	// 可以使用下划线(_)来忽略返回值
	for key, val := range m {
		fmt.Println("Key:", key, "Value:", val)
	}
	// 通过make函数来初始化字典
	m1 := make(map[string]string)
	m1["A"] = "Apple"
	m1["B"] = "Banana"
	m1["O"] = "Orange"
	m1["P"] = "Pear"
	fmt.Println(m1)
	// 如果键值不存在，返回零值
	// 判断是否存在键
	// 返回值有两个，一个是值，另一个是是否存在此键的bool型变量
	if val, ok := m1["C"]; ok {
		fmt.Println(val)
	}
	// delete
	delete(m1, "A")
	fmt.Println(m1)
	// 嵌套map
	var facebook = make(map[string]map[string]int)
    facebook["0616020432"] = map[string]int{"Jemy": 25}
    facebook["0616020433"] = map[string]int{"Andy": 23}
    facebook["0616020434"] = map[string]int{"Bill": 22}
    for stu_no, stu_info := range facebook {
        fmt.Println("Student:", stu_no)
        for name, age := range stu_info {
            fmt.Println("Name:", name, "Age:", age)
        }
        fmt.Println()
    }
}