#include <iostream>
#include <stack>
using namespace std;
class Node{
	int data;
	Node *left;
	Node *right;
	public:
	Node(){
		data = 0;
		left = NULL;
		right = NULL;
	}
	friend class BST;	
};
class BST{
	Node *root;
	public:
	BST(){
		root = new Node();
	}
	void createBST(){
		cout<<"Enter the root data\n";		
		cin>>root->data;
		int choice = 0;
		cout<<"Do u want to enter more nodes\n";
		cout<<"1 : Yes 2 : No\n";
		cin>>choice;
		while(choice==1){
			choice = 0;
			Node *temp = root;
			Node *newNode = new Node();
			cout<<"Enter data for new Node\n";
			cin>>newNode->data;
			Node *prev = NULL;
			while(temp!=NULL){
				prev = temp;		
				if(temp->data >= newNode->data){
					temp = temp->left;
				}
				else{
					temp = temp->right;
				}
			}
			if(prev->data >= newNode->data)
				prev->left = newNode;
			else
				prev->right = newNode;
			cout<<"Do u want to enter more nodes\n";
			cout<<"1 : Yes 2 : No\n";
			cin>>choice;
		}	
	}
	void displayInorder(){
		stack<Node*> st;
		Node *temp = root;
		cout<<"Inorder traversal of BST is\n";
		while(true){
			while(temp!=NULL){
				st.push(temp);
				temp = temp->left;
			}
			if(st.empty()!=true && temp==NULL){
				temp = st.top();
				st.pop();
				cout<<temp->data<<"\n";
				temp = temp->right;
			}
			else{
				break;
			}
		}
	}
};
int main(){
	BST bst;	
	bst.createBST();
	bst.displayInorder();
	return 0;
}
