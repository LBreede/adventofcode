string wirepath = chs("wirepath");
string dirlist[] = split(wirepath, ",");

float x = 0.0, y = 0.0, z = 0.0;
vector pos = set(x,y,z);
int first = addpoint(geoself(), pos);
int pts[] = array(first);

string d; int n, pt;

foreach(string dir; dirlist)
{
    d = dir[0];
    n = atoi(dir[1:]);
    
    for (int i=0; i<n; i++)
    {
        if      (d == "U") y += 1;
        else if (d == "R") x += 1;
        else if (d == "D") y -= 1;
        else if (d == "L") x -= 1;
    }
    pos = set(x,y,z);
    pt = addpoint(geoself(), pos);
    append(pts, pt);
}

addprim(geoself(), "polyline", pts);