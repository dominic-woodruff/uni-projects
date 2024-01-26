//Dominic Woodruff

#include <stdio.h>
#include <unistd.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>


//Runs pipes between here, lex.c, compare.c, and sort command in bash
//Lex is ran and output is piped to sort, which is piped to compare
//input is a text file, the output checks every set of chars is a
//word in the dictionary or not
int main(int argc, char * argv[]){
    char * newArgs[5];
    pid_t lex;
    int lexDes[2];
    pipe(lexDes);
    lex = fork();

    if(lex == 0){
        newArgs[0] = "./lex.out";
        newArgs[1] = argv[1];
        newArgs[2] = NULL;

        close(lexDes[0]);
        dup2(lexDes[1], 1);
        close(lexDes[1]);

        execvp(newArgs[0], newArgs);
    } 
    else{
        close(lexDes[1]); 
    }

    pid_t sort;
    int sortDes[2];
    pipe(sortDes);
    sort = fork();

    if(sort == 0){
        printf("hi");
        newArgs[0] = "sort";
        newArgs[1] = "-f";
        newArgs[2] = "-u";
        newArgs[3] = NULL;

        dup2(lexDes[0], 0);
        dup2(sortDes[1], 1);
        close(lexDes[0]);
        close(sortDes[0]);
        close(sortDes[1]);

        execvp(newArgs[0], newArgs);
    }
    else{
        close(lexDes[0]);
    }

    pid_t compare;
    compare = fork();

    if (compare == 0){
        newArgs[0] = "./compare.out";
        newArgs[1] = argv[3];
        newArgs[2] = argv[2];
        newArgs[3] = NULL;

        dup2(sortDes[0], 0);
        close(sortDes[1]);
        close(sortDes[0]);
        

        execvp(newArgs[0], newArgs);
    }
    else{
        close(sortDes[1]);
    }  
    close(sortDes[0]);

}