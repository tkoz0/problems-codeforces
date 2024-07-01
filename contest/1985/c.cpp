#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

// why the fuck does codeforces do shit that has lots of collisions in std::unordered_map
#include <unordered_set>
#include <set>

typedef unsigned long long ull;

int main()
{
    ull t;
    ull *a = (ull*)malloc(200000*sizeof(ull));
    scanf("%llu",&t);
    while (t--)
    {
        ull n;
        scanf("%llu",&n);
        assert(n <= 200000);
        std::set<ull> nums;
        ull s = 0, answer = 0;
        for (ull i = 0; i < n; ++i)
            scanf("%llu",a+i);
        for (ull i = 0; i < n; ++i)
        {
            s += a[i];
            nums.emplace(a[i]);
            if (s % 2 == 0 and nums.contains(s/2))
                ++answer;
        }
        printf("%llu\n",answer);
    }
    free(a);
    return 0;
}
