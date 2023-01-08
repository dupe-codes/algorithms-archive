(ns org.dupe.main
  (:gen-class))

(defn -main
      "Hello"
      [& args]
      (apply println "Hello world! I am Clojure!" args))