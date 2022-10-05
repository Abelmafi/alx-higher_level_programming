#include <stdio.h>
#include <stdbool.h>
#include <string.h>


#define MAX_NAME 256
#define TABLE_SIZE 10

typedef struct {
	char name[MAX_NAME];
	int age;
} person;

person *hash_table[TABLE_SIZE];

unsigned int hash(char *name)
{
	unsigned int hash_value = 0;
	for (int i = 0; i < strlen(name); i++)
	{
		hash_value += name[i];
		hash_value = (hash_value * name[i]) % TABLE_SIZE;
	}
	return (hash_value);
}

bool init_hash_table()
{
	for(int i = 0; i < TABLE_SIZE; i++)
	{
		hash_table[i] = NULL;
	}
}

void print_table()
{
	for (int i = 0; i < TABLE_SIZE; i++)
	{
		if (hash_table[i] == NULL)
			printf("\t%i\t---\n", i);
		else
			printf("\t%i\t%s\n", i, hash_table[i]->name);
	}
}

bool hash_table_insert(person *p)
{
	if (p == NULL)
		return false;
	int index = hash(p->name);
	for (int i = 0; i < TABLE_SIZE; i++)
	{
		int try = (i + index) % TABLE_SIZE;
		if (hash_table[try] == NULL) {
		hash_table[try] = p;
		return true;
		}
	}
	return true;
}
person *hash_table_lookup(char *name)
{
	int index = hash(name);
	if (hash_table[index] != NULL && strncmp(name, hash_table[index]->name, TABLE_SIZE) == 0)
		return (hash_table[index]);
	else
		return NULL;
}

person *hash_table_delete(char *name)
{
        int index = hash(name);
        if (hash_table[index] != NULL && strncmp(name, hash_table[index]->name, TABLE_SIZE) == 0)
	{
		person *tmp = hash_table[index];
		hash_table[index] = NULL;
                return (tmp);
	}
        else
                return NULL;
}


int main()
{
	init_hash_table();
	//print_table();

	person jakob = {.name = "jakob", .age = 66};
	person elias = {.name = "elias", .age = 46};
	person chery = {.name = "chery", .age = 36};
	person sari = {.name = "sari", .age = 76};
	person merry = {.name = "merry", .age = 546};
	person hlina = {.name = "hlina", .age = 35};
	person boni = {.name = "boni", .age = 75};
	person kebi = {.name = "kebi", .age = 24};
	person dani = {.name = "dani", .age = 46};
	person bruk = {.name = "bruk", .age = 46};

	hash_table_insert(&jakob);
	hash_table_insert(&elias);
	hash_table_insert(&chery);
	hash_table_insert(&sari);
	hash_table_insert(&merry);
	hash_table_insert(&hlina);
	hash_table_insert(&boni);
	hash_table_insert(&kebi);
	hash_table_insert(&dani);
	hash_table_insert(&bruk);

	print_table();

	person *tmp = hash_table_lookup("elias");
	hash_table_delete("chery");
	print_table();
	if (tmp == NULL)
		printf("%s\n", "Not there");
	else
		printf("\tFound! %d, %s\n", tmp->age, tmp->name);
	
	return 0;
}


