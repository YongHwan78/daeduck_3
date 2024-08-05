package day_05;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySw10 extends JFrame {
	JButton btn;
	JLabel lbl_last;
	JLabel lbl_first;
	JTextArea ta;
	private JPanel contentPane;
	private JTextField tf_first;
	private JTextField tf_last;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySw10 frame = new MySw10();
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
	public MySw10() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 286, 453);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);

		lbl_first = new JLabel("시작별수:");
		lbl_first.setBounds(35, 10, 72, 28);
		contentPane.add(lbl_first);

		tf_first = new JTextField();
		tf_first.setBounds(119, 14, 116, 21);
		contentPane.add(tf_first);
		tf_first.setColumns(10);

		lbl_last = new JLabel("끝별수:");
		lbl_last.setBounds(35, 48, 72, 28);
		contentPane.add(lbl_last);

		tf_last = new JTextField();
		tf_last.setColumns(10);
		tf_last.setBounds(119, 52, 116, 21);
		contentPane.add(tf_last);

		JButton btn = new JButton("별 출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(35, 96, 200, 28);
		contentPane.add(btn);

		ta = new JTextArea();
		ta.setBounds(35, 134, 200, 250);
		contentPane.add(ta);
	}
	public void myclick() {
		String f = tf_first.getText();
		String l = tf_last.getText();
		int fNumI = Integer.parseInt(f);
		int lNumI = Integer.parseInt(l);
		String str ="";
		String str_old = "";
		for (int i = 0; i < lNumI; i++) {
			if(i < fNumI) continue;
			str_old = ta.getText();
			str += star(i);
			
		}
		ta.setText(str_old+str+"\n");
		
	}
	public String star(int cnt) {
		String ret = "";
		for (int i = 0; i < cnt; i++) {
			ret+="*";
		}
		
		ret+= "\n";
		
		return ret;
	}


}
