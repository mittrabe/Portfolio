package chess;
import java.util.Scanner;
import java.util.ArrayList;


public class Rabehl_WarTacToe
{
  static ArrayList<Integer> drawn1 = new ArrayList<Integer>();
  static ArrayList<Integer> drawn2 = new ArrayList<Integer>();
  static ArrayList<Integer> hold = new ArrayList<Integer>();
  static Rabehl_WarDeckOfCards deck0 = new Rabehl_WarDeckOfCards(1);
  static Rabehl_WarDeckOfCards deck1 = new Rabehl_WarDeckOfCards(0);
  static Rabehl_WarDeckOfCards deck2 = new Rabehl_WarDeckOfCards(0);
  
  static String[][] board = new String[3][3];
  static int row;
  static int col;
  static String mark;
  
  static boolean check = false;
  static boolean cat;
  static String choice;
  static Scanner input = new Scanner(System.in);
  
 
  static int p1Round = 0;
  static int p2Round = 0;
  static int p1TicCount = 0;
  static int p2TicCount = 0;
 
  
  static String turn = new String();
  
  
 public static void main(String[] args)
 {
    
    Scanner input = new Scanner(System.in);
    boolean isTurn = true;
    int stats = 0;
    int totalRound = 0;
    
    int draw1;
    int draw2;
    
    drawn1.add(42);
    drawn2.add(42);
    
    
    deck0.shuffle();
    
    
    for(int i = 0; i < 52; i++)
    {
      if(i%2 == 0)
      {
        deck1.addCard(deck0.getDeck().get(i));
        
      }
      if(i%2 == 1)
      {
        deck2.addCard(deck0.getDeck().get(i));
      }
    } 
    
    
    while(isTurn == true && (drawn1.size() > 0 || drawn2.size() > 0))
    {
      if(deck1.getDeck().size() == 0)
      {
        System.out.println("\nPlayer 1's deck is out of cards...Reshuffling deck\n");
         
        printDots();
        
        System.out.println("\nShuffling Complete");
        
        
      deck1.replace(drawn1);
      
      }
      
      
      if(deck2.getDeck().size() == 0)
      {
        System.out.println("\nPlayer 2's deck is out of cards...Reshuffling deck\n");
         
         printDots();
        
        System.out.println("\nShuffling Complete");
        
      deck2.replace(drawn2);
      
      }
      
      System.out.println("\n\nDraw?\nEnter '1' to draw or '2' to access game stats");
        turn = input.nextLine();
        
        if(turn.equals("2"))
        {
        	System.out.println("\n\nWhich player would you like to access the stats of?");
        	System.out.println("\n[1] Player 1\n[2] Player 2");
        	
        	stats = input.nextInt();
        	getStats(stats);
        	
        	
        	
        }
        while(!turn.equals("1") && !turn.equals("2"))
        {
        	System.out.println("\nError: Please input '1' to draw or '2' to access game stats");
        }
      
      while(isTurn == true && (deck1.getDeck().size() > 0 && deck2.getDeck().size() > 0))
      {
        /*deck1.printDeck();   //These are here for testing purposes
        deck2.printDeck(); */
        
        draw1 = deck1.draw();
        if(draw1 > 10)
        {
          System.out.println("\nPlayer 1 drew: " + checkFace(draw1));
        }
        else
          System.out.println("\nPlayer 1 drew: " + draw1);
        
        draw2 = deck2.draw();
        if(draw2 > 10)
        {
          System.out.println("\nPlayer 2 drew: " + checkFace(draw2) + "\n");
        }
        else
          System.out.println("\nPlayer 2 drew: " + draw2 + "\n");
        
        hold.add(0,draw1);
        hold.add(1,draw2);
        
        
        try
        {
          Thread.sleep(1000);
        }
        catch(Exception e)
        {
          System.out.println(e);
        }
        
        
        compareDrawn(hold);
       
        if(deck1.getDeck().size() > 0 && deck2.getDeck().size() > 0)
        {
        System.out.println("\n\nDraw again?\nType '1' to redraw or '2' to access game stats");
        turn = input.nextLine();
        
        
        if(turn.equals("2"))
        {
        	System.out.println("\n\nWhich player would you like to access the stats of?");
        	System.out.println("\n[1] Player 1\n[2] Player 2");
        	
        	stats = input.nextInt();
        	getStats(stats);
        	
        	System.out.println("\n\n\nEnter '1' to draw");
        	turn = input.nextLine();
        	
        }
        while(!turn.equals("1") && !turn.equals("2"))
        {
        	System.out.println("\nError: Please input '1' to draw or '2' to access game stats");
        	turn = input.nextLine();
        }
        if(turn.equals("1"))
        {
          isTurn = true;
        }
        else
        {
          isTurn = false;
        }
        }
        totalRound++;
      }
    }
    if(deck1.getDeck().size() == 0 && deck2.getDeck().size() > 0)
    {
    	System.out.println("Player 2 is the winner!");
    }
    else if(deck2.getDeck().size() == 0 && deck1.getDeck().size() > 0)
    {
    	System.out.println("Player 1 is the winner!");
    }
    System.out.println("\n\nThe game was completed in " + totalRound + " turns!");
  }

