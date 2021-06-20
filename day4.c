#include<stdio.h>

#define CHARBUFF_SIZE 100 //the size of the character buffer - my longest line was 82 chars

const char mandatory_fields[7][4] = { //4 for end of string
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
};


int main()
{   
    //read a word
    //truncate it to 3 chars - (just insert \0)
    //add one to a count if it's in the manditory_fields
    //if we're on an empty new line (strlen is 1?)
    //check if the count is 7
    //if so add it to the count of valid password
    int valid_count = 0;
    int fields_count = 0;

    FILE *fp;
    char buff[CHARBUFF_SIZE]; 
    fp = fopen("day4.txt", "r");
    fgets(buff, CHARBUFF_SIZE, (FILE*)fp);
    printf("1 : %s\n", buff );
}