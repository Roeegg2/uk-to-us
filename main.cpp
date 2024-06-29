#include <iostream>
#include <string>
#include <fstream>
#include <cstring>

#define LETTER_TO_INDEX(letter) (letter - 97)
#define INDEX_TO_LETTER(index) (index + 97)

class Word_Tree {
public:
	Word_Node* root;

	Word_Tree();
	Word_Node insert_to_tree(Word_Node root, std::string us, std::string uk);
};

class Word_Node {
public:
	std::string uk;
	std::string us;

	Word_Node* sons[26];
	Word_Node(std::string us, std::string uk);
};

Word_Node::Word_Node(std::string us, std::string uk)
{
	this->uk = uk;
	this->us = us;

	memset(sons, 0, sizeof(sons));
}

Word_Node Word_Tree::insert_to_tree(Word_Node* root, std::string us, std::string uk)
{
	Word_Node *current_node = new Word_Node(us, uk);
	if (root == nullptr) {
		std::cout << "inserting root" << std::endl;
	}
	for (int i = 0; i < 26; i++) {
		if (current_node)
	}
	// {
	// 	int index = LETTER_TO_INDEX(uk[i]);

	// 	if (current_node->sons[index] == NULL)
	// 	{
	// 		current_node->sons[index] = new uk_to_us_node();
	// 	}

	// 	current_node = current_node->sons[index];
	// }

	// current_node->us = us;
	// current_node->uk = uk;
}

int main()
{
	std::ifstream us_words("us_words.txt", std::ios::in);
	std::ifstream uk_words("uk_words.txt", std::ios::in);

	std::string us_word;
	std::string uk_word;

	while (us_words >> us_word && uk_words >> uk_word) {
		insert_to_tree(us_word, uk_word);
	}
}