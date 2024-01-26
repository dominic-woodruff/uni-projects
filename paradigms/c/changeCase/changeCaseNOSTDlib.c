//Dominic Woodruff

#include <stdio.h>

const char * flipStr(char str[]);
int flipChar(int flip);
int islower(int character);
int isupper(int character);
int tolower(int character);
int toupper(int character);

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

//return 1 if the input is lowercase and 0 otherwise
int islower(int character){
    return (character >= 'a' && character <= 'z');
}

//return 1 if the input is uppercase and 0 otherwise
int isupper(int character){
    return (character >= 'A' && character <= 'Z');  
}

//forces the 5th bit to 1 (makes ascii lowercase)
int tolower(int character){
    if(isupper(character)){
        return character | 0x20;
    }
    return character;
}

//forces the 5th bit to 0 (makes ascii uppercase)
int toupper(int character){
    if(islower(character)){
        return character & 0xDF;
    }
    return character;
}