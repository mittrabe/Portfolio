package chess;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.nio.file.Paths;
import java.util.ArrayList;

import javax.swing.*;
import javax.swing.event.SwingPropertyChangeSupport;

import javazoom.jl.decoder.JavaLayerException;
import javazoom.jl.player.Player;

//Things to do
//~~~~~~~~~~~~~~~~
//1) Fix current exit button so that it doesn't end the program and simply closes the window
//2) Make it so the music isn't tied to this specific computer (line 2654)

public class DrawingPanel extends JPanel implements ActionListener {

	protected static String getFilePath() {
		String filePath = Paths.get(".").toAbsolutePath().toString().replace(".", ""); // Get folder path

		filePath += "Chess Piece Images\\";

		return filePath;
	}
	protected static void printPath(String path){
		System.out.println(path);
	}
	// Represents each individual type of piece
	// ---------------------------------------------------------------------------
	
	private String bPawnName = new String("Black Pawn");
	private String bPawnLink = new String("Chess Piece Images/bPawn.png");
	private String bPawnColor = new String("Black");
	private String bPawnType = new String("Piece");
	private ImageIcon bPawn = new ImageIcon(this.getClass().getResource(bPawnLink));

	/*
	 * private String bPawnName1 = "Black Pawn"; private String bPawnLink1 =
	 * getFilePath() + "bPawn.png"; private String bPawnColor1 = new
	 * String("Black"); private String bPawnType1 = new String("Piece"); private
	 * ImageIcon bPawn1 = new ImageIcon(this.getClass().getResource(bPawnLink));
	 */

	private String bRookName = new String("Black Rook");
	private String bRookLink = new String("/Chess Piece Images/bRook.png");
	private String bRookColor = new String("Black");
	private String bRookType = new String("Piece");
	private ImageIcon bRook = new ImageIcon(this.getClass().getResource(bRookLink));

	private String bKnightName = new String("Black Knight");
	private String bKnightLink = new String("/Chess Piece Images/bKnight.png");
	private String bKnightColor = new String("Black");
	private String bKnightType = new String("Piece");
	private ImageIcon bKnight = new ImageIcon(this.getClass().getResource(bKnightLink));

	private String bBishopName = new String("Black Bishop");
	private String bBishopLink = new String("/Chess Piece Images/bBishop.png");
	private String bBishopColor = new String("Black");
	private String bBishopType = new String("Piece");
	private ImageIcon bBishop = new ImageIcon(this.getClass().getResource(bBishopLink));

	private String bKingName = new String("Black King");
	private String bKingLink = new String("/Chess Piece Images/bKing.png");
	private String bKingColor = new String("Black");
	private String bKingType = new String("Piece");
	private ImageIcon bKing = new ImageIcon(this.getClass().getResource(bKingLink));

	private String bQueenName = new String("Black Queen");
	private String bQueenLink = new String("/Chess Piece Images/bQueen.png");
	private String bQueenColor = new String("Black");
	private String bQueenType = new String("Piece");
	private ImageIcon bQueen = new ImageIcon(this.getClass().getResource(bQueenLink));

	private String wPawnName = new String("White Pawn");
	private String wPawnLink = new String("/Chess Piece Images/wPawn.png");
	private String wPawnColor = new String("White");
	private String wPawnType = new String("Piece");
	private ImageIcon wPawn = new ImageIcon(this.getClass().getResource(wPawnLink));

	private String wRookName = new String("White Rook");
	private String wRookLink = new String("/Chess Piece Images/wRook.png");
	private String wRookColor = new String("White");
	private String wRookType = new String("Piece");
	private ImageIcon wRook = new ImageIcon(this.getClass().getResource(wRookLink));

	private String wKnightName = new String("White Knight");
	private String wKnightLink = new String("/Chess Piece Images/wKnight.png");
	private String wKnightColor = new String("White");
	private String wKnightType = new String("Piece");
	private ImageIcon wKnight = new ImageIcon(this.getClass().getResource(wKnightLink));

	private String wBishopName = new String("White Bishop");
	private String wBishopLink = new String("/Chess Piece Images/wBishop.png");
	private String wBishopColor = new String("White");
	private String wBishopType = new String("Piece");
	private ImageIcon wBishop = new ImageIcon(this.getClass().getResource(wBishopLink));

	private String wKingName = new String("White King");
	private String wKingLink = new String("/Chess Piece Images/wKing.png");
	private String wKingColor = new String("White");
	private String wKingType = new String("Piece");
	private ImageIcon wKing = new ImageIcon(this.getClass().getResource(wKingLink));

	private String wQueenName = new String("White Queen");
	private String wQueenLink = new String("/Chess Piece Images/wQueen.png");
	private String wQueenColor = new String("White");
	private String wQueenType = new String("Piece");
	private ImageIcon wQueen = new ImageIcon(this.getClass().getResource(wQueenLink));

	private String emptyName = new String("Empty");
	private String emptyLink = new String("/Chess Piece Images/transparent.png");
	private String emptyColor = new String("null");
	private String emptyType = new String("Space");
	private ImageIcon empty = new ImageIcon(this.getClass().getResource(emptyLink));

	private ImageIcon exitIcon = new ImageIcon(this.getClass().getResource("/Chess Piece Images/exitIcon.png"));
	private ImageIcon volumeIcon = new ImageIcon(this.getClass().getResource("/Chess Piece Images/volumeIcon.png"));

	// Each button represents a square on the board
	// -----------------------------------------------------------------------------
	private RButton a1;
	private RButton a2;
	private RButton a3;
	private RButton a4;
	private RButton a5;
	private RButton a6;
	private RButton a7;
	private RButton a8;
	private RButton b1;
	private RButton b2;
	private RButton b3;
	private RButton b4;
	private RButton b5;
	private RButton b6;
	private RButton b7;
	private RButton b8;
	private RButton c1;
	private RButton c2;
	private RButton c3;
	private RButton c4;
	private RButton c5;
	private RButton c6;
	private RButton c7;
	private RButton c8;
	private RButton d1;
	private RButton d2;
	private RButton d3;
	private RButton d4;
	private RButton d5;
	private RButton d6;
	private RButton d7;
	private RButton d8;
	private RButton e1;
	private RButton e2;
	private RButton e3;
	private RButton e4;
	private RButton e5;
	private RButton e6;
	private RButton e7;
	private RButton e8;
	private RButton f1;
	private RButton f2;
	private RButton f3;
	private RButton f4;
	private RButton f5;
	private RButton f6;
	private RButton f7;
	private RButton f8;
	private RButton g1;
	private RButton g2;
	private RButton g3;
	private RButton g4;
	private RButton g5;
	private RButton g6;
	private RButton g7;
	private RButton g8;
	private RButton h1;
	private RButton h2;
	private RButton h3;
	private RButton h4;
	private RButton h5;
	private RButton h6;
	private RButton h7;
	private RButton h8;

	// Represents the two colors of square
	private int red1 = 238;
	private int green1 = 219; // lighter square
	private int blue1 = 179;

	private int red2 = 181;
	private int green2 = 135; // darker square
	private int blue2 = 99;

