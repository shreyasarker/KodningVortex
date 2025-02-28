package L4;

// Employee class
class Employee {
    String name;
    int age;
    String position;
    double salary;

    Employee(String name, int age, String position, double salary) {
        this.name = name;
        this.age = age;
        this.position = position;
        this.salary = salary;
    }

    void displayDetails() {
        System.out.println("Employee Details:");
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Position: " + position);
        System.out.println("Salary: " + salary);
        System.out.println(); // To separate different employee details
    }
}

public class EmployeeMain {
    public static void main(String[] args) {
        Employee employee1 = new Employee("John Doe", 30, "Software Engineer", 80000.0);
        Employee employee2 = new Employee("Alice Smith", 28, "HR Manager", 60000.0);
        Employee employee3 = new Employee("Bob Johnson", 35, "Product Manager", 90000.0);

        employee1.displayDetails();
        employee2.displayDetails();
        employee3.displayDetails();
    }
}
