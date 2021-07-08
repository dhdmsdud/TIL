package ifEX;

public class switchCase {

	public static void main(String[] args) {
		
		int rank = 9;
		char medalColor;
		
		switch(rank) {
		case 1 : medalColor = 'G';
			break;
		case 2 : medalColor = 'S';
			break;
		case 3 : medalColor = 'B';
			break;
		default : medalColor = 'A';
		}
	System.out.println(rank + "등 메달의 색은" + medalColor + "입니다.");
	}

}
