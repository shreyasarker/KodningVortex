package L6;

class Parent {
    // Protected method: Can be accessed within this class, by subclasses, and
    // within the same package
    protected void protect() {
        System.out.println("I'm inside protected method");
    }
}

class Child extends Parent {
    // Private method: Only accessible within this class
    private void privateMethod() {
        System.out.println("I'm inside private method");
    }

    // Public method to demonstrate calling privateMethod from within the class
    public void callPrivateMethod() {
        privateMethod(); // This works because it's within the same class
    }
}

public class AccessMain {
    public static void main(String[] args) {
        // Creating an object of the Child class
        Child kid = new Child();

        // Calling the protected method from the Parent class using the Child object
        kid.protect(); // This works because 'protect' is inherited by 'Child'

        // Calling the public method of 'Child' to indirectly call the private method
        kid.callPrivateMethod(); // This works because 'privateMethod' is accessible within 'Child'

        System.out.println("Hello world!");
    }
}
