import itertools
import operator
import random
import time
import os
from collections import defaultdict
from  tkinter.messagebox import*
os.system('msg * 3D - TIC TAC TOE')
showinfo("",'MADE BY SHIVAM')
showinfo("BY-SHIVAM",'CAN YOU DEFEAT MY AI')
showinfo("BY-SHIVAM",'STARTS WITH 0')
def SHIVAM():
    os.system('cls')
    class Connect3DError(Exception):
        pass

    class Connect3D(object):
        x=int(input("ENTER GRID SIZE YOU WANT (recomended >= 2) : "))
        
        """Class to store the Connect3D game data.
        The data is stored in a 1D list, but is converted to a 3D representation for the user.
        """
        player_symbols = 'XO'
        grid_size_recommended = x

        def __init__(self, grid_size=grid_size_recommended):
            """Set up the grid and which player goes first.

            Parameters:
                grid_size (int): How long each side of the grid should be.
                    The game works best with even numbers, 4 is recommended.
            """

            try:
                self.current_player
            except AttributeError:
                self.current_player = random.randint(0, 1)

            self._display_score = False

            try:
                self.grid_size = int(grid_size)
            except TypeError:
                raise TypeError('grid_size must be an integer')
            self.grid_data = ['' for i in range(pow(grid_size, 3))]

            self.grid_size_squared = pow(self.grid_size, 2)

            #Calculate the edge numbers for each direction
            self.direction_edges = {}
            self.direction_edges['U'] = range(self.grid_size_squared)
            self.direction_edges['D'] = range(self.grid_size_squared*(self.grid_size-1), self.grid_size_squared*self.grid_size)
            self.direction_edges['R'] = [i*self.grid_size+self.grid_size-1 for i in range(self.grid_size_squared)]
            self.direction_edges['L'] = [i*self.grid_size for i in range(self.grid_size_squared)]
            self.direction_edges['F'] = [i*self.grid_size_squared+j+self.grid_size_squared-self.grid_size for i in range(self.grid_size) for j in range(self.grid_size)]
            self.direction_edges['B'] = [i*self.grid_size_squared+j for i in range(self.grid_size) for j in range(self.grid_size)]
            self.direction_edges[' '] = []

            #Calculate the addition needed to move in each direction
            self.direction_maths = {}
            self.direction_maths['D'] = self.grid_size_squared
            self.direction_maths['R'] = 1
            self.direction_maths['F'] = self.grid_size
            self.direction_maths['U'] = -self.direction_maths['D']
            self.direction_maths['L'] = -self.direction_maths['R']
            self.direction_maths['B'] = -self.direction_maths['F']
            self.direction_maths[' '] = 0


        def __repr__(self):
            """Format the data to allow it to be imported again as a new object."""
            grid_data_joined = ''.join(str(i).ljust(1) for i in self.grid_data)
            return "Connect3D.from_string('{}.{}')".format(grid_data_joined, self.current_player)

        def __str__(self):
            """Use the grid_data to output a grid of the correct size.
            Each value in grid_data must be 1 character or formatting will be wrong.

            >>> grid_data = range(8)

            >>> print Connect3D.from_string(''.join(str(i) if i != '' else ' ' for i in grid_data))
                 ________
                / 0 / 1 /|
               /___/___/ |
              / 2 / 3 /  |
             /___/___/   |
            |   |____|___|
            |   / 4 /|5 /
            |  /___/_|_/
            | / 6 / 7|/
            |/___/___|

            """
            k = 0

            grid_range = range(self.grid_size)
            grid_output = []

            if self._display_score:
                grid_output.append(self.show_score())

            for j in grid_range:

                row_top = ' '*(self.grid_size*2+1) + '_'*(self.grid_size*4)
                if j:
                    row_top = '|' + row_top[:self.grid_size*2-1] + '|' + '_'*(self.grid_size*2) + '|' + '_'*(self.grid_size*2-1) + '|'
                grid_output.append(row_top)

                for i in grid_range:
                    row_display = ' '*(self.grid_size*2-i*2) + '/' + ''.join((' ' + str(self.grid_data[k+x]).ljust(1) + ' /') for x in grid_range)
                    k += self.grid_size
                    row_bottom = ' '*(self.grid_size*2-i*2-1) + '/' + '___/'*self.grid_size

                    if j != grid_range[-1]:
                        row_display += ' '*(i*2) + '|'
                        row_bottom += ' '*(i*2+1) + '|'
                    if j:
                        row_display = row_display[:self.grid_size*4+1] + '|' + row_display[self.grid_size*4+2:]
                        row_bottom = row_bottom[:self.grid_size*4+1] + '|' + row_bottom[self.grid_size*4+2:]

                        row_display = '|' + row_display[1:]
                        row_bottom = '|' + row_bottom[1:]

                    grid_output += [row_display, row_bottom]

            return '\n'.join(grid_output)

        def _get_winning_player(self):
            """Return a list of the player(s) with the highest points.

            >>> C3D = Connect3D()
            >>> C3D.update_score()

            When X has a higher score.
            >>> C3D.current_points['X'] = 5
            >>> C3D.current_points['O'] = 1
            >>> C3D._get_winning_player()
            ['X']

            When both scores are the same.
            >>> C3D.current_points['O'] = 5
            >>> C3D._get_winning_player()
            ['O', 'X']

            When there are no winners.
            >>> C3D = Connect3D()
            >>> C3D.update_score()
            >>> C3D._get_winning_player()
            []
            """
            self.update_score()
            return get_max_dict_keys(self.current_points)

        @classmethod
        def from_string(cls, data):
            """Create new Connect3D instance from a string.

            Parameters:
                data (str): Passed in from __repr__, 
                    contains the grid data and current player.
                    Will still work if no player is defined.
                    Format: "joined(grid_data).current_player"
            """
            split_data = data.split('.')
            grid_data = [i if i != ' ' else '' for i in split_data[0]]
            new_c3d_instance = cls(calculate_grid_size(grid_data))

            new_c3d_instance.grid_data = grid_data

            if len(split_data) > 1:
                new_c3d_instance.current_player = split_data[1]

            return new_c3d_instance

        @classmethod
        def from_list(cls, grid_data, player=None):
            """Create new Connect3D instance from a list.

            Parameters:
                grid_data (list/tuple): 1D list of grid cells, amount must be a cube number.

                player (int or None): Current player to continue the game with.
            """
            new_c3d_instance = cls(calculate_grid_size(grid_data))

            new_c3d_instance.grid_data = [i if i != ' ' else '' for i in grid_data]

            if player is not None:
                new_c3d_instance.current_player = player

            return new_c3d_instance

        def play(self, player1=True, player2=False, grid_shuffle_chance=None):
            """Start or continue a game.
            If using computer players, there is a minimum time delay to avoid it instantly making moves.

            Parameters:
                player1 (bool): If player 1 is a human player.

                player2 (bool): If player 2 is a human player.

                grid_shuffle_chance (int, float or None, optional): Percentage chance to shuffle 
                    the grid after each turn.
                    Reverts to the default chance if left as None.
            """


            self.current_player = int(not self.current_player)
            min_time_update = 0.1


            #Game loop
            while True:

                current_time = time.time()

                #Switch current player
                self.current_player = int(not self.current_player)

                was_flipped = self.shuffle(chance=grid_shuffle_chance)

                #Display score and grid
                self.update_score()
                self._display_score = True
                print (self)
                self._display_score = False

                if was_flipped:
                    print ("Grid was flipped!")


                #Check if no spaces are left
                if '' not in self.grid_data:
                    winning_player = self._get_winning_player()
                    if len(winning_player) == 1:
                        # print ('Player {} won!'.format(winning_player[0]))
                         showinfo('WINNER','Player {} won!'.format(winning_player[0]))
                    else:
                         #print ('The game was a draw!')
                         showinfo('','The game was a draw!')

                    #Ask to play again and check if answer is a variant of 'yes' or 'ok'
                    #print ('Play again?')
                    #play_again = input().lower()
                    if askyesno('play','play again ?')==True:
                        #if any(i in play_again for i in ('y', 'k')):
                        SHIVAM()
                    if False:
                        return
                        break
                    else:
                        return
                        break


                #Player takes a move, function returns True if it updates the grid, otherwise loop again
                print ("Player {}'s turn...".format(self.player_symbols[self.current_player]))
                if (player1 and not self.current_player) or (player2 and self.current_player):
                    while not self.make_move(self.player_symbols[self.current_player], input().replace(',', ' ').replace('.', ' ').split()):
                        print ("Grid cell is not available, try again.")
                else:
                    ai_go = SimpleC3DAI(self, self.current_player).calculate_next_move()
                    if not self.make_move(self.player_symbols[self.current_player], ai_go):
                        raise Connect3DError('Something unknown went wrong with the AI')
                    else:
                        print ("AI moved to point {}.".format(PointConversion(self.grid_size, ai_go).to_3d()))

                    #Wait a short while
                    time.sleep(max(0, min_time_update, time.time()-current_time))
                print


        def make_move(self, id, *args):
            """Update the grid data with a new move.

            Parameters:
                id (str): Character to write into the grid.

                args (int, tuple or list): Where in the grid to place the ID.
                    Can be input as an integer (grid cell number), 3 integers,
                    a tuple or list (3D coordinates)

            >>> C3D = Connect3D(2)

            >>> C3D.make_move('a', 1)
            True
            >>> C3D.make_move('b', 1)
            False
            >>> C3D.make_move('c', -1)
            False
            >>> C3D.make_move('d', 2, 2, 2)
            True
            >>> C3D.make_move('e', [1, 1, 2])
            True
            >>> C3D.make_move('f', (1, 1, 3))
            False

            >>> C3D.grid_data
            ['', 'a', '', '', 'e', '', '', 'd']
            >>> print C3D
                 ________
                /   / a /|
               /___/___/ |
              /   /   /  |
             /___/___/   |
            |   |____|___|
            |   / e /|  /
            |  /___/_|_/
            | /   / d|/
            |/___/___|
            """

            #Convert points to the grid cell ID
            if len(args) == 1:
                if not str(args[0]).replace('-','').isdigit():
                    if len(args[0]) == 1:
                        try:
                            i = int(args[0][0])
                        except ValueError:
                            return False
                    else:
                        i = PointConversion(self.grid_size, args[0]).to_int()
                else:
                    i = int(args[0])
            else:
                i = PointConversion(self.grid_size, tuple(args)).to_int()

            #Add to grid if cell is empty
            if 0 <= i <len(self.grid_data) and not self.grid_data[i] and i is not None:
                self.grid_data[i] = id
                return True
            else:
                return False


        def shuffle(self, chance=None, second_chance=None, repeats=None, no_shuffle=[]):
            """Mirror the grid in the X, Y, or Z axis.

            Each time one of the directions is flipped, there is a 50% chance of it happening again.
            This means it has the same overall chance to flip, but it is not limited to a single axis.

            Parameters:
                chance:
                    Percent chance of a flip happening.
                    Default: 10
                    Type: int/float

                second_chance:
                    Percent chance of subsequent flips happening after the first.
                    Default: 50
                    Type: int/float

                repeats:
                    Number of attempts to flip at the above chance.
                    Default: 3
                    Type: int

                no_shuffle:
                    List of directions already flipped so it won't reverse anything.
                    Type: list
            """
            #Set defaults
            if chance is None:
                chance = 33
            if second_chance is None:
                second_chance = 50
            if repeats is None:
                repeats = 3

            #Calculate range of random numbers
            chance = min(100, chance)
            if chance > 0:
                chance = int(round(400/chance))-1

                #Attempt to flip grid
                for i in range(repeats):
                    shuffle_num = random.randint(0, chance)
                    if shuffle_num in (0, 1, 2, 3) and shuffle_num not in no_shuffle:
                        no_shuffle.append(shuffle_num)
                        if shuffle_num == 0:
                            self.grid_data = SwapGridData(self.grid_data).x()
                        if shuffle_num == 1:
                            self.grid_data = SwapGridData(self.grid_data).y()
                        if shuffle_num == 2:
                            self.grid_data = SwapGridData(self.grid_data).z()
                        if shuffle_num == 3:
                            self.grid_data = SwapGridData(self.grid_data).reverse()
                        if self.shuffle(chance=second_chance, no_shuffle=no_shuffle) or not not no_shuffle:
                            return True


        def update_score(self):
            """Recalculate the score.

            There are 26 total directions from each point, or 13 lines, calculated in 
            the DirectionCalculation() class. For each of the 13 lines, look both ways
            and count the number of values that match the current player.

            This will find any matches from one point, so it's simple to then iterate 
            through every point. A hash of each line is stored to avoid duplicates.
            """

            try:
                self.grid_data_last_updated
            except AttributeError:
                self.grid_data_last_updated = None

            if self.grid_data_last_updated != hash(tuple(self.grid_data)):

                #Store hash of grid_data in it's current state to avoid unnecessarily running the code again when there's been no changes
                self.grid_data_last_updated = hash(tuple(self.grid_data))


                self.current_points = defaultdict(int)
                all_matches = set()

                #Loop through each point
                for starting_point in range(len(self.grid_data)):

                    current_player = self.grid_data[starting_point]

                    if current_player:

                        for i in DirectionCalculation().opposite_direction:

                            #Get a list of directions and calculate movement amount
                            possible_directions = [list(i)]
                            possible_directions += [[j.replace(i, '') for i in possible_directions[0] for j in DirectionCalculation().direction_group.values() if i in j]]
                            direction_movement = sum(self.direction_maths[j] for j in possible_directions[0])

                            #Build list of invalid directions
                            invalid_directions = [[self.direction_edges[j] for j in possible_directions[k]] for k in (0, 1)]
                            invalid_directions = [join_list(j) for j in invalid_directions]

                            num_matches = 1
                            list_match = [starting_point]

                            #Use two loops for the opposite directions
                            for j in (0, 1):

                                current_point = starting_point

                                while current_point not in invalid_directions[j] and 0 < current_point < len(self.grid_data):
                                    current_point += direction_movement * int('-'[:j] + '1')
                                    if self.grid_data[current_point] == current_player:
                                        num_matches += 1
                                        list_match.append(current_point)
                                    else:
                                        break

                            #Add a point if enough matches
                            if num_matches == self.grid_size:

                                list_match = hash(tuple(sorted(list_match)))
                                if list_match not in all_matches:
                                    all_matches.add(list_match)
                                    self.current_points[current_player] += 1


        def show_score(self, digits=False, marker='/'):
            """Print the current points.

            Parameters:
                digits (bool, optional): If the score should be output as a number,
                    or as individual marks.

                marker (str, optional): How each point should be displayed if 
                    digits are not being used.

            >>> C3D = Connect3D()
            >>> C3D.update_score()
            >>> C3D.current_points['X'] = 5
            >>> C3D.current_points['O'] = 1

            >>> C3D.show_score(False, '/')
            'Player X: /////  Player O: /'
            >>> C3D.show_score(True)
            'Player X: 5  Player O: 1'
            """
            self.update_score()
            multiply_value = 1 if digits else marker
            return 'Player X: {x}  Player O: {o}'.format(x=multiply_value*(self.current_points['X']), o=multiply_value*self.current_points['O'])


        def reset(self):
            """Empty the grid without creating a new Connect3D object."""
            self.grid_data = ['' for i in range(pow(self.grid_size, 3))]


    class DirectionCalculation(object):
        """Calculate which directions are possible to move in, based on the 6 directions.
        Any combination is fine, as long as it doesn't go back on itself, hence why X, Y 
        and Z have been given two values each, as opposed to just using six values.

        Because the code to calculate score will look in one direction then reverse it, 
        the list then needs to be trimmed down to remove any duplicate directions (eg. 
        up/down and upright/downleft are both duplicates)

        The code will output the following results, it is possible to use these instead of the class.
            direction_group = {'Y': 'UD', 'X': 'LR', 'Z': 'FB', ' ': ' '}
            opposite_direction = ('B', 'D', 'DF', 'LDB', 'DB', 'L', 'LUB', 'LUF', 'LF', 'RU', 'LB', 'LDF', 'RD')
        """

        direction_group = {}
        direction_group['X'] = 'LR'
        direction_group['Y'] = 'UD'
        direction_group['Z'] = 'FB'
        direction_group[' '] = ' '

        #Come up with all possible directions
        all_directions = set()
        for x in [' ', 'X']:
            for y in [' ', 'Y']:
                for z in [' ', 'Z']:
                    x_directions = list(direction_group[x])
                    y_directions = list(direction_group[y])
                    z_directions = list(direction_group[z])
                    for i in x_directions:
                        for j in y_directions:
                            for k in z_directions:
                                all_directions.add((i+j+k).replace(' ', ''))

        #Narrow list down to remove any opposite directions
        opposite_direction = all_directions.copy()
        for i in all_directions:
            if i in opposite_direction:
                new_direction = ''
                for j in list(i):
                    for k in direction_group.values():
                        if j in k:
                            new_direction += k.replace(j, '')
                opposite_direction.remove(new_direction)


    class PointConversion(object):
        """Used to convert the cell ID to 3D coordinates or vice versa.
        Mainly used for inputting the coordinates to make a move.

        The cell ID is from 0 to grid_size^3, and coordinates are from 1 to grid_size.
        This means an ID of 0 is actually (1,1,1), and 3 would be (4,1,1).

                   - X -
                 __1___2_
            /  1/ 0 / 1 /|
           Y   /___/___/ |
          /  2/ 2 / 3 /  |
             /___/___/   |
            |   |____|___|
         | 1|   / 4 /|5 /
         Z  |  /___/_|_/
         | 2| / 6 / 7|/
            |/___/___|

        Parameters:
            grid_size:
                Size of the grid.
                Type: int

            i:
                Cell ID or coordinates.
                Type int/tuple/list

        Functions:
            to_3d
            to_int
        """
        def __init__(self, grid_size, i):
            self.grid_size = grid_size
            self.i = i

        def to_3d(self):
            """Convert cell ID to a 3D coordinate.

            >>> grid_size = 4
            >>> cell_id = 16

            >>> PointConversion(grid_size, cell_id).to_3d()
            (1, 1, 2)
            """
            cell_id = int(self.i)
            z = cell_id / pow(self.grid_size, 2) 
            cell_id %= pow(self.grid_size, 2)
            y = cell_id / self.grid_size
            x = cell_id % self.grid_size
            return tuple(cell_id+1 for cell_id in (x, y, z))

        def to_int(self):
            """Convert 3D coordinates to the cell ID.

            >>> grid_size = 4
            >>> coordinates = (4,2,3)

            >>> PointConversion(grid_size, coordinates).to_int()
            39
            """
            x, y, z = [int(i) for i in self.i]
            if all(i > 0 for i in (x, y, z)):
                return (x-1)*pow(self.grid_size, 0) + (y-1)*pow(self.grid_size, 1) + (z-1)*pow(self.grid_size, 2)
            return None


    class SwapGridData(object):
        """Use the size of the grid to calculate how flip it on the X, Y, or Z axis.
        The flips keep the grid intact but change the perspective of the game.

        Parameters:
            grid_data (list/tuple): 1D list of grid cells, amount must be a cube number.
        """
        def __init__(self, grid_data):
            self.grid_data = list(grid_data)
            self.grid_size = calculate_grid_size(self.grid_data)

        def x(self):
            """Flip on the X axis.

            >>> SwapGridData(range(8)).x()
            [1, 0, 3, 2, 5, 4, 7, 6]
            >>> print Connect3D.from_list(SwapGridData(range(8)).x())
                 ________
                / 1 / 0 /|
               /___/___/ |
              / 3 / 2 /  |
             /___/___/   |
            |   |____|___|
            |   / 5 /|4 /
            |  /___/_|_/
            | / 7 / 6|/
            |/___/___|
            """
            return join_list(x[::-1] for x in split_list(self.grid_data, self.grid_size))

        def y(self):
            """Flip on the Y axis.

            >>> SwapGridData(range(8)).y()
            [2, 3, 0, 1, 6, 7, 4, 5]
            >>> print Connect3D.from_list(SwapGridData(range(8)).y())
                 ________
                / 2 / 3 /|
               /___/___/ |
              / 0 / 1 /  |
             /___/___/   |
            |   |____|___|
            |   / 6 /|7 /
            |  /___/_|_/
            | / 4 / 5|/
            |/___/___|
            """
            group_split = split_list(self.grid_data, pow(self.grid_size, 2))
            return join_list(join_list(split_list(x, self.grid_size)[::-1]) for x in group_split)

        def z(self):
            """Flip on the Z axis.

            >>> SwapGridData(range(8)).z()
            [4, 5, 6, 7, 0, 1, 2, 3]
            >>> print Connect3D.from_list(SwapGridData(range(8)).z())
                 ________
                / 4 / 5 /|
               /___/___/ |
              / 6 / 7 /  |
             /___/___/   |
            |   |____|___|
            |   / 0 /|1 /
            |  /___/_|_/
            | / 2 / 3|/
            |/___/___|
            """
            return join_list(split_list(self.grid_data, pow(self.grid_size, 2))[::-1])

        def reverse(self):
            """Reverse the grid.

            >>> SwapGridData(range(8)).reverse()
            [7, 6, 5, 4, 3, 2, 1, 0]
            >>> print Connect3D.from_list(SwapGridData(range(8)).reverse())
                 ________
                / 7 / 6 /|
               /___/___/ |
              / 5 / 4 /  |
             /___/___/   |
            |   |____|___|
            |   / 3 /|2 /
            |  /___/_|_/
            | / 1 / 0|/
            |/___/___|
            """
            return self.grid_data[::-1]


    def calculate_grid_size(grid_data):
        """Cube root the length of grid_data to find the grid size."""
        return int(round(pow(len(grid_data), 1.0/3.0), 0))


    def split_list(x, n):
        """Split a list by n characters."""
        n = int(n)
        return [x[i:i+n] for i in range(0, len(x), n)]


    def join_list(x):
        """Convert nested lists into one single list."""
        return [j for i in x for j in i]


    def get_max_dict_keys(x):
        """Return a list of every key containing the max value.

        Parameters:
            x (dict): Dictionary to sort and get highest value.
                It must be a dictionary of integers to work properly.
        """
        if x:
            sorted_dict = sorted(x.items(), key=operator.itemgetter(1), reverse=True)
            if sorted_dict[0][1]:
                return sorted([k for k, v in x.items() if v == sorted_dict[0][1]])
        return []


    class SimpleC3DAI(object):
        """AI coded to play Connect3D."""

        def __init__(self, C3DObject, player_num):
            """Set up the AI for a single move using the current state of Connect3D."""
            self.C3DObject = C3DObject
            self.player_num = player_num
            self.player = self.C3DObject.player_symbols[self.player_num]
            self.enemy = self.C3DObject.player_symbols[int(not self.player_num)]
            self.gd_len = len(self.C3DObject.grid_data)

        def max_cell_points(self):
            """Get maximum number of points that can be gained from each empty cell,
            that is not blocked by an enemy value.
            """
            max_points = defaultdict(int)
            filled_grid_data = [i if i else self.player for i in self.C3DObject.grid_data]
            for cell_id in range(self.gd_len):
                if cell_id == self.player:
                    max_points[cell_id] += self.check_grid(filled_grid_data, cell_id, self.player)
            return get_max_dict_keys(max_points)

        def check_for_n_minus_one(self, grid_data=None):
            """Find all places where anyone has n-1 points in a row, by substituting
            in a point for each player in every cell.

            Parameters:
                grid_data (list or None, optional): Pass in a custom grid_data, 
                    leave as None to use the Connect3D one.
            """
            if grid_data is None:
                grid_data = list(self.C3DObject.grid_data)

            matches = defaultdict(list)
            for cell_id in range(len(grid_data)):
                if not grid_data[cell_id]:
                    for current_player in (self.player, self.enemy):
                        if self.check_grid(grid_data, cell_id, current_player):
                            matches[current_player].append(cell_id)
            return matches

        def look_ahead(self):
            """Look two moves ahead to detect if someone could get a point.
            Uses the check_for_n_minus_one function from within a loop.

            Will return 1 as the second parameter if it has looked up more than a single move.
            """
            #Try initial check
            match = self.check_for_n_minus_one()
            if match:
                return (match, 0)

            #For every grid cell, substitute a player into it, then do the check again
            grid_data = list(self.C3DObject.grid_data)
            for i in range(self.gd_len):
                if not self.C3DObject.grid_data[i]:
                    old_value = grid_data[i]
                    for current_player in (self.player, self.enemy):
                        grid_data[i] = current_player
                        match = self.check_for_n_minus_one(grid_data)
                        if match:
                            return (match, 1)
                    grid_data[i] = old_value

            return (defaultdict(list), 0)

        def check_grid(self, grid_data, cell_id, player):
            """Duplicate of the Connect3D.update_score method, but set up to check individual cells.

            Parameters:
                grid_data (list/tuple): 1D list of grid cells, amount must be a cube number.

                cell_id (int): The cell ID, or grid_data index to update.

                player (int): Integer representation of the player, can be 0 or 1.
            """
            max_points = 0
            for i in DirectionCalculation().opposite_direction:

                #Get a list of directions and calculate movement amount
                possible_directions = [list(i)]
                possible_directions += [[j.replace(i, '') for i in possible_directions[0] for j in DirectionCalculation().direction_group.values() if i in j]]
                direction_movement = sum(self.C3DObject.direction_maths[j] for j in possible_directions[0])

                #Build list of invalid directions
                invalid_directions = [[self.C3DObject.direction_edges[j] for j in possible_directions[k]] for k in (0, 1)]
                invalid_directions = [join_list(j) for j in invalid_directions]

                num_matches = 1

                #Use two loops for the opposite directions
                for j in (0, 1):

                    current_point = cell_id

                    while current_point not in invalid_directions[j] and 0 < current_point < len(grid_data):
                        current_point += direction_movement * int('-'[:j] + '1')
                        if grid_data[current_point] == player:
                            num_matches += 1
                        else:
                            break

                #Add a point if enough matches
                if num_matches == self.C3DObject.grid_size:
                     max_points += 1

            return max_points

        def calculate_next_move(self):
            """Groups together the AI methods in order of importance.
            Will throw an error if grid_data is full, since the game should have ended by then anyway.
            """

            next_moves = []

            if len(''.join(self.C3DObject.grid_data)) > (self.C3DObject.grid_size-2) * 2:

                point_based_move, far_away = SimpleC3DAI(self.C3DObject, self.player_num).look_ahead()
                order_of_importance = [self.enemy, self.player][::int('-'[:int(far_away)]+'1')]
                grid_data_len = len(''.join(self.C3DObject.grid_data))

                state = None

                if point_based_move:
                    if point_based_move[self.enemy]:
                        next_moves = point_based_move[self.enemy]
                        state = 'Blocking opposing player'

                    elif point_based_move[self.player]:
                        next_moves = point_based_move[self.player]
                        state = 'Gaining points'

                else:
                    next_moves = self.max_cell_points()
                    state = 'Random placement'

                if not next_moves:
                    next_moves = [i for i in range(self.gd_len) if not self.C3DObject.grid_data[i]]
                    if state is None:
                        state = 'Struggling'

            else:
                next_moves = [i for i in range(self.gd_len) if not self.C3DObject.grid_data[i]]
                state = 'Starting'

            print ('AI Objective: ' + state + '.')

            return random.choice(next_moves)


    if __name__ == '__main__':
        c3d = Connect3D()
        c3d.play(True, False)
SHIVAM()
