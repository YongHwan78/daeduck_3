package day_05;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.SwingConstants;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Iterator;

import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class mySW04 extends JFrame {

	private JPanel contentPane;
	private JTextField tf01;
	private JTextField tf02;
	private JTextField tf03;
	private JButton btn;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					mySW04 frame = new mySW04();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public mySW04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		tf01 = new JTextField();
		tf01.setBounds(21, 39, 79, 36);
		contentPane.add(tf01);
		tf01.setColumns(10);
		
		tf02 = new JTextField();
		
		
		tf02.setColumns(10);
		tf02.setBounds(158, 39, 79, 36);
		contentPane.add(tf02);
		
		tf03 = new JTextField();
		
		tf03.setColumns(10);
		tf03.setBounds(345, 39, 79, 36);
		contentPane.add(tf03);
		
		JLabel lbl_1 = new JLabel("에서");
		lbl_1.setHorizontalAlignment(SwingConstants.CENTER);
		lbl_1.setBounds(100, 49, 57, 15);
		contentPane.add(lbl_1);
		
		btn = new JButton("까지 합은");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				calc();
				
			}
		});
		
		btn.setBounds(236, 45, 97, 23);
		contentPane.add(btn);
	}
	
	void calc() {
		String numS = tf01.getText();
		int num1 = Integer.parseInt(numS);
		String numS2 = tf02.getText();
		int num2 = Integer.parseInt(numS2);
		int sum = 0;
		
		
		for (int i = num1; i <= num2; i++) {
			sum += i;
		}
		
		tf03.setText(""+sum);
		
	}
	
	
}