	private int moveR = 212;
	private int moveG = 189; // move___ represents the color for the spaces that can be moved to.
	private int moveB = 106;

	private int selectR = 217;
	private int selectG = 162; // select_____ represents the color for a selected piece.
	private int selectB = 50;

	private int grey1 = 190;
	private int grey2 = 120;

	private boolean selected = false; // Used to determine whether a button push is the second or the first
	private boolean vSelected = false; // vSelected == whether or not the volume button is being selected

	private String turn = new String("White");
	private String tempTurn = new String();

	private RButton here; // Button/piece at starting location
	private RButton there; // Button at location being moved to

	RButton board[][] = new RButton[8][8]; // Contains the array of buttons/squares of the board
	ImageIcon pieces[][] = new ImageIcon[8][8]; // Contains images of each piece in the order in which they are at the
												// start of the game
	String names[][] = new String[8][8]; // contains the names of each piece in the order in which they are at the start
											// of the game
	String links[][] = new String[8][8]; // contains the links to each piece image in the order in which they are at the
											// start of the game
	String color[][] = new String[8][8]; // contains the links to each piece color in the order in which they are at the
											// start of the game
	String type[][] = new String[8][8]; // You get the idea

	ArrayList<RButton> moves = new ArrayList<RButton>(); // moves contains all possible moves for a given piece

	ArrayList<ImageIcon> wGraveYard = new ArrayList<ImageIcon>(); // contains all captured white pieces
	ArrayList<ImageIcon> bGraveYard = new ArrayList<ImageIcon>(); // contains all captured black pieces

	Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();

	private String game = new String();

	private boolean repaint = false; // Used for the code that only needs to be run once

	int miniInt = 0;

	String musicVol; // music muted -or- unmuted

	int winner = 0;

	Thread obj = new Thread(new MultiThreadMp3());

	JFrame frame = new JFrame();

	public DrawingPanel() {
		setPreferredSize(screenSize);
		setFocusable(true);
		setBackground(Color.white);
		setVisible(true);

		obj.start(); // Starts the music

	}

