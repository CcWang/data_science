# assume one of the argument could be certain value, than assign that value to the 
# argument, so you could skip pass that argument
def add_numbers(x,y,z=None):
	if(z ==None):
		return x+y;
	else:
		return x+y+z;

print(add_numbers(1,2));
print(add_numbers(1,2,3));

def add_number(x, y, kind="add"):
	if(kind == 'add'):
		return ("it is add", x+y);
	else:
		return ("it is not add", y-x);

print (add_number(8,10));
print(add_number(180, 250, 'not add'));