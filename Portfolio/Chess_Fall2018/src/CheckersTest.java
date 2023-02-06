import java.util.Scanner;

public class CheckersTest 
{
	static Piece[][] board = new Piece[8][8];

	static Piece player1 = new Piece(" O ");
	static Piece player2 = new Piece(" X ");
	static Piece empty = new Piece("   ");

	static int row;
	static int col;

	static String here = new String();
	static String there = new String();
	static Scanner input = new Scanner(System.in);

	public static void main(String[] args)
	{

		for(row = 0; row < board.length; row++)
		{
			for(col = 0; col < board[row].length; col++)
			{
				if(row%2 != 0 && (row <= 2))
				{
					for(col = 0; col < board[row].length; col++)
					{
						if(col%2 == 0)
						{
							board[row][col] = player2;
						}
						else
						{
							board[row][col] = empty;
						}
					}
				}
				else if (row%2 == 0 && (row <= 2))
				{
					for(col = 0; col < board[row].length; col++)
					{
						if(col%2 != 0)
						{
							board[row][col] = player2;
						}
						else 
						{
							board[row][col] = empty;
						}
					}
				}
				else if(row%2 != 0 && (row >= 5))
				{
					for(col = 0; col < board[row].length; col++)
					{
						if(col%2 == 0)
						{
							board[row][col] = player1;
						}
						else
						{
							board[row][col] = empty;
						}
					}
				}
				else if (row%2 == 0 && (row >= 5))
				{
					for(col = 0; col < board[row].length; col++)
					{
						if(col%2 != 0)
						{
							board[row][col] = player1;
						}
						else 
						{
							board[row][col] = empty;
						}
					}
				}

				else if(row > 2 && row < 5)
				{
					for(col = 0; col < board[row].length; col++)
					{
						board[row][col] = empty;
					}
				}
			}
		}
		printBoard(board);
		
		for(int i = 0; i <= 3; i++)
		{
		move("player 1(O)");

		move("player 2(X)");
		}

	}
	public static void printBoard(Piece[][] str)
	{
		System.out.println("   1  2  3  4  5  6  7  8");
		System.out.println("  -----------------------" );
		
		for(row = 0; row < str.length; row++)
		{
			if(row == 0)
				System.out.print("A|");
			if(row == 1)
				System.out.print("B|");
			if(row == 2)
				System.out.print("C|");
			if(row == 3)
				System.out.print("D|");
			if(row == 4)
				System.out.print("E|");
			if(row == 5)
				System.out.print("F|");
			if(row == 6)
				System.out.print("G|");
			if(row == 7)
				System.out.print("H|");
			
			for(col = 0; col < str.length; col++)
			{
		
				System.out.print(str[row][col]);
			}
			System.out.println();
		}
	}

	public static void move(String player)
	{
		System.out.println("\n" + player + ", select a piece to move:\n");
		System.out.println("Enter piece location (i.e. A1, B5, G3, etc.)\n\n");

		here = input.nextLine();
		System.out.println("Selected: " + here);

		System.out.println("\nSelect where to move to:");
		there = input.nextLine();

		if(player.equals("player 1(O)"))
			player1.move(here, there, board, player1, player2, empty);
		else if(player.equals("player 2(X)"))
			player2.move(here, there, board, player1, player2, empty);
		
		printBoard(board);
	}
}


