// code-sample-cpp.cpp : This file contains the 'main' function. Program execution begins and ends there.

#include <iostream>

using namespace std;

int main()
{
	char utf8_et = 0xe9;
    string origines[2] = {"Allemagne", "Vietnam"};
    string lieuDeNaissance = "France";
	cout << "Je suis originaire de l'" << origines[0] << " et du " << origines[1] << " mais je suis n" << utf8_et << " en " << lieuDeNaissance << endl;
    return 0;
}
