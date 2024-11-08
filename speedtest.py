import timeit
import main

number = 9
n = 100

result = timeit.timeit(stmt='main.iseven_modulo(number)', globals=globals(), number=n)
print(f"iseven_modulo: {result / n} seconds")

result = timeit.timeit(stmt='main.iseven_binary(number)', globals=globals(), number=n)
print(f"iseven_binary: {result / n} seconds")

result = timeit.timeit(stmt='main.iseven_intdev(number)', globals=globals(), number=n)
print(f"iseven_intdev: {result / n} seconds")

result = timeit.timeit(stmt='main.iseven_count(number)', globals=globals(), number=n)
print(f"iseven_count: {result / n} seconds")

result = timeit.timeit(stmt='main.iseven_string(number)', globals=globals(), number=n)
print(f"iseven_string: {result / n} seconds")

result = timeit.timeit(stmt='main.iseven_round(number)', globals=globals(), number=n)
print(f"iseven_round: {result / n} seconds")

result = timeit.timeit(stmt='main.iseven_addition(number)', globals=globals(), number=n)
print(f"iseven_addition: {result / n} seconds")

result = timeit.timeit(stmt='main.iseven_recursive(number)', globals=globals(), number=n)
print(f"iseven_recursive: {result / n} seconds")

result = timeit.timeit(stmt='main.iseven_lookup(number)', globals=globals(), number=n)
print(f"iseven_lookup: {result / n} seconds")

result = timeit.timeit(stmt='main.iseven_isint(number)', globals=globals(), number=n)
print(f"iseven_isint: {result / n} seconds")