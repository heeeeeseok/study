import java.util.Arrays;

class Solution {
    int[][] USERS;
    int[] EMOTICONS;
    int maxCount = -1;
    int maxPrice = -1;
    public int[] solution(int[][] users, int[] emoticons) {
        USERS = users;
        EMOTICONS = emoticons;

        dfs(0, 0.1, new long[users.length]);
        dfs(0, 0.2, new long[users.length]);
        dfs(0, 0.3, new long[users.length]);
        dfs(0, 0.4, new long[users.length]);


        return new int[]{maxCount, maxPrice};
    }

    void dfs(int idx, double discount, long[] prices) {
        if (idx == EMOTICONS.length) {
            int count = 0;
            int totalPrice = 0;

            for (int i = 0; i < USERS.length; i++) {
                if (USERS[i][1] <= prices[i])
                    count++;
                else
                    totalPrice += prices[i];
            }

            if (count > maxCount) {
                maxCount = count;
                maxPrice = totalPrice;
            } else if (count == maxCount) {
                if (totalPrice > maxPrice)
                    maxPrice = totalPrice;
            }

            return;
        }

        long[] newPrices = Arrays.copyOf(prices, USERS.length);

        for (int i = 0; i < USERS.length; i++)
            if (USERS[i][0] <= (discount * 100))
                newPrices[i] += (EMOTICONS[idx] * (1 - discount));

        dfs(idx + 1, 0.1, newPrices);
        dfs(idx + 1, 0.2, newPrices);
        dfs(idx + 1, 0.3, newPrices);
        dfs(idx + 1, 0.4, newPrices);
    }
}
