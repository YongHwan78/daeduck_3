package day_04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import java.awt.Font;
import javax.swing.SwingConstants;
import javax.swing.JButton;
import java.awt.Color;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySW01_1 extends JFrame {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					
					MySW01_1 frame = new MySW01_1();
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
	public MySW01_1() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300); // setSize
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
				// 인스턴스 명
		JLabel lbl = new JLabel("KIGGGG HWAN YONG");
		lbl.setFont(new Font("굴림", Font.BOLD, 19));
		lbl.setBounds(46, 48, 306, 29);
		contentPane.add(lbl);
		
		JButton btn = new JButton("CLICK");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				lbl.setText("김환용");
				System.out.println("시작");
			}
		});
		lbl.setLabelFor(btn);
		
		btn.setForeground(new Color(192, 192, 192));
		btn.setFont(new Font("굴림", Font.BOLD, 12));
		btn.setBounds(46, 184, 97, 23);
		contentPane.add(btn);
	}
}
