public class Main {
    public static void main(String[] args) {
        Cookie cookieOne = new Cookie("Brown");
        Cookie cookieTwo = new Cookie("Green");

        cookieOne.setColor("Pink");

        System.out.println(cookieOne.getColor());
        System.out.println(cookieTwo.getColor());
    }
}