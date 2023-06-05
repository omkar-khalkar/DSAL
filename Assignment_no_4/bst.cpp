/*
Beginning with an empty binary search tree, Construct binary search tree by inserting the values in the order given.
 After constructing a binary tree -
i. Insert new node,
 ii. Find number of nodes in longest path from root, 
 iii. Minimum data value found in the tree, 
 iv. Change a tree so that the roles of the left and right pointers are swapped at every node,
  v. Search a value
  
*/

#include<iostream>
using namespace std;

struct node{
	node* left=NULL;
	node* right=NULL;
	int data;
};

class bt{
	public:
	bool flag;
	node* root=NULL;
	void add();
	void insert(node*root,node*n);
	void display(node* root);
	void minMax(node * root);
	void mirror(node*root);
	void search(node *root,int key);
	void check(bool flag);
};

void bt::add(){
	node *n=new node();
	cout<<"Enter: ";
	cin>>n->data;
	
	if(root==NULL){
		root=n;
	}
	else{
		insert(root,n);
	}
}

void bt::insert(node* root,node *n){
	if(n->data < root->data){
		if(root->left==NULL){
			root->left=n;
			//cout<<"left of "<<root->data<<endl;
		}
		else{
			insert(root->left,n);
		}
	}
	if(n->data > root->data){
		if(root->right==NULL){
			root->right=n;
			//cout<<"right of "<<root->data<<endl;
		}
		else{
			insert(root->right,n);
		}
	}
	
}

void bt::display(node* root){
	if(root!=NULL){
		display(root->left);
		cout<<root->data<<" ";
		display(root->right);
	}
	
}

void bt::minMax(node * root){
	node * temp;
	temp=root;
	

	while(temp->left!=NULL){
		temp=temp->left;
	}
	cout<<"minimum is: "<<temp->data<<endl;
	temp=root;
	while(temp->right!=NULL){
		temp=temp->right;
	}
	cout<<"maximum is: "<<temp->data<<endl;
		
}

void bt::mirror(node * root){
	if(root!=NULL){
	node*temp;
	temp=root->left;
	root->left=root->right;
	root->right=temp;
	mirror(root->left);
	mirror(root->right);
	}
}	

void bt::search(node *root,int key){
	
	flag=false;
	if(root!=NULL){
		if(key==root->data){
			
			flag=true;
			return ;
			
		}
		else if(key < root->data){
			search(root->left,key);
		}
		else{
			search(root->right,key);
		}
	}
	else{
		return ;
	}
	
	
}

void bt::check(bool flag){
	if(flag==true){
		
		cout<<"Element found!!\n";
	}
	else{
		cout<<"Element not found!!\n";
	}
}

int main(){
	bt b;
	int ch;
	char ctn='y';
	do{
		cout<<"1.To add\n2.To display\n3.To minMax\n4.To search\n5.To mirror\n0.To exit\n";
		cout<<"Enter your Choice : ";
		cin>>ch;
		
		switch(ch){
			case 1:
				while(ctn=='y'){
					b.add();
					cout<<"Do u want to continue: ";
					cin>>ctn;
				}
				break;
			case 2:
				b.display(b.root);
				cout<<endl;
				break;
			case 3:
				b.minMax(b.root);
				cout<<endl;
				break;
			case 4:
				int ele;
				cout<<"Enter element to be search: ";
				cin>>ele;
				b.search(b.root,ele);
				b.check(b.flag);
				cout<<endl;
				break;
			case 5:
				b.mirror(b.root);
				b.display(b.root);
				cout<<endl;
				break;
			
		}
			
				
	}
	while(ch!=0);
 

	
}