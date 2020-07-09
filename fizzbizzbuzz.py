def FizzBuzz (start, stop):
    if type (start)!= int and type (stop) != int :
        print ("not an interger") 
    
    for fizzbuzz in range(start,stop):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
           print("FizzBuzz")
           continue
        elif fizzbuzz % 3 == 0:
           print("Fizz")
           continue
        elif fizzbuzz % 5 == 0:
           print("Buzz")
           continue
        print(fizzbuzz)
FizzBuzz("3000","7000")



