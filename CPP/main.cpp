#include <iostream>
#include "heap.cpp"

int main(int argc, char **argv){
    std::cout << "Hello World!!" << std::endl;
    Heap* myHeap = new Heap();
    int retVal = myHeap->createHeap();
    std::cout << retVal << std::endl;
    return 0;
}

