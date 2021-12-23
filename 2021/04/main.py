class Board:
    def __init__(self, width, height):
        self.rows = []
        self.width = width
        self.height = height
        self.won = False

        for i in range(self.height):
            row = []
            for _ in range(self.width):
                row.append(MyNumber(0))
            self.rows.append(row)

    def info(self):
        msg = ''
        for row in range(self.height):
            for column in range(self.width):
                current_number = self.rows[row][column]

                current_number_str = ''
                if current_number.value < 10:
                    current_number_str += ' '

                current_number_str += str(current_number.value) + ' - ' + str(
                    current_number.is_marked)

                if column == self.width - 1:
                    msg += current_number_str
                else:
                    msg += current_number_str + ', '
            msg += '\n'
        return msg

    def get_board_sum(self):
        sum = 0
        for row in range(self.height):
            for column in range(self.width):
                current_number = self.rows[row][column]
                if current_number.is_marked == False:
                    sum += current_number.value

        return sum

    def mark_number(self, number):
        for row in range(self.height):
            for column in range(self.width):
                current_number = self.rows[row][column]

                if current_number.value == number:
                    current_number.is_marked = True

    def is_winner(self):

        if self.won == True:
            return False

        # rows
        for row in range(self.height):
            sum = 0
            for column in range(self.width):
                current_number = self.rows[row][column]
                if current_number.is_marked:
                    sum += 1

            if sum == self.width:
                self.won = True
                return True

        # columns
        for column in range(self.width):
            sum = 0
            for row in range(self.height):
                current_number = self.rows[row][column]
                if current_number.is_marked:
                    sum += 1

            if sum == self.height:
                self.won = True
                return True

        return False


class MyNumber:
    def __init__(self, value):
        self.value = value
        self.is_marked = False


def my_split(line):
    numbers = []

    for i in range(0, len(line) - 1, 3):
        num = line[i] + line[i + 1]
        numbers.append(int(num))

    return numbers


if __name__ == '__main__':

    width = 5
    height = 5

    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()

    drawn_numbers = [int(x) for x in lines[0].split(',')]
    print(drawn_numbers)

    boards = []
    for i in range(2, len(lines), 6):
        board = Board(width, height)
        for j in range(width):
            numbers = [x for x in my_split(lines[i + j])]
            for k in range(height):
                board.rows[j][k] = MyNumber(numbers[k])

        boards.append(board)

    print(len(boards))

    print(boards[0].info())
    print(boards[len(boards) - 1].info())

    for number in drawn_numbers:
        for board in boards:
            board.mark_number(number)
            
            if board.is_winner():
                sum = board.get_board_sum()
                final_score = sum * number
                print(final_score)