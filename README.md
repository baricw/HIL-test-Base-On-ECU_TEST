# Welcome to GitHub Desktop!

This is your README. READMEs are where you can communicate what your project is and how to use it.

Write your name on line 6, save it, and then head back to GitHub Desktop.测试用例编写说明
本文主要针对可自动生成package的用例的编写进行说明。
用例结构如下图所示：
 ![image](https://user-images.githubusercontent.com/51228521/112479626-30f42800-8db0-11eb-9104-dacad088d735.png)

现在对每个模块进行详细说明。
1、	测试用例ID
这一部分填写的是每一条用例的名字，便于用例的区分。
2、	初始条件
主要填写用例开始时的初始化。
![image](https://user-images.githubusercontent.com/51228521/112479657-381b3600-8db0-11eb-9c52-df29a1ea3bf0.png)
Step之间用英文符号 ; 隔开
Step与具体步骤之间用英文符号  ：隔开，表示步骤标题与步骤信号的区分
Step中每个信号使用英文符号 ， 隔开，表示步骤中信号之间的区分
信号与值之间使用英文符号 = 隔开
涉及到CAN信号恢复使用  CAN信号=sw
等待时间 wait=1，表示等待1s
3、	测试步骤
具体的测试步骤
![image](https://user-images.githubusercontent.com/51228521/112479685-3f424400-8db0-11eb-8d69-2ab60a0c4c89.png)
编写方式同初始条件
4、	退出条件
退出前的操作
![image](https://user-images.githubusercontent.com/51228521/112479717-46695200-8db0-11eb-9c6e-ac190470457e.png)
编写方式同初始条件
5、	期望结果
![image](https://user-images.githubusercontent.com/51228521/112479748-4c5f3300-8db0-11eb-8b02-e32d3083e67f.png)
Check之间用英文符号 ; 隔开
Check与具体步骤之间用英文符号  ：隔开，表示步骤标题与步骤信号的区分
Check中每个信号使用英文符号 ， 隔开，表示步骤中信号之间的区分
信号名与期望结果之间使用 英文符号() 隔开
期望结果有四种格式，分别表示不同的期望方式
第一种是value==1，value>=1, value<=1, value!=1, value>1, value<1, value==1 or value==2, value==1 and value==2, abs(2 - value) <= 1,
round(2.135,3)=round(value,3),注：round函数返回数值的小数点四舍五入到n个数字，round（2.1357,3）返回2.1357的带有3个小数的值2.135。
Value==（>=, <= !=,>,<）变量名
例如：VCU_TargetClutchMode(value==1)
第二种是带until+时间，在时间内实际结果与期望结果有一次相等即为真，例如：VCU_ePTReady_H(value==1@until5)。
第三种是带save=变量名，例如：VCU_ePTReady_H(save=s0)
第四种是带still+时间，在时间内实际结果与期望结果一直相等为真，例如：VCU_ChargeAllowed(value==1@still10)
注：until和still只能处在第二个@后面，并且until和still不能同时使用
后续会添加其他功能。
6、	结果分析
![image](https://user-images.githubusercontent.com/51228521/112479790-541ed780-8db0-11eb-896c-a7d353b69a56.png)
生成trace analysis。
例如：CheckBusFrameDlc是Trace step templates/My templates中的函数名，
FrameLength是函数的参数，KL30是参数的实例（KL30必须在用例中出现过的mapName）
7、	用例ID为空跳过功能
![image](https://user-images.githubusercontent.com/51228521/112479828-5b45e580-8db0-11eb-9aa5-219add7598ba.png)
如果测试用例ID是空的话自动跳过读取生成用来（可用空出的行标明用例模块和暂时不用的用例可先去除测试用例ID）。
8、	其他
由于测试需求，增加信号类型分类。目前信号分为以下几种类型：
（1）IO标准命名
工具使用示意图
  
![image](https://user-images.githubusercontent.com/51228521/112479871-6731a780-8db0-11eb-94ed-d8c97a87a76b.png)
