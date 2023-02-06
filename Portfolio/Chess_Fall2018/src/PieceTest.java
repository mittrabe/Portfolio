import java.util.Scanner;

public class PieceTest 
{
	private String player = new String();
	private int row;
	private int col;
	private int row2;
	private int col2;
	private String leftRight;


	public PieceTest(String p)
	{
		player = p;
	}

	public String toString()
	{
		return player;
	}

	public void move(String str, String str2, Piece[][] board, Piece player1, Piece player2, Piece empty)
	{
		decodeStr(str, str2);

		if(player.equals("player1(O)"))
		{
			if(leftRight.equals("left"))
			{
				if(col == 0)
				{
					System.out.println("Can't move there.");
				}
				else if(board[row2][col2].equals(board[row-1][col-1]))
				{
					board[row2][col2] = player1;
					board[row][col] = empty;
				}
				if(board[row2][col2].equals(board[row-2][col-2]))
				{
					if(board[row-1][col-1].toString().equals(player2.toString()))
					{
						if(col == 1)
						{
							System.out.println("Can't move there.");
						}
						else if(col > 1)
						{
							board[row2][col2] = player1;
							board[row-1][col-1] = empty;
							board[row][col] = empty;
						}
					}
					else
					{
						System.out.println("Can't move there.");
					}
				}
				
			}
			else if(leftRight.equals("right"))
			{
				if(col == 7)
				{
					System.out.println("Can't move there.");
				}
				
				else if(board[row2][col2].equals(board[row+1][col+1]))
				{
					board[row2][col2] = player1;
					board[row][col] = empty;
				}
				
				if(board[row2][col2].equals(board[row+2][col+2]))
				{
					if(board[row+1][col+1].toString().equals(player2.toString()))
					{
						if(col == 6)
						{
							System.out.println("Can't move there.");
						}
						else if(col < 6)
						{
							board[row2][col2] = player1;
							board[row+1][col+1] = empty;
							board[row][col] = empty;
						}
					}
					
					else
					{
						System.out.println("Can't move there.");
					}
				}

			}
		}
		else if(player.equals("player2(X)"))
		{
			if(leftRight.equals("left"))
			{

			}
			else if(leftRight.equals("right"))
			{

			}
		}


	}

	public void decodeStr(String str, String str2)
	{
		int first = 0;
		int second = 0;
		int first2 = 0;
		int second2 = 0;

		if(str.substring(0,1).equalsIgnoreCase("A"))
		{
			first = 0;
		}
		else if(str.substring(0,1).equalsIgnoreCase("B"))
		{
			first = 1;
		}
		else if(str.substring(0,1).equalsIgnoreCase("C"))
		{
			first = 2;
		}
		else if(str.substring(0,1).equalsIgnoreCase("D"))
		{
			first = 3;
		}
		else if(str.substring(0,1).equalsIgnoreCase("E"))
		{
			first = 4;
		}
		else if(str.substring(0,1).equalsIgnoreCase("F"))
		{
			first = 5;
		}
		else if(str.substring(0,1).equalsIgnoreCase("G"))
		{
			first = 6;
		}
		else if(str.substring(0,1).equalsIgnoreCase("H"))
		{
			first = 7;
		}

		if(str.substring(1,2).equalsIgnoreCase("1"))
		{
			second = 0;
		}
		else if(str.substring(1,2).equalsIgnoreCase("2"))
		{
			second = 1;
		}
		else if(str.substring(1,2).equalsIgnoreCase("3"))
		{
			second = 2;
		}
		else if(str.substring(1,2).equalsIgnoreCase("4"))
		{
			second = 3;
		}
		else if(str.substring(1,2).equalsIgnoreCase("5"))
		{
			second = 4;
		}
		else if(str.substring(1,2).equalsIgnoreCase("6"))
		{
			second = 5;
		}
		else if(str.substring(1,2).equalsIgnoreCase("7"))
		{
			second = 6;
		}
		else if(str.substring(1,2).equalsIgnoreCase("8"))
		{
			second = 7;
		}

		row = first;
		col = second;



		if(str2.substring(0,1).equalsIgnoreCase("A"))
		{
			first2 = 0;
		}
		else if(str2.substring(0,1).equalsIgnoreCase("B"))
		{
			first2 = 1;
		}
		else if(str2.substring(0,1).equalsIgnoreCase("C"))
		{
			first2 = 2;
		}
		else if(str2.substring(0,1).equalsIgnoreCase("D"))
		{
			first2 = 3;
		}
		else if(str2.substring(0,1).equalsIgnoreCase("E"))
		{
			first2 = 4;
		}
		else if(str2.substring(0,1).equalsIgnoreCase("F"))
		{
			first2 = 5;
		}
		else if(str2.substring(0,1).equalsIgnoreCase("G"))
		{
			first2 = 6;
		}
		else if(str2.substring(0,1).equalsIgnoreCase("H"))
		{
			first2 = 7;
		}

		if(str2.substring(1,2).equalsIgnoreCase("1"))
		{
			second2 = 0;
		}
		else if(str2.substring(1,2).equalsIgnoreCase("2"))
		{
			second2 = 1;
		}
		else if(str2.substring(1,2).equalsIgnoreCase("3"))
		{
			second2 = 2;
		}
		else if(str2.substring(1,2).equalsIgnoreCase("4"))
		{
			second2 = 3;
		}
		else if(str2.substring(1,2).equalsIgnoreCase("5"))
		{
			second2 = 4;
		}
		else if(str2.substring(1,2).equalsIgnoreCase("6"))
		{
			second2 = 5;
		}
		else if(str2.substring(1,2).equalsIgnoreCase("7"))
		{
			second2 = 6;
		}
		else if(str2.substring(1,2).equalsIgnoreCase("8"))
		{
			second2 = 7;
		}

		row2 = first2;
		col2 = second2;


		if(col > col2)
		{
			leftRight = "left";
		}
		else if(col < col2)
		{
			leftRight = "right";
		}
	}
}
