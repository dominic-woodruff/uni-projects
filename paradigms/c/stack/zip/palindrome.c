//Dominic Woodruff

#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include "stackADT.h"

//get input file
FILE * readInput(char *input, char *argv[]) {
    FILE *input_file;
    input_file = fopen(argv[1], "r");
    return input_file;
}
    
//output to output file 
void output(int bool, char *argv[], char input[]) {
    FILE *output_file;
    output_file = fopen(argv[2], "a");
    char output[101];
    if(bool)
        strcpy(output, "is a palindrome\n\n");
    else
        strcpy(output, "is not a palindrome\n\n");
    strcat(input, output);
    strcpy(output, input);
    printf("%s", output);
    fprintf(output_file, "%s\n", output);
    fclose(output_file);
}

//get rid of special characters and non alphas
void standardize(char *input){
    int input_index = 0;
    int output_index = 0;
    while(input[input_index]){
        if(isalpha(input[input_index])){
            input[output_index] = tolower(input[input_index]);
            output_index++;
        }
        input_index++;
    }
    input[output_index] = '\0';
}

//initilize the stack and push all chars in input onto it
void createStack(char *input, stacktype *stack) {
    int input_index = 0;
    while(input[input_index]){
        push(stack, input[input_index]);
        input_index++;
    }
}

//reverse the string by popping stack into a new string
void reverseString(stacktype *stack, char *reverse) {
    char popped;
    reverse[0] = '\0';
    while(stack->size > 0){
        popped = pop(stack)->element;
        strncat(reverse, &popped, 1);
    }
}

//check if input is palindrome
int checkPalindrome(char *input, char *reverse) {
    return strcmp(input,reverse)==0;
}

//set of function calls that determine if
// the input is a palindrome using a stack
void driver(char input[], char *argv[]){
    int bool;
    stacktype *stack = create();
    char copy[101];
    strcpy(copy, input);
    standardize(input);
    createStack(input, stack);
    char reverse[stack->size];
    reverseString(stack, reverse);
    bool = checkPalindrome(input, reverse);
    output(bool, argv, copy);
    destroy(stack);
}

//sends input through the driver
int main(int argc, char * argv[]){
    char input[101];
    FILE *output_file;                //clears the 
    output_file = fopen(argv[2], "w");//output file
    fclose(output_file);
    FILE * input_file = readInput(input, argv);
    while(fgets(input, 101, input_file) != NULL){ 
        driver(input, argv);
    }
    fclose(input_file);
}
