package UserInterface;

import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.Collections;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import javax.swing.*;
import javax.swing.text.*;
import java.sql.*;

public class DayPanel extends JPanel implements ActionListener, KeyListener {

    //=======================================================================================================
    // PROPERTIES
    //=======================================================================================================

    //Which ever day is clicked on will become the currentButton and the subPanel will display that day's events
    protected CalendarButton currentButton;
    public void setCurrentButton(CalendarButton button) {currentButton = button;}
    public CalendarButton getCurrentButton() {return currentButton;}

    //numberOfEvents keeps track of the total number of events for a day including the ones just added.
    protected int numberOfEvents = 0;
    public void setNumberOfEvents(int num) {numberOfEvents = num;}
    public int getNumberOfEvents() {return numberOfEvents;}

    protected JTextField textField = new JTextField();

    // Code for how to use textAreas and JScrollPane came from:
    // https://docs.oracle.com/javase/tutorial/uiswing/components/textarea.html
    protected JTextArea textArea = new JTextArea(3, 17);

    protected Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();

    protected JComboBox startTimeComboBox;
    protected JComboBox endTimeComboBox;
    protected static final String fullTimeList[] = {"12:00 am", "12:15 am", "12:30 am", "12:45 am", "1:00 am", "1:15 am", "1:30 am", "1:45 am",
            "2:00 am", "2:15 am", "2:30 am", "2:45 am", "3:00 am", "3:15 am", "3:30 am", "3:45 am",
            "4:00 am", "4:15 am", "4:30 am", "4:45 am", "5:00 am", "5:15 am", "5:30 am", "5:45 am",
            "6:00 am", "6:15 am", "6:30 am", "6:45 am", "7:00 am", "7:15 am", "7:30 am", "7:45 am",
            "8:00 am", "8:15 am", "8:30 am", "8:45 am", "9:00 am", "9:15 am", "9:30 am", "9:45 am",
            "10:00 am", "10:15 am", "10:30 am", "10:45 am", "11:00 am", "11:15 am", "11:30 am", "11:45 am",
            "12:00 pm", "12:15 pm", "12:30 pm", "12:45 pm", "1:00 pm", "1:15 pm", "1:30 pm", "1:45 pm",
            "2:00 pm", "2:15 pm", "2:30 pm", "2:45 pm", "3:00 pm", "3:15 pm", "3:30 pm", "3:45 pm",
            "4:00 pm", "4:15 pm", "4:30 pm", "4:45 pm", "5:00 pm", "5:15 pm", "5:30 pm", "5:45 pm",
            "6:00 pm", "6:15 pm", "6:30 pm", "6:45 pm", "7:00 pm", "7:15 pm", "7:30 pm", "7:45 pm",
            "8:00 pm", "8:15 pm", "8:30 pm", "8:45 pm", "9:00 pm", "9:15 pm", "9:30 pm", "9:45 pm",
            "10:00 pm", "10:15 pm", "10:30 pm", "10:45 pm", "11:00 pm", "11:15 pm", "11:30 pm", "11:45 pm"};

    //numberTimeList is a mirror image of the fullTimeList but with each element reformatted to be an int.
    //It's used to sort each event by startTime
    protected static final int numberTimeList[] = {0, 15, 30, 45, 100, 115, 130, 145,
            200, 215, 230, 245, 300, 315, 330, 345,
            400, 415, 430, 445, 500, 515, 530, 545,
            600, 615, 630, 645, 700, 715, 730, 745,
            800, 815, 830, 845, 900, 915, 930, 945,
            1000, 1015, 1030, 1045, 1100, 1115, 1130, 1145,
            1200, 1215, 1230, 1245, 1300, 1315, 1330, 1345,
            1400, 1415, 1430, 1445, 1500, 1515, 1530, 1545,
            1600, 1615, 1630, 1645, 1700, 1715, 1730, 1745,
            1800, 1815, 1830, 1845, 1900, 1915, 1930, 1945,
            2000, 2015, 2030, 2045, 2100, 2115, 2130, 2145,
            2200, 2215, 2230, 2245, 2300, 2315, 2330, 2345};


    //contains the current page number
    protected int pageNumber = 1;
    public void setPageNumber(int num) {pageNumber = num;}
    public int getPageNumber() {return pageNumber;}

    //contains the total number of pages
    protected int numberOfPages = 2;
    public void setNumberOfPages(int num) {numberOfPages = num;}
    public int getNumberOfPages() {return numberOfPages;}

