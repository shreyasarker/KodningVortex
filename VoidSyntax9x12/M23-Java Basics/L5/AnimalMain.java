package L5;

// Base class: Animal
class Animal {
    String name;

    Animal(String name) {
        this.name = name;
    }

    void makeSound() {
        System.out.println(name + " makes a sound");
    }
}

// Derived class: Mammal (inherits from Animal)
class Mammal extends Animal {
    boolean hasFur;

    Mammal(String name, boolean hasFur) {
        super(name); // Calls Animal class constructor
        this.hasFur = hasFur;
    }

    void displayMammalInfo() {
        System.out.println(name + " is a mammal.");
        System.out.println("Has fur: " + hasFur);
    }
}

// Derived class: Dog (inherits from Mammal)
class Dog extends Mammal {
    String breed;

    Dog(String name, boolean hasFur, String breed) {
        super(name, hasFur); // Calls Mammal class constructor
        this.breed = breed;
    }

    void displayDogInfo() {
        displayMammalInfo();
        System.out.println(name + " is a " + breed + " dog.");
        makeSound();
    }

    // Overriding makeSound method to provide specific sound for Dog
    @Override
    void makeSound() {
        System.out.println(name + " barks!");
    }
}

public class AnimalMain {
    public static void main(String[] args) {
        // Create a Dog object (which inherits from Animal and Mammal)
        Dog dog1 = new Dog("Buddy", true, "Golden Retriever");

        dog1.displayDogInfo();
    }
}
