package com.bruse;

import cn.hutool.core.date.DateUtil;

import java.util.Date;

public class HutoolTest {

    public static void main(String[] args) {
        Date date = DateUtil.parse("2019-09-19");
        System.out.println(date);
    }
}
