python
Validate Input

Write a program to validate the input data(First Name, Last Name, EmployeeID, Zip code). The first name and the last name must
be filled in, which at least two letters. EmployeeID must be in such format:"AA-1234". Zip code must be numeric.

从命令后得到 first name、last name、 Zip code 和 EmployeeID.
然后程序判断：
    姓名是否为空
    姓名是否包含至少2个字母（默认为字母）
    id是否符合"AA-1111"格式
    Zip code是否是纯数字


项目说明：

>src目录下为题目代码源文件，需要完成的内容为validate.py里的validate方法。
>src目录下的__init__.py文件不需要改动。

>test目录下为测试用例文件，不可进行修改。


示例：

	输入：
	Enter the first name:
	JEnter the last name:
	Enter the ZIP code: ABCDE
	Enter an employee ID: A12-1234

	输出：(不包含每行开头的‘* ’部分；不要输出额外的内容，否则会影响结果判断的正确性)
	* "J" is not a valid first name. It is too short.
	* The last name must be filled in.
	* The ZIP code must be numeric.
	* A12-1234 is not a valid ID.
