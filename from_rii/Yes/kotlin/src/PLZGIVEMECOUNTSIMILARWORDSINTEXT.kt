import java.io.File

fun main() {
    var f = File("data/inpat.txt")
            .readText()
            .split(" ").toSet()
    println(f)
    print("Miss compliment")
}