import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.Set;
import java.util.Stack;
import java.util.stream.Collectors;

public class day_5 {
    public static void main(String[] args) {

        try {
            List<Character> polymer = Files.lines(Paths.get("input/day_5.txt"))
                    .flatMap(line -> line.chars().mapToObj(i -> (char) i))
                    .collect(Collectors.toList());

            System.out.println(combust(polymer));
            System.out.println(findMinCombustion(polymer));

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static int findMinCombustion(List<Character> polymer) {
        Set<Character> chars = "abcdefghijklmnopqrstuvwxyz".chars().mapToObj(i -> (char) i).collect(Collectors.toSet());

        int minimumPolymerSize = polymer.size();

        for (char c : chars) {
            List<Character> tmpPolymer = polymer.stream()
                    .filter(character -> Character.toLowerCase(character) != Character.toLowerCase(c))
                    .collect(Collectors.toList());

            int tmpSize = combust(tmpPolymer);

            if (tmpSize < minimumPolymerSize) {
                minimumPolymerSize = tmpSize;
            }
        }

        return minimumPolymerSize;
    }

    private static boolean canReact(char a, char b) {
        return Character.toLowerCase(a) == Character.toLowerCase(b) &&
                ((Character.isLowerCase(a) && Character.isUpperCase(b))
                        || (Character.isUpperCase(a) && Character.isLowerCase(b)));
    }

    private static int combust(List<Character> polymer) {
        Stack<Character> polymerStack = new Stack<>();

        for (Character c : polymer) {
            if (!polymerStack.empty() && canReact(polymerStack.peek(), c)) {
                polymerStack.pop();
            } else {
                polymerStack.push(c);
            }
        }

        return polymerStack.size();
    }
}