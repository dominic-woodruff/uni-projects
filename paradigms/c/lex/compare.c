//Dominic Woodruff

#include <stdio.h>
#include <ctype.h>
#include <string.h>


//Checks if a word is in the dictionary
int findword(int argc, char * path, char * target){
    char dictionary[255]; 
    FILE * input_file;
    input_file = fopen(path, "r");
    int found = 0;
    char string[255]; 
    char key[strlen(target)]; 
    strcpy(key, target);
    for(int i = 0; key[i]; i++){
        key[i] = tolower(key[i]);
    }
    while(fgets(string, 255, input_file) != NULL){
        found = strcmp(key, string);
        if(found == 0 | found == -10){  //strcmp == -10 is when they match but one has a "\n" char
            printf("%s is in the dictionary.\n", target);
            return 1;
        }
        if(found < 0 & found > -10){
            printf("%s is not in the dictionary\n", target);
            return 0;
        }
    }
    printf("%s is not in the dictionary\n", target);
    return 0;
}

//loops through argc and checks if every argument after the output file is in the dictionary
int main(int argc, char * argv[]){
    int isWord;
    char *output;
    char input[81];
    FILE * output_file;
    output_file = fopen("output.txt", "w");

    while (fgets(input, 80, stdin) != NULL) {
        isWord = findword(argc, argv[1], input);
        if(isWord){
            output = strcat(input, " is in the dictionary\n");
            fputs(output, output_file);
        }
        else{
            output = strcat(input, " is not in the dictionary\n");
            fputs(output, output_file);
        }
    }
}
