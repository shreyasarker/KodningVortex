package L6;

// Superclass
class Superclass {
    int number = 56; // Variable in the superclass
}

// Subclass (Child class)
class Subclass extends Superclass {
    // Variable with the same name as in the superclass (hiding the superclass
    // variable)
    int number = 96;

    // Method to print the value of number
    void printNumber() {
        System.out.println("Value in Subclass: " + number); // Refers to the subclass variable
        System.out.println("Value in Superclass: " + super.number); // Accessing superclass variable using super
    }
}

// Main class
class SuperMain {
    public static void main(String args[]) {
        Subclass sub = new Subclass();
        sub.printNumber(); // Calling the method to print both values
    }
}
