#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	const char *friends[] = { "muzi", "ryan", "frodo", "neo" };
	const char* gifts[] = { "muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi" };
	size_t friends_len = sizeof(friends) / sizeof(friends[0]) ;
	size_t gifts_len = sizeof(gifts) / sizeof(gifts[0]);
	unordered_map<string, pair<int, int> > dict;
	for (const char *target : friends) {
		int req = 0;
		int resp = 0;
		for (const char* gift : gifts) {
			char temp[] = "";
			string tempGift = gift;
			vector<string> tempGifts;
			if (tempGift.find(*target) != string::npos) { //찾았다면
				int spaceIndex = tempGift.find(" ");
				tempGifts.push_back(tempGift.substr(0,spaceIndex));
				tempGifts.push_back(tempGift.substr(spaceIndex+1));
				cout << "tempGifts[0] : " << tempGifts[0] << endl;
				cout << "tempGifts[1] : " << tempGifts[1] << endl;
				cout << endl;
			}
		}
		dict[to_string(*target)] = pair<int, int>(10,20);
	}
	return 0;
	
}