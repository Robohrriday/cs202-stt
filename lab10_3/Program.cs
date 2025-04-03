public class LoopAndFunctionDemo
{
    public void PrintNumbersWithForLoop()
    {
        for (int i = 1; i <= 10; i++)
        {
            Console.WriteLine(i);
        }
    }

    public void AskUserUntilExit()
    {
        string? input;
        do
        {
            Console.WriteLine("Enter something (type 'exit' to stop):");
            input = Console.ReadLine();
            if (input != null && input.ToLower() != "exit")
            {
                Console.WriteLine($"You entered: {input}");
            }
        } while (input != null && input.ToLower() != "exit");
    }

    // Method to calculate factorial of a given number
    public long CalculateFactorial(int number)
    {
        if (number < 0)
        {
            throw new ArgumentException("Factorial is not defined for negative numbers.");
        }
        long factorial = 1;
        for (int i = 1; i <= number; i++)
        {
            factorial *= i;
        }
        return factorial;
    }
}

class Program
{
    static void Main(string[] args)
    {
        LoopAndFunctionDemo demo = new LoopAndFunctionDemo();

        Console.WriteLine("Printing numbers from 1 to 10:");
        demo.PrintNumbersWithForLoop();

        Console.WriteLine("\nStarting user input loop (type 'exit' to proceed to factorial calculation):");
        demo.AskUserUntilExit();

        Console.WriteLine("\nEnter a non-negative integer to calculate its factorial:");
        string? input = Console.ReadLine();
        if (input != null && int.TryParse(input, out int number) && number >= 0)
        {
            try
            {
                long factorial = demo.CalculateFactorial(number);
                Console.WriteLine($"The factorial of {number} is {factorial}.");
            }
            catch (ArgumentException ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
        else
        {
            Console.WriteLine("Invalid input. Please enter a non-negative integer.");
        }
    }
}
