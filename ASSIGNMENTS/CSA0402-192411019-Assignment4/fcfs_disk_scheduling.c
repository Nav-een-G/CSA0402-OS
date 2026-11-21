#include <stdio.h>
#include <stdlib.h>

int main()
{
    int queue[] = {98, 183, 37, 122, 14, 124, 65, 67};
    int head = 53, total = 0, i;

    printf("FCFS DISK SCHEDULING\n");
    printf("Sequence: %d", head);

    for(i = 0; i < 8; i++)
    {
        total += abs(head - queue[i]);
        head = queue[i];

        printf(" -> %d", head);
    }

    printf("\nTotal Head Movement = %d", total);

    return 0;
}