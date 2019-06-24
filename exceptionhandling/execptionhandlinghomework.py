cars = {'make': 'bmw', 'model': '550i', 'year': '2016'}


def exceptionHandling():
    try:
        print(cars['color'])
    except:
        print("In except block")
    finally:
        print("In finally block")

exceptionHandling()