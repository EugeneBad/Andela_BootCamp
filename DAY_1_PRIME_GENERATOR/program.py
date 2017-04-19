def prime_list(number):
    if type(number) is not int:
        raise TypeError('Please pass only integers to the function')

    else:
        if number <= 0:
            raise ValueError('Please pass values greater than zero')
        elif number == 1:
            return [1]
        elif number == 2:
            return [1, 2]
        elif number > 2:
            list_of_primes = [1, 2]

            for digit in range(3, number+1):
                non_factor_counter = 0
                for checker in range(2, digit):
                    if digit % checker != 0:
                        non_factor_counter += 1
                if non_factor_counter == digit-2:
                    list_of_primes.append(digit)
            return list_of_primes
