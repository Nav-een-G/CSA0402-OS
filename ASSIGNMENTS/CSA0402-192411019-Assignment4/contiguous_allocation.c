#include <stdio.h>

int main()
{
    int start[4] = {0, 6, 14, 19};
    int size[4] = {6, 8, 5, 7};
    int i, j;

    printf("CONTIGUOUS FILE ALLOCATION\n");

    for(i = 0; i < 4; i++)
    {
        printf("File %c: ", 'A' + i);

        for(j = start[i]; j < start[i] + size[i]; j++)
            printf("%d ", j);

        printf("\n");
    }

    return 0;
}