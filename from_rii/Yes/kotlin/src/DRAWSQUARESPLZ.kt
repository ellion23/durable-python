fun main() {
    var L1 = mutableListOf<Int>(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
    var L2 = mutableListOf<Int>()
    for (i in L1) {
        L2.add(i*i)
    }
    print(L2)
}

