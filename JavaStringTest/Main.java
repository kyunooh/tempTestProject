class Main {
    public static void main(String[] args) {
        String a = "abcd";
        String b = "abcd";
        String c = new String("abcd");
        String d = "ab" + "cd";
        System.out.println(" \"abcd\" == \"abcd\" : " + ("abcd" == "abcd"));
        System.out.println(" a == \"abcd\" : " + (a == "abcd"));
        System.out.println(" a == b : " + (a == b));
        System.out.println(" \"abcd\" == c : " + ("abcd" == c));
        System.out.println(" a == c : " + (a == c));
        System.out.println(" a == d : " + (a == d));
        System.out.println(" c == d : " + (c == d));
    }
}
