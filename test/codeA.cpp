//a.cpp
#include<stdio.h>
typedef struct //定义一个新的数据类型
{
	int yue;//月份
	int tian;//天
}Date;
void f(Date x, Date y);//函数声明
int main()
{
	Date date1, date2;
	//类型赋值
	printf("输入一个日期（mm/dd）：\n");
	scanf_s("%d/%d", &date1.yue, &date1.tian);
	printf("再输入一个日期（在上一个日期之后）（mm/dd）：\n");
	scanf_s("%d/%d", &date2.yue, &date2.tian);
	//调用函数
	f(date1, date2);
	return 0;
}
void f(Date x, Date y)
{
	int m, n;
	int t;
	//计算两个日期的天数
	switch (x.yue)
	{
	case 1:m = x.tian; break;
	case 2:m = x.tian + 31; break;
	case 3:m = x.tian + 59; break;
	case 4:m = x.tian + 90; break;
	case 5:m = x.tian + 120; break;
	case 6:m = x.tian + 151; break;
	case 7:m = x.tian + 181; break;
	case 8:m = x.tian + 212; break;
	case 9:m = x.tian + 243; break;
	case 10:m = x.tian + 273; break;
	case 11:m = x.tian + 304; break;
	case 12:m = x.tian + 334; break;
	}
	switch (y.yue)
	{
	case 1:n = y.tian; break;
	case 2:n = y.tian + 31; break;
	case 3:n = y.tian + 59; break;
	case 4:n = y.tian + 90; break;
	case 5:n = y.tian + 120; break;
	case 6:n = y.tian + 151; break;
	case 7:n = y.tian + 181; break;
	case 8:n = y.tian + 212; break;
	case 9:n = y.tian + 243; break;
	case 10:n = y.tian + 273; break;
	case 11:n = y.tian + 304; break;
	case 12:n = y.tian + 334; break;
	}
	t = n - m;
	printf("：%d\n", t);
}