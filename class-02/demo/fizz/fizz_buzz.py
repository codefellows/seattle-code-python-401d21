# fizz buzz problem domain
# if number divisible by 3 return fizz
# if number divisible by 5 return buzz
# if number divisible by both return fizzbuzz
# if not divisible by either return the number

def fizz_buzz(num):
    # Handle 3 or Fizz
    if num % 15 == 0:
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    return num
