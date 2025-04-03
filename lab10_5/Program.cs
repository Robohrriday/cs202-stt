public class Calculator
{
    private double number1;
    private double number2;

    public Calculator(double num1, double num2)
    {
        number1 = num1;
        number2 = num2;
    }

    public double Add()
    {
        return number1 + number2;
    }

    public double Subtract()
    {
        return number1 - number2;
    }

    public double Multiply()
    {
        return number1 * number2;
    }

    //public double? Divide()
    //{
    //    if (number2 == 0)
    //        return null;
    //    else
    //        return number1 / number2;
    //}

    public double? Divide()
    {
        try
        {
            if (number2 == 0)
            {
                throw new DivideByZeroException();
            }
            return number1 / number2;
        }
        catch (DivideByZeroException)
        {
            return null;
        }
    }

    public string CheckSumEvenOdd()
    {
        double sum = Add();
        if (Math.Abs(sum - Math.Round(sum)) < 1e-9)
        {
            int intSum = (int)Math.Round(sum);
            if (intSum % 2 == 0)
                return "The sum is even.";
            else
                return "The sum is odd.";
        }
        else
        {
            return "The sum is not an integer.";
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Enter the first number:");
        string? input1 = Console.ReadLine();
        if (!double.TryParse(input1, out double num1))
        {
            Console.WriteLine("Invalid input for first number.");
            return;
        }

        Console.WriteLine("Enter the second number:");
        string? input2 = Console.ReadLine();
        if (!double.TryParse(input2, out double num2))
        {
            Console.WriteLine("Invalid input for second number.");
            return;
        }

        Calculator calc = new Calculator(num1, num2);

        double sum = calc.Add();
        Console.WriteLine($"Sum: {sum}");

        double difference = calc.Subtract();
        Console.WriteLine($"Difference: {difference}");

        double product = calc.Multiply();
        Console.WriteLine($"Product: {product}");

        double? quotient = calc.Divide();
        if (quotient.HasValue)
            Console.WriteLine($"Quotient: {quotient.Value}");
        else
            Console.WriteLine("Cannot divide by zero");

            Console.WriteLine(calc.CheckSumEvenOdd());
    }
}
