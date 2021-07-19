package array;

public class ObjectCopy {

	public static void main(String[] args) {
		
		Book[] bookArray1 = new Book[3];
		Book[] bookArray2 = new Book[3];
		
		bookArray1[0] = new Book("toystory1", "pixar");
		bookArray1[1] = new Book("toystory2", "pixar");
		bookArray1[2] = new Book("toystory3", "pixar");
		
		System.arraycopy(bookArray1, 0, bookArray2, 0, 3);
		
		for (int i=0; i<bookArray2.length; i++) {
			bookArray2[i].showBookInfo();
		}
		
		bookArray1[0].setBookname("¶óÇ¬Á©");
		bookArray1[0].setAuthor("µðÁî´Ï");
		
		System.out.println("===¾èÀºº¹»ç bookArray1===");
		for (int i=0; i<bookArray1.length; i++) {
			bookArray1[i].showBookInfo();
		}
		
		System.out.println("===¾èÀºº¹»ç bookArray2===");
		for (int i=0; i<bookArray2.length; i++) {
			bookArray2[i].showBookInfo();
		}
	}
	

}
