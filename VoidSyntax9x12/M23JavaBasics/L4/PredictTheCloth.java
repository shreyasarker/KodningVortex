package VoidSyntax9x12.M23JavaBasics.L4;

public class PredictTheCloth {
    public static void main(String[] args) {
        boolean isRaining = true;

        if (isRaining) {
            System.out.println("It is raining.");

            boolean isHeavyRain = true;
            if (isHeavyRain) {
                System.out.println("It is heavy rain. Stay indoors.");
            } else {
                System.out.println("It's just light rain. You can go out with an umbrella.");
            }
        } else {
            System.out.println("It is not raining.");

            boolean isSunny = true;
            if (isSunny) {
                System.out.println("It is sunny. Great day to go outside!");
            } else {
                System.out.println("It is cloudy. You might need a jacket.");
            }
        }
    }
}
