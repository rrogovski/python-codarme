my_string = "Is this a string?"
my_int = 42
my_float = 3.1415
my_bool = True

my_array_of_types = [my_string, my_int, my_float, my_bool]

for i in range(len(my_array_of_types)):
    print(f"What type is this? : {my_array_of_types[i]} => This is a {type(my_array_of_types[i])}")