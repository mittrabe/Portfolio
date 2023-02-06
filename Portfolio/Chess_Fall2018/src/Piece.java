import java.util.Scanner;

public class Piece
{
	private String player = new String();
	private int row;
	private int col;
	private int row2;
	private int col2;
	private String leftRight;
	private int numTaken;
	private String subPlayer = new String();
	private String otherPlayer = new String();
	private Piece[][] subBoard = new Piece[8][8];
	private Piece[][] subSubBoard = new Piece[8][8];
	private String subMovePlayer = new String();
	private boolean canCombo;
	private String empty;
	private Scanner input = new Scanner(System.in);
	private int row3;
	private int col3;
	private int row4;
	private int col4;
	private String there = new String();
	private boolean rightCombo;
	private boolean leftCombo;
	private boolean comboMoveLeft;
	private boolean comboMoveRight;
	
	public Piece(String p)
	{
		player = p;
	}

	public String toString()
	{
		return player;
	}

	public int move(String str, String str2, Piece[][] board, Piece player1, Piece player2, Piece empty)
	{
		numTaken = 0;

		this.empty = empty.toString();


		for(int row = 0; row < board.length; row++)
		{
			for(int col = 0; col < board[row].length; col++)
			{
				subBoard[row][col] = board[row][col];
			}
		}


		if(player.equals(" o "))
		{
			subPlayer = " o ";
			otherPlayer = " x ";
			subMovePlayer = "player 1(O)";

			decodeStr(str, str2);
			checkMove(subBoard, row, col, row2, col2);

			if(leftRight.equals("left"))
			{
				if(col == 0)
				{
					System.out.println("Can't move there. Try again.\n");
					Checkers.subMove(subPlayer);
				}
				else if(board[row2][col2].equals(board[row-1][col-1]))
				{
					board[row2][col2] = player1;
					board[row][col] = empty;
					
				}
				else if(board[row2][col2].equals(board[row-2][col-2]))
				{
					if(board[row-1][col-1].toString().equals(player2.toString()))
					{
						if(col == 1)
						{
							System.out.println("Can't move there. Try again.\n");
							Checkers.subMove(subPlayer);
						}
						else if(col > 1)
						{
							board[row2][col2] = player1;
							board[row-1][col-1] = empty;
							board[row][col] = empty;
							
							numTaken++; 
							
							for(int row = 0; row < board.length; row++)
							{
								for(int col = 0; col < board[row].length; col++)
								{
									subBoard[row][col] = board[row][col];
								}
							}
							
						/*	setBoard();
							
							checkCombo(subSubBoard, row2, col2);
							
							
							if(canCombo == true)
							{
								System.out.println("\n" + subMovePlayer + ", you may capture one or more pieces, enter 'yes' to move again, and 'no' to end your turn!\n");
								comboChoice(input.nextLine());
								
							

							if(comboMoveLeft == true)
							{
								board[row3][col3] = player1;
								board[row-1][col-1] = empty;
								board[row][col] = empty;
								numTaken++;
							}
							else if(comboMoveRight == true)
							{
								board[row2][col2] = player1;
								board[row-1][col+1] = empty;
								board[row][col] = empty;
							}
							}*/
						}
					}
					else
					{
						System.out.println("Can't move there. Try again.\n");
						Checkers.subMove(subPlayer);
					}
				}

			}
			else if(leftRight.equals("right"))
			{
				if(col == 7)
				{
					System.out.println("Can't move there. Try again.\n");
					Checkers.subMove(subPlayer);
				}

				else if(board[row2][col2].equals(board[row-1][col+1]))
				{
					board[row2][col2] = player1;
					board[row][col] = empty;
				}

				else if(board[row2][col2].equals(board[row-2][col+2]))
				{
					if(board[row-1][col+1].toString().equals(player2.toString()))
					{
						if(col == 6)
						{
							System.out.println("Can't move there. Try again.\n");
							Checkers.subMove(subPlayer);
						}
						else if(col < 6)
						{
							board[row2][col2] = player1;
							board[row-1][col+1] = empty;
							board[row][col] = empty;

							numTaken++;
							
							for(int row = 0; row < board.length; row++)
							{
								for(int col = 0; col < board[row].length; col++)
								{
									subBoard[row][col] = board[row][col];
								}
							}
							
							setBoard();
							
							/*checkCombo(subSubBoard, row2, col2);
							
							
							if(canCombo == true)
							{
							Checkers.printBoard(subBoard);
								System.out.println("\n" + subMovePlayer + ", you may capture one or more pieces, enter 'yes' to move again, and 'no' to end your turn!\n");
								comboChoice(input.nextLine());
								
							

							if(comboMoveLeft == true)
							{
								board[row3][col3] = player1;
								board[row-1][col-1] = empty;
								board[row][col] = empty;
								numTaken++;
							}
							
							else if(comboMoveRight == true)
							{
								board[row2][col2] = player1;
								board[row-1][col-1] = empty;
								board[row][col] = empty;
								numTaken++;
							}

							}*/
						}
					}

					else
					{
						System.out.println("Can't move there. Try again.\n");
						Checkers.subMove(subPlayer);
					}
				}

			}
		}


		else if(player.equals(" x "))
		{
			subPlayer = " x "; 
			otherPlayer = " o ";
			subMovePlayer = "player 2(X)";

			decodeStr(str, str2);
			checkMove(subBoard, row, col, row2, col2);

			if(leftRight.equals("left"))
			{
				if(col == 0)
				{
					System.out.println("Can't move there. Try again.\n");
					Checkers.subMove(subMovePlayer);
				}
				else if(board[row2][col2].equals(board[row+1][col-1]))
				{
					board[row2][col2] = player2;
					board[row][col] = empty;
				}
				else if(board[row2][col2].equals(board[row+2][col-2]))
				{
					if(board[row+1][col-1].toString().equals(player1.toString()))
					{
						if(col == 1)
						{
							System.out.println("Can't move there. Try again.\n");
							Checkers.subMove(subMovePlayer);
						}
						else if(col > 1)
						{
							board[row2][col2] = player2;
							board[row+1][col-1] = empty;
							board[row][col] = empty;

							numTaken++;
							
							
							for(int row = 0; row < board.length; row++)
							{
								for(int col = 0; col < board[row].length; col++)
								{
									subBoard[row][col] = board[row][col];
								}
							}
							
							setBoard();
							
							/*checkCombo(subSubBoard, row2, col2);
							
							
							if(canCombo == true)
							{
								System.out.println("\n" + subMovePlayer + ", you may capture one or more pieces, enter 'yes' to move again, and 'no' to end your turn!\n");
								comboChoice(input.nextLine());
								
							

							if(comboMoveLeft == true)
							{
								board[row3][col3] = player2;
								board[row+1][col-1] = empty;
								board[row][col] = empty;
								numTaken++;
							}
							
							else if(comboMoveRight == true)
							{
								board[row2][col2] = player2;
								board[row+1][col+1] = empty;
								board[row][col] = empty;
								numTaken++;
							}

							} */
						}
					}
					else
					{
						System.out.println("Can't move there. Try again.\n");
						Checkers.subMove(subMovePlayer);
					}
				}

			}
			else if(leftRight.equals("right"))
			{
				{
					if(col == 7)
					{
						System.out.println("Can't move there. Try again.\n");
						Checkers.subMove(subMovePlayer);
					}

					else if(board[row2][col2].equals(board[row+1][col+1]))
					{
						board[row2][col2] = player2;
						board[row][col] = empty;
					}

					else if(board[row2][col2].equals(board[row-2][col+2]))
					{
						if(board[row-1][col+1].toString().equals(player1.toString()))
						{
							if(col == 6)
							{
								System.out.println("Can't move there. Try again.\n");
								Checkers.subMove(subMovePlayer);
							}
							else if(col < 6)
							{
								board[row2][col2] = player2;
								board[row-1][col-1] = empty;
								board[row][col] = empty;

								numTaken++;
								
								for(int row = 0; row < board.length; row++)
								{
									for(int col = 0; col < board[row].length; col++)
									{
										subBoard[row][col] = board[row][col];
									}
								}
								
								setBoard();
								
								/*checkCombo(subSubBoard, row2, col2);
								
								
								if(canCombo == true)
								{
									System.out.println("\n" + subMovePlayer + ", you may capture one or more pieces, enter 'yes' to move again, and 'no' to end your turn!\n");
									comboChoice(input.nextLine());
									
				

								if(comboMoveLeft == true)
								{
									board[row3][col3] = player2;
									board[row+1][col-1] = empty;
									board[row][col] = empty;
									numTaken++;
								}
								
								else if(comboMoveRight == true)
								{
									board[row2][col2] = player2;
									board[row+1][col+1] = empty;
									board[row][col] = empty;
									numTaken++;
								}

								}*/
							}
						}

						else
						{
							System.out.println("Can't move there. Try again.\n");
							Checkers.subMove(subMovePlayer);
						}
					}

				}
			}
		}

		return numTaken;
	}

