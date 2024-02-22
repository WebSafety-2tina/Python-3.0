<?php

// 设置时区为中国标准时间
date_default_timezone_set('Asia/Shanghai');

// 生成随机数字和英文字母的函数
function generateRandomString($length = 10) {
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $randomString = '';
    for ($i = 0; $i < $length; $i++) {
        $randomString .= $characters[rand(0, strlen($characters) - 1)];
    }
    return $randomString;
}

// 每 5 分钟执行一次
while (true) {
    // 生成随机字符串
    $randomString = generateRandomString();

    // 输出当前时间和随机字符串
    echo date('Y-m-d H:i:s') . ' - ' . $randomString . "\n";

    // 休眠 5 分钟
    sleep(300);
}
