package dayseven;

import java.util.*;

public class MemoryBank {
    int cycles = 0;

    List<Integer> buckets;
    Set<String> seenStates;

    // 0, 2, 7, and 0
    public MemoryBank() {
        this.buckets = new ArrayList<>();
        this.seenStates = new HashSet<>();
    }

    public MemoryBank(Integer[] banks) {
        this();
        this.buckets.addAll(Arrays.asList(banks));
        this.seenStates.add(this.toString());
    }

    public boolean cycle() {
        this.cycles++;
        int index = indexWithMost();
        int amount = buckets.get(index);
        buckets.set(index, 0);

        while (amount > 0) {
            index = (index + 1) % buckets.size();
            amount --;
            buckets.set(index, buckets.get(index) + 1);
        }

        String repr = buckets.toString();
        System.out.println("cycle: " + this.cycles + " state: " + repr);
        if (seenStates.contains(repr)) {
           // did not complete in a unique state
           return false;
        }

        seenStates.add(repr);
        return true;
    }

    public int indexWithMost() {
        int index = 0;
        int amount = buckets.get(index);

        for (int i = 0; i < buckets.size(); i++) {
            if (buckets.get(i) > amount) {
                index = i;
                amount = buckets.get(i);
            }
        }
        return index;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (Integer s : this.buckets) {
            sb.append("" + s);
            sb.append(",");
        }

        return sb.toString();
    }
}
