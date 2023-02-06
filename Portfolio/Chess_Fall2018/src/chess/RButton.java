package chess;

import javax.swing.JButton;

public class RButton extends JButton
{
	String name;
	String link;
	String color;
	String type;
	int row;
	int col;
	int red;
	int green;
	int blue;
	int x;
	int y;
	boolean lastThere;
	boolean lastHere;
	
	public RButton(String n, String l, String c, String t, int r, int cl, int rD, int g, int b, int x, int y, boolean tH, boolean h)
	{
		name = n;
		link = l;
		color = c;
		type = t;
		row = r;
		col = cl;
		red = rD;
		green = g;
		blue = b;
		this.x = x;
		this.y = y;
		lastThere = tH;
		lastHere = h;
		
	}
	
	public void setName(String n)
	{
		name = n;
	}
	
	public String getName()
	{
		return name;
	}
	
	
	public void setLink(String l)
	{
		link = l;
	}
	
	public String getLink()
	{
		return link;
	}
	
	
	public void setColor(String c)
	{
		color = c;
	}
	
	public String getColor()
	{
		return color;
	}
	
	public void setType(String t)
	{
		type = t;
	}
	
	public String getType()
	{
		return type;
	}
	
	public void setRow(int r)
	{
		row = r;
	}
	
	public int getRow()
	{
		return row;
	}
	
	public void setCol(int cl)
	{
		col = cl;
	}
	
	public int getCol()
	{
		return col;
	}
	
	
	public void setRed(int rD)
	{
		red = rD;
	}
	
	public int getRed()
	{
		return red;
	}
	
	
	public void setGreen(int g)
	{
		green = g;
	}
	
	public int getGreen()
	{
		return green;
	}
	
	
	public void setBlue(int b)
	{
		blue = b;
	}
	
	public int getBlue()
	{
		return blue;
	}
	
	
	public void setX(int x)
	{
		this.x = x;
	}
	
	public int getX()
	{
		return x;
	}
	
	
	public void setY(int y)
	{
		this.y = y;
	}
	
	public int getY()
	{
		return y;
	}
	
	
	public void setLastThere(boolean tH)
	{
		lastThere = tH;
	}
	
	public boolean isLastThere()
	{
		return lastThere;
	}
	
	
	public void setLastHere(boolean h)
	{
		lastHere = h;
	}
	
	public boolean isLastHere()
	{
		return lastHere;
	}
}
