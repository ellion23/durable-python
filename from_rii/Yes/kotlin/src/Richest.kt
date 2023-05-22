import java.io.File
fun main() {
    var spy_sock: MutableMap<String, Int> = mutableMapOf()
    val f = File("data/inpot.txt")
            .readText()
            .split("\n")
    for (i in f) {
        var raw_num = i.strip().split(" ")
        spy_sock[raw_num[0]] = raw_num[1].strip().toInt()
    }
    println(spy_sock)
}