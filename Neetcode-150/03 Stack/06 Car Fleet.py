# Title: Car Fleet
# Link: https://neetcode.io/problems/car-fleet
# Difficulty: Medium 
# Tags: Stack

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Combine the two info
        pos_speed = list(zip(position, speed))

        # Sort the cars in terms of their position
        pos_speed.sort(reverse = True, key = lambda x: x[0])

        # Compute the time taken to arrival (TTA) for each car
        tta = [(target - info[0]) / info[1] for info in pos_speed]

        # Let's assume the first car takes the max time to arrive
        max_tta = tta[0]

        # Fleet count is 1 when we are operating on the 
        # first car
        count = 1

        #Iterate from the 2nd car
        for curr in range(1, len(tta)):

            # If the TTA for the current car > max_TTA observed
            # so far, the current car can never catch up before the
            # destination is reached...
            if tta[curr] > max_tta:

                # Hence, start a new fleet
                count += 1

                # Update the max_TTA to the current TTA
                # Now, a fleet can only be formed if a car's TTS
                # is <= this max TTA.
                max_tta = tta[curr]

        return count