    //an arrayList that contains each page of events
    protected ArrayList<ArrayList<Event>> arrayOfPages = new ArrayList<ArrayList<Event>>();
    public void setArrayOfPages(ArrayList<ArrayList<Event>> arr) {arrayOfPages = arr;}
    public ArrayList<ArrayList<Event>> getArrayOfPages(){return arrayOfPages;}

    //Each page of events is their own arrayList
    protected ArrayList<Event> page1 = new ArrayList<Event>();
    public void setPage1(ArrayList<Event> arr) {page1 = arr;}
    public ArrayList<Event> getPage1(){return page1;}

    protected ArrayList<Event> page2 = new ArrayList<Event>();
    public void setPage2(ArrayList<Event> arr) {page2 = arr;}
    public ArrayList<Event> getPage2(){return page2;}


    // Code relating to pop up menus retrieved from:
    // https://www.zentut.com/java-swing/how-to-create-popup-menu-in-java-swing/
    protected final JPopupMenu popup = new JPopupMenu();
    public JPopupMenu getPopup(){return popup;}

    // Any event added while this box is checked can be added to multiple days if the user clicks on each day before adding the event
    protected final JCheckBox multiDayCheckBox = new JCheckBox("Multi-Day Event");
    public JCheckBox getMultiDayCheckBox(){return multiDayCheckBox;}

    protected ArrayList<CalendarButton> multiDayEventList = new ArrayList<CalendarButton>();
    public void setMultiDayCheckBox(ArrayList<CalendarButton> arr){multiDayEventList = arr;}
    public ArrayList<CalendarButton> getMultiDayEventList(){return multiDayEventList;}

    //=======================================================================================================
    // CONSTRUCTORS
    //=======================================================================================================

    DayPanel() {

        this.setBackground(Color.WHITE);
        this.setVisible(false);



        arrayOfPages.add(page1);
        arrayOfPages.add(page2);

        // CalendarButton fakeButton = new CalendarButton();
        // drawPanelComponents(fakeButton);

        //fakeEvent is simply a placeHolder event
        Event fakeEvent = new Event();
        setUpPopupMenu(fakeEvent);
    }


    //=======================================================================================================
    // METHODS
    //=======================================================================================================

