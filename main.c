
#include <stdio.h>
#include <gmp.h>


void factorial(int n, mpz_t factorial);

int main()
{
    int n = 20000;
    mpz_t fact;
    mpz_init(fact);

    factorial(n, fact);
    printf("Hello, World!\n");
    printf("n: %d, factorial: ", n);
    mpz_out_str(stdout, 10, fact);
    return 0;
}




void factorial(int n, mpz_t factorial)
{
    mpz_set_ui(factorial, 1);
    for (int i = 1; i <= n; i++)
    {
        mpz_mul_ui(factorial, factorial, i);
    }
}