	public void paintComponent(Graphics g) {
		super.paintComponent(g);

		g.setColor(new Color(56, 22, 13)); // Brown border thing
		g.fillRect(0, 850, 2000, 150);
		g.fillRect(0, 0, 50, 850);
		g.fillRect(0, 0, 2000, 50);
		g.fillRect(850, 0, 50, 850);
		g.fillRect(1850, 0, 50, 850);
		g.fillRect(0, 1000, 2000, 150);
		g.fillRect(1900, 0, 50, 850);

		g.setColor(new Color(red2, green2, blue2)); // ScoreBoard background (left half)
		g.fillRect(900, 50, 475, 800);

		g.setColor(new Color(red1, green1, blue1)); // ScoreBoard background (right half)
		g.fillRect(1375, 50, 475, 800);

		g.setColor(new Color(red2, green2, blue2));
		Font font = new Font("Helvetica", Font.BOLD, 100);
		g.setFont(font);

		g.drawString("Board", 300, 950);
		font = new Font("Helvetica", font.BOLD, 80);
		g.drawString("Scoreboard", 1100, 950);

		font = new Font("Helvetica", Font.ITALIC, 38);
		g.setFont(font);

		if (turn.equals("White")) // This should in theory highlight the name of the player whose turn it is
		{
			g.setColor(new Color(moveR, moveG, moveB)); // highlights player name
			g.fillRect(970, 60, 300, 60);

			g.setColor(new Color(red1, green1, blue1)); // unhighlights other player name
			g.fillRect(1470, 60, 300, 60);
		} else if (turn.equals("Black")) {
			g.setColor(new Color(moveR, moveG, moveB));
			g.fillRect(1470, 60, 300, 60);

			g.setColor(new Color(red2, green2, blue2));
			g.fillRect(970, 60, 300, 60);
		}

		g.setColor(Color.white);
		g.drawString("Player 1 (White)", 980, 100); // Sets the headers of the left half of the ScoreBoard
		g.drawString("--------------------", 980, 124);

		g.setColor(Color.black);
		g.drawString("Player 2 (Black)", 1480, 100); // Sets the header of the right half of the ScoreBoard
		g.drawString("--------------------", 1480, 124);

		g.setColor(Color.white);
		String letters = "ABCDEFGH";
		int y = 120;
		for (int i = 0; i < 8; i++) {
			g.drawString(letters.substring(i, i + 1), 10, y);

			y += 100;
		}
		String numbers = "12345678";
		int x = 85;
		for (int i = 0; i < 8; i++) {
			g.drawString(numbers.substring(i, i + 1), x, 38);

			x += 100;
		}

		g.drawString("A", 10, 120);
		g.drawString("B", 10, 220);

		RButton exit = new RButton("exit", "", "", "", 0, 0, 0, 0, 0, 1870, 0, false, false); // This button allows you
																								// to exit out of game

		exit.setBackground(Color.red);
		exit.setSize(48, 48);
		exit.setLocation(1870, 0);
		exit.setIcon(exitIcon);
		exit.addActionListener(this);

		add(exit);

		RButton volume = new RButton("volume", "", "", "", 0, 0, 0, 0, 0, 1868, 1028, false, false);

		volume.setBackground(new Color(red2, green2, blue2));
		volume.setSize(50, 50);
		volume.setLocation(1868, 1028);
		volume.setIcon(volumeIcon);
		volume.addActionListener(this);

		add(volume);

		vSelected = false;

		if (repaint == false) // Anything within this 'if' statement will only happen the first time
								// paintComponent is ran
		{
			setArray();

			setBoard(board, names, links);

			musicVol = "unmuted";

		}

		repaint = true;

		// --------------------------------------------------------------------
		// | Previous Turn MiniMap |
		// --------------------------------------------------------------------

		int miniY = 885;

		for (int row = 0; row < board.length; row++) {
			int miniX = 815;

			if (row != 0)
				miniY += 15;

			for (int col = 0; col < board[row].length; col++) {
				if (row % 2 == 0) {
					if (col % 2 == 0) {
						g.setColor(new Color(red1, green1, blue1));
						g.fillRect(miniX, miniY, 15, 15);

						// if(moves.contains(board[row][col]))

						if (board[row][col].isLastThere() == true) {
							g.setColor(new Color(moveR, moveG, moveB));
							g.fillRect(miniX, miniY, 15, 15);
							board[row][col].setLastThere(false);
						}
						if (board[row][col].isLastHere() == true) {
							g.setColor(new Color(selectR, selectG, selectB));
							g.fillRect(miniX, miniY, 15, 15);
							board[row][col].setLastHere(false);
						}

						if (board[row][col].getColor().equals("null")) {
						} else if (board[row][col].getColor().equals("Black")) {
							g.setColor(Color.black);
							g.fillRect(miniX + 5, miniY + 5, 5, 5);
						} else if (board[row][col].getColor().equals("White")) {
							g.setColor(Color.white);
							g.fillRect(miniX + 5, miniY + 5, 5, 5);
						}

					} else {
						g.setColor(new Color(red2, green2, blue2));
						g.fillRect(miniX, miniY, 15, 15);

						if (board[row][col].isLastThere() == true) {
							g.setColor(new Color(moveR, moveG, moveB));
							g.fillRect(miniX, miniY, 15, 15);
							board[row][col].setLastThere(false);
						}
						if (board[row][col].isLastHere() == true) {
							g.setColor(new Color(selectR, selectG, selectB));
							g.fillRect(miniX, miniY, 15, 15);
							board[row][col].setLastHere(false);
						}

						if (board[row][col].getColor().equals("null")) {
						} else if (board[row][col].getColor().equals("Black")) {
							g.setColor(Color.black);
							g.fillRect(miniX + 5, miniY + 5, 5, 5);
						} else if (board[row][col].getColor().equals("White")) {
							g.setColor(Color.white);
							g.fillRect(miniX + 5, miniY + 5, 5, 5);
						}

					}
				}

				else if (row % 2 != 0) {
					if (col % 2 == 0) {
						g.setColor(new Color(red2, green2, blue2));
						g.fillRect(miniX, miniY, 15, 15);
						g.fillRect(miniX, miniY, 15, 15);

						if (board[row][col].isLastThere() == true) {
							g.setColor(new Color(moveR, moveG, moveB));
							g.fillRect(miniX, miniY, 15, 15);
							board[row][col].setLastThere(false);
						}
						if (board[row][col].isLastHere() == true) {
							g.setColor(new Color(selectR, selectG, selectB));
							g.fillRect(miniX, miniY, 15, 15);
							board[row][col].setLastHere(false);
						}

						if (board[row][col].getColor().equals("null")) {
						} else if (board[row][col].getColor().equals("Black")) {
							g.setColor(Color.black);
							g.fillRect(miniX + 5, miniY + 5, 5, 5);
						} else if (board[row][col].getColor().equals("White")) {
							g.setColor(Color.white);
							g.fillRect(miniX + 5, miniY + 5, 5, 5);
						}

					} else {
						g.setColor(new Color(red1, green1, blue1));
						g.fillRect(miniX, miniY, 15, 15);

						if (board[row][col].isLastThere() == true) {
							g.setColor(new Color(moveR, moveG, moveB));
							g.fillRect(miniX, miniY, 15, 15);
							board[row][col].setLastThere(false);
						}
						if (board[row][col].isLastHere() == true) {
							g.setColor(new Color(selectR, selectG, selectB));
							g.fillRect(miniX, miniY, 15, 15);
							board[row][col].setLastHere(false);
						}

						if (board[row][col].getColor().equals("null")) {
						} else if (board[row][col].getColor().equals("Black")) {
							g.setColor(Color.black);
							g.fillRect(miniX + 5, miniY + 5, 5, 5);
						} else if (board[row][col].getColor().equals("White")) {
							g.setColor(Color.white);
							g.fillRect(miniX + 5, miniY + 5, 5, 5);
						}

					}
				}
				miniX += 15;
			}
		}

		if (bGraveYard.size() > 0 || wGraveYard.size() > 0) // Sets the scoreboard (or graveyard)
		{
			int j = 960;
			int k = j;
			int j2 = 1435;
			int k2 = j2;

			if (bGraveYard.size() < 4) {
				for (int i = 0; i < bGraveYard.size(); i++) {
					g.drawImage(bGraveYard.get(i).getImage(), j, 125, null);
					j += 100;
				}
			}

			else if (bGraveYard.size() >= 4 && bGraveYard.size() < 8) {
				for (int i = 0; i < 4; i++) {
					g.drawImage(bGraveYard.get(i).getImage(), j, 125, null);
					j += 100;
				}
				j = k;
				for (int i = 4; i < bGraveYard.size(); i++) {
					g.drawImage(bGraveYard.get(i).getImage(), j, 225, null);
					j += 100;
				}
			}

			else if (bGraveYard.size() >= 8 && bGraveYard.size() < 12) {
				for (int i = 0; i < 4; i++) {
					g.drawImage(bGraveYard.get(i).getImage(), j, 125, null);
					j += 100;
				}
				j = k;
				for (int i = 4; i < 8; i++) {
					g.drawImage(bGraveYard.get(i).getImage(), j, 225, null);
					j += 100;
				}
				j = k;
				for (int i = 8; i < bGraveYard.size(); i++) {
					g.drawImage(bGraveYard.get(i).getImage(), j, 325, null);
					j += 100;
				}
			}

			else if (bGraveYard.size() >= 12 && bGraveYard.size() < 16) {
				for (int i = 0; i < 4; i++) {
					g.drawImage(bGraveYard.get(i).getImage(), j, 125, null);
					j += 100;
				}
				j = k;
				for (int i = 4; i < 8; i++) {
					g.drawImage(bGraveYard.get(i).getImage(), j, 225, null);
					j += 100;
				}
				j = k;
				for (int i = 8; i < 12; i++) {
					g.drawImage(bGraveYard.get(i).getImage(), j, 325, null);
					j += 100;
				}
				j = k;
				for (int i = 12; i < bGraveYard.size(); i++) {
					g.drawImage(bGraveYard.get(i).getImage(), j, 425, null);
					j += 100;
				}
			}

			if (wGraveYard.size() < 4) {
				for (int i = 0; i < wGraveYard.size(); i++) {
					g.drawImage(wGraveYard.get(i).getImage(), j2, 125, null);
					j2 += 100;
				}
			}

			else if (wGraveYard.size() >= 4 && wGraveYard.size() < 8) {
				for (int i = 0; i < 4; i++) {
					g.drawImage(wGraveYard.get(i).getImage(), j2, 125, null);
					j2 += 100;
				}
				j2 = k2;
				for (int i = 4; i < wGraveYard.size(); i++) {
					g.drawImage(wGraveYard.get(i).getImage(), j2, 225, null);
					j2 += 100;
				}
			}

			else if (wGraveYard.size() >= 8 && wGraveYard.size() < 12) {
				for (int i = 0; i < 4; i++) {
					g.drawImage(wGraveYard.get(i).getImage(), j2, 125, null);
					j2 += 100;
				}
				j2 = k2;
				for (int i = 4; i < 8; i++) {
					g.drawImage(wGraveYard.get(i).getImage(), j2, 225, null);
					j2 += 100;
				}
				j2 = k2;
				for (int i = 8; i < wGraveYard.size(); i++) {
					g.drawImage(wGraveYard.get(i).getImage(), j2, 325, null);
					j2 += 100;
				}
			}

			else if (wGraveYard.size() >= 12 && wGraveYard.size() < 16) {
				for (int i = 0; i < 4; i++) {
					g.drawImage(wGraveYard.get(i).getImage(), j2, 125, null);
					j2 += 100;
				}
				j2 = k2;
				for (int i = 4; i < 8; i++) {
					g.drawImage(wGraveYard.get(i).getImage(), j2, 225, null);
					j2 += 100;
				}
				j2 = k2;
				for (int i = 8; i < 12; i++) {
					g.drawImage(wGraveYard.get(i).getImage(), j2, 325, null);
					j2 += 100;
				}
				j2 = k2;
				for (int i = 12; i < wGraveYard.size(); i++) {
					g.drawImage(wGraveYard.get(i).getImage(), j2, 425, null);
					j2 += 100;
				}
			}

		}

		if (game.equals("over")) // Game over screen
		{
			g.setColor(new Color(64, 64, 64)); // border
			g.fillRect(0, 850, 2000, 150);
			g.fillRect(0, 0, 50, 850);
			g.fillRect(0, 0, 2000, 50);
			g.fillRect(850, 0, 50, 850);
			g.fillRect(1850, 0, 50, 850);
			g.fillRect(0, 1000, 2000, 150);
			g.fillRect(1900, 0, 50, 850);

			g.setColor(new Color(grey2, grey2, grey2)); // ScoreBoard background (left half)
			g.fillRect(900, 50, 475, 800);

			g.setColor(new Color(grey1, grey1, grey1)); // ScoreBoard background (right half)
			g.fillRect(1375, 50, 475, 800);

			g.setColor(new Color(grey2, grey2, grey2));
			font = new Font("Helvetica", Font.BOLD, 100);
			g.setFont(font);

			g.drawString("Board", 300, 950);
			font = new Font("Helvetica", font.BOLD, 80);
			g.drawString("Scoreboard", 1100, 950);

			font = new Font("Helvetica", Font.ITALIC, 38);
			g.setFont(font);

			if (turn.equals("White")) // This should in theory highlight the name of the player whose turn it is
			{
				g.setColor(new Color(220, 220, 220)); // highlights player name
				g.fillRect(970, 60, 300, 60);

				g.setColor(new Color(grey1, grey1, grey1)); // unhighlights other player name
				g.fillRect(1470, 60, 300, 60);
			} else if (turn.equals("Black")) {
				g.setColor(new Color(220, 220, 220));
				g.fillRect(1470, 60, 300, 60);

				g.setColor(new Color(grey2, grey2, grey2));
				g.fillRect(970, 60, 300, 60);
			}

			g.setColor(Color.white);
			g.drawString("Player 1 (White)", 980, 100); // Sets the headers of the left half of the ScoreBoard
			g.drawString("--------------------", 980, 124);

			g.setColor(Color.black);
			g.drawString("Player 2 (Black)", 1480, 100); // Sets the header of the right half of the ScoreBoard
			g.drawString("--------------------", 1480, 124);

			g.setColor(Color.white);
			letters = "ABCDEFGH";
			y = 120;
			for (int i = 0; i < 8; i++) {
				g.drawString(letters.substring(i, i + 1), 10, y);

				y += 100;
			}
			numbers = "12345678";
			x = 85;
			for (int i = 0; i < 8; i++) {
				g.drawString(numbers.substring(i, i + 1), x, 38);

				x += 100;
			}

			g.drawString("A", 10, 120);
			g.drawString("B", 10, 220);

			exit = new RButton("exit", "", "", "", 0, 0, 0, 0, 0, 1870, 0, false, false); // This button allows you to
																							// exit out of game

			exit.setBackground(Color.red);
			exit.setSize(48, 48);
			exit.setLocation(1870, 0);
			exit.setIcon(exitIcon);
			exit.addActionListener(this);

			add(exit);

			g.setColor(Color.red);
			font = new Font("Helvetica", font.BOLD, 135);
			g.setFont(font);

			g.drawString("Game Over", 950, 500);

			for (int row = 0; row < board.length; row++) {

				for (int col = 0; col < board[row].length; col++) {
					if (row % 2 == 0) {
						if (col % 2 == 0) {
							board[row][col].setBackground(new Color(grey1, grey1, grey1));
						} else {
							board[row][col].setBackground(new Color(grey2, grey2, grey2));
						}
					}

					else if (row % 2 != 0) {
						if (col % 2 == 0) {
							board[row][col].setBackground(new Color(grey2, grey2, grey2));
						} else {
							board[row][col].setBackground(new Color(grey1, grey1, grey1));
						}
					}
				}
			}
		}
	}

