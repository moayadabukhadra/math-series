from math_series.series import fibonacci,locas,sum_series
def test_fibonacci_one():
  expected = 0 
  n = 0 
  actual = fibonacci(n)
  assert actual == expected

  
def test_fibonacci_two():
  expected = 3 
  n = 5 
  actual = fibonacci(n)
  assert actual == expected
  
def test_locas_one():
  expected = 2 
  n =  0 
  actual = locas(n) 
  assert actual == expected 

  
def test_locas_two():
  expected = 7 
  n =  5 
  actual = locas(n) 
  assert actual == expected
  
  
def test_sum_one():
  expected = 34
  n = 10 
  actual = sum_series(n)
  assert actual == expected
  
def test_sum_series_two():
  expected = 7 
  n = 5 
  x = 2 
  y = 1 
  actual = sum_series(n, x, y)
  assert actual == expected
  
def test_sum_series_3rd():
  expected =  241
  n = 10 
  x = 5 
  y = 4 
  actual = sum_series(n, x, y)
  assert actual == expected