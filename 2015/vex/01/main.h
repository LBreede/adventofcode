//--- Day 1: Not Quite Lisp ---

string input = s@input;

int floor = 0;
int i = 1;
int floor_trigger = -1;

foreach (string c; input)
{
    floor += c == "(";
    floor -= c == ")";
    
    if (floor < 0 && floor_trigger == -1) {
        floor_trigger = i;
    }
    else {
        i++;
    }
}

i@output_1 = floor;
i@output_2 = floor_trigger;

printf("The instructions take Santa to the " + itoa(floor) + "th floor.\n");
printf("Character position " + itoa(floor_trigger) + " causes Santa to first enter the basement.\n");