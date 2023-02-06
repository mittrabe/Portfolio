package UserInterface;

import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;

import javax.swing.*;

public class CalendarButton extends JButton {

    //=======================================================================================================
    // PROPERTIES
    //=======================================================================================================

    protected int day = 0;
    public void setDay(int num) {day = num;}
    public int getDay() {return day;}

    protected String dayOfWeek = "";
    public void setDayOfWeek(String val) {dayOfWeek = val;}
    public String getDayOfWeek() {return dayOfWeek;}

    protected String date = "";
    public void setDate(String val) {date = val;}
    public String getDate() {return date;}

    protected Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();

    //Contains every single event on that day
    protected ArrayList<Event> dayEvents = new ArrayList<Event>();
    public void setDayEvents(ArrayList<Event> arr) { dayEvents = arr;}
    public ArrayList<Event> getDayEvents(){return dayEvents;}

    //Contains just the text of every single event on that day
    protected ArrayList<String> dayEventDetails = new ArrayList<String>();
    public void setDayEventDetails(ArrayList<String> arr) { dayEventDetails = arr;}
    public ArrayList<String> getDayEventDetails(){return dayEventDetails;}

    //Array list filled with 'Event' objects that had been saved and deserialized
    private ArrayList<Event> loadSavedEvents = new ArrayList<Event>();
    public ArrayList<Event> getLoadSavedEvents() {
        return loadSavedEvents;
    }
    public void setLoadSavedEvents(ArrayList<Event> loadSavedEvents) {
        this.loadSavedEvents = loadSavedEvents;
    }

    //if multiDaySelected equals true, this button has been selected to have a multiday event added to it
    protected boolean multiDaySelected = false;
    public void setMultiDaySelected(boolean val){multiDaySelected = val;}
    public boolean getMultiDaySelected(){return multiDaySelected;}

    protected boolean isCurrentButton = false;
    public void setIsCurrentButton(boolean val){isCurrentButton = val;}
    public boolean getIsCurrentButton(){return isCurrentButton;}


    //=======================================================================================================
    // CONSTRUCTORS
    //=======================================================================================================

    /**
     * Default Constructor
     */
    public CalendarButton() {}

    /**
     * Full Constructor
     * @param day
     */
    public CalendarButton(int day) {
        setDay(day);
    }

    //=======================================================================================================
    // METHODS
    //=======================================================================================================


    public void paintComponent(Graphics g)
    {
        super.paintComponent(g);

        //code for clearing the entire button comes from:
        // https://stackoverflow.com/questions/6902771/jpanel-graphics-clearing-and-repainting
        //g.clearRect(0, 0, getWidth(), getHeight()); [CURRENTLY UNUSED]

        setBackground(Color.WHITE);

        Font font = new Font("Helvetica", Font.PLAIN, 25);
        g.setFont(font);

        if(this.getDay() == 0)
            g.drawString("", (int) (this.getWidth()*.8), (int) (this.getHeight()*.2));
        else
            g.drawString(this.getDay()+"", (int) (this.getWidth()*.80), (int) (this.getHeight()*.2) );


        //This batch of code prints the first two of each day onto the button
        if(this.getDayEvents().size() > 0) {
            font = new Font("helvetica", Font.BOLD, 16);
            g.setFont(font);
            for(int i = 0; i < 2; i++) {
                String displayedEvent = getDayEvents().get(i).getEventText();
                if(i == 0) {
                    g.setColor(new Color(253,171,48));
                    g.fillRect((int) (this.getWidth()*.01), (int) (this.getHeight()*.48), (int) (this.getWidth()*.99),(int) (this.getHeight()*.18));
                    g.setColor(Color.BLACK);
                    if(getDayEvents().get(i).getEventText().length() > 19)
                        displayedEvent = getDayEvents().get(i).getEventText().substring(0, 19) + ". . .";

                    g.drawString(displayedEvent, (int) (this.getWidth()*.07), (int) (this.getHeight()*.60));
                    if(getDayEvents().size() == 1)
                        break;
                }
                else {
                    g.setColor(new Color(64,187,240));
                    g.fillRect((int) (this.getWidth()*.01), (int) (this.getHeight()*.68), (int) (this.getWidth()*.99),(int) (this.getHeight()*.18));
                    g.setColor(Color.BLACK);
                    if(getDayEvents().get(i).getEventText().length() > 19)
                        displayedEvent = getDayEvents().get(i).getEventText().substring(0, 19) + ". . .";

                    g.drawString(displayedEvent, (int) (this.getWidth()*.07), (int) (this.getHeight()*.80));
                }
            }
        }


        //This batch of code shows the number of events a given day has.
        if(this.getDayEvents().size() > 0) {
            g.setColor(new Color(218,212,44));
            g.fillOval((int) (this.getWidth()*.05), (int) (this.getHeight()*.03), (int) (this.getWidth()*.18), (int) (this.getWidth()*.18));
            font = new Font("Helvetica", Font.PLAIN, 24);
            g.setFont(font);
            if(getDayEvents().size() >= 10) {
                font = new Font("Helvetica", Font.PLAIN, 22);
                g.setFont(font);
                g.setColor(Color.BLACK);
                g.drawString(getDayEvents().size() + "",(int) (this.getWidth()*.08), (int) (this.getWidth()*.15));
            }
            else {
                g.setColor(Color.BLACK);
                g.drawString(getDayEvents().size() + "", (int) (this.getWidth() * .1), (int) (this.getWidth() * .15));
            }

        }

        //If a day has been selected for a multiDayEvent, it's color will be changed.
        if(multiDaySelected == true || isCurrentButton == true){
            setBackground(new Color(255, 248, 161));
        }

    }

    public void readEvent(String eventDate, int fileID){
        //deserialize 'Event' objects
        File directory = new File(getDate());
        File file = new File(getDate() + "\\" + 0 + ".bin");
        if(directory.exists()) {
            if(file.exists()) {
                for(int i = 0; i < directory.listFiles().length; i++) {
                    try {
                        ObjectInputStream inputStream = new ObjectInputStream(new FileInputStream(eventDate + "\\" + i + ".bin"));
                        Event e = (Event) inputStream.readObject();
                        dayEvents.add(e);
                        inputStream.close();

                    } catch (FileNotFoundException e) {
                        e.printStackTrace();
                    } catch (IOException e) {
                        e.printStackTrace();
                    } catch (ClassNotFoundException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }
}
