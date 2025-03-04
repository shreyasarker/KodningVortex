package VoidSyntax9x12.M23JavaBasics.L6;

// Class representing a Student
class Student {
    int id;
    String name;
    float stipend;

    // Default constructor (no parameters)
    Student() {
        this.id = 101;
        this.name = "Default Student";
        this.stipend = 5000.0f;
    }

    // Constructor with 2 parameters
    Student(int id, String name) {
        this.id = id;
        this.name = name;
        this.stipend = 7000.0f; // Assigning a new default stipend
    }

    // Constructor with 3 parameters
    Student(int id, String name, float stipend) {
        this.id = id;
        this.name = name;
        this.stipend = stipend;
    }

    // Method to display student details
    void displayDetails() {
        System.out.println("ID: " + this.id + " | Name: " + this.name + " | Stipend: " + this.stipend);
    }
}

// Main class to test the Student class
public class MOverloading {
    public static void main(String[] args) {
        // Creating student objects using different constructors
        Student st1 = new Student(); // Calls the default constructor
        Student st2 = new Student(78, "Riya"); // Calls the constructor with 2 parameters
        Student st3 = new Student(305, "Daniel", 12000.50f); // Calls the constructor with 3 parameters

        // Displaying student details
        st1.displayDetails();
        st2.displayDetails();
        st3.displayDetails();
    }
}
