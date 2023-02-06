package chess;
import java.util.ArrayList;
import java.util.Random;

public class Rabehl_WarDeckOfCards
{
  ArrayList<Integer> deck;
  int[] drawn;
  Random generator = new Random();
  int card = 0;
  
  public Rabehl_WarDeckOfCards(int num)
  {
    deck = new ArrayList<Integer>();
    if(num == 1)
    {
      for(Integer i = 2; i <= 14; i++)
      {
        for(Integer j = 1; j <= 4; j++)
        {
        deck.add(i); 
        }
      }
    }
  }
  
  public ArrayList<Integer> getDeck()
  {
    return deck;
  }
  public void addCard(Integer num)
  {
    deck.add(num);
  }
  
  public void printDeck()
  {
    System.out.println(deck);
  }
  
  public void replace(ArrayList<Integer> drawn)
  {
    System.out.println("drawn: " + drawn);
    for(int i = 0; i < drawn.size(); i++)
    {
      deck.add(i,drawn.get(0));
      drawn.remove(0);
    }
    System.out.println("new drawn: " + drawn + "\ndeck: " + deck);
  }
  
  public int draw()
  {
    card = deck.get(0);
    deck.remove(0);
    
    return card;
  }
  
  public void shuffle()
  {
    Integer num2;
    Integer num1;
    Integer temp;
    int size;
    int slot1;
    int slot2;
    for(int i = 0; i < 1001; i++)
    {
      slot2 = generator.nextInt(deck.size()-1);
      num2 = deck.get(slot2);
      
      slot1 = generator.nextInt(deck.size()-1);
      num1 = deck.get(slot1);
      
      temp = num1;
      
      while(slot2 == slot1)
      {
        slot2 = generator.nextInt(deck.size()-1);
        num2 = deck.get(slot2);
        
        slot1 = generator.nextInt(deck.size()-1);
        num1 = deck.get(slot1);
        
        temp = num1;
      }
      deck.set(slot1, num2);
      deck.set(slot2, num1);
    }
  }
  
  public void replaceAllCards()
  {
    for(int i = 0; i < drawn.length-1; i++)
    {
      deck.add(drawn[i]);
      
    }
    
  }
}