 public static String checkFace(int draw)
  {
    if(draw == 11)
      return "Jack";
    else if(draw == 12)
      return "Queen";
    else if(draw == 13)
      return "King";
    else if(draw == 14)
      return "Ace"; 
    return "";
  }
  
  public static void compareDrawn(ArrayList<Integer> pair)
  {
    if(drawn1.size() > 0 && drawn2.size() > 0 && (drawn1.get(0) == 42 || drawn2.get(0) == 42))
    {
      drawn1.remove(0);
      drawn2.remove(0);
    }
     if(pair.get(0) > pair.get(1))
    {
      System.out.println("Player 1s was higher");
      drawn1.add(pair.get(0));
      drawn1.add(pair.get(1));
      p1Round++;
    //  countCard("Player1", pair);
    }
    else if(pair.get(0) < pair.get(1))
    {
      System.out.println("Player 2s was higher");
      drawn2.add(pair.get(0));
      drawn2.add(pair.get(1));
      p2Round++;
    //  countCard("Player 2", pair);
    }
    else if(pair.get(0) == pair.get(1))
    {
      System.out.print("Initializing TicTacToe\n");
      
      printDots();
      
      //TicTacToe Starts Here
        
    boolean turn = true;
    char char1;
    char char2;
    int test;
    int win = 0;
    
    for(row = 0; row < board.length; row++)
    {
      for(col = 0; col < board[row].length; col++)
      {
        board[row][col] = " ";
      }
    }
    
    check = false;
    while((win != 1 || win != 2) && (cat == false))
    {
      win = checkWin(board);
      checkCat(board);
      
      if(check == true)
        break;
      
      while(turn == true && (win != 1 || win != 2) && cat == false)
      {
        mark = "X";
        System.out.println("Player 1s turn(x)!\n\nInput where you would like to go\n(I.E. A1, B3, C2, etc.");
        
        printBoard(board);
        choice = input.next();
        
        board = setBoard(choice);
        turn = false;
        
        
      }
      
      win = checkWin(board);
      checkCat(board);
      
      if(check == true)
        break;
      
      while(turn == false && (win != 1 || win != 2) && cat == false)
      {
        mark = "O";
        System.out.println("Player 2s turn(O)!\n\nInput where you would like to go\n(I.E. A1, B3, C2, etc.");
        
        printBoard(board);
        choice = input.next();
        
        board = setBoard(choice);
        turn = true;
      }
    }
    printBoard(board);
    if(win == 1)
    {
      System.out.println("\nPlayer 1(X) wins!"); //This still doesn't add in the extra 3 cards for wars
      drawn1.add(pair.get(0));
      drawn1.add(pair.get(1));
      win = 0;
      p1Round++;
      p1TicCount++;
    //  countCard("Player 1", pair);
    }
    else if(win == 2)
    {
      System.out.println("\nPlayer 2(O) wins!");
      drawn2.add(pair.get(0));
      drawn2.add(pair.get(0));
      win = 0;
      p2Round++;
      p2TicCount++;
    //  countCard("Player 2", pair);
    }
    else if(checkCat(board) == true)
    {
      System.out.println("\nCat's Game!");
    int random = (int)Math.random()*1+1;
    
    if(random == 1)
    {
    	System.out.println("\nPlayer 1(X) Wins this round by random lottery!");
    	 drawn1.add(pair.get(0));
         drawn1.add(pair.get(1));
         win = 0;
         p1Round++;
         p1TicCount++;
    }
    else if(random == 2)
    {
    	System.out.println("\nPlayer 2(O) Wins this round by random lottery!");
    	drawn2.add(pair.get(0));
        drawn2.add(pair.get(0));
        p2Round++;
        p2TicCount++;
    }
    }
    }
    
  }
  
  
  public static void printDrawn(ArrayList<Integer> drawn)
  {
    for(int i = 0; i < drawn.size(); i++)
    {
      if(i == 0)
        System.out.print(drawn.get(i));
      else
        System.out.print(", " + drawn.get(i));
    }
  }
  
