//Dominic Woodruff

#include <stdio.h>
#include <ctype.h>

int start(char string[]);
int Alpha(char string[]);
int notAlpha(char string[]);
int finish();

int main(int argc, char * argv[]){
    FILE * input_file;
    input_file = fopen(argv[1], "r");
    char string[101];
    fgets(string, 101, input_file);
    printf("input: \n%s\n", string);
    printf("output:\n");
    start(string);
}

int start(char string[]){
    if(string[0] == '\0'){
        finish();
        return 1;
    }
    if (isalpha(string[0])){
        printf("%c", string[0]);
        Alpha(string + 1);
    } 
    else{
        notAlpha(string + 1);
    }
    return 1;
}

int Alpha(char string[]){
    if(string[0] == '\0'){
        finish();
        return 1;
    }
    if (isalpha(string[0])){
        printf("%c", string[0]);
        Alpha(string + 1);
    } 
    else{
        printf("\n");
        notAlpha(string + 1);
    }
    return 1;
}

int notAlpha(char string[]){
    if(string[0] == '\0'){
        finish();
        return 1;
    }
    if (isalpha(string[0])){
        printf("%c", string[0]);
        Alpha(string + 1);
    } 
    else{
        notAlpha(string + 1);
    }
    return 1;
}

int finish(){
    printf("\n");
    return 1;
}