#include "stdio.h"

int main(){
	char tape[20000] = {0};
	char *ptr = tape;
	++ptr;
	++*ptr;
	++*ptr;
	++*ptr;
	while (*ptr){
		++*ptr;
	}
	for(int i=0; i<5; ++i){
		--*ptr;
	}

	putchar(*ptr);
	--ptr;
	if(*ptr == 3){
		++*ptr;
		++*ptr;
		--*ptr;
		--*ptr;
	}
	else if(*ptr == 2){
		++*ptr;
		--*ptr;
	}
	else{
		++*ptr;
	}
	for(int i=0; i<71; ++i){
		++*ptr;
		--*ptr;
		putchar(*ptr);
	}
	*ptr *= 2;
}
