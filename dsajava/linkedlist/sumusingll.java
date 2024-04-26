/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(); // Dummy node to simplify the code
        ListNode curr = dummy; // Pointer to track the current node of the result list
        int carry = 0; // Initialize carry to 0

        while (l1 != null || l2 != null || carry != 0) {
            int sum = carry; // Initialize sum to carry

            if (l1 != null) {
                sum += l1.val;
                l1 = l1.next;
            }

            if (l2 != null) {
                sum += l2.val;
                l2 = l2.next;
            }

            carry = sum / 10; // Update carry
            sum = sum % 10; // Update sum

            curr.next = new ListNode(sum); // Create a new node with the sum
            curr = curr.next; // Move the pointer to the next node
        }

        return dummy.next; // Return the next node of the dummy node, which is the head of the result list
    }
}
