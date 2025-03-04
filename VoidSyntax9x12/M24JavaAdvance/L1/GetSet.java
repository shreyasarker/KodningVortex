package VoidSyntax9x12.M24JavaAdvance.L1;

// Class with encapsulated fields
class Student {
    // Private field
    private String name;

    // Setter method to set the value of the private variable
    public void setName(String name) {
        this.name = name;
    }

    // Getter method to get the value of the private variable
    public String getName() {
        return this.name;
    }
}

public class GetSet {
    public static void main(String[] args) {
        // Creating an object of the Student class
        Student student = new Student();

        // Using setter method to set the value of the private variable 'name'
        student.setName("John Doe");

        // Using getter method to retrieve the value of the private variable 'name'
        System.out.println("Student Name: " + student.getName());
    }
}
