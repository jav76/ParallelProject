#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>
#include <math.h>

double factorial(double num);

int main(void)
{
	int size, rank;
	int n, local_n, block_start, block_end;
	double local_sum = 0.0;
	double sum = 0.0;

	double local_start, local_stop, local_elapsed, elapsed;

  	MPI_Comm comm = MPI_COMM_WORLD;
  	MPI_Init(NULL, NULL);
  	MPI_Comm_size(comm, &size);
   	MPI_Comm_rank(comm, &rank);
	
	//retrieve n from user
	if (rank == 0)
	{
		printf("Enter value for n\n");
		scanf("%d", &n);
	}

	//broadcast n
	MPI_Bcast(&n, 1, MPI_INT, 0, comm);
	
	local_start = MPI_Wtime();

	//calculate block
	for (long long i = rank; i < n; i += size)
	{	
		local_sum += 1.0 / factorial((double)i);
#		ifdef DEBUG
		printf("local sum is %0.15lf for process %d on index [%lld]\n", local_sum, rank, i);
#		endif
	}

	local_stop = MPI_Wtime();

	local_elapsed = local_stop - local_start;
#	ifdef DEBUG
	printf("%lfs is local elapsed time for rank %d\n", local_elapsed, rank);
#	endif

	//get the longest time taken of all the processes
	MPI_Reduce(&local_elapsed, &elapsed, 1, MPI_DOUBLE, MPI_MAX, 0, comm);

	
	//add sums together with reduce
	MPI_Reduce(&local_sum, &sum, 1, MPI_DOUBLE, MPI_SUM, 0, comm);
	
	//print out sum
	if (rank == 0)
	{ 
		printf("Time to complete %d terms with %d processes was %lf seconds.\n", n, size, elapsed);
		printf("e = %lf\n", sum); 
	}
	MPI_Finalize();
	return 0;
}

//calculate factorial of double
double factorial(double num)
{
	if (num == 0.0)
	{
		return 1.0;
	}
	else
	{
		return num * factorial(num - 1.0);
	}
}
