def fun_b():
    print("---2----")
def fun_a():
    print("---1----")
    fun_b()
    print("----3----")
fun_a()  