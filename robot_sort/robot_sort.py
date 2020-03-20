class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)
    def __str__(self):
        print(f'~~~ The full list is {self._list}. \n~~~ I am holding {self._item}. \nI am at position {self._position}.')

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # TURN ON LIGHT
        self.set_light_on()
        # WHILE THE LIGHT IS ON...
        while self.light_is_on():
            # AND WHILE THE ROBOT CAN MOVE TO THE RIGHT...
            while self.can_move_right():
                # IF EITHER OF THE ITEMS ARE NONE...
                if self.compare_item() == None:
                    print(f'swapping {self._item} for {self._list[self._position]}')
                    # SWAP THE ITEM
                    self.swap_item()
                    self.set_light_on()
                    # THEN MOVE TO THE NEXT NUMBER
                    self.move_right()

                # IF THE ITEM BEING HELD IS GREATER THAN THE ITEM AT THE LIST'S POSITION
                if self.compare_item() == 1:
                    print(f'{self._item} > {self._list[self._position]}')
                    # TURN OFF THE LIGHT
                    self.set_light_off()
                # OTHERWISE...
                else:
                    print(f'{self._item} < {self._list[self._position]}')
                    # SWAP THE ITEMS
                    self.swap_item()
                    self.set_light_on()
                # MOVE TO THE NEXT NUMBER
                self.move_right()
                
                # IF THE NUMBER BEING HELD IS GREATER THAN THE ITEM AT THE LIST'S POSITION, BUT THE ROBOT CAN NOT MOVE TO THE RIGHT...
                if self.compare_item() == 1 and self.can_move_right() == False:
                    print('found nothing bigger and can\'t move anymore')
                    # SWAP THE ITEMS
                    self.swap_item()
                    self.set_light_on()
                # if self.compare_item() == -1 and self.can_move_right() == False:
                #     print('found nothing bigger and can\'t move anymore')
                #     # SWAP THE ITEMS
                #     self.move_left()
                #     self.set_light_off()

            # WHILE THE ROBOT CAN MOVE TO THE LEFT
            while self.can_move_left():
                # IF THE NUMBER BEING HELD IS LESS THAN THE ITEM AT THE LIST'S POSITION...
                if self.compare_item() == -1:
                    print(f'GOING LEFT {self._item} < {self._list[self._position]}')
                    # TURN OFF LIGHT
                    self.set_light_off()
                # ELSE IF THE NUMBER BEING HELD IS GREATER THAN THE ITEM AT THE LIST'S POSITION...
                elif self.compare_item() == 1:
                    print(f'{self._item} < {self._list[self._position]}')
                    # SWAP THE ITEMS
                    self.swap_item()
                    self.set_light_on()
                    
                # MOVE TO THE LEFT
                self.move_left()
                
                if self.compare_item() == 1 and self.can_move_left() == False:
                    print('found nothing bigger and can\'t move anymore')
                    # SWAP THE ITEMS
                    self.move_right()

                # IF EITHER OF THE NUMBERS BEING COMPARED IS NONE AND THE ROBOT CAN NOT MOVE LEFT...
                if self.compare_item() == None and self.move_left() == False:
                    print('found nothing smaller and can\'t move anymore')
                    # SWAP THE ITEMS
                    self.swap_item()
                    self.set_light_on()
                    # MOVE TO THE NEXT ITEM
                    self.move_right()
                    return self.sort()
        self.__str__()
        return


        # ATTEMPT 2
        # self.set_light_on()
        # while self.light_is_on():
        #     if self.can_move_right():
        #         # Loop through array
        #             # Compare each number

        #         print(self._item, self._list[self._position])
        #         # If either item is None, swap
        #         if self.compare_item() == None:
        #             self.set_light_on()
        #             self.swap_item()
        #             self.move_right()
        #         # If item that robot is holding is greater, swap/turn light on
        #         if self.compare_item() == 1:
        #             self.set_light_on()
        #             self.swap_item()
        #             self.move_right()
        #             print(self._item, self._list[self._position])
        #         # If item that robot is holding is smaller, don't swap/turn light off
        #         # elif self.compare_item() == -1:
        #         #     self.set_light_off()
        #         #     self.move_right()
        #         else:
        #             self.set_light_off()
        #             self.move_right()
        #     # If robot can not move right and the item that robot is holding is greater, swap/turn light on then move all the way to the left and recurse function
        #     elif self.can_move_right() == False and self.compare_item() == 1:
        #         self.set_light_on()
        #         self.swap_item()
        #         while self.can_move_left():
        #             self.move_left()
        #         print('HERE', self._item, self._position)
        #         self.sort()
        #     else:
        #         while self.can_move_left():
        #             self.move_left()
        #         self.sort()
        # self.__str__()
        # return

        # robot will pick up item
        # what determines left vs right...?
        # robot moves right or left
        # compares item to position item
        # swap if need be; moved to next if not
        # if reaches end...
            ## move back to original position
            ## place item back move to next position
            ## pick up item

        # Compare the held item with the item in front of the robot:
        # If the held item's value is greater, return 1.
        # If the held item's value is less, return -1.
        # If the held item's value is equal, return 0.
        # If either item is None, return None.


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    # l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]
    l = [5, 4, 3, 2, 1]
    # l = [11, 13, 7, 17, 9, 20, 1, 21, 2, 4, 22, 16, 15, 10, 23, 19, 8, 3, 5, 14, 6, 0, 24, 12, 18]
    # l = [20, 77, 45, 16, 15, 91, 12, 6, 24, 89, 53, 19, 85, 56, 13, 74, 48, 98, 9, 92, 25, 35, 54, 44, 50, 5, 75, 34, 2, 42, 87, 49, 76, 52, 43, 23, 7, 80, 66, 14, 46, 90, 88, 40, 97, 10, 57, 63, 1, 18, 67, 79, 96, 27, 73, 28, 32, 61, 30, 8, 17, 93, 26, 51, 60, 55, 62, 31, 47, 64, 39, 22, 99, 95, 83, 70, 38, 69, 36, 41, 37, 65, 84, 3, 29, 58, 0, 94, 4, 11, 33, 86, 21, 81, 72, 82, 59, 71, 68, 78]

    robot = SortingRobot(l)

    robot.sort()
    print('FINAL CALL', robot._list)