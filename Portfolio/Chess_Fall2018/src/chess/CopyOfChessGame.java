package chess;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.net.URL;
import javax.imageio.ImageIO;
import javax.swing.*;
import java.io.FileInputStream;
import java.io.FileNotFoundException;

import javazoom.jl.decoder.JavaLayerException;
import javazoom.jl.player.Player;


public class CopyOfChessGame extends Frame
{
	static JButton board[][] = new JButton[8][8];
	static Thread object = new Thread(new MultiThreadMp3());
	static JFrame frame = new JFrame("Chess Board");
	static CopyOfDrawingPanel chessBoard; 
	
	static int win = 0;
	
	public static void main(String[] args)
	{      
		chessBoard = new CopyOfDrawingPanel();
		
		setJFrame();
	
		while(true)
		{
			try
			{
				Thread.sleep(1000);
			}
			catch(Exception e)
			{
				System.out.println(e);
			}
			if(chessBoard.getGameOver().equals("over"))
			break;
			
		}
		setWin(chessBoard.getWinner());
		
		System.out.println(getWin());
	}
	
	
	
	public static void setJFrame()
	{	
		Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
		frame.setPreferredSize(screenSize);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setUndecorated(true);
		frame.getContentPane().add(chessBoard);
		frame.pack();
		
		
		frame.setVisible(true);
	}
	
	public static void setWin(int w)
	{
		win = w;
	}
	
	public static int getWin()
	{
		return win;
	}
}