  public static void printBoard(String[][] str)
  {
    System.out.println("    1   2   3");
    System.out.println("A "+"  "+str[0][0]+" | "+str[0][1]+" | "+str[0][2]);
    System.out.println("   ---|---|---");
    System.out.println("B "+"  "+str[1][0]+" | "+str[1][1]+" | "+str[1][2]);
    System.out.println("   ---|---|---");
    System.out.println("C "+"  "+str[2][0]+" | "+str[2][1]+" | "+str[2][2]);
    
  }
  
  public static String[][] setBoard(String choice)
  {  
    if(choice.charAt(0) == 'A' || choice.charAt(0) == 'a')
      row = 0;
    else if(choice.charAt(0) == 'B' || choice.charAt(0) == 'b')
      row = 1;
    else if(choice.charAt(0) == 'C' || choice.charAt(0) == 'c')
      row = 2;
    if(choice.charAt(1) == '1')
      col = 0;
    else if(choice.charAt(1) == '2')
      col = 1;
    else if(choice.charAt(1) == '3')
      col = 2;
    
    while(choice.charAt(0) != 'A' && choice.charAt(0) != 'a' && choice.charAt(0) != 'B' && choice.charAt(0) != 'b' && choice.charAt(0) != 'C' && choice.charAt(0) != 'c')
	  {
    	 System.out.println("Can't play there! Try again");
         printBoard(board);
         
         choice = input.next();
         if(choice.charAt(0) == 'A' || choice.charAt(0) == 'a')
           row = 0;
         else if(choice.charAt(0) == 'B' || choice.charAt(0) == 'b')
           row = 1;
         else if(choice.charAt(0) == 'C' || choice.charAt(0) == 'c')
           row = 2;
         if(choice.charAt(1) == '1')
           col = 0;
         else if(choice.charAt(1) == '2')
           col = 1;
         else if(choice.charAt(1) == '3')
           col = 2;
	  }
    
    while(board[row][col] != " ")
    {
      System.out.println("Can't play there! Try again");
      printBoard(board);
      
      choice = input.next();
      if(choice.charAt(0) == 'A' || choice.charAt(0) == 'a')
        row = 0;
      else if(choice.charAt(0) == 'B' || choice.charAt(0) == 'b')
        row = 1;
      else if(choice.charAt(0) == 'C' || choice.charAt(0) == 'c')
        row = 2;
      if(choice.charAt(1) == '1')
        col = 0;
      else if(choice.charAt(1) == '2')
        col = 1;
      else if(choice.charAt(1) == '3')
        col = 2;
    }
    board[row][col] = mark;
    return board;
  }

