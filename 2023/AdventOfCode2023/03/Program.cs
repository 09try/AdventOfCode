var test1 = Part1("test01.txt");
var part1 = Part1("01.txt");
var test2 = Part2("test01.txt");
var part2 = Part2("01.txt");

Console.WriteLine(test1);
Console.WriteLine(part1);
Console.WriteLine(test2);
Console.WriteLine(part2);
Console.ReadKey();

int Part1(string path)
{
    var res = 0;
    var used = new HashSet<(int, int)>();
    var usedR = 0;

    string[] lines = File.ReadAllLines(path);
    var grid = new char[lines.Length, lines[0].Length];

    for (int i = 0; i < lines.Length; i++)
        for (int j = 0; j < lines[0].Length; j++)
            grid[i, j] = lines[i][j];

    var R = grid.GetLength(0);
    var C = grid.GetLength(1);

    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            if (grid[i, j] != '.' && !char.IsDigit(grid[i, j]))
            {
                // up
                if (i - 1 >= 0 && char.IsDigit(grid[i - 1, j]))
                    res += GetNum(used, grid, i - 1, j, C);

                // down
                if (i + 1 < R && char.IsDigit(grid[i + 1, j]))
                    res += GetNum(used, grid, i + 1, j, C);

                // left
                if (j - 1 >= 0 && char.IsDigit(grid[i, j - 1]))
                    res += GetNum(used, grid, i, j - 1, C);

                // right
                if (j + 1 < C && char.IsDigit(grid[i, j + 1]))
                    res += GetNum(used, grid, i, j + 1, C);

                // up left
                if (i - 1 >= 0 && j - 1 >= 0 && char.IsDigit(grid[i - 1, j - 1]))
                    res += GetNum(used, grid, i - 1, j - 1, C);

                // up right
                if (i - 1 >= 0 && j + 1 < C && char.IsDigit(grid[i - 1, j + 1]))
                    res += GetNum(used, grid, i - 1, j + 1, C);

                // down left
                if (i + 1 < R && j - 1 >= 0 && char.IsDigit(grid[i + 1, j - 1]))
                    res += GetNum(used, grid, i + 1, j - 1, C);

                // down right
                if (i + 1 < R && j + 1 < C && char.IsDigit(grid[i + 1, j + 1]))
                    res += GetNum(used, grid, i + 1, j + 1, C);
            }
        }

        usedR++;

        if (usedR > 1)
            used = new HashSet<(int, int)>();
    }

    return res;
}

int Part2(string path)
{
    var res = 0;
    var used = new HashSet<(int, int)>();
    var usedR = 0;

    string[] lines = File.ReadAllLines(path);
    var grid = new char[lines.Length, lines[0].Length];

    for (int i = 0; i < lines.Length; i++)
        for (int j = 0; j < lines[0].Length; j++)
            grid[i, j] = lines[i][j];

    var R = grid.GetLength(0);
    var C = grid.GetLength(1);

    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            if (grid[i, j] == '*')
            {
                var cnt = 0;

                // up
                if (i - 1 >= 0 && char.IsDigit(grid[i - 1, j]))
                    cnt++;

                // down
                if (i + 1 < R && char.IsDigit(grid[i + 1, j]))
                    cnt++;

                // left
                if (j - 1 >= 0 && char.IsDigit(grid[i, j - 1]))
                    cnt++;

                // right
                if (j + 1 < C && char.IsDigit(grid[i, j + 1]))
                    cnt++;

                // up left
                if (i - 1 >= 0 && j - 1 >= 0 && char.IsDigit(grid[i - 1, j - 1]))
                    cnt++;

                // up right
                if (i - 1 >= 0 && j + 1 < C && char.IsDigit(grid[i - 1, j + 1]))
                    cnt++;

                // down left
                if (i + 1 < R && j - 1 >= 0 && char.IsDigit(grid[i + 1, j - 1]))
                    cnt++;

                // down right
                if (i + 1 < R && j + 1 < C && char.IsDigit(grid[i + 1, j + 1]))
                    cnt++;

                if (cnt < 2)
                    continue;

                var nums = new List<int>();

                // up
                if (i - 1 >= 0 && char.IsDigit(grid[i - 1, j]))
                {
                    var n = GetNum(used, grid, i - 1, j, C);
                    if (n != 0)
                        nums.Add(n);
                }

                // down
                if (i + 1 < R && char.IsDigit(grid[i + 1, j]))
                {
                    var n = GetNum(used, grid, i + 1, j, C);
                    if (n != 0)
                        nums.Add(n);
                }

                // left
                if (j - 1 >= 0 && char.IsDigit(grid[i, j - 1]))
                {
                    var n = GetNum(used, grid, i, j - 1, C);
                    if (n != 0)
                        nums.Add(n);
                }

                // right
                if (j + 1 < C && char.IsDigit(grid[i, j + 1]))
                {
                    var n = GetNum(used, grid, i, j + 1, C);
                    if (n != 0)
                        nums.Add(n);
                }

                // up left
                if (i - 1 >= 0 && j - 1 >= 0 && char.IsDigit(grid[i - 1, j - 1]))
                {
                    var n = GetNum(used, grid, i - 1, j - 1, C);
                    if (n != 0)
                        nums.Add(n);
                }

                // up right
                if (i - 1 >= 0 && j + 1 < C && char.IsDigit(grid[i - 1, j + 1]))
                {
                    var n = GetNum(used, grid, i - 1, j + 1, C);
                    if (n != 0)
                        nums.Add(n);
                }

                // down left
                if (i + 1 < R && j - 1 >= 0 && char.IsDigit(grid[i + 1, j - 1]))
                {
                    var n = GetNum(used, grid, i + 1, j - 1, C);
                    if (n != 0)
                        nums.Add(n);
                }

                // down right
                if (i + 1 < R && j + 1 < C && char.IsDigit(grid[i + 1, j + 1]))
                {
                    var n = GetNum(used, grid, i + 1, j + 1, C);
                    if (n != 0)
                        nums.Add(n);
                }

                if (nums.Count == 2)
                    res += nums[0] * nums[1];
            }
        }

        usedR++;

        if (usedR > 1)
            used = new HashSet<(int, int)>();
    }

    return res;
}

int GetNum(HashSet<(int, int)> used, char[,] grid, int r, int c, int C)
{
    var num = 0;

    var t = c - 1;
    while (t >= 0 && char.IsDigit(grid[r, t]))
        t--;

    t++;

    while (t < C && char.IsDigit(grid[r, t]))
    {
        if (used.Contains((r, t)))
            return 0;

        num *= 10;
        num += grid[r, t] - '0';

        used.Add((r, t));
        t++;
    }

    return num;
}
