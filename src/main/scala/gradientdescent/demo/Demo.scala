package gradientdescent.demo

import gradientdescent.impl.GradientDescent

object Demo {

  def main(args: Array[String]): Unit = {
    val gradientDescent = new GradientDescent()
    println(gradientDescent.descend)
  }

}
