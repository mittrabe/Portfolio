package UserInterface;

import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.Queue;
import java.util.LinkedList;

import javax.swing.*;
class PrimaryPanel extends JPanel {

    //=======================================================================================================
    // PROPERTIES
    //=======================================================================================================

    protected String month = "Month";
    public void setMonth(String val) {month = val;}
    public String getMonth() {return month;}

    protected int monthLength = 0;
    public void setMonthLength(int num) {monthLength = num;}
    public int getMonthLength() {return monthLength;}

    protected Queue<CalendarButton> dateList = new LinkedList<>();
    public void setDateList(Queue<CalendarButton> list){dateList = list;}
    public Queue<CalendarButton> getDateList(){return dateList;}

    //=======================================================================================================
    // CONSTRUCTORS
    //=======================================================================================================

    /**
     * Default Constructor
     */
    public PrimaryPanel() {}

    /**
     * Full Constructor
     * @param month
     * @param monthLength
     */
    public PrimaryPanel(String month) {
        setMonth(month);

        if(month.equals("January") || month.equals("March") || month.equals("May") || month.equals("July") ||
                month.equals("August") || month.equals("October") || month.equals("December")){
            setMonthLength(31);
        }
        else if(month.equals("April") || month.equals("June") || month.equals("September") || month.equals("November")){
            setMonthLength(30);
        }
        else if(month.equals("February"))
            setMonthLength(28);
    }

    //=======================================================================================================
    // METHODS
    //=======================================================================================================
}