

def test_function(number, yes):
    return yes * number
hello = test_function(5, test_function(3, ' Hello There\n'))
print(hello)