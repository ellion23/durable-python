//val scan = java.util.Scanner(System.`in`)
val scan = java.util.Scanner(System.`in`).useLocale(java.util.Locale.JAPANESE)

fun main() {
    println("Napishitedvachisla: ")
    val a = scan.nextInt()
    val b = scan.nextDouble()
    println("Your payment for this week is $a $b")
}
main()