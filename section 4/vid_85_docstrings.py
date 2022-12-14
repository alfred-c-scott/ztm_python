def test(a):
    """
    Info: this function tests and prints a param
    """
    print(a)

# after the docstring in triple quotes above is added you can hover over the test() function in an editor
# and the text within the docstring will be displayed - try it below
test('!!!!')

help(test)

print(test.__doc__)