    /**
     * sets up all of the components on the DayPanel
     * @param day
     */
    public void drawPanelComponents(CalendarButton day) {
        currentButton = day;

        loadPages();

        JLabel header = new JLabel(currentButton.getDate(), SwingConstants.CENTER);
        header.setFont(new Font(header.getFont().getName(), header.getFont().getStyle(), 24));
        header.setAlignmentY(TOP_ALIGNMENT);
        header.setName("header");
        add(header);

        String crossMark = "274C";
        String symbol = String.valueOf(Character.toChars(Integer.parseInt(crossMark, 16)));
        JButton exit = new JButton(symbol);
        exit.setBorder(BorderFactory.createLineBorder(Color.BLACK, 1));
        exit.setAlignmentY(RIGHT_ALIGNMENT);
        exit.setPreferredSize(new Dimension((int) ((screenSize.getWidth() * .15) * .12), (int) ((screenSize.getHeight() * .75) * 0.04)));
        exit.addActionListener(this);
        exit.setName("exit");
        add(exit);

        JLabel dash = new JLabel("------------------------", SwingConstants.CENTER);
        dash.setFont(new Font(dash.getFont().getName(), dash.getFont().getStyle(), 25));
        dash.setAlignmentX(CENTER_ALIGNMENT);
        dash.setName("dash");
        add(dash);

        JLabel enterDetails = new JLabel("Enter Event Details:", SwingConstants.CENTER);
        enterDetails.setFont(new Font(enterDetails.getFont().getName(), enterDetails.getFont().getStyle(), 15));
        enterDetails.setAlignmentX(LEFT_ALIGNMENT);
        enterDetails.setName("enterDetails");
        add(enterDetails);

        Font font = new Font("Helvetica", Font.BOLD, 16);

        textField.setFont(font);
        textField.setPreferredSize(new Dimension((int) ((screenSize.getWidth() * .15) * .6), (int) ((screenSize.getHeight() * .75) * 0.04)));
        textField.setBorder(BorderFactory.createLineBorder(Color.BLACK, 2));
        textField.addActionListener(this);
        textField.addKeyListener(this);
        textField.setName("Event Text Field");
        add(textField);

        JLabel enterStartTime = new JLabel("Enter Event Start Time:", SwingConstants.CENTER);
        enterStartTime.setFont(new Font(enterStartTime.getFont().getName(), enterStartTime.getFont().getStyle(), 14));
        enterStartTime.setAlignmentX(LEFT_ALIGNMENT);
        enterStartTime.setName("enterStartTime");
        add(enterStartTime);

        startTimeComboBox = new JComboBox(fullTimeList);
        startTimeComboBox.setName("startTimeComboBox");
        startTimeComboBox.setSelectedItem("8:00 am");
        add(startTimeComboBox);

        JLabel enterEndTime = new JLabel("Enter Event End Time:", SwingConstants.CENTER);
        enterEndTime.setFont(new Font(enterEndTime.getFont().getName(), enterEndTime.getFont().getStyle(), 14));
        enterEndTime.setAlignmentX(LEFT_ALIGNMENT);
        enterEndTime.setName("enterEndTime");
        add(enterEndTime);

        endTimeComboBox = new JComboBox(fullTimeList);
        endTimeComboBox.setName("endTimeComboBox");
        endTimeComboBox.setSelectedItem("9:00 am");
        add(endTimeComboBox);

        // blank and blank 2 are used to center the multiDayCheckBox and keep it on its own line
        JLabel blank = new JLabel("               ");
        blank.setName("blank");
        add(blank);

        // Code pertaining to JCheckBoxes comes from:
        // https://www.geeksforgeeks.org/java-swing-jcheckbox-examples/
        multiDayCheckBox.setFont(new Font(multiDayCheckBox.getFont().getName(), multiDayCheckBox.getFont().getStyle(), 14));
        multiDayCheckBox.setName("MultiDayCheckBox");
        add(multiDayCheckBox);

        JLabel blank2 = new JLabel("               ");
        blank2.setName("blank2");
        add(blank2);

        JButton addEventButton = new JButton("Add Event");
        addEventButton.setBorder(BorderFactory.createLineBorder(Color.BLACK, 1));
        addEventButton.setPreferredSize(new Dimension((int) ((screenSize.getWidth() * .15) * .25), (int) ((screenSize.getHeight() * .75) * 0.025)));
        addEventButton.addActionListener(this);
        addEventButton.setName("Add Event");
        add(addEventButton);

        JLabel dash2 = new JLabel("_______________________", SwingConstants.CENTER);
        dash2.setFont(new Font(dash2.getFont().getName(), dash2.getFont().getStyle(), 22));
        dash2.setAlignmentX(CENTER_ALIGNMENT);
        dash2.setName("dash2");
        add(dash2);


        if(currentButton.getDayEvents().size() > 0)
            printPage();

        addPageComponents();

    }

    /**
     * Adds the events of a button to the different pages.
     */
    public void loadPages() {
        int count = 0;
        int eventsLeft = currentButton.getDayEvents().size();
        for(int i = 0; i < currentButton.getDayEvents().size(); i++) {

            for(int k = 0; k < arrayOfPages.size(); k++) {

                for(int j = 0; j < 5; j++) {
                    if(eventsLeft == 0)
                        break;
                    arrayOfPages.get(k).add(currentButton.getDayEvents().get(count));
                    count++;
                    eventsLeft--;
                    setNumberOfEvents(getNumberOfEvents() + 1);

                }
            }
        }
    }

    /**
     * Adds the buttons to change the page and label to display the page number
     */
    public void addPageComponents() {

        JButton pageLeft = new JButton("<");
        pageLeft.setBorder(BorderFactory.createLineBorder(Color.BLACK, 1));
        pageLeft.setPreferredSize(new Dimension((int) ((screenSize.getWidth() * .15) * .1), (int) ((screenSize.getHeight() * .75) * 0.04)));
        pageLeft.addActionListener(this);
        pageLeft.setName("Page Left");
        add(pageLeft);

        JLabel pageLabel = new JLabel(getPageNumber() + "", SwingConstants.CENTER);
        pageLabel.setFont(new Font(pageLabel.getFont().getName(), pageLabel.getFont().getStyle(), 15));
        pageLabel.setBorder(BorderFactory.createLineBorder(Color.BLACK, 1));
        pageLabel.setPreferredSize(new Dimension((int) ((screenSize.getWidth() * .15) * .1), (int) ((screenSize.getHeight() * .75) * 0.04)));
        pageLabel.setName("Page Label");
        add(pageLabel);

        JButton pageRight = new JButton(">");
        pageRight.setBorder(BorderFactory.createLineBorder(Color.BLACK, 1));
        pageRight.setPreferredSize(new Dimension((int) ((screenSize.getWidth() * .15) * .1), (int) ((screenSize.getHeight() * .75) * 0.04)));
        pageRight.addActionListener(this);
        pageRight.setName("Page Right");
        add(pageRight);


    }

