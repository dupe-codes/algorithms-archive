package gradientdescent.impl

import breeze.linalg

class GradientDescent {

  // Initialize with (1) function takes current variables and returns gradient vector


  // Guess initial x(0), k = 0
  //
  // while gradient greater than epsilon OR number of iterations < desired epochs
  //  compute gradient vector given x(i)or
  //  compute x(i+1) = x(i) - eta * (gradient vector)
  //  k = k + 1
  //
  // return x(k)

  def descend: linalg.Vector[Double] = {
    val nums = linalg.Vector(1.0)
    nums + linalg.Vector(2.0)
  }


}
