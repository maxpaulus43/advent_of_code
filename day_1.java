import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class day_1 {
    public static void main(String[] args) {
        try {
            List<String> lines = Files.lines(Paths.get("input/day_1.txt")).collect(Collectors.toList());
            System.out.println(getSum(lines));
            System.out.println(findRepeatSum(lines));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static int getSum(List<String> input) {
        return input.stream().mapToInt(Integer::parseInt).sum();
    }

    private static int findRepeatSum(List<String> input) {
        int[] nums = input.stream().mapToInt(Integer::parseInt).toArray();

        int sum = 0;
        Set<Integer> m = new HashSet<>();

        int i = 0;
        while (true) {
            sum += nums[i];
            if (m.contains(sum)) {
                return sum;
            } else {
                m.add(sum);
            }
            i = (i + 1) % nums.length;
        }
    }
}
