package me.jelly.lambda;

import java.util.concurrent.TimeUnit;
import java.util.function.Supplier;

/**
 * Created by jelly on 8/5/16.
 */
public class SupplierTest {

    public static void main(String[] args) {
        final Supplier<String> helloSupplier = () -> "Hello ";

        System.out.println(helloSupplier.get() + "world");


        long start = System.currentTimeMillis();

        printIfValidIndex(0, () -> getVeryExpensiveValue());
        printIfValidIndex(0, () -> getVeryExpensiveValue());
        printIfValidIndex(0, () -> getVeryExpensiveValue());


        System.out.println("It took " + (System.currentTimeMillis() - start) / 1000 + "seconds.");
    }

    private static String getVeryExpensiveValue() {
        // Let's just say it has very expensive calculation here!
        try {
            TimeUnit.SECONDS.sleep(3);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        return "Jelly";
    }

//    private static void printIfValidIndex(int number, String value) {
        private static void printIfValidIndex(int number, Supplier<String> valueSupplier) {
        if(number >= 0) {
            System.out.println("The value is " + valueSupplier.get() + ".");
        } else {
            System.out.println("invalid");
        }
    }

}
