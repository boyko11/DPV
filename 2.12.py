def fun(n):
    if n > 1:
        print("still going")
        fun(n/2)
        fun(n/2)

fun(16)