# testCmake
used to learn how to write CMake

### pre knowledge
you can get cmake tutorial from: http://blog.csdn.net/fan_hai_ping/article/details/42524205
 
### instructions
通过一个hello world的小程序，说明cmake的用法；这个工程很简单，就是输出hello world，但是我们将hello.cpp单独放在lib文件夹中，将头文件hello.h放在include文件夹中，主目录下放置main.cpp；这种目录结构将适用于以后较大的工程设计；bin文件夹是编译后输出可执行文件的文件夹，build是执行cmake和make的文件夹；

### demo

```Shell
cd build
cmake ../
make 

../bin/main  #you will get hello
```
