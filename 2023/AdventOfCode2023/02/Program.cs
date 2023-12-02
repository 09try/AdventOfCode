var test1 = Part1("test01.txt");
var part1 = Part1("01.txt");
var test2 = Part2("test02.txt");
var part2 = Part2("01.txt");

Console.WriteLine(test1);
Console.WriteLine(part1);
Console.WriteLine(test2);
Console.WriteLine(part2);
Console.ReadKey();

static int Part1(string path)
{
    var res = 0;

    var lines = File.ReadAllLines(path);
    var limit = new Dictionary<string, int>
    {
        { "red", 12 },
        { "green", 13 },
        { "blue", 14 }
    };

    foreach (var line in lines)
    {
        var cnt = new Dictionary<string, int>
        {
            { "red", 0 },
            { "green", 0 },
            { "blue", 0 }
        };

        var splitRes = line.Split(':');
        var game = Convert.ToInt32(splitRes[0].Replace("Game ", ""));
        var sets = splitRes[1].Split(';');
        bool possible = true;

        for (int i = 0; i < sets.Length && possible; i++)
        {
            var set = sets[i];

            var cubes = set.Split(',');

            foreach (var cube in cubes)
            {
                var color = "";
                var count = "";

                foreach (var c in cube)
                {
                    if (char.IsLetter(c))
                        color += c;

                    if (char.IsDigit(c))
                        count += c;
                }

                cnt[color] += Convert.ToInt32(count);

                if (Convert.ToInt32(count) > limit[color])
                {
                    possible = false;
                    break;
                }
            }
        }

        if (possible)
            res += game;
    }

    return res;
}

static int Part2(string path)
{
    var res = 0;

    var lines = File.ReadAllLines(path);

    foreach (var line in lines)
    {
        var cnt = new Dictionary<string, int>
        {
            { "red", 0 },
            { "green", 0 },
            { "blue", 0 }
        };

        var splitRes = line.Split(':');
        var game = Convert.ToInt32(splitRes[0].Replace("Game ", ""));
        var sets = splitRes[1].Split(';');

        for (int i = 0; i < sets.Length; i++)
        {
            var set = sets[i];

            var cubes = set.Split(',');

            foreach (var cube in cubes)
            {
                var color = "";
                var count = "";

                foreach (var c in cube)
                {
                    if (char.IsLetter(c))
                        color += c;

                    if (char.IsDigit(c))
                        count += c;
                }

                cnt[color] = Math.Max(Convert.ToInt32(count), cnt[color]);
            }
        }

        res += cnt["red"] * cnt["green"] * cnt["blue"];
    }

    return res;
}