package L5;

public class AgeMain {

    int age;

    AgeMain(int age) {
        age = age;
        // this.age = age;
    }

    public static void main(String[] args) {
        AgeMain obj = new AgeMain(24);
        System.out.println("obj.age = " + obj.age);
    }
}