  public static int checkWin(String[][] str)
  {
    if(board[0][0].equals("X") && board[1][0].equals("X") && board[2][0].equals("X"))
    {
      check = true;
      return 1;
    }
    else if(board[0][1].equals("X") && board[1][1].equals("X") && board[2][1].equals("X"))
    {
      check = true;
      return 1;
    }
    else if(board[0][2].equals("X") && board[1][2].equals("X") && board[2][2].equals("X"))
    {
      check = true;
      return 1;
    }
    else if(board[0][0].equals("X") && board[0][1].equals("X") && board[0][2].equals("X"))
    {
      check = true;
      return 1;
    }
    else if(board[1][0].equals("X") && board[1][1].equals("X") && board[1][2].equals("X"))
    {
      check = true;
      return 1;
    }
    else if(board[2][0].equals("X") && board[2][1].equals("X") && board[2][2].equals("X"))
    {
      check = true;
      return 1;
    }
    else if(board[0][0].equals("O") && board[1][0].equals("O") && board[2][0].equals("O"))
    {
      check = true;
      return 2;
    }
    else if(board[0][1].equals("O") && board[1][1].equals("O") && board[2][1].equals("O"))
    {
      check = true;
      return 2;
    }
    else if(board[0][2].equals("O") && board[1][2].equals("O") && board[2][2].equals("O"))
    {
      check = true;
      return 2;
    }
    else if(board[0][0].equals("O") && board[0][1].equals("O") && board[0][2].equals("O"))
    {
      check = true;
      return 2;
    }
    else if(board[1][0].equals("O") && board[1][1].equals("O") && board[1][2].equals("O"))
    {
      check = true;
      return 2;
    }
    else if(board[2][0].equals("O") && board[2][1].equals("O") && board[2][2].equals("O"))
    {
      check = true;
      return 2;
    }
    else if(board[0][0].equals("X") && board[1][1].equals("X") && board[2][2].equals("X"))
    {
      check = true;
      return 1;
    }
    else if(board[2][0].equals("X") && board[1][1].equals("X") && board[0][2].equals("X"))
    {
      check = true;
      return 1;
    }
    else if(board[0][0].equals("O") && board[1][1].equals("O") && board[2][2].equals("O"))
    {
      check = true;
      return 2;
    }
    else if(board[2][0].equals("O") && board[1][1].equals("O") && board[0][2].equals("O"))
    {
      check = true;
      return 2;
    }
    return 0;
  }
  
  public static boolean checkCat(String[][] str)
  {
    for(int row = 0; row < str.length; row++)
    {
      for(int col = 0; col < str[row].length; col++)
      {
        if(str[row][col] == " ")
        {
          cat = false;
          return cat;
        }
        else if (str[row][col] == "X" || str[row][col] == "O")
          cat = true;
      }
    }
    return cat;
  }
  
  public static void printDots()

  {
	  try
      {
        Thread.sleep(1000);
      }
      catch(Exception e)
      {
        System.out.println(e);
      }
    System.out.print(".");
    try
      {
        Thread.sleep(1000);
      }
      catch(Exception e)
      {
        System.out.println(e);
      }
      System.out.print(".");
      try
      {
        Thread.sleep(1000);
      }
      catch(Exception e)
      {
        System.out.println(e);
      }
      System.out.print(".");
      try
      {
        Thread.sleep(1000);
      }
      catch(Exception e)
      {
        System.out.println(e);
      }
  }

