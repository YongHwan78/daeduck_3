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

public class mySW03 extends JFrame {

	private JPanel contentPane;
	private JTextField tf01;
	private JTextField tf02;
	private JTextField tf03;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					mySW03 frame = new mySW03();
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
	public mySW03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		tf01 = new JTextField();
		tf01.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int num1 = Integer.parseInt(tf01.getText());
			}
		});
		tf01.setBounds(21, 39, 79, 36);
		contentPane.add(tf01);
		tf01.setColumns(10);
		
		tf02 = new JTextField();
		tf02.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int num2 = Integer.parseInt(tf02.getText());
				
			}
		});
		
		
		tf02.setColumns(10);
		tf02.setBounds(158, 39, 79, 36);
		contentPane.add(tf02);
		
		tf03 = new JTextField();
		tf03.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				calc();
			}
		});
		tf03.setColumns(10);
		tf03.setBounds(295, 39, 79, 36);
		contentPane.add(tf03);
		
		JLabel lbl = new JLabel("=");
		lbl.setHorizontalAlignment(SwingConstants.CENTER);
		lbl.setBounds(237, 49, 57, 15);
		contentPane.add(lbl);
		
		JLabel lbl_1 = new JLabel("*");
		lbl_1.setHorizontalAlignment(SwingConstants.CENTER);
		lbl_1.setBounds(100, 49, 57, 15);
		contentPane.add(lbl_1);
	}
	
	void calc() {
		String a1 = tf01.getText(); 
		String a2 = tf02.getText(); 
		
		int aNum = Integer.parseInt(a1);
		int aNum2 = Integer.parseInt(a2);
		int sum = aNum*aNum2;
		
		tf03.setText(""+sum);
	}
}
