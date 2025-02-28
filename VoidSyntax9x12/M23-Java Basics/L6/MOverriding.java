package L6;

// Parent class
class Animal {
    void sound() {
        System.out.println("Animal makes a sound");
    }
}

// Child class 1
class Dog extends Animal {
    // Overriding the sound method
    @Override
    void sound() {
        System.out.println("Dog barks");
    }
}

// Child class 2
class Cat extends Animal {
    // Overriding the sound method
    @Override
    void sound() {
        System.out.println("Cat meows");
    }
}

public class MOverriding {
    public static void main(String[] args) {
        // Creating objects of child classes
        Animal myDog = new Dog();
        Animal myCat = new Cat();

        // Calling the overridden method
        myDog.sound(); // This will call Dog's sound() method
        myCat.sound(); // This will call Cat's sound() method
    }
}
