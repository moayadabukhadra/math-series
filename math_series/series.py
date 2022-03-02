
def fibonacci( n ):
        if n <= 1 :
                return 0
        if n == 2:

                return 1

        n_1 = fibonacci( n-1 )

        n_2 = fibonacci( n-2 )
 
        n = n_1 + n_2
 
       
        return n
 
nth_fibo = fibonacci( 3 ) 
print(nth_fibo)







def locas( n ):
        if n <= 1 :
                return 2
        if n == 2:

                return 1

        n_1 = locas( n-1 )

        n_2 = locas( n-2 )
 
        n = n_1 + n_2
 
       
        return n
 
nth_locas = locas( 3 ) 
 
print (nth_locas)





def sum_series(n,x=0,y=1):
        if n <= 1 :
                return x
        if n == 2:

                return y

        n_1 = sum_series( n-1 ,x,y)

        n_2 = sum_series( n-2 ,x ,y )
 
        n = n_1 + n_2
        
        return n


nth_sum_series = sum_series(10 , 5,4)
print(nth_sum_series)




