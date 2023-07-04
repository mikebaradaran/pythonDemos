

public class Employee
{
    public double Salary { get; set; }
    public int Age { get; set; }
    public List<Skill> Skills { get; set; }

    public Employee(double salary, int age, List<Skill> skills) {
        this.ID = id;
        this.Salary = salary; // ...
    }
}

public class HR
{
    public bool makePayment(Employee emp, double money)
    {
        PaymentSystem paymentSystem = new PaymentSystem();
        return paymentSystem.Pay(emp.ID, money);
    }
}