	public void setArray() // sets the various arrays into the order that they appear on the board
	{
		pieces[0][0] = bRook;
		pieces[0][1] = bKnight;
		pieces[0][2] = bBishop;
		pieces[0][3] = bKing;
		pieces[0][4] = bQueen;
		pieces[0][5] = bBishop;
		pieces[0][6] = bKnight;
		pieces[0][7] = bRook;

		for (int i = 0; i < 8; i++) {
			pieces[1][i] = bPawn;
		}

		pieces[7][0] = wRook;
		pieces[7][1] = wKnight;
		pieces[7][2] = wBishop;
		pieces[7][3] = wKing;
		pieces[7][4] = wQueen;
		pieces[7][5] = wBishop;
		pieces[7][6] = wKnight;
		pieces[7][7] = wRook;

		for (int i = 0; i < 8; i++) {
			pieces[6][i] = wPawn;
		}

		for (int row = 2; row < 6; row++) {
			for (int col = 0; col < pieces[row].length; col++) {
				pieces[row][col] = empty;
			}
		}

		board[0][0] = a1;
		board[0][1] = a2;
		board[0][2] = a3;
		board[0][3] = a4;
		board[0][4] = a5;
		board[0][5] = a6;
		board[0][6] = a7;
		board[0][7] = a8;

		board[1][0] = b1;
		board[1][1] = b2;
		board[1][2] = b3;
		board[1][3] = b4;
		board[1][4] = b5;
		board[1][5] = b6;
		board[1][6] = b7;
		board[1][7] = b8;

		board[2][0] = c1;
		board[2][1] = c2;
		board[2][2] = c3;
		board[2][3] = c4;
		board[2][4] = c5;
		board[2][5] = c6;
		board[2][6] = c7;
		board[2][7] = c8;

		board[3][0] = d1;
		board[3][1] = d2;
		board[3][2] = d3;
		board[3][3] = d4;
		board[3][4] = d5;
		board[3][5] = d6;
		board[3][6] = d7;
		board[3][7] = d8;

		board[4][0] = e1;
		board[4][1] = e2;
		board[4][2] = e3;
		board[4][3] = e4;
		board[4][4] = e5;
		board[4][5] = e6;
		board[4][6] = e7;
		board[4][7] = e8;

		board[5][0] = f1;
		board[5][1] = f2;
		board[5][2] = f3;
		board[5][3] = f4;
		board[5][4] = f5;
		board[5][5] = f6;
		board[5][6] = f7;
		board[5][7] = f8;

		board[6][0] = g1;
		board[6][1] = g2;
		board[6][2] = g3;
		board[6][3] = g4;
		board[6][4] = g5;
		board[6][5] = g6;
		board[6][6] = g7;
		board[6][7] = g8;

		board[7][0] = h1;
		board[7][1] = h2;
		board[7][2] = h3;
		board[7][3] = h4;
		board[7][4] = h5;
		board[7][5] = h6;
		board[7][6] = h7;
		board[7][7] = h8;

		names[0][0] = bRookName;
		names[0][1] = bKnightName;
		names[0][2] = bBishopName;
		names[0][3] = bKingName;
		names[0][4] = bQueenName;
		names[0][5] = bBishopName;
		names[0][6] = bKnightName;
		names[0][7] = bRookName;

		for (int i = 0; i < 8; i++) {
			names[1][i] = bPawnName;
		}

		names[7][0] = wRookName;
		names[7][1] = wKnightName;
		names[7][2] = wBishopName;
		names[7][3] = wKingName;
		names[7][4] = wQueenName;
		names[7][5] = wBishopName;
		names[7][6] = wKnightName;
		names[7][7] = wRookName;

		for (int i = 0; i < 8; i++) {
			names[6][i] = wPawnName;
		}

		for (int row = 2; row < 6; row++) {
			for (int col = 0; col < pieces[row].length; col++) {
				names[row][col] = emptyName;
			}
		}

		links[0][0] = bRookLink;
		links[0][1] = bKnightLink;
		links[0][2] = bBishopLink;
		links[0][3] = bKingLink;
		links[0][4] = bQueenLink;
		links[0][5] = bBishopLink;
		links[0][6] = bKnightLink;
		links[0][7] = bRookLink;

		for (int i = 0; i < 8; i++) {
			links[1][i] = bPawnLink;
		}

		links[7][0] = wRookLink;
		links[7][1] = wKnightLink;
		links[7][2] = wBishopLink;
		links[7][3] = wKingLink;
		links[7][4] = wQueenLink;
		links[7][5] = wBishopLink;
		links[7][6] = wKnightLink;
		links[7][7] = wRookLink;

		for (int i = 0; i < 8; i++) {
			links[6][i] = wPawnLink;
		}

		for (int row = 2; row < 6; row++) {
			for (int col = 0; col < pieces[row].length; col++) {
				links[row][col] = emptyLink;
			}
		}

		color[0][0] = bRookColor;
		color[0][1] = bKnightColor;
		color[0][2] = bBishopColor;
		color[0][3] = bKingColor;
		color[0][4] = bQueenColor;
		color[0][5] = bBishopColor;
		color[0][6] = bKnightColor;
		color[0][7] = bRookColor;

		for (int i = 0; i < 8; i++) {
			color[1][i] = bPawnColor;
		}

		color[7][0] = wRookColor;
		color[7][1] = wKnightColor;
		color[7][2] = wBishopColor;
		color[7][3] = wKingColor;
		color[7][4] = wQueenColor;
		color[7][5] = wBishopColor;
		color[7][6] = wKnightColor;
		color[7][7] = wRookColor;

		for (int i = 0; i < 8; i++) {
			color[6][i] = wPawnColor;
		}

		for (int row = 2; row < 6; row++) {
			for (int col = 0; col < pieces[row].length; col++) {
				color[row][col] = emptyColor;
			}
		}

		type[0][0] = bRookType;
		type[0][1] = bKnightType;
		type[0][2] = bBishopType;
		type[0][3] = bKingType;
		type[0][4] = bQueenType;
		type[0][5] = bBishopType;
		type[0][6] = bKnightType;
		type[0][7] = bRookType;

		for (int i = 0; i < 8; i++) {
			type[1][i] = bPawnType;
		}

		type[7][0] = wRookType;
		type[7][1] = wKnightType;
		type[7][2] = wBishopType;
		type[7][3] = wKingType;
		type[7][4] = wQueenType;
		type[7][5] = wBishopType;
		type[7][6] = wKnightType;
		type[7][7] = wRookType;

		for (int i = 0; i < 8; i++) {
			type[6][i] = wPawnType;
		}

		for (int row = 2; row < 6; row++) {
			for (int col = 0; col < pieces[row].length; col++) {
				type[row][col] = emptyType;
			}
		}
	}

