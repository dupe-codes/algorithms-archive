package demo

object App {
  def main(args: Array[String]): Unit = {
    println(greeting())
  }

  private def greeting(): String = "Hello, world! I am Scala!"
}
