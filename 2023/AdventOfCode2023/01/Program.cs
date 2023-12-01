var test1 = Part1("test01.txt");
var part1 = Part1("01.txt");
var test2 = Part2("test02.txt");
var part2 = Part2("01.txt");

Console.WriteLine(test1);
Console.WriteLine(part1);
Console.WriteLine(test2);
Console.WriteLine(part2);
Console.ReadKey();

static int Part1(string fileName)
{
    var lines = File.ReadAllLines(fileName);
    var total = 0;

    foreach (var line in lines)
    {
        var curr = 0;

        for (int i = 0; i < line.Length; i++)
        {
            if (char.IsDigit(line[i]))
            {
                curr *= 10;
                curr += line[i] - '0';
                break;
            }
        }

        for (int i = line.Length - 1; i >= 0; i--)
        {
            if (char.IsDigit(line[i]))
            {
                curr *= 10;
                curr += line[i] - '0';
                break;
            }
        }


        total += curr;
    }

    return total;
}

static int Part2(string fileName)
{
    var lines = File.ReadAllLines(fileName);
    var total = 0;

    var nums = new Dictionary<string, int>
    {
        { "one", 1 },
        { "two", 2 },
        { "six", 6 },

        { "four", 4 },
        { "five", 5 },
        { "nine", 9 },

        { "three", 3 },
        { "seven", 7 },
        { "eight", 8 }
    };

    foreach (var line in lines)
    {
        var three = "";
        var four = "";
        var five = "";
        var first = -1;
        var last = -1;

        for (int i = 0; i < line.Length; i++)
        {
            var c = line[i];

            three += c;
            four += c;
            five += c;

            if (three.Length > 3)
                three = three.Remove(0, 1);

            if (four.Length > 4)
                four = four.Remove(0, 1);

            if (five.Length > 5)
                five = five.Remove(0, 1);

            if (char.IsDigit(c))
            {
                if (first == -1)
                    first = c - '0';

                last = c - '0';
            }

            if (nums.ContainsKey(three))
            {
                if (first == -1)
                    first = nums[three];

                last = nums[three];
            }

            if (nums.ContainsKey(four))
            {
                if (first == -1)
                    first = nums[four];

                last = nums[four];
            }

            if (nums.ContainsKey(five))
            {
                if (first == -1)
                    first = nums[five];

                last = nums[five];
            }
        }

        var tmp = Convert.ToInt32(first.ToString() + last.ToString());
        total += tmp;
    }

    return total;
}