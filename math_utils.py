import math
class MathUtils:
  """
  Class that implements mathematical operations.
  """

  @staticmethod
  def add(a: int | float, b: int | float) -> int | float:
    """
    Just adds two numbers together.
    """
    return a + b

  @staticmethod
  def subtract(a: int | float, b: int | float) -> int | float:
    """
    Just subtracts two numbers.
    """
    return a - b

  @staticmethod
  def divide(a: int | float, b: int | float) -> float:
    """
    Just divides two numbers.
    """
    if b == 0:
      raise ValueError("You cannot divide by zero!")
    return a / b

  @staticmethod
  def multiply(a: int | float, b: int | float) -> int | float:

    return a * b

  @staticmethod
  def power(a: int | float, b: int | float) -> int | float:

    return a ** b

  @staticmethod
  def sqrt(a: int | float) -> float:

    if a < 0:
      raise ValueError("Cannot the square root of a negative number!")
    return math.sqrt(a)

  @staticmethod
  def absolute(a: int | float) -> int | float:

    return abs(a)