	public void setBoard(RButton[][] board, String[][] names, String[][] links) {
		int y = 50;

		int numRow = 0; // These two variables are for the array of pieces
		int numCol = 0;

		RButton square = new RButton("", "", "", "", 0, 0, 0, 0, 0, 0, 0, false, false);

		for (int row = 0; row < board.length; row++) {
			if (row != 0)
				numRow++;

			int x = 50;

			if (row != 0)
				y += 100;

			numCol = 0;
			for (int col = 0; col < board[row].length; col++) {
				square = new RButton(names[row][col], links[row][col], color[row][col], type[row][col], row, col, 0, 0,
						0, x, y, false, false);

				if (row % 2 == 0) {
					if (col % 2 == 0) {
						setSquareInfo(square, x, y, numRow, numCol, red1, green1, blue1);

						board[row][col] = square;

						add(square);
					} else {
						setSquareInfo(square, x, y, numRow, numCol, red2, green2, blue2);

						board[row][col] = square;

						add(square);
					}
				}

				else if (row % 2 != 0) {
					if (col % 2 == 0) {
						setSquareInfo(square, x, y, numRow, numCol, red2, green2, blue2);

						board[row][col] = square;

						add(square);
					} else {
						setSquareInfo(square, x, y, numRow, numCol, red1, green1, blue1);

						board[row][col] = square;

						add(square);
					}
				}
				numCol++;
				x += 100;
			}
		}
	}

	public void setSquareInfo(RButton square, int x, int y, int numRow, int numCol, int red, int green, int blue) {
		square.setRed(red);
		square.setGreen(green);
		square.setBlue(blue);

		square.setBackground(new Color(square.getRed(), square.getGreen(), square.getBlue()));
		square.setSize(100, 100);
		square.setX(x);
		square.setY(y);
		square.setLocation(square.getX(), square.getY());
		square.setIcon(pieces[numRow][numCol]);
		square.addActionListener(this);

	}

	@SuppressWarnings("deprecation")
	public void actionPerformed(ActionEvent e) {
		if (((RButton) e.getSource()).getName().equals("exit")) // e.getSource() lets you use whichever button was
																// clicked
		{
			System.exit(0);

		}

		if (((RButton) e.getSource()).getName().equals("volume")) // e.getSource() lets you use whichever button was
																	// clicked
		{
			if (musicVol.equals("muted")) {
				musicVol = "unmuted";
				obj.resume(); // Resumes music
			} else if (musicVol.equals("unmuted")) {
				obj.suspend(); // Actually pauses music instead of muting it.

				musicVol = "muted";
			}
			remove((RButton) e.getSource());

			vSelected = true;

			repaint();
		}

		// ---------------------------------------------------------------------------------
		// | This code refers to the piece you are trying to move |
		// ---------------------------------------------------------------------------------
		if (vSelected != true) {
			if (!game.equals("over")) {

				if (selected == false) {
					tempTurn = turn;

					here = (RButton) e.getSource();
					selected = true;

					if (!here.getName().equals("emptyName") && !here.getName().equals("volume")) {
						here.setBackground(new Color(selectR, selectG, selectB));

						movePiece(here, here.getRow(), here.getCol());
					}
				}

				// ---------------------------------------------------------------------------------
				// | This code refers to where you are trying to move |
				// ---------------------------------------------------------------------------------
				else if (selected == true) // selected being true means that a piece has already been selected (aka,
											// there is the square being moved to)
				{
					there = (RButton) e.getSource();

					if (here.equals(there)) {
						selected = false;
						turn = tempTurn;
						resetSquareColor(board);
					} else if (moves.contains((RButton) there)) {
						selected = false;

						setMove(here, there, board);
						resetSquareColor(board);

					} else if (!moves.contains((RButton) there)) {
						selected = false;
						turn = tempTurn;
						resetSquareColor(board);
					}
				}
			}
		}
	}

