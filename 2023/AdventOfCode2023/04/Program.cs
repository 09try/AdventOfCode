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
    var lines = File.ReadLines(path);

    foreach (var line in lines)
    {
        ProcessLine(line, out List<int> yourNums, out List<int> winNums);

        var points = 0;

        foreach (var n in yourNums)
        {
            if (winNums.Contains(n))
                if (points > 0)
                    points *= 2;
                else
                    points++;
        }

        res += points;
    }

    return res;
}

int Part2(string path)
{
    var res = 0;
    var lines = File.ReadLines(path).ToList();
    var queue = new Queue<int>();
    var cache = new Dictionary<int, int>();
    var card = 1;

    foreach (var line in lines)
    {
        ProcessLine(line, out List<int> yourNums, out List<int> winNums);

        var matches = 0;

        foreach (var n in yourNums)
            if (winNums.Contains(n))
                matches++;

        res++;

        cache.Add(card, matches);

        for (int i = 0; i < matches; i++)
            queue.Enqueue(card + i + 1);

        card++;
    }

    while (queue.Count > 0)
    {
        int currCard = queue.Dequeue();
        var matches = cache[currCard];

        res++;

        for (int i = 0; i < matches; i++)
            queue.Enqueue(currCard + i + 1);
    }

    return res;
}

void ProcessLine(string line, out List<int> yourNums, out List<int> winNums)
{
    winNums = new List<int>();
    yourNums = new List<int>();

    var win = false;
    var your = false;
    var curr = "";

    var i = 6;

    while (i < line.Length)
    {
        if (line[i] == ' ' && win)
        {
            if (int.TryParse(curr, out int n))
                winNums.Add(n);

            curr = "";
        }

        if (line[i] == ' ' && your)
        {
            if (int.TryParse(curr, out int n))
                yourNums.Add(n);

            curr = "";
        }

        if (win || your)
            curr += line[i];

        if (line[i] == ':')
            win = true;

        if (line[i] == '|')
        {
            win = false;
            your = true;
        }

        i++;
    }

    yourNums.Add(Convert.ToInt32(curr));
}