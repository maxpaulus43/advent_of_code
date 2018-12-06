import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.LinkedList;
import java.util.List;
import java.util.stream.Collectors;

public class day_5 {
    public static void main(String[] args) {
        try {
            List<Character> polymer = Files.lines(Paths.get("input/day_5.txt"))
                    .flatMap(line -> line.chars().mapToObj(i -> (char) i))
                    .collect(Collectors.toCollection(LinkedList::new));

            System.out.println(part1(polymer));
            System.out.println(part2(polymer));

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static int part1(List<Character> polymer) {
        combust(new LinkedList<>(polymer));
        return polymer.size();
    }

    private static int part2(List<Character> polymer) {
        Set<Character> chars = "abcdefghijklmnopqrstuvwxyz".chars()
            .mapToObj(i -> (char) i)
            .collect(Collectors.toSet());

        int minimumPolymerLen = polymer.size();

        for (char c : chars) {
            List<Character> tmpPolymer = new LinkedList<>(polymer);
            
            tmpPolymer.removeIf(character -> Character.toLowerCase(character) == Character.toLowerCase(c));
            
            combust(tmpPolymer);

            if (tmpPolymer.size() < minimumPolymerLen) {
                minimumPolymerLen = tmpPolymer.size();
            }
        }

        return minimumPolymerLen;
    }

    private static boolean canReact(char a, char b) {
        return Character.toLowerCase(a) == Character.toLowerCase(b) &&
                ((Character.isLowerCase(a) && Character.isUpperCase(b))
                        || (Character.isUpperCase(a) && Character.isLowerCase(b)));
    }

    private static void combust(List<Character> polymer) {
        int i = 1;
        while (i < polymer.size()) {
            if (canReact(polymer.get(i - 1), polymer.get(i))) {
                polymer.remove(i);
                polymer.remove(i - 1);
                if (i > 1) i--;
            } else {
                i++;
            }
        }
    }
}