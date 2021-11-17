#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <math.h>
#include <time.h>

long thread_count;
long long n;
double sum;
pthread_mutex_t mutex;

double factorial(double num);
void* pthreadE(void* thread);

int main(int argc, char* argv[])
{

	clock_t start, stop;
	double elapsed;

	if (argc != 2)
	{
		printf("usage: %s <number of threads>\n", argv[0]);
		exit(0);
	}

	long thread;
	pthread_t* thread_handles;
	thread_count = strtol(argv[1], NULL, 10);
	thread_handles = malloc(thread_count * sizeof(pthread_t));
	
	//retrieve n from user
	printf("Enter value for n\n");
	scanf("%lld", &n);

	if (n % thread_count != 0)
	{
		printf("n must be evenly divisible by number of threads\nExiting...\n");
		exit(0);
	}
	

	//calculate block
	start = clock();
	pthread_mutex_init(&mutex, NULL);
	for (thread = 0; thread < thread_count; thread++)
	{
		pthread_create(&thread_handles[thread], NULL, pthreadE, (void*) thread);
	}
	for (thread = 0; thread < thread_count; thread++)
	{
		pthread_join(thread_handles[thread], NULL);
	}
	pthread_mutex_destroy(&mutex);
	stop = clock();

	elapsed = ((double)(stop - start)) / CLOCKS_PER_SEC;
	
	//print out sum
	printf("Time to complete %lld terms with %ld processes was %lf seconds.\n", n, thread_count, elapsed);
	printf("e = %0.15lf\n", sum); 

	return 0;
}

//calculate factorial of long 
double factorial(double num)
{
	if (num == 0)
	{
		return 1;
	}
	else
	{
		return num * factorial(num - 1);
	}
}

void* pthreadE(void* thread)
{
	long rank = (long) thread;
	long long local_size = n / thread_count;
	long long local_start = local_size * rank;
	long long local_end = local_start + local_size;
	double local_sum = 0.0;

	for (long long i = local_start; i < local_end; i++)
	{
		local_sum += 1.0 / factorial((double)i);
		printf("local sum is %0.15lf for process %ld\n", local_sum, rank);	
	}
	
	pthread_mutex_lock(&mutex);
	sum += local_sum;
	pthread_mutex_unlock(&mutex);
}
