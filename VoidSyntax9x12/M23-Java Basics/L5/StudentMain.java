package L5;

// Base class: Person
class Person {
    String name;
    int age;

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    void displayPersonDetails() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
}

// Derived class: Student (inherits from Person)
class Student extends Person {
    int rollNumber;
    String grade;

    Student(String name, int age, int rollNumber, String grade) {
        super(name, age);
        this.rollNumber = rollNumber;
        this.grade = grade;
    }

    void displayStudentDetails() {
        displayPersonDetails();
        System.out.println("Roll Number: " + rollNumber);
        System.out.println("Grade: " + grade);
    }
}

public class StudentMain {
    public static void main(String[] args) {
        Student student1 = new Student("John Doe", 20, 101, "A");

        student1.displayStudentDetails();
    }
}
