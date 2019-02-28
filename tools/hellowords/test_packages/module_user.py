from hellowords.test_packages.simple_module import strong_computations
from bubble_sort import strange_bubble_sort
def more_strong_computations():
    print("module_user.more_strong_computations")
    print(strong_computations())
    print("running bubble sort")
    print(strange_bubble_sort([1,2,5,3]))

if __name__ == '__main__':
    print(strong_computations())