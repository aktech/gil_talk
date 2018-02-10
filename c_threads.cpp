#include <ctime>
#include <iostream>
#include <chrono>
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
using namespace std;

void *task(void *n_) {
    long long int n = *((long long int*)n_);
    for (long long int i = 0; i <= n; i++) {}
}


int main (int argc, char ** argv) {
    long long int N = 100000000;
    long long int *arg = (long long int *)malloc(sizeof(*arg));
    std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
    *arg = N;
    *task(arg);
    std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
    cout << "Elapsed time with 1 thread:  " << std::chrono::duration_cast<std::chrono::milliseconds>(end - begin).count() / 1000.0 <<std::endl;

    pthread_t thread1, thread2;
    int i1, i2;
    *arg = N/2;
    begin = std::chrono::steady_clock::now();

    i1 = pthread_create(&thread1, NULL, task, arg);
    i2 = pthread_create(&thread2, NULL, task, arg);

    pthread_join(thread1,NULL);
    pthread_join(thread2,NULL);

    end = std::chrono::steady_clock::now();;
    cout << "Elapsed time with 2 threads: " << std::chrono::duration_cast<std::chrono::milliseconds>(end - begin).count() / 1000.0 <<std::endl;
    return 0;
}

