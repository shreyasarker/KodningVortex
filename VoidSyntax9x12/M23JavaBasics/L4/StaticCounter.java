package VoidSyntax9x12.M23JavaBasics.L4;

public class StaticCounter {

    int number = 10;
    static int number2 = 10;

    void increment() {
        number = number + 1;
        number2 = number2 + 1;
    }

    public static void main(String[] args) {
        StaticCounter obj1 = new StaticCounter();
        StaticCounter obj2 = new StaticCounter();
        StaticCounter obj3 = new StaticCounter();
        obj1.increment();
        obj2.increment();
        obj3.increment();

        System.out.println(obj1.number);
        System.out.println(StaticCounter.number2);
        System.out.println(obj2.number);
        System.out.println(StaticCounter.number2);
        System.out.println(obj3.number);
        System.out.println(StaticCounter.number2);

    }
}
