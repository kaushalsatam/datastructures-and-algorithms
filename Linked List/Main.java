public class Main {
    public static void main(String[] args) {
        LinkedList newLinkedList = new LinkedList(18);
        newLinkedList.append(10);
        newLinkedList.append(72);

        // newLinkedList.getHead();
        // newLinkedList.getTail();
        // newLinkedList.getLength();

        // newLinkedList.printList();
        // newLinkedList.removeLast();
        // System.out.println();
        // newLinkedList.printList();
        // System.out.println();
        // newLinkedList.prepend(69);
        // newLinkedList.printList();
        // newLinkedList.removeFirst();
        // System.out.println();
        newLinkedList.printList();
        System.out.println();
        // newLinkedList.set(2, 56);
        // newLinkedList.set(1, 69);
        newLinkedList.insert(2, 5);
        newLinkedList.printList();
        System.out.println();
        newLinkedList.remove(2);
        newLinkedList.printList();
        System.out.println();
        newLinkedList.reverse();
        newLinkedList.printList();
    }
}