	public void decodeStr(String str, String str2)
	{
		int first = 0;
		int second = 0;
		int first2 = 0;
		int second2 = 0;
		String rowError = "ijklmnopqrstuvwxyzIJKLMNOPQRSTUVWXYZ1234567890-=!@#$%^&*()_+[]\\{}|;':\",./<>?`~";
		String colError = "`~!@#$%^&*()_+-=qwertyuiop[]\\QWERTYUIOP{}|asdfghjkl;'ASDFGHJKL:\"zxcvbnm,./ZXCVBNM<>?";


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
		else if(rowError.contains(str.substring(0,1)))
		{
			System.out.println("\nError: Selection out of bounds or does not exist! Reselect:\n");
			Checkers.subMove(subMovePlayer);
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
		else if(colError.contains(str.substring(1,2)))
		{
			System.out.println("\nError: Selection out of bounds or does not exist! Reselect:\n");
			Checkers.subMove(subMovePlayer);
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
		else if(rowError.contains(str2.substring(0,1)))
		{
			System.out.println("\nError: Cannot move there (out of bounds or does not exist)! Reselect:\n");
			Checkers.subMove(subMovePlayer);
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
		else if(colError.contains(str2.substring(1,2)))
		{
			System.out.println("\nError: Cannot move there (out of bounds or does not exist)! Reselect:\n");
			Checkers.subMove(subMovePlayer);
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
		else if(col == col2)
		{
			System.out.println("\nError: Can only move Diagonally! \nReselect: \n");
			Checkers.subMove(subMovePlayer);
		}
	}


	public void checkMove(Piece[][] board, int row, int col, int row2, int col2)
	{
		if(!board[row][col].toString().equals(player))
		{
			System.out.println("\nError: Wrong piece. \nReselect: \n");
			Checkers.subMove(subMovePlayer);
		}
		else if(board[row2][col2].toString().equals(otherPlayer) || board[row2][col2].toString().equals(player))
		{
			System.out.println("\nError: Can't move ontop of another piece. \nReselect:\n");
			Checkers.subMove(subMovePlayer);
		}
		else if(!board[row][col].toString().equals(subPlayer))
		{
			System.out.println("\nError: Selected piece does not exist! \nReselect:\n");
			Checkers.subMove(subMovePlayer);
		}


		if(player.equals(" o "))
		{

			if(leftRight.equals("left"))
			{
				if(board[row2][col2] != board[row-1][col-1]) //Not entering this?
				{
					if(board[row2][col2] == board[row-2][col-2] && board[row-1][col-1].toString().equals(otherPlayer.toString()))
					{

					}
					else
					{
						System.out.println("\nError: Can't move there. \nReselect: \n");
						Checkers.subMove(subMovePlayer);
					}
				}
			}

			else if(leftRight.equals("right"))
			{
				if(board[row2][col2] != board[row-1][col+1])
				{
					if(board[row2][col2] == board[row-2][col+2] && board[row-1][col+1].toString().equals(otherPlayer.toString()))
					{

					}
					else
					{
						System.out.println("\nError: Can't move there. \nReselect: \n");
						Checkers.subMove(subMovePlayer);
					}
				}
			}
		}

		else if(player.equals(" x "))
		{
			if(leftRight.equals("left"))
			{
				if(board[row2][col2] != board[row+1][col-1])
				{
					if(board[row2][col2] == board[row+2][col-2] && board[row+1][col-1].toString().equals(otherPlayer.toString()))
					{

					}
					else
					{
						System.out.println("\nError: Can't move there. \nReselect: \n");
						Checkers.subMove(subMovePlayer);
					}
				}
			}

			else if(leftRight.equals("right"))
			{
				if(board[row2][col2] != board[row+1][col+1])
				{
					if(board[row2][col2] == board[row+2][col+2] && board[row+1][col+1].toString().equals(otherPlayer.toString()))
					{

					}
					else
					{
						System.out.println("\nError: Can't move there. \nReselect: \n");
						Checkers.subMove(subMovePlayer);
					}
				}
			}
		}
	}

	public void setBoard()
	{
		for(int row = 0; row < subBoard.length; row++)
		{
			for(int col = 0; col < subBoard[row].length; col++)
			{
				subSubBoard[row][col] = subBoard[row][col];
			}
		}
	}


	public void checkCombo(Piece[][] board, int row2, int col2)
	{
		row = row2;
		col = col2;

		if(player.equals(" o "))
		{
			if(col2 < 3)
			{
				if(board[row-2][col+2].toString().equals(empty))
				{
					if(board[row-1][col+1].toString().equals(otherPlayer))
					{
						canCombo = true;
						rightCombo = true;
						
						row2 = row-2; //row2 indicates that the combo is to the right
						col2 = col+2;
					}
					else
					{
						canCombo = false;
						rightCombo = false;
					}
				}
			}
			
			else if(col2 > 6)
			{
				if(board[row-2][col-2].toString().equals(empty))
				{
					if(board[row-1][col-1].toString().equals(otherPlayer))
					{
						canCombo = true;
						leftCombo = true;
						
						row3 = row-2; //row3 indicates that the combo is to the left
						col3 = col-2;
					}
					else
					{
						canCombo = false;
						leftCombo = false;
					}
				}
			}
			
			else if(col2 >= 3 && col2 <= 6)
			{
				if(board[row-2][col+2].toString().equals(empty))
				{
					if(board[row-1][col+1].toString().equals(otherPlayer))
					{
						canCombo = true;
						rightCombo = true;
						
						row2 = row-2;
						col2 = col+2;
					}
					else
					{
						canCombo = false;
						leftCombo = false;
					}
				}
				if(board[row-2][col-2].toString().equals(empty))
				{
					if(board[row-1][col-1].toString().equals(otherPlayer))
					{
						canCombo = true;
						leftCombo = true;
						
						row3 = row-2;
						col3 = col-2;
					}
					else
					{
						canCombo = false;
						leftCombo = false;
					}
				}
			}

		}

		else if(player.equals(" x "))
		{
			if(col2 < 3)
			{
				if(board[row+2][col+2].toString().equals(empty))
				{
					if(board[row+1][col+1].toString().equals(otherPlayer))
					{
						canCombo = true;
						rightCombo = true;
						
						row2 = row+2; 
						col2 = col+2;
					}
					else
					{
						canCombo = false;
						leftCombo = false;
					}
				}
			}
			
			else if(col2 > 6)
			{
				if(board[row+2][col-2].toString().equals(empty))
				{
					if(board[row+1][col-1].toString().equals(otherPlayer))
					{
						canCombo = true;
						leftCombo = true;
						
						row3 = row+2;
						col3 = col-2;
					}
					else
					{
						canCombo = false;
						leftCombo = false;
					}
				}
			}
			
			else if(col2 >= 3 && col2 <= 6)
			{
				if(board[row+2][col+2].toString().equals(empty))
				{
					if(board[row+1][col+1].toString().equals(otherPlayer))
					{
						canCombo = true;
						rightCombo = true;
						
						row2 = row+2;
						col2 = col+2;
					}
					else
					{
						canCombo = false;
						rightCombo = false;
					}
				}
				if(board[row+2][col-2].toString().equals(empty))
				{
					if(board[row+1][col-1].toString().equals(otherPlayer))
					{
						canCombo = true;
						leftCombo = true;
						
						row3 = row+2;
						col3 = col-2;		
					}
					else
					{
						canCombo = false;
						leftCombo = false;
					}
				}
			}
		}
	}
	
	public void comboChoice(String choice)
	{
		
			if(choice.equals("yes") || choice.equals("Yes"))
			{
				comboMove(subSubBoard, row, col, row2, col2);
			}
			else if(choice.equals("no") || choice.equals("No"))
			{
				comboMoveRight = false;
				comboMoveLeft = false;
			}
			else if((!choice.equals("yes") || !choice.equals("Yes")) && (!choice.equals("no") || !choice.equals("No")))
			{
				System.out.println("\nError: Invalid entry (Please enter, 'yes' to capture another piece, or 'no' to end your turn)\n");
				comboChoice(input.nextLine());
			}
	}
	
	public void comboMove(Piece[][] board, int row, int col, int row2, int col2)
	{
		Checkers.printBoard(subSubBoard);
		
		System.out.println("\nSelect where to move:\n");
		there = input.nextLine();
		
		comboDecode(there);
		 
		if(board[row4][col4].equals(board[row2][col2]) && rightCombo == true)
		{
			comboMoveLeft = true;
			comboMoveRight = false;
		}
		else if(board[row4][col4].equals(board[row3][col3]) && leftCombo == true)
		{
			comboMoveRight = true;
			comboMoveLeft = false;
		}
		else if(!board[row4][col4].equals(board[row2][col2]) && !board[row4][col4].equals(board[row3][col3]))
		{
			System.out.println("\nError: Can't move there.\nReselect:\n");
			
			comboMove(subSubBoard, row, col, row2, col2);
		}
	}
	
	public void comboDecode(String str2) 
	{
		int first2 = 0;
		int second2 = 0;
		String rowError = "ijklmnopqrstuvwxyzIJKLMNOPQRSTUVWXYZ1234567890-=!@#$%^&*()_+[]\\{}|;':\",./<>?`~";
		String colError = "`~!@#$%^&*()_+-=qwertyuiop[]\\QWERTYUIOP{}|asdfghjkl;'ASDFGHJKL:\"zxcvbnm,./ZXCVBNM<>?";
	
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
		else if(rowError.contains(str2.substring(0,1)))
		{
			System.out.println("\nError: Cannot move there (out of bounds or does not exist)! Reselect:\n");
			Checkers.subMove(subMovePlayer);
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
		else if(colError.contains(str2.substring(1,2)))
		{
			System.out.println("\nError: Cannot move there (out of bounds or does not exist)! Reselect:\n");
			Checkers.subMove(subMovePlayer);
		}

		row4 = first2;
		col4 = second2;
	} 
}
