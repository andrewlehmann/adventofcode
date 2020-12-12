package Day11;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

/** Created by Drew on 12/8/2020. */
public class Day11 {
  private static boolean listsAreEqual(List<List<Character>> first, List<List<Character>> second) {
    for (int i = 0; i < first.size(); i++) {
      for (int j = 0; j < first.get(0).size(); j++) {
        if (first.get(i).get(j) != second.get(i).get(j)) {
          return false;
        }
      }
    }

    return true;
  }

  public static void main(String[] args) throws FileNotFoundException {
    List<List<Character>> seatingChart = new ArrayList<>();

    try (Scanner s = new Scanner(new File("./src/Day11/input.txt"))) {
      while (s.hasNextLine()) {
        seatingChart.add(s.nextLine().chars().mapToObj(c -> (char) c).collect(Collectors.toList()));
      }
    }

    int counter = 1;
    List<List<Character>> prev = seatingChart;
    List<List<Character>> next = processRules(seatingChart);

    while (!listsAreEqual(prev, next)) {
      prev = next.stream().map(ArrayList::new).collect(Collectors.toList());
      next = processRules(prev);
      counter++;
    }

    System.out.println("Num times processed: " + counter);

    System.out.println(
        "Num seats occupied: " + next.stream().flatMap(List::stream).filter(e -> e == '#').count());
  }

  private static List<Character> getAdjacentElements(
      int i, int j, List<List<Character>> seatingChart) {
    List<Character> adjacentToEntry = new ArrayList<>();

    for (int x = (i > 0 ? -1 : 0); x <= (i < seatingChart.size() - 1 ? 1 : 0); x++) {
      for (int y = (j > 0 ? -1 : 0); y <= (j < seatingChart.get(0).size() - 1 ? 1 : 0); y++) {
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

    List<Character> adjacentToEntry = getAdjacentElements(i, j, seatingChart);

    if (entry == 'L') {
      return adjacentToEntry.stream().noneMatch(e -> e == '#') ? '#' : 'L';
    }

    return adjacentToEntry.stream().filter(e -> e == '#').count() >= 4 ? 'L' : '#';
  }

  private static List<List<Character>> processRules(List<List<Character>> seatingChart) {
    List<List<Character>> newChart = new ArrayList<>();

    for (int i = 0; i < seatingChart.size(); i++) {
      newChart.add(new ArrayList<>());

      for (int j = 0; j < seatingChart.get(0).size(); j++) {
        char newValueForEntry = processEntry2(i, j, seatingChart);
        newChart.get(i).add(newValueForEntry);
      }
    }

    return newChart;
  }

  // PART 2
  private static boolean canSeeOccupiedSeat(
      int i, int j, int slopeX, int slopeY, List<List<Character>> seatingChart) {
    int x = i + slopeX;
    int y = j + slopeY;

    while (x >= 0 && y >= 0 && x < seatingChart.size() && y < seatingChart.get(0).size()) {
      char seat = seatingChart.get(x).get(y);

      switch (seat) {
        case '#':
          return true;
        case 'L':
          return false;
        default:
          x += slopeX;
          y += slopeY;
      }
    }

    return false;
  }

  private static List<Boolean> getLineOfSight(int i, int j, List<List<Character>> seatingChart) {
    return Arrays.asList(
        canSeeOccupiedSeat(i, j, 1, 1, seatingChart),
        canSeeOccupiedSeat(i, j, 1, -1, seatingChart),
        canSeeOccupiedSeat(i, j, -1, 1, seatingChart),
        canSeeOccupiedSeat(i, j, -1, -1, seatingChart),
        canSeeOccupiedSeat(i, j, 0, 1, seatingChart),
        canSeeOccupiedSeat(i, j, 0, -1, seatingChart),
        canSeeOccupiedSeat(i, j, 1, 0, seatingChart),
        canSeeOccupiedSeat(i, j, -1, 0, seatingChart));
  }

  private static char processEntry2(int i, int j, List<List<Character>> seatingChart) {
    char entry = seatingChart.get(i).get(j);

    if (entry == '.') {
      return '.';
    }

    List<Boolean> lineOfSight = getLineOfSight(i, j, seatingChart);

    if (entry == 'L') {
      return lineOfSight.stream().noneMatch(e -> e) ? '#' : 'L';
    }

    return lineOfSight.stream().filter(e -> e).count() >= 5 ? 'L' : '#';
  }
}
