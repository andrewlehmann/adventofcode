package Day1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.Scanner;

public class Day1 {

    public static void main(String[] args) throws FileNotFoundException {
        List<Integer> inputs = new ArrayList<>();

        try (Scanner s = new Scanner(new File("./src/Day1/input.txt"))) {

            while (s.hasNext()) {
                inputs.add(Integer.parseInt(s.next()));
            }

            s.close();
        }

        int result = getFinalResult(inputs);

        System.out.println("result: " + result);
    }

    public static int getFinalResult(List<Integer> theInputs) {
        for (int i = 0; i < theInputs.size(); i++) {
            int current = theInputs.get(i);

            Optional<Integer> productOfOtherTwo = solve(theInputs, 2020 - current);

            if (productOfOtherTwo.isPresent()) {
                return productOfOtherTwo.get() * current;
            }
        }

        return -1;
    }

    /**
     * Get the product of the 2 numbers that add up to targetSum (if present), else Optional.empty()
     */
    public static Optional<Integer> solve(List<Integer> theInputs, int targetSum) {
        for (int i = 0; i < theInputs.size(); i++) {
            int current = theInputs.get(i);
            int remainingValue = targetSum - current;

            if (theInputs.stream().anyMatch(e -> e == remainingValue)) {
                return Optional.of(current * remainingValue);
            }
        }

        return Optional.empty();
    }
}
