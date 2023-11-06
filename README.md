Advanced Python course 

## Python 虚拟机
1. 运行python
2. 建立一个新的Frame，在Frame中执行byte code，每一条bytecode在c中有相应的执行
3. 每一个Frame里，python会维护一个stack，bytecode跟栈进行交互。
4. 计算-->拿结果-->返回