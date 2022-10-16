// Creating Abstract Class
abstract class Abs {
  // Creating Abstract Methods
  void say();
  void write();
}

class AbstractClass extends Abs {
  @override
  void say() {
    print("Yo Yo!!");
  }

  @override
  void write() {
    print("Dart Abstract Class");
  }
}

main() {
  AbstractClass abst = AbstractClass();
  abst.say();
  abst.write();
}
