#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define TABLE_SIZE 10
typedef struct person{
	char *name;
	int age;
	struct person *next;
} person;

/*typedef struct hash_table_s
{
     unsigned long int size;
     hash_node_t **array;
} hash_table_t;*/

person *hash_table[10];

unsigned int hash(char *s)
{
	unsigned int hash_value = 0;
	for (int i = 0; i < strlen(s); i++)
	{
		hash_value += s[i];
		hash_value = (hash_value * s[i]) % TABLE_SIZE;
	}
	return hash_value;
}

bool init_hash_table()
{
        for(int i = 0; i < TABLE_SIZE; i++)
                hash_table[i] = NULL;
}

bool hash_table_insert(person *p)
{
	if (p == NULL)
		return NULL;
	int index = hash(p->name);
	p->next = hash_table[index];
	hash_table[index] = p;
	return true;
}

person *hash_table_lookup(char *name)
{
	int index = hash(name);
	person *tmp = hash_table[index];
	while (tmp != NULL && strcmp(tmp->name, name) != 0)
	{
		tmp = tmp->next;
	}
	return tmp;
}

person *hash_table_delete(char *name)
{
        int index = hash(name);
        person *tmp = hash_table[index];
	person *prev = NULL;
        while (tmp != NULL && strcmp(tmp->name, name) != 0)
        {
		prev = tmp;
                tmp = tmp->next;
        }
	if (tmp == NULL)
		return NULL;
	if (prev == NULL)
		hash_table[index] = tmp->next;
	else
		prev->next = tmp->next;
        return tmp;
}

void print_table()
{
	for (int i = 0; i < TABLE_SIZE; i++)
	{
		if (hash_table[i] == NULL)
			printf("\t%i\t----\n", i);
		else
		{
			printf("\t%i\t ", i);
			person *tmp = hash_table[i];
			while(tmp)
			{
				printf("%s - ", tmp->name);
				tmp = tmp->next;
			}
			printf("\n");
		}
	}
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

