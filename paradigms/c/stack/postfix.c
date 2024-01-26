//Dominic Woodruff

#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include "stackADT.h"

//output to output file
void output(double answer, char *argv[]) {
    FILE *output_file;
    char output[32];
    
    output_file = fopen(argv[2], "w");
    fprintf(output_file, "%f\n", answer);
    fclose(output_file);
}

//get input from input file
char* readInput(char *input, char *argv[]) {
    FILE *input_file;
    input_file = fopen(argv[1], "r");
    fgets(input, 101, input_file);
    fclose(input_file);
}

void processToken(stacktype *stack, char *token){
    if(strcmp(token, "+") == 0){
        double second = pop(stack)->element;
        double first = pop(stack)->element;
        push(stack, first + second);
    }
    else if(strcmp(token, "-") == 0){
        double second = pop(stack)->element;
        double first = pop(stack)->element;
        push(stack, first - second);
    }
    else if(strcmp(token, "*") == 0){
        double second = pop(stack)->element;
        double first = pop(stack)->element;
        push(stack, first * second);
    }
    else if(strcmp(token, "/") == 0){
        double second = pop(stack)->element;
        double first = pop(stack)->element;
        push(stack, first / second);
    }
    else{
        double value = atof(token);
        push(stack, value);
    }
}

int main(int argc, char * argv[]){
    char input[101];
    char string[101];
    double answer;
    stacktype *stack = create();
    readInput(input, argv);
    char *token;
    token = strtok(input, " ");
    while( token != NULL ) {
        fprintf(stderr, " %s ", token );
        processToken(stack, token);
        token = strtok(NULL, " ");
    }
    pop(stack);
    printf("output = %f\n", pop(stack)->element);

    destroy(stack);
}