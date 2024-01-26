//Dominic Woodruff

#include <stdio.h>

//Add 2 numbers and return result using printf and scanf
int main(){
    int sum;
    int num1;
    int num2;
    printf("Enter a number to add\n");
    scanf("%d", &num1);
    printf("Enter a  second number to add\n");
    scanf("%d", &num2);
    sum = num1 + num2;
    printf("The sum is %d\n", sum);
    return 0;
}
