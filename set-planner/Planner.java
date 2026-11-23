import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Planner {
    record Set(String band, int start, int end, int score) {}
    record Plan(int score, List<Set> sets) {}

    static Plan choose(List<Set> input) {
        var sets = new ArrayList<>(input);
        sets.sort(Comparator.comparingInt(Set::end));
        int n = sets.size();
        int[] best = new int[n + 1], previous = new int[n];
        boolean[] take = new boolean[n];
        for (int i = 0; i < n; i++) {
            Set s = sets.get(i);
            int lo = 0, hi = i;
            while (lo < hi) {
                int mid = (lo + hi) >>> 1;
                if (sets.get(mid).end() <= s.start()) lo = mid + 1;
                else hi = mid;
            }
            previous[i] = lo;
            int with = Math.addExact(best[lo], s.score());
            take[i] = with > best[i];
            best[i + 1] = Math.max(with, best[i]);
        }
        var chosen = new ArrayList<Set>();
        for (int i = n; i > 0;) {
            if (take[i - 1]) {
                chosen.add(sets.get(i - 1));
                i = previous[i - 1];
            } else i--;
        }
        Collections.reverse(chosen);
        return new Plan(best[n], List.copyOf(chosen));
    }

    public static void main(String[] args) throws Exception {
        if (args.length != 1) throw new IllegalArgumentException("Pass a festival TSV path");
        var sets = new ArrayList<Set>();
        for (String line : Files.readAllLines(Path.of(args[0]))) {
            if (line.isBlank() || line.startsWith("#")) continue;
            String[] f = line.split("\\t", -1);
            if (f.length != 4) throw new IllegalArgumentException("Expected four tab-separated fields");
            Set s = new Set(f[0], Integer.parseInt(f[1]), Integer.parseInt(f[2]), Integer.parseInt(f[3]));
            if (s.band().isBlank() || s.start() < 0 || s.end() <= s.start() || s.score() < 0)
                throw new IllegalArgumentException("Invalid set: " + line);
            sets.add(s);
        }
        Plan plan = choose(sets);
        for (Set s : plan.sets()) System.out.printf("%d-%d  %s%n", s.start(), s.end(), s.band());
        System.out.println("Total points: " + plan.score());
    }
}
