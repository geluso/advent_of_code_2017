import java.io.*;
import java.util.*;

public class DayTwo {
  public static void main(String[] args) throws Exception {
    String filename = "day2_input.txt";
    Scanner scanner = new Scanner(new File(filename));

    int checksum = 0;
    while (scanner.hasNextLine()) {
      String ll = scanner.nextLine();
      System.out.println(ll);

      Scanner line = new Scanner(ll);
      List<Integer> nums = new ArrayList<>();
      while (line.hasNextInt()) {
        nums.add(line.nextInt());
      }

      checksum += findDivisibleDifference(nums);
      System.out.println();
    }

    System.out.println(checksum);
  }

  public static int findDivisibleDifference(List<Integer> nums) {
    for (int i = 0; i < nums.size(); i++) {
      for (int j = 0; j < nums.size(); j++) {
        int numerator = nums.get(i);
        int denominator = nums.get(j);
        if (i != j && numerator % denominator == 0) {
          System.out.println(numerator  + "/" + denominator + " " + (1.0 * numerator) / (1.0 * denominator));
          return numerator / denominator;
        }
      }
    }
    return 0;
  }
}
