package day_05;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Iterator;

public class MySw06 extends JFrame {
	JLabel lbl;
	JTextArea ta;
	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySw06 frame = new MySw06();
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
	public MySw06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 278, 412);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lbl = new JLabel("출력단수");
		lbl.setBounds(27, 26, 57, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(124, 23, 91, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				gugudan();
				
			}
		});
		btn.setBounds(27, 61, 188, 31);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(27, 115, 188, 235);
		contentPane.add(ta);
		
	}
	
	void gugudan() {
		ta.setLineWrap(true);
		String dan= tf.getText();
		lbl.setText(dan+" 단");
		int danN = Integer.parseInt(dan);
		int sum = 0;
		String gugudan = "";
		
		for (int i = 1; i <= 9; i++) {
			sum = i*danN;
			gugudan += danN+ "*" +i + "=" + sum +"\r\n" ;
		}
		
		ta.setText(gugudan);
	}
	
}
