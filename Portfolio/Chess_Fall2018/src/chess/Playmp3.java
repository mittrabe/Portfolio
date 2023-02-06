package chess;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import javazoom.jl.decoder.JavaLayerException;
import javazoom.jl.player.Player;

public class Playmp3 
{
	
	public static void main(String[] args)
	{
		try
		{
		FileInputStream fileInputStream = new FileInputStream("C:\\Users\\1magi\\eclipse-workspace\\Rabehl_WarTacToe\\bin\\chess\\tavernMusic.mp3");
		Player player = new Player(fileInputStream);
		player.play();
		}
		catch(FileNotFoundException e)
		{
			System.out.println(e);
		} 
		catch(JavaLayerException e) 
		{
			System.out.println(e);
		}
	}
}
