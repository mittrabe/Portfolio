package UserInterface;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Toolkit;
import java.io.*;
import java.nio.file.DirectoryNotEmptyException;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

import javax.swing.BorderFactory;
import javax.swing.JLabel;
import javax.swing.JTextArea;

public class Event extends JTextArea{

    //========================================================================================
    // PROPERTIES
    //========================================================================================

    protected Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();

    private String eventText;
    public void setEventText(String val) {eventText = val;}
    public String getEventText() {return eventText;}

    private String startTime;
    public void setStartTime(String val) {startTime = val;}
    public String getStartTime() {return startTime;}

    private int startTimeInt;
    public void setStartTimeInt(int num) {startTimeInt = num;}
    public int getStartTimeInt() {return startTimeInt;}

    private String endTime;
    public void setEndTime(String val) {endTime = val;}
    public String getEndTime() {return endTime;}

    private int endTimeInt;
    public void setEndTimeInt(int num) {endTimeInt = num;}
    public int getEndTimeInt() {return endTimeInt;}

    private String fullEvent;
    public void setFullEvent(String val) {fullEvent = val;}
    public String getFullEvent() {return fullEvent;}

    private int eventNumber;
    public void setEventNumber(int num) {eventNumber = num;}
    public int getEventNumber() {return eventNumber;}

    private static int eventID;
    public void setEventID(int num) {eventID = num;}
    public static int getEventID() {return eventID;}

    public static ArrayList<Event> loadSavedEvents = new ArrayList<Event>();
    public static ArrayList<Event> getLoadSavedEvents() {
        return loadSavedEvents;
    }
    public void setLoadSavedEvents(ArrayList<Event> loadSavedEvents) {
        this.loadSavedEvents = loadSavedEvents;
    }

//========================================================================================
    // CONSTRUCTORS
    //========================================================================================

    public Event() {}

    public Event(Event event) {
        setEventText(event.getEventText());
        setStartTime(event.getStartTime());
        setEndTime(event.getEndTime());
        setFullEvent(event.getFullEvent());
        setText(event.getFullEvent());

        //When a JTextArea is set to not be editable, the user can still highlight & copy text
        setEditable(false);
        setFont(new Font("Helvetica", Font.BOLD, 15));
        setLineWrap(true);
        setWrapStyleWord(true); //setWrapStyleWord(true) must always be preceded by setLineWrap(true);

        setName("event");
    }

    public Event(String eventText, String startTime, String endTime, int startTimeInt, int endTimeInt, int eventNumber) {
        setEventText(eventText);
        setStartTime(startTime);
        setEndTime(endTime);
        setStartTimeInt(startTimeInt);
        setEndTimeInt(endTimeInt);

        setEditable(false);
        setFont(new Font("Helvetica", Font.PLAIN, 15));
        setLineWrap(true);
        setWrapStyleWord(true);

        setFullEvent(eventText + "\n" + startTime + " - " + endTime);

        setText(getFullEvent());

        setName("event");

        setEventNumber(eventNumber);

    }

    //========================================================================================
    // METHODS
    //========================================================================================
    /**
     * Check for and create directory for each 'day' known as 'date'
     */
    public static void createDateDirectory(String eventDate){
        String folderName = eventDate;
        File dir = new File(folderName);
        try{
            dir.mkdir();
        } catch (SecurityException e){
            e.printStackTrace();
        }
    }

    /**
     * Automatically scans 'date' folder for any serialized events
     * Reads and deserializes any events in the 'date' folder
     * Displays deserialzed events
     */

    public static void scanAndDeserialize(String date){

        int IDIterator = 0;

        final File folder = new File(date+IDIterator);

        List<String> result = new ArrayList<>();

        search(".*\\.bin", folder, result);

        for (String s : result) {
            IDIterator++;
            // readEvent(IDIterator);


        }

    }

    /**
     * Method used to list only files that end with ".bin"
     * @param pattern
     * @param folder
     * @param result
     */

    public static void search(final String pattern, final File folder, List<String> result) {
        for (final File f : folder.listFiles()) {

            if (f.isDirectory()) {
                search(pattern, f, result);
            }

            if (f.isFile()) {
                if (f.getName().matches(pattern)) {
                    result.add(f.getAbsolutePath());
                }
            }

        }
    }


    /**
     * Serializes the object and saves as a Bin in each 'date' directory
     */
    public static void serializeEvent(String eventDate, int numberOfEvent, Event event) {
        //Write the object to a bin file using the Event ID as the file name
        File fileName = new File(eventDate+"\\"+numberOfEvent+".bin");
        try{
            ObjectOutputStream outputStream = new ObjectOutputStream(new FileOutputStream(fileName));
            outputStream.writeObject(event);
            outputStream.close();

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    /**
     * Get directory location
     */

    public static File getDirectoryPath(String eventDate){
        File myfolder = new File(eventDate);

        return myfolder;
    }

    /**
     *  Deletes event file from 'date' directory
     */
    public static void deleteEventFile(String date, int fileID){

        try{
            Files.deleteIfExists(Paths.get(date+"\\"+ (fileID-1) + ".bin"));
        } catch (DirectoryNotEmptyException e) {
            e.printStackTrace();
        } catch(NoSuchFileException e){
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}