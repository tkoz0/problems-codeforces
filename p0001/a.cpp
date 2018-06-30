#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <assert.h>
#include <iostream>

#define LONGEST 1000000000

int main(int argc, char **argv)
{
    uint32_t n, m, a;
    scanf("%u %u %u", &n, &m, &a);
    assert(n and n <= LONGEST);
    assert(m and m <= LONGEST);
    assert(a and a <= LONGEST);
    n = (n+a-1)/a; // number of tiles needed in each dimension
    m = (m+a-1)/a;
    std::cout << (((uint64_t) n) * ((uint64_t) m)) << std::endl;
    return 0;
}
