string input = chs("input");
string linelist[] = split(input, "\n");
string direction, amount;

string better_linelist[];
foreach(string L; linelist)
{
    direction = split(L, " ")[0];
    amount = split(L, " ")[1];
    append(better_linelist, direction);
    append(better_linelist, amount);
}

int i = 0;
string dir;
int x;
int horizontal = 0;
int depth = 0;
int aim = 0;

vector pos = set(horizontal, -depth, 0.0);
int pt = addpoint(geoself(), pos);

setpointattrib(geoself(), "horizontal", pt, horizontal);
setpointattrib(geoself(), "depth", pt, depth);
setpointattrib(geoself(), "aim", pt, aim);

int pts[] = array(pt);

while (i < len(better_linelist))
{
    dir = better_linelist[i];
    x = atoi(better_linelist[i+1]);
    
    if (dir == "forward")
    {
        horizontal += x;
        depth += aim * x;
    }
    else if (dir == "up")   aim -= x;
    else if (dir == "down") aim += x;
    
    pos = set(horizontal, -depth, 0.0);
    pt = addpoint(geoself(), pos);
    
    setpointattrib(geoself(), "horizontal", pt, horizontal);
    setpointattrib(geoself(), "depth", pt, depth);
    setpointattrib(geoself(), "aim", pt, aim);
    
    append(pts, pt);
    
    i += 2;
}
addprim(geoself(), "polyline", pts);