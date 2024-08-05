package day_05;

import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.border.EmptyBorder;

public class MySw08 extends JFrame {
    String tell_no = "";
    private JPanel contentPane;
    private JTextField tf;

    public static void main(String[] args) {
        EventQueue.invokeLater(new Runnable() {
            public void run() {
                try {
                    MySw08 frame = new MySw08();
                    frame.setVisible(true);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
    }

    public MySw08() {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setBounds(100, 100, 303, 338);
        contentPane = new JPanel();
        contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
        setContentPane(contentPane);
        contentPane.setLayout(null);

        tf = new JTextField();
        tf.setHorizontalAlignment(SwingConstants.RIGHT);
        tf.setBounds(22, 10, 245, 21);
        contentPane.add(tf);
        tf.setColumns(10);

        JButton btn1 = new JButton("1");
        btn1.setBounds(22, 41, 71, 21);
        contentPane.add(btn1);
        btn1.addActionListener(new MyListener());

        JButton btn2 = new JButton("2");
        btn2.setBounds(109, 41, 71, 21);
        contentPane.add(btn2);
        btn2.addActionListener(new MyListener());

        JButton btn3 = new JButton("3");
        btn3.setBounds(196, 41, 71, 21);
        contentPane.add(btn3);
        btn3.addActionListener(new MyListener());

        JButton btn4 = new JButton("4");
        btn4.setBounds(22, 79, 71, 21);
        contentPane.add(btn4);
        btn4.addActionListener(new MyListener());

        JButton btn5 = new JButton("5");
        btn5.setBounds(109, 78, 71, 21);
        contentPane.add(btn5);
        btn5.addActionListener(new MyListener());

        JButton btn6 = new JButton("6");
        btn6.setBounds(196, 78, 71, 21);
        contentPane.add(btn6);
        btn6.addActionListener(new MyListener());

        JButton btn7 = new JButton("7");
        btn7.setBounds(22, 117, 71, 21);
        contentPane.add(btn7);
        btn7.addActionListener(new MyListener());

        JButton btn8 = new JButton("8");
        btn8.setBounds(109, 115, 71, 21);
        contentPane.add(btn8);
        btn8.addActionListener(new MyListener());

        JButton btn9 = new JButton("9");
        btn9.setBounds(196, 115, 71, 21);
        contentPane.add(btn9);
        btn9.addActionListener(new MyListener());

        JButton btn0 = new JButton("0");
        btn0.setBounds(22, 156, 71, 21);
        contentPane.add(btn0);
        btn0.addActionListener(new MyListener());

        JButton btnCall = new JButton("☎");
        btnCall.setBounds(109, 156, 158, 21);
        contentPane.add(btnCall);
        btnCall.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                numberInput();
            }
        });

        JButton btnClear = new JButton("Clear");
        btnClear.setBounds(22, 197, 245, 21);
        contentPane.add(btnClear);
        btnClear.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                tell_no = "";
                tf.setText("");
            }
        });
        
    }

    void numberInput() {
        JOptionPane.showMessageDialog(null, "calling\n"+tell_no);
    }

    class MyListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            JButton btn = (JButton) e.getSource();
            tell_no += btn.getText();
            tf.setText(tell_no);
        }
    }
}
