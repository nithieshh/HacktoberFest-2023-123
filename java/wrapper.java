import java.util.*;

public class WrapperClass {
   public static void main(String[] args) {
      WrapperClass x = new WrapperClass();
      WrapperClass b = new WrapperClass();
      x = null;
      b = null;
      new WrapperClass();
      System.gc();  // Requesting Garbage Collection
   }

   @Override
   protected void finalize() {
      System.out.print("this is GC ");
   }
}
