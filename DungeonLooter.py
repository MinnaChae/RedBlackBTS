import random
import numpy as np


class Adventurer:
    """
    The adventurer has a finite carry capacity.  They cannot carry more than their carry_weight.  They also contain
    a coin_purse to keep all of their different coins that sum up to a total value.
    """

    def __init__(self, carry_weight):
        self.carry_weight = carry_weight
        self.coin_purse = {}
        self.inventory = []
        self.total_coin_purse_value = 0
        self.total_possible_carry_weight = carry_weight
        self.total_actual_carry_weight = 0
        self.total_value=0

    def show_inventory(self):
        """
        *** STUDENT TO IMPLEMENT ***
        Shows Inventory
        :return: A String representation of the players inventory.
        """

        """
        
        === SAMPLE SHOW INVENTORY ===
        Adventurer (Total Carry Capacity: 100)
        Total Carry Weight: 70
        Total Carry Value: 537
        Total Coin Purse Value: 89

        == COINS ==
        bronze (1): 0
        copper (2): 0
        nickel (5): 1
        silver (13): 0
        gold (20): 1
        diamond (32): 2
        lunastone (100): 0

        == INVENTORY ==
        dagger: Wgt=4, V=90
        armor: Wgt=52, V=118
        herbs: Wgt=1, V=19
        herbs: Wgt=2, V=17
        clothing: Wgt=5, V=43
        dagger: Wgt=4, V=60
        jewels: Wgt=2, V=190
        """
        advent_str = "=== SHOW INVENTORY === \n"
        advent_str += f"Adventurer (Total Carry capacity: {self.total_possible_carry_weight}) \n"

        items_total_carry_weight = 0
        self.total_coin_purse_value = 0
        for items in self.inventory:
            items_str += str(items.name) + " : Wgt="+str(items.weight) + " V=" +str(items.value)
            items_str += '\n'
            items_total_carry_weight += items.weight

            self.total_actual_carry_weight += items.weight
            self.total_value += items.value

        advent_str += f"Total Carry Weight: {self.total_actual_carry_weight }\n"
        advent_str += f"Total Carry Value: {self.total_value} \n"
        advent_str += f"Total Coin Purse Value: {self.total_value} \n"
        print(advent_str)
        print(items_str)


class Chest:
    """
    A chest is a container of Items that can be randomly populated.
    """

    def __init__(self, n=10):
        self.contents = []
        for i in range(n):
            self.contents.append(Item.generate_random_item())

    def __str__(self):
        ret_str = ""
        x = 0
        tot_wgt = 0
        tot_val = 0
        for i in self.contents:
            ret_str += f'{x}: {i} \n'
            tot_wgt += i.weight
            tot_val += i.value
            x += 1
        return f"Chest: Item Count={x}, Total Value={tot_val}, Total Weight={tot_wgt}\n{ret_str}"

    def print(self):
        for i in self.contents:
            print(i)

    def remove(self, item):
        """
        Removes the provided item from the chest.
        :param item: The item object that should be removed from the list.
        :return: True if item was found/removed, False otherwise
        """
        try:
            self.contents.remove(item)
            return True
        except ValueError as e:
            return False


class Item:
    """
    An Item can be of multiple types and those types have a min and max value and weight.  When an item of a specific
    type is generated, it should contain a value that is within that range.  To add different types to the game,
    simply add them to the static field Item.TYPES as shown.  This is used by the generator to create a random item.
    """
    TYPES = {
        'dagger': {
                'weight': (1, 5),
                'value': (10, 100)
        },
        'jewels': {
                'weight': (1, 5),
                'value': (50, 500)
        },
        'clothing': {
                'weight': (5, 10),
                'value': (1, 50)
        },
        'herbs': {
                'weight': (1, 2),
                'value': (3, 20)
        },
        'gems': {
                'weight': (1, 5),
                'value': (25, 250)
        },
        'armor': {
                'weight': (25, 75),
                'value': (50, 1000)
        }
    }

    def __init__(self, name, weight, value):
        """
        Creates an item with the provided type (name), weight and value.
        :param name: The name of the item.  Usually just the 'type' of item it is.
        :param weight: The weight of the item.  (numeric)
        :param value: The value of the item (int).
        """
        self.name = name
        self.weight = weight
        self.value = value

    def __str__(self):
        return f"{self.name}: Wgt={self.weight}, V={self.value}"

    @staticmethod
    def generate_random_item(of_type=None):
        """
        Will generate a random item of any type or of a specific type when provided.
        :param of_type: The TYPE of item to generate.  If omitted, the method will generate an item of random Type.
        :return: An instantiated Item.
        """
        if of_type is None:
            of_type = random.choice(list(Item.TYPES))

        w_min, w_max = Item.TYPES[of_type]['weight']
        v_min, v_max = Item.TYPES[of_type]['value']
        w = random.randint(w_min, w_max)
        v = random.randint(v_min, v_max)
        return Item(of_type, w, v)


