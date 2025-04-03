public class Student
{
    public string Name { get; set; }
    public int ID { get; set; }
    public double Marks { get; set; }


    public Student(string name, int id, double marks)
    {
        Name = name;
        ID = id;
        Marks = marks;
    }

    public Student(Student other)
    {
        Name = other.Name;
        ID = other.ID;
        Marks = other.Marks;
    }

    public Student() : this("Unknown", 0, 0.0) { }


    public string GetGrade()
    {
        if (Marks >= 90)
            return "A";
        else if (Marks >= 80)
            return "B";
        else if (Marks >= 70)
            return "C";
        else if (Marks >= 60)
            return "D";
        else
            return "F";
    }

    //public static void Main(string[] args)
    //{

    //    Student student1 = new Student("Alice", 101, 85.5);
    //    Console.WriteLine("Student Details:");
    //    Console.WriteLine($"Name: {student1.Name}, ID: {student1.ID}, Marks: {student1.Marks}, Grade: {student1.GetGrade()}");

    //    Student student2 = new Student(student1);
    //    student2.Name = "Bob";
    //    Console.WriteLine("\nCopied and Modified Student Details:");
    //    Console.WriteLine($"Name: {student2.Name}, ID: {student2.ID}, Marks: {student2.Marks}, Grade: {student2.GetGrade()}");


    //    Student student3 = new Student();
    //    Console.WriteLine("\nDefault Student Details:");
    //    Console.WriteLine($"Name: {student3.Name}, ID: {student3.ID}, Marks: {student3.Marks}, Grade: {student3.GetGrade()}");
    //}
}

public class StudentIITGN : Student
{
    public string Hostel_Name_IITGN { get; set; }

    public StudentIITGN(string name, int id, double marks, string hostelName)
        : base(name, id, marks)
    {
        Hostel_Name_IITGN = hostelName;
    }

    public static void Main(string[] args)
    {
        StudentIITGN iitgnStudent = new StudentIITGN("Charlie", 202, 92.0, "Hostel A");
        Console.WriteLine("IITGN Student Details:");
        Console.WriteLine($"Name: {iitgnStudent.Name}, ID: {iitgnStudent.ID}, Marks: {iitgnStudent.Marks}, Grade: {iitgnStudent.GetGrade()}, Hostel: {iitgnStudent.Hostel_Name_IITGN}");
    }
}