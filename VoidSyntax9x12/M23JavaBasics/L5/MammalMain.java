package VoidSyntax9x12.M23JavaBasics.L5;

// Parent class
class Mammals {
    void mam() {
        System.out.println("Inside Mammals Class");
    }
}

// Child class 1
class Lion extends Mammals {
    void roar() {
        System.out.println("Inside Lion class");
    }
}

// Child class 2
class Human extends Mammals {
    void hum() {
        System.out.println("Inside Human");
    }
}

public class MammalMain {
    public static void main(String args[]) {
        Lion obj1 = new Lion(); // object of Lion class
        obj1.roar(); // This will work
        obj1.mam(); // This will work

        Human obj2 = new Human(); // object of Human class
        obj2.hum(); // This will work
        obj2.mam(); // This will work
    }
}
