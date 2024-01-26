//Dominic Woodruff

//#include "myIntType.h"
#include "myCharType.h"
//#include "myDoubleType.h"


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