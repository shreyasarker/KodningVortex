package L6;

// Base class 'Shape' to demonstrate method overriding and overloading
class Shape {

    // Overloaded method: calculates area of a circle given the radius (1 parameter)
    double calculateArea(double radius) {
        return Math.PI * radius * radius; // Area of a circle: π * r^2
    }

    // Overloaded method: calculates area of a rectangle given length and width (2
    // parameters)
    double calculateArea(double length, double width) {
        return length * width; // Area of rectangle: length * width
    }

    // Method that will be overridden by subclass
    void displayShapeInfo() {
        System.out.println("This is a generic shape.");
    }
}

// Subclass 'Circle' that extends 'Shape' and overrides displayShapeInfo method
class Circle extends Shape {

    // Overriding method: providing specific implementation for Circle
    @Override
    void displayShapeInfo() {
        System.out.println("This is a circle.");
    }

    // Overloading the 'calculateArea' method to show usage of both overloaded
    // versions
    double calculateArea(double radius, double height) {
        // For demonstration, let's calculate the area of a cylinder (π * r^2 * h)
        return Math.PI * radius * radius * height;
    }
}

public class ACPTestLearning {
    public static void main(String[] args) {
        // Create a Shape object and use the overloaded methods
        Shape shape = new Shape();
        System.out.println("Area of circle with radius 5: " + shape.calculateArea(5)); // Calls the circle method
        System.out.println("Area of rectangle with length 5 and width 10: " + shape.calculateArea(5, 10)); // Calls the
                                                                                                           // rectangle
                                                                                                           // method

        // Create a Circle object and use the overridden and overloaded methods
        Circle circle = new Circle();
        circle.displayShapeInfo(); // Calls the overridden method in Circle class
        System.out.println("Area of cylinder with radius 5 and height 10: " + circle.calculateArea(5, 10));
    }
}
