import kotlin.math.max

fun main() {
    val year = 2400

    if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)) {
        print("Yes.")
    }else {
        print("No.")
    }
}
main()