#include <iostream>
using namespace std;

int * apply_all(int *array1, int array1_size, int *array2, int array2_size){
	 int arrys_sizes = array1_size * array2_size;
	 int *new_arry;
	 new_arry = new int[arrys_sizes];
	 
	 int index =0;
	 
	 for (int i = 0; i< array2_size; i++){
		 for(int j = 0; j< array1_size; j++) {
			 new_arry[index] = array2[i]*array1[j];
			 index++;
		 }
	 }
	 return new_arry;
}

void print(int *ary, int array_size) {
	cout << "[ ";
	for (int i =0; i< array_size; i++ ){
		cout << ary[i] << " ";
	}
	cout << "]" << endl;
}

int main() {
    const size_t array1_size {5};
    const size_t array2_size {3};
    
    int array1[] {1,2,3,4,5};
    int array2[] {10,20,30};
    
    cout << "Array 1: " ;
    print(array1,array1_size);
    
    cout << "Array 2: " ;
    print(array2,array2_size);
    
    int *results = apply_all(array1, array1_size, array2, array2_size);
    constexpr size_t results_size {array1_size * array2_size};

    cout << "Result: " ;
    print(results, results_size);
    
    cout << endl;

    return 0;
}
