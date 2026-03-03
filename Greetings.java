public class UserGreeting {

    public static void greet(String name) {
        if (name == null || name.trim().isEmpty()) {
            System.out.println("Welcome to Luna Assistant!");
        } else {
            System.out.println("Welcome " + name + " to Luna Assistant!");
        }
    }
}