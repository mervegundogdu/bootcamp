#include <bits/stdc++.h>
using namespace std;

void encryptDecrypt(unsigned char* data, int len, const string& key) {
    int klen = (int)key.size();
    for (int i = 0; i < len; i++) {
        data[i] ^= (unsigned char)key[i % klen];  // repeating-key XOR
    }
}

void printHex(const unsigned char* data, int len) {
    for (int i = 0; i < len; i++) printf("%02X ", data[i]);
    printf("\n");
}

int main() {
    string key = "merve";

    unsigned char sampleString[] = "skysec";
    int len = (int)strlen((char*)sampleString);  // uzunluğu EN BAŞTA al

    printf("Plaintext: %s\n", sampleString);

    // Encrypt
    encryptDecrypt(sampleString, len, key);
    printf("Encrypted (HEX): ");
    printHex(sampleString, len);

    // Decrypt
    encryptDecrypt(sampleString, len, key);
    printf("Decrypted: %s\n", sampleString);

    return 0;
}

