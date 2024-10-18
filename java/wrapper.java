import java.util.*;

public class WrapperClassExample {
    public static void main(String[] args) {
        WrapperClassExample x = new WrapperClassExample();
        WrapperClassExample b = new WrapperClassExample();
        x = null;
        b = null;

        // Request for garbage collection
        System.gc();
        
        // Adding a small delay so garbage collection has time to complete (optional)
        try {
            Thread.sleep(100);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    @Override
    protected void finalize() throws Throwable {
        System.out.println("Garbage collector called");
        super.finalize();
    }
}
