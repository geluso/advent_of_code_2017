package dayseven;

public class Main {
    public static void main(String[] args) {
                //{0,2,7,0};
        Integer[] banks = {2,8,8,5,4,2,3,1,5,5,1,2,15,13,5,14};
        MemoryBank bank1 = new MemoryBank(banks);

        while (bank1.cycle()) {}
    }
}