class Game:
    """
    The controller for the game handling the different Coin Denominations and maintaining the states of chests and
    acting as the "shop" that can also sell the items for the Adventurer.
    """
    COINS = {
        1: 'bronze',
        2: 'copper',
        5: 'nickel',
        13: 'silver',
        20: 'gold',
        32: 'diamond',
        100: 'lunastone'
    }

    def __init__(self, player):
        self.player = player
        self.chests = []
        self.max_capacity = 0

    def show_player_inventory(self):
        print(self.player.show_inventory())

    def add_chest(self, chest):
        """
        Adds a chest to the game.
        :param chest: The Chest to add to the game.
        :return: None
        """
        self.chests.append(chest)

    def show_chests(self):
        """
        *** STUDENT TO IMPLEMENT ***
        Prints a list of the chest contents to the screen.
        :return: None
        """

        """
        === SAMPLE SHOW CHESTS === 
        Chest 0:
        = CONTENTS =
        dagger: Wgt=4, V=90
        armor: Wgt=52, V=118
        herbs: Wgt=1, V=19
        herbs: Wgt=2, V=17
        clothing: Wgt=5, V=43
        dagger: Wgt=4, V=60
        jewels: Wgt=2, V=190

        Chest 1:
        = CONTENTS = 
        clothing: Wgt=5, V=43
        dagger: Wgt=4, V=60
        """
        i = 1
        for a_chest in self.chests:
            print(f"Chest {i}")
            print(a_chest)
            i +=1

    def loot_chests(self):
        """
        *** STUDENT TO IMPLEMENT ***
        For each chest in the game, determine the optimal content to remove [0-1] knapsack
        and add the item to the adventurers inventory.
        Chests may still have contents remaining after looting.

        Note after looting each chest, the remaining carry weight of the adventurer will be
        reduced.  The adventurer does NOT have to select the optimal ORDER of looting chests
        if there are more than one.  For example, if the first chest contains 100 lbs of clothes
        and the second contains 100 lbs of jewels, if the adventurer loots the clothing chest
        first, then the opportunity to loot the jewels will be missed, and that is ok.

        :return: None
        """
        #loot multiple chest optimally

        #loot first chest, add to inventory, reduce adventurer's weight
        #Loot first chest
        #add the inventory to the bag
        #reduce adventurer's carry_weight
        #loot 2nd chest
        chest_count = []
        item_weight = []
        item_value = []
        item_name = []
        item_index = []
        count = 0
        max_carry_weight = self.player.carry_weight
        current_carry_weight = 0
        item_item = []
        i = 0
        for a_chest in self.chests:
            chest_count.append(i)
            for items in a_chest.contents:
                # a_chest.remove(items)
                item_item.append(items)
                item_index.append(count)
                item_name.append(items.name)
                item_weight.append(items.weight)
                item_value.append(items.value)
                count += 1
            count = 0
            solution = self.knapsack(item_weight, item_value, max_carry_weight)
            results = self.knapsack_recovery(solution, item_weight, item_value)
            for index in results:
                self.player.inventory.append(item_item[index])
                a_chest.remove(item_item[index])

            item_item.clear()
            item_weight.clear()
            item_value.clear()
            item_name.clear()
            item_index.clear()
            i += 1



    def knapsack(self, weights, values, capacity):
        solution = np.zeros((len(weights), capacity + 1))
        # INITIALIZE THE FIRST ITEM
        for j in range(capacity + 1):
            solution[0, j] = values[0] if j >= weights[0] else 0

        for i in range(1, len(weights)):
            for j in range(capacity + 1):
                if j - weights[i] >= 0:  # IF THIS ITEM CAN FIT
                    with_item = solution[i - 1, j - weights[i]] + values[i]
                else:
                    with_item = -1

                without_item = solution[i - 1, j]
                solution[i, j] = max(without_item, with_item)

        return solution

    def knapsack_recovery(self, solution, weights, values):
        rows, cols = solution.shape

        curr_row = rows - 1
        curr_col = cols - 1

        result = []

        curr_val = solution[curr_row, curr_col]

        while curr_val > 0:
            if curr_row == 0:
                result.append(curr_row)
                break
            elif curr_val != solution[curr_row - 1, curr_col]:
                result.append(curr_row)
                curr_val = curr_val - values[curr_row]
                curr_col = curr_col - weights[curr_row]
                curr_row -= 1
            else:
                curr_row -= 1

        return result

    def sell_items(self):
        """
        *** STUDENT TO IMPLEMENT ***
        Sell items will take the entirety of the adventurers inventory, calculate its total
        value and "sell it." This will remove it all items from inventory and in return "payment"
        matching that total value will be added to the adventurer's coin_purse, consisting of the
        optimal set of denominations.  For example, if the total inventory is valued at 124, the
        coin_purse will have the following denominations added:
            1 Diamond (100 value)
            1 Gold (20 value)
            2 Nickel (2x2 = 4 value)

        :return: None
        """

        #sell/get the value of the items

        pass


if __name__ == "__main__":
    # chest = Chest()
    # g = Game()




    # CREATE A PLAYER WITH FINITE CARRY CAPACITY
    player = Adventurer(carry_weight=100)
    game = Game(player)
    #
    # # INDICATE THERE IS NO INVENTORY AND NO MONEY
    # game.show_player_inventory()
    #
    # # CREATE CHESTS WITH RANDOM CONTENT AND ADD IT TO THE GAME
    game.add_chest(Chest())
    # game.add_chest(Chest())

    #
    # # SHOW THE CONTENT OF ANY CHESTS IN THE GAME
    game.show_chests()
    #
    # # THE GAME SHOULD HAVE A METHOD THAT WILL OPTIMALLY LOOT THE ITEMS
    # # IN THE CHEST [0-1 KNAPSACK] AND ADD IT TO THE PLAYER'S INVENTORY
    # # ANY ITEMS NO IN THE CHEST SHOULD REMAIN
    game.loot_chests()
    #
    game.show_chests()
    game.show_player_inventory()
    #
    # # THE CAME SHOULD HAVE A METHOD TO TAKE INVENTORY FROM THE PLAYER
    # # CONVERT IT INTO PROPER DENOMINATIONS, AND PLACE THAT DATA INTO THE COIN PURSE
    # game.sell_items()
    #
    # game.show_player_inventory()





