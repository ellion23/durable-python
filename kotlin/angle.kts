//fun main() {
//    val nook = -192
//    if (nook in 1..89) {
//        print("Острий")
//    }else if (nook == 90) {
//        print("Сядь прямо")
//    }else if (nook in 91..179) {
//        print("Тупий")
//    }else if (nook == 180) {
//        print("Развернись!")
//    }else {
//        print("Не, ну ты... " + (360-nook))
//    }
//}
//
//main()

fun main() {
    val ugl = 90
    val faction = when(ugl) {
        in 1..89 -> "Острий"
        90 -> "Прямий"
        in 91..179 -> "Тупий"
        180 -> "Развернутий"
        else -> "undefined"
    }
    print(faction)
}
main()