
public class randomTest {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		
		int rand1 = 1 + (int)(Math.random()*10);
		int rand2; //= 1 + (int)(Math.random()*10);
		System.out.println("Random one: " +rand1);
		
		
		
		for(int i = 0; i < rand1; i++){
			rand2 =  1 + (int)(Math.random()*10);
			System.out.println("Random two: " +rand2);
		}
	}

}
