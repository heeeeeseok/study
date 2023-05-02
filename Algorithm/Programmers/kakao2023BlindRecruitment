import static java.lang.Math.max;
import java.util.Stack;


class Solution {
    static public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long result = 0;
        Stack<Integer> dstack = new Stack<>();
        Stack<Integer> pstack = new Stack<>();

        for (int i = 0; i < n; i++) {
            if (deliveries[i] > 0)
                dstack.add(i);

            if (pickups[i] > 0)
                pstack.add(i);
        }

        // 두 스택 모두 비었다면
        while (!dstack.isEmpty() || !pstack.empty()) {
            if (dstack.isEmpty())
                result += (pstack.peek() + 1) * 2;
            else if (pstack.empty())
                result += (dstack.peek() + 1) * 2;
            else
                result += (max(dstack.peek(), pstack.peek()) + 1) * 2;

            doDeliver(cap, deliveries, dstack);
            doPickup(cap, pickups, pstack);
        }

        return result;
    }

    static void doPickup(int cap, int[] array, Stack<Integer> pstack) {
        int boxCount = 0;
        while (boxCount < cap && !pstack.isEmpty()) {
            int cur = pstack.peek();
            // 현재 여유 공간만큼만 수거
            if (array[cur] > (cap - boxCount)) {
                array[cur] -= (cap - boxCount);
                break;
            }

            // 현재 집에서 수거할 상자 모두 수거
            else {
                boxCount += array[cur];
                array[cur] = 0;
            }

            pstack.pop();
        }
    }
    static void doDeliver(int cap, int[] array, Stack<Integer> dstack) {
        int boxCount = cap;
        while (boxCount > 0 && !dstack.isEmpty()) {
            int cur = dstack.peek();

            // 현재 가진 상자만큼만 배달
            if (array[cur] > boxCount) {
                array[cur] -= boxCount;
                break;
            }

            // 현재 집에 배달할 상자 모두 배달
            else {
                boxCount -= array[cur];
                array[cur] = 0;
            }

            dstack.pop();
        }
    }
}
