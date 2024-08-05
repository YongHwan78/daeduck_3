package day_05;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySw07 extends JFrame {
	private JPanel contentPane;
	private JTextField tf_mine;
	private JTextField tf_com;
	private JTextField tf_result;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySw07 frame = new MySw07();
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
	public MySw07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 300, 348);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);

		JLabel lbl = new JLabel("나 :");
		lbl.setBounds(29, 24, 57, 15);
		contentPane.add(lbl);

		JLabel lbl_com = new JLabel("컴 :");
		lbl_com.setBounds(29, 62, 57, 15);
		contentPane.add(lbl_com);

		JLabel lbl_result = new JLabel("결과 :");
		lbl_result.setBounds(29, 101, 57, 15);
		contentPane.add(lbl_result);

		tf_mine = new JTextField();
		tf_mine.setBounds(106, 21, 116, 21);
		contentPane.add(tf_mine);
		tf_mine.setColumns(10);

		tf_com = new JTextField();
		tf_com.setColumns(10);
		tf_com.setBounds(106, 59, 116, 21);
		contentPane.add(tf_com);

		tf_result = new JTextField();
		tf_result.setColumns(10);
		tf_result.setBounds(106, 98, 116, 21);
		contentPane.add(tf_result);
		
		JButton btn = new JButton("게임하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				playGame();
			}
		});
		btn.setBounds(29, 152, 169, 33);
		contentPane.add(btn);
	}

	void playGame() {
		String com = "";
		String res = "";
		double rnd = Math.random();
		if (rnd > 0.5)
			com = "짝";
		else
			com = "홀";

		String my = tf_mine.getText();

		tf_com.setText(com);
		if (my.equals(com)) {
			res = "승리";
		} else {
			res = "패배";
		}
		tf_result.setText(res);
		

	}

}
