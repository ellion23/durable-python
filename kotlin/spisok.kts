fun main() {
    val patronList= mutableListOf("Sara", "Rabinovich", "Yosa", "Mikhail")
    patronList.forEachIndexed { index, patron -> println("Move! You are on a place #${index+1} in oven's list... $patron.") }
}
main()