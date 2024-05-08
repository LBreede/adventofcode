#include <stdio.h>
#include <stdlib.h>

int part_one(int *arr, int size)
{
    for (int i = 0; i < size; i++)
    {
        for (int j = i + 1; j < size; j++)
        {
            if (arr[i] + arr[j] == 2020)
            {
                return arr[i] * arr[j];
            }
        }
    }
    return -1;
}

int part_two(int *arr, int size)
{
    for (int i = 0; i < size; i++)
    {
        for (int j = i + 1; j < size; j++)
        {
            for (int k = j + 1; k < size; k++)
            {
                if (arr[i] + arr[j] + arr[k] == 2020)
                {
                    return arr[i] * arr[j] * arr[k];
                }
            }
        }
    }
    return -1;
}

int main(int argc, char *argv[])
{
    // Check if the correct number of command-line arguments is provided
    if (argc != 2)
    {
        printf("ERROR: Usage: %s <filename>\n", argv[0]);
        return 1; // Return 1 to indicate an error
    }

    FILE *fp = fopen(argv[1], "r");

    if (fp == NULL)
    {
        printf("ERROR: File not found\n");
        return -1;
    }
    // Dynamically allocate memory for the array
    int *arr = NULL;
    int size = 0;
    int num;

    // Read integers from the file and dynamically resize the array
    while (fscanf(fp, "%d", &num) == 1)
    {
        size++;                                 // Increase the size of the array
        arr = realloc(arr, size * sizeof(int)); // Resize the array
        if (arr == NULL)
        {
            printf("ERROR: Memory allocation failed\n");
            return -1;
        }
        arr[size - 1] = num; // Store the integer in the array
    }
    fclose(fp);

    // printf("DEBUG: int size = %d\n", size);

    int result_one = part_one(arr, size);
    int result_two = part_two(arr, size);

    printf("Part one: %d\n", result_one);
    printf("Part two: %d\n", result_two);
    return 0;
}