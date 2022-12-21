#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int r, c;
	cin >> r >> c;

	float pizza_area = (float)M_PI*pow(r, 2);
	float cheese_area = (float)M_PI*pow(r-c, 2);

	cout << (float)100*(cheese_area / pizza_area) << endl;
}

