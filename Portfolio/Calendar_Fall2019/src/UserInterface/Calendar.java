package UserInterface;

import java.awt.*;
import java.awt.event.*;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.TimerTask;

import javax.swing.*;

public class Calendar extends JFrame implements ActionListener {

    //=======================================================================================================
    // PROPERTIES
    //=======================================================================================================

    //GridLayout(rows, columns)
    protected GridLayout gridLayout = new GridLayout(0,7);

    protected Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();

    //Banner is the strip above the weekdays that display the month
    protected JPanel banner = new JPanel();
    protected final PrimaryPanel primaryPanel = new PrimaryPanel("January");
    protected DayPanel subPanel = new DayPanel();

    protected ArrayList<CalendarButton> dates = new ArrayList<CalendarButton>();
    public void setDates(ArrayList<CalendarButton> arr) {dates = arr;}
    public ArrayList<CalendarButton> getDates(){return dates;}

    //dateArrayI is used to save the index of the previous button in order to replace the old button once the previous button is updated
    protected int dateArrayI = 0;

    //=======================================================================================================
    // CONSTRUCTORS
    //=======================================================================================================

    /**
     * Full Constructor
     * @param name
     */
    public Calendar(String name) {
        super(name);
        setResizable(true);
        setMinimumSize(new Dimension((int) (screenSize.getWidth()*.65), (int) (screenSize.getHeight()*.85)));

    }

    //=======================================================================================================
    // METHODS
    //=======================================================================================================

    public static void main(String[] args) {

        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            public void run() {

                createAndShowGUI();
            }
        });
    }

    /**
     * Creates the frame containing the Calendar
     */
    private static void createAndShowGUI() {
        //Create and set up the window
        Calendar frame = new Calendar("Calendar");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //set up the content pane.
        frame.addComponenetsToPane(frame.getContentPane());

        //Display the window.
        frame.pack();
        frame.setVisible(true);
    }

    /**
     * Sets up the different panels and other components
     * @param pane
     */
    public void addComponenetsToPane(final Container pane) {

        gridLayout.setHgap(2);
        gridLayout.setVgap(2);

        primaryPanel.setLayout(gridLayout);
        primaryPanel.setBackground(Color.BLACK);


        //banner is using the flowLayout (which is the default layout)
        banner.setBackground(Color.WHITE);

        JLabel calendarMonth = new JLabel(primaryPanel.getMonth());
        calendarMonth.setForeground(new Color(13,143,207));
        Font font = new Font("Helvetica", Font.BOLD, 125);
        calendarMonth.setFont(font);
        banner.add(calendarMonth);

        //code from: https://docs.oracle.com/javase/tutorial/uiswing/components/border.html
        banner.setBorder(BorderFactory.createLineBorder(Color.black));


        primaryPanel.setPreferredSize(new Dimension((int) (screenSize.getWidth()*.75), (int) (screenSize.getHeight()*.75)));
        subPanel.setPreferredSize(new Dimension((int) (screenSize.getWidth()*.15), (int) (screenSize.getHeight()*.75)));
        banner.setPreferredSize(new Dimension((int) (screenSize.getWidth()*.75), (int) (screenSize.getHeight()*.15)));


        primaryPanel.add(new JLabel("Sunday", SwingConstants.CENTER));
        primaryPanel.add(new JLabel("Monday", SwingConstants.CENTER));
        primaryPanel.add(new JLabel("Tuesday", SwingConstants.CENTER));
        primaryPanel.add(new JLabel("Wednesday", SwingConstants.CENTER));
        primaryPanel.add(new JLabel("Thursday", SwingConstants.CENTER));
        primaryPanel.add(new JLabel("Friday", SwingConstants.CENTER));
        primaryPanel.add(new JLabel("Saturday", SwingConstants.CENTER));

        //This loop formats the visuals of the days of the week
        for(int i = 0; i < 7; i++) {
            font = primaryPanel.getComponent(i).getFont();
            JLabel label = (JLabel) primaryPanel.getComponent(i);
            label.setFont(new Font(font.getName(), font.getStyle(), 20));
            label.setOpaque(true);
            label.setBackground(new Color(14, 143, 207));
            label.setForeground(Color.WHITE);
        }


        createButtonArray(primaryPanel);

        // This loop adds the buttons to the primaryPanel
        for(int i = 0; i < dates.size(); i++) {
            primaryPanel.getDateList().add(dates.get(i));
        }

        int listSize = primaryPanel.getDateList().size();
        for(int i = 0; i < listSize; i++){
            primaryPanel.add(primaryPanel.getDateList().remove());
        }



        pane.add(primaryPanel, BorderLayout.CENTER);
        pane.add(banner, BorderLayout.NORTH);
        pane.add(subPanel, BorderLayout.WEST);
    }

    /**
     * Creates an array of buttons and gives each button a corresponding day of the week
     * @param primaryPanel
     */
    public void createButtonArray(PrimaryPanel primaryPanel) {

        String[] weekDays = {"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"};

        for(int i = 1; i <= 35; i++) {
            if(i > primaryPanel.getMonthLength()) {
                dates.add(new CalendarButton(0));
            }
            else {
                dates.add(new CalendarButton(i));
                dates.get(i-1).addActionListener(this);
            }
            if(i-1 < 7) {
                dates.get(i-1).setDayOfWeek(weekDays[i-1]);
            }
            else
                dates.get(i-1).setDayOfWeek(weekDays[(i-1)%7]);

            dates.get(i-1).setDate(dates.get(i-1).getDayOfWeek() + " " + dates.get(i-1).getDay());
            dates.get(i-1).readEvent(dates.get(i-1).getDate(), 1);
            subPanel.sort(dates.get(i-1));
        }
    }

    @Override
    public void actionPerformed(ActionEvent e) {

        if(subPanel.isVisible() == true && subPanel.getMultiDayCheckBox().isSelected() == true){
            for(int i = 0; i < dates.size(); i++){
                if(dates.get(i) == (CalendarButton)e.getSource())
                    dateArrayI = i;
            }
            if(((CalendarButton)e.getSource()).getMultiDaySelected() == false && !subPanel.getCurrentButton().equals((CalendarButton)e.getSource())) {
                ((CalendarButton) e.getSource()).setMultiDaySelected(true);
                subPanel.getMultiDayEventList().add((CalendarButton) e.getSource());
            }
            dates.set(dateArrayI, (CalendarButton)e.getSource());
        }
        else if(((CalendarButton)e.getSource()).getMultiDaySelected() == true)
            ((CalendarButton) e.getSource()).setMultiDaySelected(false);

        if(subPanel.isVisible() == false) {

            subPanel.removeAll();
            subPanel.setNumberOfEvents(0);
            subPanel.drawPanelComponents((CalendarButton)e.getSource());
            ((CalendarButton)e.getSource()).setIsCurrentButton(true);
            subPanel.setVisible(true);
        }
    }

}