    /**
     * removes the change page components
     */
    public void removePageComponents() {
        Component[] componentList = getComponents();
        for(Component c : componentList) {
            if(c.getName().equals("Page Left") || c.getName().equals("Page Label") || c.getName().equals("Page Right"))
                remove(c);
        }
        repaint();
    }

    /**
     * Adds the different features to the popup menu and implements action listeners for them
     * @param event
     */
    public void setUpPopupMenu(Event event) {
        popup.removeAll();
        popup.setBackground(Color.WHITE);
        popup.setPreferredSize(new Dimension((int) ((screenSize.getWidth()*.1)), (int) ((screenSize.getHeight() * .1))));

        String crossMark = "274C";
        String symbol = String.valueOf(Character.toChars(Integer.parseInt(crossMark, 16)));
        JMenuItem closePopupButton = new JMenuItem(symbol  + "  Close...");
        closePopupButton.setFont(new Font(closePopupButton.getFont().getName(), closePopupButton.getFont().getStyle(), 20));
        closePopupButton.setBorder(BorderFactory.createLineBorder(Color.GRAY, 1));
        closePopupButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                popup.setVisible(false);
            }
        });
        popup.add(closePopupButton);

        String edit = "1F589";
        symbol = String.valueOf(Character.toChars(Integer.parseInt(edit, 16)));
        JMenuItem editEventButton = new JMenuItem(symbol  + "  Edit Event...");
        editEventButton.setFont(new Font(editEventButton.getFont().getName(), editEventButton.getFont().getStyle(), 20));
        editEventButton.setBorder(BorderFactory.createLineBorder(Color.GRAY, 1));
        editEventButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                removeSingleEvent(event);

                textField.setText(event.getEventText());
                startTimeComboBox.setSelectedItem(event.getStartTime());
                endTimeComboBox.setSelectedItem(event.getEndTime());
                popup.setVisible(false);
            }
        });
        popup.add(editEventButton);

        String delete = "1F5D1";
        symbol = String.valueOf(Character.toChars(Integer.parseInt(delete, 16)));
        JMenuItem deleteEventButton = new JMenuItem(symbol + "  Delete Event...");
        deleteEventButton.setFont(new Font(deleteEventButton.getFont().getName(), deleteEventButton.getFont().getStyle(), 20));
        deleteEventButton.setBorder(BorderFactory.createLineBorder(Color.GRAY, 1));
        deleteEventButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                removeSingleEvent(event);
                popup.setVisible(false);
            }
        });
        popup.add(deleteEventButton);
    }

    /**
     * Removes all components with the name "event"
     */
    public void removeEvents() {
        Component[] componentList = getComponents();
        for(Component c : componentList) {
            if(c.getName().equals("event") || c.getName().equals("Open Popup") || c.getName().equals("Scroll Pane"))
                remove(c);
        }
        repaint();
    }

    /**
     * removes a single event from both the button and the page arrayList
     * @param event
     */
    public void removeSingleEvent(Event event) {

        for(int i = 0; i < getComponents().length; i++) {
            if(getComponents()[i].equals(event)) {
                remove(getComponents()[i+2]);
                remove(getComponents()[i+1]);
                remove(getComponents()[i]);
                break;
            }
        }

        for(Event c : currentButton.getDayEvents()) {

            c.deleteEventFile(currentButton.getDate(), getNumberOfEvents());

            if(c.getFullEvent().equals(event.getFullEvent())) {
                currentButton.getDayEvents().remove(c);
                //currentButton.getDayEventDetails().remove(c.getEventText());
                break;
            }
        }

        for(ArrayList<Event> c : arrayOfPages) {
            for (Event k : c) {
                if (k.getFullEvent().equals(event.getFullEvent())) {
                    c.remove(k);
                    break;
                }
            }
        }

        if(numberOfPages > 2) {
            if (arrayOfPages.get(numberOfPages - 2).size() == 0) {
                arrayOfPages.remove(numberOfPages - 1);
                numberOfPages--;
            }
        }
        numberOfEvents--;


        resetPage();

    }

    /**
     * adds a page's event followed by the options button and a dashed line
     */
    public void printPage() {

        if(arrayOfPages.get(getPageNumber()-1).size() != 0) {
            for(int i = 0; i < arrayOfPages.get(getPageNumber()-1).size(); i++) {
                Event dayEvent = new Event(arrayOfPages.get(getPageNumber()-1).get(i));


                //JTextArea is used to allow the text to span multiple lines where as the normal JLabel does not.
                //JScrollPane is used because it enables the text to automatically wrap to each line
                JScrollPane scrollPane = new JScrollPane(dayEvent);
                scrollPane.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED);
                scrollPane.setHorizontalScrollBarPolicy(JScrollPane.HORIZONTAL_SCROLLBAR_NEVER);
                scrollPane.setPreferredSize(new Dimension((int) ((screenSize.getWidth() * .15) * .85), (int) ((screenSize.getHeight() * .75) * 0.08)));
                scrollPane.setBorder(BorderFactory.createLineBorder(Color.BLACK, 1));
                scrollPane.setName("Scroll Pane");
                add(scrollPane);

                String options = "1F6E0";
                String symbol = String.valueOf(Character.toChars(Integer.parseInt(options, 16)));
                JButton openPopup = new JButton(symbol);
                openPopup.setPreferredSize(new Dimension((int) ((screenSize.getWidth() * .15) * .1), (int) ((screenSize.getHeight() * .75) * 0.04)));
                openPopup.setFont(new Font(openPopup.getFont().getName(), openPopup.getFont().getStyle(), 23));
                openPopup.setBorder(BorderFactory.createLineBorder(Color.BLACK, 1));
                openPopup.addActionListener(this);
                openPopup.setName("Open Popup");
                add(openPopup);

                //While putting this in would make each event more distinct from eachother, it greatly increases the amount of space used
               /* JLabel dashLine = new JLabel("---------------------------------------------------------", SwingConstants.CENTER);
                dashLine.setFont(new Font(dashLine.getFont().getName(), dashLine.getFont().getStyle(), 16));
                dashLine.setAlignmentX(CENTER_ALIGNMENT);
                dashLine.setName("event");
                add(dashLine);*/
            }
        }
    }

    /**
     * Removes all elements from the arrayOfPages
     */
    public void clearArrayOfPages(){
        for(int i = 0; i < arrayOfPages.size(); i++) {
            arrayOfPages.get(i).clear();
        }
    }

    /**
     * Allows the user to enter events by hitting [enter]
     */
    public void keyPressed(KeyEvent event) {

        if (event.getKeyCode() == KeyEvent.VK_ENTER) {
            createEvent(textField.getText(), (String)startTimeComboBox.getSelectedItem(), (String)endTimeComboBox.getSelectedItem());
            revalidate();
        }
    }


    public void actionPerformed(ActionEvent e) throws ClassCastException {

        if(((JButton)e.getSource()).getName().equals("Open Popup")) {
            if(popup.isVisible() == false) {
                popup.setLocation(MouseInfo.getPointerInfo().getLocation());

                for(int i = 0; i < getComponents().length; i++) {
                    if(e.getSource().equals(getComponents()[i])) {
                        JViewport viewport = ((JScrollPane)getComponents()[i-1]).getViewport();
                        Event event = (Event)viewport.getView();
                        setUpPopupMenu(event);
                        break;
                    }
                }

                popup.setVisible(true);

            }
            else if(popup.isVisible() == true) {
                popup.setVisible(false);
            }
        }

        if(((JButton)e.getSource()).getName().equals("exit")){
            setVisible(false);
            popup.setVisible(false);
            textField.setText("");
            startTimeComboBox.setSelectedIndex(0);
            endTimeComboBox.setSelectedIndex(0);
            pageNumber = 1;
            clearArrayOfPages();
            currentButton.setIsCurrentButton(false);

        }

        else if(((JButton)e.getSource()).getName().equals("Add Event")) {
            createEvent(textField.getText(), (String)startTimeComboBox.getSelectedItem(), (String)endTimeComboBox.getSelectedItem());
            revalidate();
        }

        else if(((JButton)e.getSource()).getName().equals("Page Left")) {
            if(getPageNumber() > 1) {
                setPageNumber(getPageNumber() - 1);
                resetPage();
            }

        }

        else if(((JButton)e.getSource()).getName().equals("Page Right")) {
            if(getPageNumber() < getNumberOfPages()) {
                setPageNumber(getPageNumber()+1);
                resetPage();
            }
        }

    }

    /**
     * Completely clears a page of events
     */
    public void resetPage() {
        removePageComponents();
        removeEvents();
        JLabel pageLabel = new JLabel(getPageNumber() + "", SwingConstants.CENTER);
        pageLabel.setFont(new Font(pageLabel.getFont().getName(), pageLabel.getFont().getStyle(), 15));
        pageLabel.setBorder(BorderFactory.createLineBorder(Color.BLACK, 1));
        pageLabel.setPreferredSize(new Dimension((int) ((screenSize.getWidth() * .15) * .1), (int) ((screenSize.getHeight() * .75) * 0.04)));
        printPage();
        addPageComponents();
        revalidate();
    }

    /**
     * merges all of the information inputed by the user and formats it into an Event
     * then adds that event to every day selected and to the DayPanel.
     */
    public void createEvent(String text, String start, String end) {
        //String eventDetails = textField.getText();
        //Get the start time
        //   String startTime = (String)startTimeComboBox.getSelectedItem();
        //Get the end time
        //  String endTime = (String)endTimeComboBox.getSelectedItem();

        Event.createDateDirectory(currentButton.getDate());

        String eventDetails = text;
        String startTime = start;
        String endTime = end;

        int startTimeInt = 0;
        int endTimeInt = 0;
        for(int i = 0; i < fullTimeList.length; i++) {
            if(startTime.equals(fullTimeList[i]))
                startTimeInt = numberTimeList[i];
            if(endTime.equals(fullTimeList[i]))
                endTimeInt = numberTimeList[i];
        }

        if(!startTime.equals(" ") && !endTime.equals(" ") && !eventDetails.trim().isEmpty())
        {
            Event event = new Event(eventDetails, startTime, endTime, startTimeInt, endTimeInt, getNumberOfEvents());

            currentButton.getDayEvents().add(event);

            if(getPageNumber()-1 != getNumberOfEvents()/5) {
                setPageNumber((getNumberOfEvents()/5)+1);

                if(getPageNumber() == getNumberOfPages()) {
                    arrayOfPages.add(new ArrayList<Event>());
                    numberOfPages++;
                }
            }

            Event.serializeEvent(currentButton.getDate(), getNumberOfEvents(), event);

            if(getMultiDayEventList().size() > 0) {
                for(int i = 0; i < getMultiDayEventList().size(); i++){
                    if(getMultiDayEventList().get(i).getMultiDaySelected() == true) {
                        Event.createDateDirectory(getMultiDayEventList().get(i).getDate());
                        getMultiDayEventList().get(i).getDayEvents().add(event);
                        getMultiDayEventList().get(i).setMultiDaySelected(false);
                        Event.serializeEvent(getMultiDayEventList().get(i).getDate(), getNumberOfEvents(), event);
                    }
                }
                multiDayEventList.clear();
            }
            sort(currentButton);
            clearArrayOfPages();
            setNumberOfEvents(0);
            loadPages();
            resetPage();
        }

        textField.setText("");
        startTimeComboBox.setSelectedItem("8:00 am");
        endTimeComboBox.setSelectedItem("9:00 am");
        multiDayCheckBox.setSelected(false);



    }


    /**
     * Sorts the events by earliest start time
     * Code Retrieved From:
     * https://stackoverflow.com/questions/23503921/java-insertion-sort-with-an-array-list-of-objects
     */
    public void sort(CalendarButton button){
        int i, j;
        for (i = 1; i < button.getDayEvents().size(); i++) {
            Event temp = button.getDayEvents().get(i);
            j = i;
            while ((j > 0) && (button.getDayEvents().get(j - 1).getStartTimeInt() > temp.getStartTimeInt())) {
                button.getDayEvents().set(j, button.getDayEvents().get(j - 1));
                j--;
            }
            button.getDayEvents().set(j, temp);
        }
    }

    @Override
    public void keyReleased(KeyEvent arg0) {
        // TODO Auto-generated method stub

    }
    @Override
    public void keyTyped(KeyEvent arg0) {
        // TODO Auto-generated method stub

    }
}