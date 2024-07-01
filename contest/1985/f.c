#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
typedef int64_t i64;
#define LL 250000

// this method is essentially simulation and too slow

int main()
{
    i64 t;
    scanf("%li",&t);
    i64 *a = (i64*)malloc(LL*sizeof(i64));
    i64 *c = (i64*)malloc(LL*sizeof(i64));
    i64 *wait = (i64*)malloc(LL*sizeof(i64));
    while (t--)
    {
        i64 h,n;
        scanf("%li%li",&h,&n);
        for (i64 i = 0; i < n; ++i)
        {
            scanf("%li",a+i);
            h -= a[i];
        }
        i64 turns = 1;
        for (i64 i = 0; i < n; ++i)
            scanf("%li",c+i);
        memcpy(wait,c,n*sizeof(i64));
        while (h > 0)
        {
            i64 waitmin = wait[0];
            for (i64 i = 0; i < n; ++i)
                if (wait[i] < waitmin)
                    waitmin = wait[i];
            turns += waitmin;
            for (i64 i = 0; i < n; ++i)
                wait[i] -= waitmin;
            for (i64 i = 0; i < n; ++i)
                if (wait[i] == 0)
                {
                    h -= a[i];
                    wait[i] = c[i];
                }
        }
        printf("%li\n",turns);
    }
    free(a);
    free(c);
    free(wait);
    return 0;
}
