import java.io.File

fun NOD(a: Int, b: Int): Int = if (b == 0) a else NOD(b, a % b)

fun main() {
    var pList = mutableListOf<kotlin.Int>()
    var f: List<String> = File("data/inpet.txt")
            .readText()
            .split(" ")
    for (i in f) {
        var c = i.toInt()
        pList.add(c)
    }
    var no = pList[0]
    for (i: Int in pList) {
        no = NOD(i, no)
    }
    print(no)
}
