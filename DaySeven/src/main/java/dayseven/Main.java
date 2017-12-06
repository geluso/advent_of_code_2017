package dayseven;

public class Main {
    public static void main(String[] args) {
                //{0,2,7,0};
        Integer[] banks = {2,8,8,5,4,2,3,1,5,5,1,2,15,13,5,14};
        MemoryBank bank1 = new MemoryBank(banks);

        // guessed 3154
        ////grep "0, 13, 12, 10, 9, 8, 7, 5, 3, 2, 1, 1, 1, 10, 6, 5" ~/Desktop/cycles
        //cycle: 1546 state: [0, 13, 12, 10, 9, 8, 7, 5, 3, 2, 1, 1, 1, 10, 6, 5]
        //cycle: 3156 state: [0, 13, 12, 10, 9, 8, 7, 5, 3, 2, 1, 1, 1, 10, 6, 5]
        while (bank1.cycle() == 0) {}
    }
}
