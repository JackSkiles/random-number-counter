

def test_function(number, yes):
    counter = 0
    while counter < number:
        print(yes)
        counter += 1

print(test_function(4, 'Hello There'))