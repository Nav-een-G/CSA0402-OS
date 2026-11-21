#include <stdio.h>
#include <stdlib.h>

int main()
{
    int queue[] = {98, 183, 37, 122, 14, 124, 65, 67};
    int visited[8] = {0};
    int head = 53, total = 0;
    int i, j, min, pos;

    printf("SSTF DISK SCHEDULING\n");
    printf("Sequence: %d", head);

    for(i = 0; i < 8; i++)
    {
        min = 9999;
        pos = -1;

        for(j = 0; j < 8; j++)
        {
            if(!visited[j] && abs(head - queue[j]) < min)
            {
                min = abs(head - queue[j]);
                pos = j;
            }
        }

        visited[pos] = 1;
        total += min;
        head = queue[pos];

        printf(" -> %d", head);
    }

    printf("\nTotal Head Movement = %d", total);

    return 0;
}