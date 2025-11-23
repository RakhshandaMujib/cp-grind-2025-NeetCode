# Title: Find the Duplicate Number
# Link: https://neetcode.io/problems/find-duplicate-integer
# Difficulty: Medium 
# Tags: Linked List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # We treat the array as a linked list:
        # - Each index is a node.
        # - nums[i] is a pointer to the next node.
        # Because one value repeats, two indices point to the same next node —
        # which forms a cycle in this "linked list".
        # Our task becomes: find the START of that cycle (the duplicate number).

        slow = fast = 0

        # PHASE 1: Detect the intersection point inside the cycle using
        # Floyd's Tortoise and Hare algorithm.
        #
        # slow moves 1 step at a time: slow = nums[slow]
        # fast moves 2 steps at a time: fast = nums[nums[fast]]
        #
        # If there's a cycle (and there always is because of the duplicate),
        # fast and slow WILL eventually meet at some node inside the cycle.
        while True:
            slow = nums[slow]            # move slow pointer one step
            fast = nums[nums[fast]]      # move fast pointer two steps
            if slow == fast:             # cycle detected when pointers converge
                break
        
        # PHASE 2: Find the start of the cycle.
        #
        # Key fact from Floyd’s proof:
        # Distance(head → cycle_start) == Distance(meeting_point → cycle_start)
        # when both pointers move at the same speed.
        #
        # So:
        # - Keep one pointer where they met.
        # - Move the other pointer to the start of the list (index 0).
        # - Move both 1 step at a time.
        # The point where they meet again is the start of the cycle,
        # which corresponds to the DUPLICATE number.
        slow2 = 0

        while slow != slow2:
            slow = nums[slow]    # move from meeting point toward cycle start
            slow2 = nums[slow2]  # move from array start toward cycle start
        
        # When slow == slow2, we've reached the start of the cycle.
        # This value is the duplicated number.
        return slow
