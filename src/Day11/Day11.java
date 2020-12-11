package Day11;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

/**
 * Created by Drew on 12/8/2020.
 */
public class Day11 {
    public static void main(String[] args) throws FileNotFoundException {
        List<List<Character>> seatingChart = new ArrayList<>();

        try (Scanner s = new Scanner(new File("./src/Day11/input.txt"))) {
            while (s.hasNextLine()) {
                seatingChart.add(s.nextLine()
                    .chars()
                    .mapToObj(c -> (char) c)
                    .collect(Collectors.toList()));
            }
            s.close();
        }

        seatingChart.add(0, new ArrayList<>());

        for (int i = 0; i < seatingChart.get(1).size(); i++) {
            seatingChart.get(0).add('.');
        }

        seatingChart.add(new ArrayList<>());

        for (int i = 0; i < seatingChart.get(1).size(); i++) {
            seatingChart.get(seatingChart.size() - 1).add('.');
        }

        seatingChart.stream().forEach(e -> {
            e.add(0, '.');
            e.add('.');
        });


        System.out.println(seatingChart);

        int counter = 0;

        List<List<Character>> prev = seatingChart;
        List<List<Character>> next = processRules(seatingChart);
        List<List<Character>> end = processRules(next);


        while (!listsAreEqual(prev, next)) {
            prev = next.stream().map(ArrayList::new).collect(Collectors.toList());
            next = processRules(prev);

            counter++;
        }
        System.out.println(seatingChart);
        System.out.println(next);
        System.out.println(end);
        System.out.println(counter);

        System.out.println(next.stream().flatMap(List::stream).filter(e -> e == '#').count());

    }

    private static boolean listsAreEqual(List<List<Character>> first, List<List<Character>> second) {
        for(int i = 0; i < first.size(); i++) {
            for(int j = 0; j < first.get(0).size(); j++) {
                if (first.get(i).get(j) != second.get(i).get(j)) {
                    return false;
                }
            }
        }

        return true;
    }


    private static List<Character> adjacentElements(int i, int j, List<List<Character>> seatingChart) {
        List<Character> adjacentToEntry = new ArrayList<>();

        for (int x = (i > 0 ? -1 : 0); x <= (i < seatingChart.size() ? 1 : 0); x++) {
            for (int y = (j > 0 ? -1 : 0); y <= (i < seatingChart.get(0).size() ? 1 : 0); y++) {
                if (x != 0 || y != 0) {
                    adjacentToEntry.add(seatingChart.get(i + x).get(j + y));
                }
            }
        }

        return adjacentToEntry;
    }
    private static char processEntry(int i, int j, List<List<Character>> seatingChart) {
        char entry = seatingChart.get(i).get(j);

        if (entry == '.') {
            return '.';
        }

        List<Character> adjacentToEntry = adjacentElements(i, j, seatingChart);

        if (entry == 'L') {
            if (adjacentToEntry.stream().noneMatch(e -> e == '#')) {
                return '#';
            }

            return 'L';
        }

        else {
            if (adjacentToEntry.stream().filter(e -> e == '#').count() >= 4) {
                return 'L';
            }

            return '#';
        }
    }

    private static List<List<Character>> processRules(List<List<Character>> seatingChart) {
        List<List<Character>> newChart = new ArrayList<>();

        for (int i = 0; i < seatingChart.size(); i++) {
            newChart.add(new ArrayList<>());
            for (int j = 0; j < seatingChart.get(0).size(); j++) {
                char newValueForEntry = processEntry(i, j, seatingChart);
                newChart.get(i).add(newValueForEntry);
            }
        }

        return newChart;
    }
}
