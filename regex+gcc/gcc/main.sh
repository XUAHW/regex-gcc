#!/bin/bash
echo "这是gcc的测试shell文件"
echo "接下来会进行预处理生成gcc_test.i->编译生成gcc_test.s->汇编生成gcc_test.o->链接产生gcc_test"
gcc -E gcc_test.c -o gcc_test.i
echo "gcc -E gcc_test.c -o gcc_test.i   ->  gcc_test.i"
gcc -S gcc_test.i -o gcc_test.s
echo "gcc -S gcc_test.i -o gcc_test.s   ->  gcc_test.s"
gcc -c gcc_test.s -o gcc_test.o
echo "gcc -c gcc_test.s -o gcc_test.o   ->  gcc_test.o"
gcc gcc_test.o -o gcc_test
echo "gcc gcc_test.o -o gcc_test        ->  gcc_test"
