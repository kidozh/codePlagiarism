
typedef struct
{
	int month;
	int day;
}date;
int f(date d1, date d2);
int main(void)
{
	date d1, d2;
	printf("输入第一个日期:\n");
	scanf_s("%d,%d", &d1.month, &d1.day);
	printf("输入第一个日期:\n");
	scanf_s("%d,%d", &d2.month, &d2.day);
	printf("相差%d天", f(d1, d2));
	return 0;
}
int f(date d1, date d2)
{
	int x, m, n;
	switch (d1.month)
	{
	case 1:
		m = d1.day;break;
	case 2:
		m = d1.day + 31;break;
	case 3:
		m = d1.day + 59;break;
	case 4:
		m = d1.day + 90;break;
	case 5:
		m = d1.day + 120;break;
	case 6:
		m = d1.day + 151;break;
	case 7:
		m = d1.day + 181;break;
	case 8:
		m = d1.day + 212;break;
	case 9:
		m = d1.day + 243;break;
	case 10:
		m = d1.day + 273;break;
	case 11:
		m = d1.day + 304;break;
	case 12:
		m = d1.day + 334;break;
	}
	switch (d2.month)
	{
	case 1:
		n = d2.day;break;
	case 2:
		n = d2.day + 31;break;
	case 3:
		n = d2.day + 59;break;
	case 4:
		n = d2.day + 90;break;
	case 5:
		n = d2.day + 120;break;
	case 6:
		n = d2.day + 151;break;
	case 7:
		n = d2.day + 181;break;
	case 8:
		n = d2.day + 212;break;
	case 9:
		n = d2.day + 243;break;
	case 10:
		n = d2.day + 273;break;
	case 11:
		n = d2.day + 304;break;
	case 12:
		n = d2.day + 334;break;
	}
	x = m - n;
	if (x >= 0)
		return x;
	else
		return -x;
}