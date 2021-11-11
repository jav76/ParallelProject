#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

double factorial(double num);

int main(int argc, char* argv[])
{
	int thread_count;
	long long n;
	double sum;
	
	double start, stop, elapsed;

	if (argc != 2)
	{
		printf("usage: %s <number of threads>\n", argv[0]);
		exit(0);
	}

	thread_count = strtol(argv[1], NULL, 10);
	
	//retrieve n from user
	printf("Enter value for n\n");
	scanf("%lld", &n);
	
	//omp parallel code
	start = omp_get_wtime();
#  pragma omp parallel for num_threads(thread_count) \
      reduction(+: sum)
	for (long long i = 0; i < n; i++)
	{
		sum += 1.0 / factorial((double)i);
		//printf("sum is %0.15lf from process %ld calculation\n", sum, rank);	
	}
	stop = omp_get_wtime();

	elapsed = stop - start;
	
	//print out sum
	printf("Time to complete %lld terms with %d processes was %lf seconds.\n", n, thread_count, elapsed);
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
