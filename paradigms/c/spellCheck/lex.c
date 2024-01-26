//Dominic Woodruff

#include <stdio.h>
#include <ctype.h>

int lex(char, int);

//Read file by char and send each through lex
int main(int argc, char * argv[]){
    FILE * input_file;
    input_file = fopen(argv[1], "r");
    char character;
    int boolean = 0;
    while(!feof(input_file)){
        char c = fgetc(input_file);
        boolean = lex(c, boolean);
    }
}

//print letters, make a new line when non alphas are read
int lex(char character, int boolean){
    if(isalpha(character)){
        putchar(character);
        return 0;
    }
    if(boolean == 1){
        return 1;
    }
    putchar('\n');
    return 1;
}