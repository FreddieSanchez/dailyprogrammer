object disemvowler extends App{
 def disemvowler(str:String): (String,String) = 
  (str.filter(_.isLetter).partition(c => !"aeiou".contains(c)))
  
  val results = for { s <- io.Source.stdin.getLines } yield disemvowler(s)
  results foreach { case (x: String,y:String) => println (x + " " + y) }
}
