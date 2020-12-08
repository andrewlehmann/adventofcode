package Day2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Created by Drew on 12/8/2020.
 */
public class Day2 {

    private static String REGEX = "(\\d+)-(\\d+)\\s([a-z]):\\s(\\w+)";

    public static void main(String[] args) throws FileNotFoundException {
        List<String> inputs = new ArrayList<>();

        try (Scanner s = new Scanner(new File("./src/Day2/input.txt"))) {
            while (s.hasNextLine()) {
                inputs.add(s.nextLine());
            }
            s.close();
        }

        Pattern regexPattern = Pattern.compile(REGEX);

        long numOfValidEntries = inputs.stream()
            .filter(e -> validateEntryPart2(regexPattern, e))
            .count();

        System.out.println("result: " + numOfValidEntries);
    }

    private static boolean validateEntry(Pattern pattern, String entry) {
        Matcher matcher = pattern.matcher(entry);

        if (!matcher.find()) {
            return false;
        }
        // An entry must have between lowerBound and upperBound occurrences of charToCheck
        int lowerBound = Integer.parseInt(matcher.group(1));
        int upperBound = Integer.parseInt(matcher.group(2));
        char charToCheck = matcher.group(3).charAt(0);
        String thePassword = matcher.group(4);

        long count = thePassword.chars().filter(ch -> ch == charToCheck).count();

        return count >= lowerBound && count <= upperBound;
    }

    private static boolean validateEntryPart2(Pattern pattern, String entry) {
        Matcher matcher = pattern.matcher(entry);

        if (!matcher.find()) {
            return false;
        }
        // An entry must have between lowerBound and upperBound occurrences of charToCheck
        int firstPosition = Integer.parseInt(matcher.group(1)) - 1;
        int secondPosition = Integer.parseInt(matcher.group(2)) - 1;
        char charToCheck = matcher.group(3).charAt(0);
        String thePassword = matcher.group(4);

        if (firstPosition >= thePassword.length() || secondPosition >= thePassword.length()) {
            return false;
        }

        boolean result = thePassword.charAt(firstPosition) == charToCheck ^ thePassword.charAt(secondPosition) == charToCheck;

        System.out.println(entry + " --- " + result);
        return result;
    }
}
