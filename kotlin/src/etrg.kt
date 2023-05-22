fun main() {
    var nu_tipa = 0.0
    var dnu_tipa:Double
    while (true) {
        dnu_tipa = readLine()!!.toDouble()
        nu_tipa += dnu_tipa
        if (dnu_tipa == 0.0) {
            break
        }
    }
    print(nu_tipa)
}
