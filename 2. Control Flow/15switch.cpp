#include <bits/stdc++.h>
using namespace std;

// Function to convert number into string
string numbers_to_strings(int argument)
{
	switch (argument)
	{
	case 0:
		return "zero";
	case 1:
		return "one";
	case 2:
		return "two";
	case 3:
		return "three";
	default:
		return "define more arguments in switch";
	};
};

int main()
{
	int argument;
	cout << "Enter the number:";
	cin >> argument;
	cout << numbers_to_strings(argument);
	return 0;
}