  public static void getStats(int i)
  {
	 if(i == 1)
	 {
		 if(deck1.getDeck().size() + drawn1.size() > deck2.getDeck().size() + drawn2.size())
		 {
			 System.out.println("Player 1 is currently leading with " + deck1.getDeck().size() + " cards in their hand, and " + (deck1.getDeck().size() + drawn1.size()) + " cards in total");
		 }
		 else if(deck1.getDeck().size() + drawn1.size() == deck2.getDeck().size() + drawn2.size())
		 {
			 System.out.println("Player 1 is currently tied with " + deck1.getDeck().size() + " cards in their hand, and " + (deck1.getDeck().size() + drawn1.size()) + " cards in total"); 
		 }
		 else if(deck1.getDeck().size() + drawn1.size() < deck2.getDeck().size() + drawn2.size())
		 {
			 System.out.println("Player 1 is currently behind player 2 with " + deck1.getDeck().size() + " cards in their hand, and " + (deck1.getDeck().size() + drawn1.size()) + " cards in total"); 
		 }
		 
		 System.out.println("\nTotal Rounds won: " + p1Round);
		 System.out.println("\nTotal TicTacToe games won: " + p1TicCount);
		/* System.out.println("\n\nPlayer 1 has Taken:");
		 System.out.println("-------------------");
		 System.out.println("Ones: " + p1One);
		 System.out.println("Twos: " + p1Two);
		 System.out.println("Threes: " + p1Three);
		 System.out.println("Fours: " + p1Four);
		 System.out.println("Fives: " + p1Five);
		 System.out.println("Sixes: " + p1Six);
		 System.out.println("Sevens: " + p1Seven);
		 System.out.println("Eights " + p1Eight);
		 System.out.println("Nines: " + p1Nine);
		 System.out.println("Tens: " + p1Ten);
		 System.out.println("Jacks: " + p1Jack);
		 System.out.println("Queens: " + p1Queen);
		 System.out.println("Kings: " + p1King);
		 System.out.println("Aces: " + p1Ace); */
		 
		 System.out.println("\n\n\nEnter '1' to draw");
     	turn = input.nextLine();
	 }
	 else if(i == 2)
	 {
		 if(deck1.getDeck().size() + drawn1.size() < deck2.getDeck().size() + drawn2.size())
		 {
			 System.out.println("Player 2 is currently leading with " + deck2.getDeck().size() + " cards in their hand, and " + (deck2.getDeck().size() + drawn2.size()) + " cards in total");
		 }
		 else if(deck1.getDeck().size() + drawn1.size() == deck2.getDeck().size() + drawn2.size())
		 {
			 System.out.println("Player 2 is currently tied with " + deck2.getDeck().size() + " cards in their hand, and " + (deck2.getDeck().size() + drawn2.size()) + " cards in total"); 
		 }
		 else if(deck1.getDeck().size() + drawn1.size() > deck2.getDeck().size() + drawn2.size())
		 {
			 System.out.println("Player 2 is currently behind player 1 with " + deck2.getDeck().size() + " cards in their hand, and " + (deck2.getDeck().size() + drawn2.size()) + " cards in total"); 
		 }
		 
		 System.out.println("\nTotal Rounds won: " + p2Round);
		 System.out.println("\nTotal TicTacToe games won: " + p2TicCount);
		/* System.out.println("\n\nPlayer 2 has Taken:");
		 System.out.println("-------------------");
		 System.out.println("Ones: " + p2One);
		 System.out.println("Twos: " + p2Two);
		 System.out.println("Threes: " + p2Three);
		 System.out.println("Fours: " + p2Four);
		 System.out.println("Fives: " + p2Five);
		 System.out.println("Sixes: " + p2Six);
		 System.out.println("Sevens: " + p2Seven);
		 System.out.println("Eights " + p2Eight);
		 System.out.println("Nines: " + p2Nine);
		 System.out.println("Tens: " + p2Ten);
		 System.out.println("Jacks: " + p2Jack);
		 System.out.println("Queens: " + p2Queen);
		 System.out.println("Kings: " + p2King);
		 System.out.println("Aces: " + p2Ace);  */
		 
		 System.out.println("\n\n\nEnter '1' to draw");
     	turn = input.nextLine();
	 }
  }
}