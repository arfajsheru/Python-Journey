import java.util.Arrays;

public class ArrayRotation {

    public static void rotate(int[] nums, int k) {
        // Step 1: Find the length of the array
        int n = nums.length;  // Array ki total length ko n mein store kar rahe hain
        
        // Step 2: Adjust k to be within the length of the array
        k = k % n;  // Agar k bada ho array ke size se, toh hum k ko normalize karte hain

        // Step 3: Create a new array to store the rotated result
        int[] rotated = new int[n];  // Rotated array ko banate hain

        // Step 4: Move last k elements to the beginning of the new array
        for (int i = 0; i < k; i++) {
            rotated[i] = nums[n - k + i];  // Last k elements ko rotated array ke starting mein daal rahe hain
        }

        // Step 5: Move the remaining n-k elements to the end of the new array
        for (int i = 0; i < n - k; i++) {
            rotated[k + i] = nums[i];  // Pehle ke elements ko rotated array ke baad mein daal rahe hain
        }

        // Step 6: Copy the rotated array back to the original nums array
        for (int i = 0; i < n; i++) {
            nums[i] = rotated[i];  // Final rotated array ko nums array mein copy kar rahe hain
        }

        // Step 7: Print the rotated array
        System.out.println(Arrays.toString(nums));  // Result ko print kar rahe hain
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4, 5, 6, 7};  // Example input array
        int k = 8;  // Number of steps to rotate
        rotate(nums, k);  // Rotate function ko call karte hain
    }
}