	public void movePiece(RButton square, int row, int col) // This method itself doesn't actually move the piece
															// directly
	{
		if (moves.size() > 0) // This will clear/refresh moves
		{
			for (int i = 0; i < moves.size(); i++) {
				moves.remove(i);
			}
		}

		String piece = square.getName();
		String color = square.getColor();

		if (piece.equals("Black Pawn") || piece.equals("White Pawn"))
			movePawn(square, color, board, row, col);

		else if (piece.equals("Black Rook") || piece.equals("White Rook"))
			moveRook(square, color, board, row, col);

		else if (piece.equals("Black Knight") || piece.equals("White Knight"))
			moveKnight(square, color, board, row, col);

		else if (piece.equals("Black Bishop") || piece.equals("White Bishop"))
			moveBishop(square, color, board, row, col);

		else if (piece.equals("Black King") || piece.equals("White King"))
			moveKing(square, color, board, row, col);

		else if (piece.equals("Black Queen") || piece.equals("White Queen"))
			moveQueen(square, color, board, row, col);
	}

	public void setMove(RButton here, RButton there, RButton[][] board) // This method actually moves the piece
	{
		ImageIcon image = (ImageIcon) here.getIcon();
		ImageIcon deadImage = (ImageIcon) there.getIcon(); // If there is a piece, deadImage will be added to the grave
															// yard

		RButton tempThere = there; // temp variables are required in order to avoid a button duplication glitch
									// that comes from editing pre-existing buttons
		RButton tempHere = here;

		remove(there); // Remove the square being moved to

		if (tempThere.getName().equals("White King") || tempThere.getName().equals("Black King")) // If either king is
																									// captured, game
																									// will be set to
																									// "over" and will
																									// prevent any
																									// further pieces
																									// from being moved
		{
			game = "over";

			if (tempThere.getName().equals("White King"))
				winner = 2; // 2 == player 2
			else if (tempThere.getName().equals("Black King"))
				winner = 1; // 1 == player 1

		}

		if (there.getType().equals("Piece")) {
			if (there.getColor().equals("White"))
				wGraveYard.add(deadImage);
			else if (there.getColor().equals("Black"))
				bGraveYard.add(deadImage);
		}
		// Change the stats of the spot being moved to to equal that of the original
		// spot
		// ----------------------------------------------------------------------------------------------------------
		tempThere.setIcon(null);
		tempThere.setIcon(image);
		tempThere.setName(here.getName());
		tempThere.setLink(here.getLink());
		tempThere.setColor(here.getColor());
		tempThere.setType(here.getType());
		// tempThere.setLastThere(true); //LastThere is for the minimap
		// there.setLastThere(true);
		add(tempThere);

		board[7 - tempThere.getRow()][7 - tempThere.getCol()].setLastThere(true);

		// Change the stats of the original spot to equal that of a blank/empty spot
		// ----------------------------------------------------------------------------------------------------------
		remove(here); // Removes piece from old spot
		tempHere.setIcon(null);
		tempHere.setIcon(empty);
		tempHere.setName(emptyName);
		tempHere.setLink(emptyLink);
		tempHere.setColor(emptyColor);
		// tempHere.setLastHere(true); //LastHere is for the minimap
		// here.setLastHere(true);
		add(tempHere);

		board[7 - tempHere.getRow()][7 - tempHere.getCol()].setLastHere(true);

		rotateBoard(board);

		repaint();

	}

