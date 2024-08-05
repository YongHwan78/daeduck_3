package day_05;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySW05 extends JFrame {

	private JPanel contentPane;
	JLabel lbl01,lbl02,lbl03,lbl04,lbl05,lbl06;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySW05 frame = new MySW05();
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
	public MySW05() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lbl01 = new JLabel("__");
		lbl01.setBounds(41, 32, 24, 22);
		contentPane.add(lbl01);
		
		lbl02 = new JLabel("__");
		lbl02.setBounds(106, 32, 24, 22);
		contentPane.add(lbl02);
		
		lbl03 = new JLabel("__");
		lbl03.setBounds(171, 32, 24, 22);
		contentPane.add(lbl03);
		
		 lbl04 = new JLabel("__");
		lbl04.setBounds(236, 32, 24, 22);
		contentPane.add(lbl04);
		
		lbl05 = new JLabel("__");
		lbl05.setBounds(301, 32, 24, 22);
		contentPane.add(lbl05);
		
		lbl06 = new JLabel("__");
		lbl06.setBounds(366, 32, 24, 22);
		contentPane.add(lbl06);
		
		JButton btn = new JButton("로또생성하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				lotto();
			}
		});
		btn.setBounds(12, 84, 390, 32);
		contentPane.add(btn);
		
	}
	private void lotto() {
		
		int[] rottoNum = new int[] {
				1,2,3,4,5,	6,7,8,9,10,
				11,12,13,14,15,	16,17,18,19,20,
				21,22,23,24,25,	26,27,28,29,30,
				31,32,33,34,35,	36,37,38,39,40,
				41,42,43,44,45	
		};
		
		for (int i = 0; i < 10000; i++) {
			int rnd = (int)(Math.random()*45);
			
			int a = rottoNum[0];
			rottoNum[0] = rottoNum[rnd];
			rottoNum[rnd] = a;
		}
		
		lbl01.setText(""+rottoNum[0]);
		lbl02.setText(""+rottoNum[1]);
		lbl03.setText(""+rottoNum[2]);
		lbl04.setText(""+rottoNum[3]);
		lbl05.setText(""+rottoNum[4]);
		lbl06.setText(""+rottoNum[5]);
	}

}
