//Dominic Woodruff

#include <stdio.h>
#include <strings.h>
#include <ctype.h>

const char * flipStr(char str[]);
int flipChar(int flip);


//Uses arguments to read from an input file, send read data to flipStr
//and write returned data to an output file
int main(int argc, char * argv[]){

    FILE * input_file;
    FILE * output_file;
    input_file = fopen(argv[1], "r");
    output_file = fopen(argv[2], "w");
    char string[101];
    fgets(string, 101, input_file);
    printf("input is:                           %s", string);
    printf("output is:                          %s", flipStr(string));
    fputs(flipStr(string), output_file);
    return 0;
}

//calls either flipChar or flipCharManual on every char depending on the 
//value of mode, flipChar if mode != 0, or flipCharManual if mode == 0
//returns a string with flipped upper/lowercase letters
const char* flipStr(char str[]){
    int index = 0;
    while(str[index]){
        str[index] = flipChar(str[index]); 
        index++;
    }
    return str;
}

//Make uppercase letters lowercase and vice-versa using char functions
int flipChar(int flip){
    if(islower(flip)){
        return toupper(flip);
    }
    return tolower(flip);
}