	public void movePawn(RButton piece, String color, RButton[][] board, int row, int col) {
		selected = true;
		if (color.equals("Black") && turn.equals("Black")) {
			if (row >= 0 && col != 7 && board[row - 1][col + 1].getColor().equals("White")) {
				board[row - 1][col + 1].setBackground(new Color(moveR, moveG, moveB));
				moves.add(board[row - 1][col + 1]);
			}
			if (row >= 0 && col != 0 && board[row - 1][col - 1].getColor().equals("White")) {
				board[row - 1][col - 1].setBackground(new Color(moveR, moveG, moveB));
				moves.add(board[row - 1][col - 1]);
			}

			if (row == 6 && board[row][col].getName().equals("Black Pawn")) {
				if (row != 0) {
					if (board[row - 1][col].getName().equals("Empty")) {
						board[row - 1][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row - 1][col]);
						if (board[row - 2][col].getName().equals("Empty")) {
							board[row - 2][col].setBackground(new Color(moveR, moveG, moveB));
							moves.add(board[row - 2][col]);
						}
					}
				}
			} else if (row != 6 && board[row][col].getName().equals("Black Pawn")) {
				if (board[row - 1][col].getName().equals("Empty")) {
					board[row - 1][col].setBackground(new Color(moveR, moveG, moveB));
					moves.add(board[row - 1][col]);
				}
			}
			turn = "White";
		} else if (color.equals("White") && turn.equals("White")) {
			if (row >= 0 && col != 7 && board[row - 1][col + 1].getColor().equals("Black")) {
				board[row - 1][col + 1].setBackground(new Color(moveR, moveG, moveB));
				moves.add(board[row - 1][col + 1]);
			}
			if (row >= 0 && col != 0 && board[row - 1][col - 1].getColor().equals("Black")) {
				board[row - 1][col - 1].setBackground(new Color(moveR, moveG, moveB));
				moves.add(board[row - 1][col - 1]);
			}

			if (row == 6 && board[row][col].getName().equals("White Pawn")) {
				if (row != 0) {
					if (board[row - 1][col].getName().equals("Empty")) {
						board[row - 1][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row - 1][col]);
						if (board[row - 2][col].getName().equals("Empty")) {
							board[row - 2][col].setBackground(new Color(moveR, moveG, moveB));
							moves.add(board[row - 2][col]);
						}
					}
				}
			} else if (row != 6 && board[row][col].getName().equals("White Pawn")) {
				if (board[row - 1][col].getName().equals("Empty")) {
					board[row - 1][col].setBackground(new Color(moveR, moveG, moveB));
					moves.add(board[row - 1][col]);
				}
			}
			turn = "Black";
		}
	}

	public void moveRook(RButton piece, String color, RButton[][] board, int r, int c) {
		selected = true;

		if (color.equals("Black") && turn.equals("Black")) {
			int row = r;
			int col = c;

			while (row >= 0) // moving the piece North
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("White")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("Black")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				row--;
			}

			row = r;
			col = c;
			while (row < 8) // moving the piece South
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("White")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("Black")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				row++;
			}

			row = r;
			col = c;
			while (col >= 0) // moving the piece west
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("White")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("Black")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				col--;
			}

			row = r;
			col = c;
			while (col < 8) // Moving the piece East
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("White")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("Black")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				col++;
			}
			turn = "White";
		}

		else if (color.equals("White") && turn.equals("White")) {

			int row = r;
			int col = c;
			while (row >= 0) // moving the piece North
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("Black")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("White")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				row--;
			}

			row = r;
			col = c;
			while (row < 8) // moving the piece South
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("Black")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("White")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				row++;
			}

			row = r;
			col = c;
			while (col >= 0) {
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("Black")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("White")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				col--;
			}

			row = r;
			col = c;
			while (col < 8) {
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("Black")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("White")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				col++;
			}
			turn = "Black";

		}

	}

	public void moveKnight(RButton piece, String color, RButton[][] board, int r, int c) {
		selected = true;
		int row = r;
		int col = c;

		if (color.equals("Black") && turn.equals("Black")) {
			if (row > 1) {
				if (col != 0) {
					if (!board[row - 2][col - 1].getColor().equals("Black")) {
						board[row - 2][col - 1].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row - 2][col - 1]);
					}
				}
				if ((col != 7)) {
					if (!board[row - 2][col + 1].getColor().equals("Black")) {
						board[row - 2][col + 1].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row - 2][col + 1]);
					}
				}
			}
			if (row < 6) {
				if (col != 0) {
					if (!board[row + 2][col - 1].getColor().equals("Black")) {
						board[row + 2][col - 1].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row + 2][col - 1]);
					}
				}
				if (col != 7) {
					if (!board[row + 2][col + 1].getColor().equals("Black")) {
						board[row + 2][col + 1].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row + 2][col + 1]);
					}
				}
			}
			if (col > 1) {
				if (row != 0) {
					if (!board[row - 1][col - 2].getColor().equals("Black")) {
						board[row - 1][col - 2].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row - 1][col - 2]);
					}
				}
				if (row != 7) {
					if (!board[row + 1][col - 2].getColor().equals("Black")) {
						board[row + 1][col - 2].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row + 1][col - 2]);
					}
				}
			}
			if (col < 6) {
				if (row != 0) {
					if (!board[row - 1][col + 2].getColor().equals("Black")) {
						board[row - 1][col + 2].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row - 1][col + 2]);
					}
				}
				if (row != 7) {
					if (!board[row + 1][col + 2].getColor().equals("Black")) {
						board[row + 1][col + 2].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row + 1][col + 2]);
					}
				}
			}

			turn = "White";
		} else if (color.equals("White") && turn.equals("White")) {
			if (row > 1) {
				if (col != 0) {
					if (!board[row - 2][col - 1].getColor().equals("White")) {
						board[row - 2][col - 1].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row - 2][col - 1]);
					}
				}
				if ((col != 7)) {
					if (!board[row - 2][col + 1].getColor().equals("White")) {
						board[row - 2][col + 1].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row - 2][col + 1]);
					}
				}
			}
			if (row < 6) {
				if (col != 0) {
					if (!board[row + 2][col - 1].getColor().equals("White")) {
						board[row + 2][col - 1].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row + 2][col - 1]);
					}
				}
				if (col != 7) {
					if (!board[row + 2][col + 1].getColor().equals("White")) {
						board[row + 2][col + 1].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row + 2][col + 1]);
					}
				}
			}
			if (col > 1) {
				if (row != 0) {
					if (!board[row - 1][col - 2].getColor().equals("White")) {
						board[row - 1][col - 2].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row - 1][col - 2]);
					}
				}
				if (row != 7) {
					if (!board[row + 1][col - 2].getColor().equals("White")) {
						board[row + 1][col - 2].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row + 1][col - 2]);
					}
				}
			}
			if (col < 6) {
				if (row != 0) {
					if (!board[row - 1][col + 2].getColor().equals("White")) {
						board[row - 1][col + 2].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row - 1][col + 2]);
					}
				}
				if (row != 7) {
					if (!board[row + 1][col + 2].getColor().equals("White")) {
						board[row + 1][col + 2].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row + 1][col + 2]);
					}
				}
			}

			turn = "Black";
		}
	}

	public void moveBishop(RButton piece, String color, RButton[][] board, int r, int c) {
		selected = true;

		if (color.equals("Black") && turn.equals("Black")) {
			int row = r;
			int col = c;

			while (row >= 0 && col >= 0) // moving the piece North West
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("White")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("Black")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				row--;
				col--;
			}

			row = r;
			col = c;
			while (row < 8 && col >= 0) // moving the piece South West
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("White")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("Black")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				row++;
				col--;
			}

			row = r;
			col = c;
			while (row >= 0 && col < 8) // moving the piece North East
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("White")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("Black")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				row--;
				col++;
			}

			row = r;
			col = c;
			while (row < 8 && col < 8) // Moving the piece East
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("White")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("Black")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				row++;
				col++;
			}
			turn = "White";
		}

		else if (color.equals("White") && turn.equals("White")) {

			int row = r;
			int col = c;
			while (row >= 0 && col >= 0) // moving the piece North West
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("Black")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("White")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				row--;
				col--;
			}

			row = r;
			col = c;
			while (row < 8 && col >= 0) // moving the piece South West
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("Black")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("White")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				row++;
				col--;
			}

			row = r;
			col = c;
			while (row >= 0 && col < 8) // moving the piece North East
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("Black")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("White")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				row--;
				col++;
			}

			row = r;
			col = c;
			while (row < 8 && col < 8) {
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("Black")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("White")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				row++;
				col++;
			}
			turn = "Black";

		}

	}

	public void moveKing(RButton piece, String color, RButton[][] board, int r, int c) {
		selected = true;
		if (color.equals("Black") && turn.equals("Black")) {
			int row = r;
			int col = c;

			if (row > 0 && !board[row - 1][col].getColor().equals("Black")) // Move North
			{
				board[row - 1][col].setBackground(new Color(moveR, moveG, moveB));
				moves.add(board[row - 1][col]);
			}
			if (col > 0 && !board[row][col - 1].getColor().equals("Black")) // Move West
			{
				board[row][col - 1].setBackground(new Color(moveR, moveG, moveB));
				moves.add(board[row][col - 1]);
			}
			if (row < 7 && !board[row + 1][col].getColor().equals("Black")) // Move South
			{
				board[row + 1][col].setBackground(new Color(moveR, moveG, moveB));
				moves.add(board[row + 1][col]);
			}
			if (col < 7 && !board[row][col + 1].getColor().equals("Black")) // Move East
			{
				board[row][col + 1].setBackground(new Color(moveR, moveG, moveB));
				moves.add(board[row][col + 1]);
			}

			if (row > 0 && col > 0 && !board[row - 1][col - 1].getColor().equals("Black")) // Move North West
			{
				board[row - 1][col - 1].setBackground(new Color(moveR, moveG, moveB));
				moves.add(board[row - 1][col - 1]);
			}
			if (row > 0 && col < 7 && !board[row - 1][col + 1].getColor().equals("Black")) // Move North East
			{
				board[row - 1][col + 1].setBackground(new Color(moveR, moveG, moveB));
				moves.add(board[row - 1][col + 1]);
			}
			if (row < 7 && col > 0 && !board[row + 1][col - 1].getColor().equals("Black")) // Move South West
			{
				board[row + 1][col - 1].setBackground(new Color(moveR, moveG, moveB));
				moves.add(board[row + 1][col - 1]);
			}
			if (row < 7 && col < 7 && !board[row + 1][col + 1].getColor().equals("Black")) // Move South East
			{
				board[row + 1][col + 1].setBackground(new Color(moveR, moveG, moveB));
				moves.add(board[row + 1][col + 1]);
			}

			turn = "White";
		} else if (color.equals("White") && turn.equals("White")) {
			int row = r;
			int col = c;

			if (row != 0 && !board[row - 1][col].getColor().equals("White")) // Move North
			{
				board[row - 1][col].setBackground(new Color(moveR, moveG, moveB));
				moves.add(board[row - 1][col]);
			}
			if (col != 0 && !board[row][col - 1].getColor().equals("White")) // Move West
			{
				board[row][col - 1].setBackground(new Color(moveR, moveG, moveB));
				moves.add(board[row][col - 1]);
			}
			if (row != 7 && !board[row + 1][col].getColor().equals("White")) // Move South
			{
				board[row + 1][col].setBackground(new Color(moveR, moveG, moveB));
				moves.add(board[row + 1][col]);
			}
			if (col != 7 && !board[row][col + 1].getColor().equals("White")) // Move East
			{
				board[row][col + 1].setBackground(new Color(moveR, moveG, moveB));
				moves.add(board[row][col + 1]);
			}

			if (row != 0 && col != 0 && !board[row - 1][col - 1].getColor().equals("White")) // Move North West
			{
				board[row - 1][col - 1].setBackground(new Color(moveR, moveG, moveB));
				moves.add(board[row - 1][col - 1]);
			}
			if (row != 0 && col != 7 && !board[row - 1][col + 1].getColor().equals("White")) // Move North East
			{
				board[row - 1][col + 1].setBackground(new Color(moveR, moveG, moveB));
				moves.add(board[row - 1][col + 1]);
			}
			if (row != 7 && col != 0 && !board[row + 1][col - 1].getColor().equals("White")) // Move South West
			{
				board[row + 1][col - 1].setBackground(new Color(moveR, moveG, moveB));
				moves.add(board[row + 1][col - 1]);
			}
			if (row != 7 && col != 7 && !board[row + 1][col + 1].getColor().equals("White")) // Move South East
			{
				board[row + 1][col + 1].setBackground(new Color(moveR, moveG, moveB));
				moves.add(board[row + 1][col + 1]);
			}
			turn = "Black";
		}
	}

	public void moveQueen(RButton piece, String color, RButton[][] board, int r, int c) {
		selected = true;
		if (color.equals("Black") && turn.equals("Black")) {
			int row = r;
			int col = c;

			while (row >= 0) // moving the piece North
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("White")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("Black")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				row--;
			}

			row = r;
			col = c;
			while (row < 8) // moving the piece South
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("White")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("Black")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				row++;
			}

			row = r;
			col = c;
			while (col >= 0) // moving the piece West
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("White")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("Black")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				col--;
			}

			row = r;
			col = c;
			while (col < 8) // Moving the piece East
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("White")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("Black")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				col++;
			}
			row = r;
			col = c;

			while (row >= 0 && col >= 0) // moving the piece North West
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("White")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("Black")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				row--;
				col--;
			}

			row = r;
			col = c;

			while (row < 8 && col >= 0) // moving the piece South West
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("White")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("Black")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				row++;
				col--;
			}

			row = r;
			col = c;
			while (row >= 0 && col < 8) // moving the piece North East
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("White")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("Black")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				row--;
				col++;
			}

			row = r;
			col = c;
			while (row < 8 && col < 8) // Moving the piece East
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("White")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("Black")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				row++;
				col++;
			}
			turn = "White";
		} else if (color.equals("White") && turn.equals("White")) {
			int row = r;
			int col = c;
			while (row >= 0) // moving the piece North
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("Black")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("White")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				row--;
			}

			row = r;
			col = c;
			while (row < 8) // moving the piece South
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("Black")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("White")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				row++;
			}

			row = r;
			col = c;
			while (col >= 0) {
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("Black")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("White")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				col--;
			}

			row = r;
			col = c;
			while (col < 8) {
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("Black")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("White")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				col++;
			}

			row = r;
			col = c;
			while (row >= 0 && col >= 0) // moving the piece North West
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("Black")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("White")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				row--;
				col--;
			}

			row = r;
			col = c;
			while (row < 8 && col >= 0) // moving the piece South West
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("Black")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("White")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				row++;
				col--;
			}

			row = r;
			col = c;
			while (row >= 0 && col < 8) // moving the piece North East
			{
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("Black")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("White")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				row--;
				col++;
			}

			row = r;
			col = c;
			while (row < 8 && col < 8) {
				if (row != r || col != c) {
					if (board[row][col].getColor().equals("Black")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
						break;
					} else if (board[row][col].getColor().equals("White")) {
						break;
					} else if (board[row][col].getColor().equals("null")) {
						board[row][col].setBackground(new Color(moveR, moveG, moveB));
						moves.add(board[row][col]);
					}
				}
				row++;
				col++;
			}
			turn = "Black";
		}
	}

	public void resetSquareColor(RButton[][] board) {
		for (int row = 0; row < board.length; row++) {
			for (int col = 0; col < board[row].length; col++) {
				board[row][col].setBackground(
						new Color(board[row][col].getRed(), board[row][col].getGreen(), board[row][col].getBlue()));
			}
		}
	}

	public String getGameOver() {
		return game;
	}

	public void rotateBoard(RButton[][] board) {
		RButton square;
		RButton square2;
		RButton temp = new RButton("", "", "", "", 0, 0, 0, 0, 0, 0, 0, false, false);
		for (int row = 0; row < 4; row++) {
			for (int col = 0; col < board[row].length; col++) {
				square = board[row][col];
				square2 = board[7 - row][7 - col];

				remove(board[row][col]);
				remove(board[7 - row][7 - col]);

				ImageIcon icon = new ImageIcon(this.getClass().getResource(square.getLink()));
				ImageIcon icon2 = new ImageIcon(this.getClass().getResource(square2.getLink()));

				temp.setIcon(icon);
				temp.setName(square.getName());
				temp.setLink(square.getLink());
				temp.setColor(square.getColor());
				temp.setType(square.getType());

				square.setIcon(icon2);
				square.setName(square2.getName());
				square.setLink(square2.getLink());
				square.setColor(square2.getColor());
				square.setType(square2.getType());
				// square.addActionListener(this);

				square2.setIcon(icon);
				square2.setName(temp.getName());
				square2.setLink(temp.getLink());
				square2.setColor(temp.getColor());
				square2.setType(temp.getType());
				// square2.addActionListener(this);

				add(square);
				add(square2);

			}
		}
	}

	public int getWinner() {
		return winner;
	}
}

class MultiThreadMp3 implements Runnable {
	public void run() {
		try {
			try {
				FileInputStream fileInputStream = new FileInputStream(
						"C:\\Users\\1magi\\eclipse-workspace\\Rabehl_WarTacToe\\bin\\chess\\jazzLounge.mp3"); 
				Player player = new Player(fileInputStream);
				player.play();
			} catch (FileNotFoundException e) {
				System.out.println(e);
			} catch (JavaLayerException e) {
				System.out.println(e);
			}

		} catch (Exception e) {
			System.out.println(e);
		}
	}
}