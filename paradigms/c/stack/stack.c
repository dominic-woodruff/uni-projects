//Dominic Woodruff

#include <malloc.h>
#include "stackADT.h"

//Implementation of a stack data structure 


//Adds data to the top of the stack
stacktype *push(stacktype *stack, dataType value){
    nodeType *newNode = (nodeType*) malloc(sizeof(nodeType));
    newNode->element = value;
    newNode->next = stack->bottom;
    stack->bottom = newNode;
    if(stack->size==0)
        stack->top = newNode;
    stack->size++;
    return stack;
}

//Removes the "top" of the stack and adjusts memory to set a new top
nodeType *pop(stacktype *stack){
    if(stack->size==0)
        return NULL;
    nodeType *temp = stack->bottom;
    stack->bottom = temp->next;
    stack->size--;
    if(stack->size==0)
        stack->top = NULL;
    return temp;
}

//Checks if the first character is the end of a string
int isEmpty(stacktype *stack){
    return (stack->size == 0);
}

//Shows the "top" of the stack
nodeType *peek(stacktype *stack){
    return stack->bottom;
}

//Creates a stack
stacktype *create(){
    stacktype *stack = (stacktype*) malloc(sizeof(stacktype));
    stack->top = NULL;
    stack->bottom = NULL;
    stack->size = 0;
    return stack;
}

//Removes the stack by freeing its memory
void *destroy(stacktype *stack){
    if(stack != NULL){
        while(stack->top != NULL){
            nodeType *temp = stack->top;
            stack->top = temp->next;
            free(temp);
        }
        free(stack);
    }
    stack = NULL;
}

typedef struct node{
    struct node *next;
    dataType element;
}nodeType;

typedef struct stackheader{
    struct node *top;
    struct node *bottom;
    int size;
}stacktype;


stacktype *push(stacktype *, dataType);
nodeType *pop(stacktype *);
int isEmpty(stacktype *);
nodeType *peek(stacktype *);
stacktype *create();
void *destroy(stacktype *);