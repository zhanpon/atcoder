fun main() {
    val n = readLine()!!.toInt()

    val items = mutableSetOf<String>()
    repeat(n) {
        items.add(readLine()!!)
    }

    println(items.size)
}
