package day_05;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.SwingConstants;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.JButton;
import javax.swing.JTextArea;

public class mySW09 extends JFrame {
	JLabel lb;
	JButton btn;
	JTextArea ta;
	private JPanel contentPane;
	private JTextField tf;
	int com = -1;
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					mySW09 frame = new mySW09();
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
	public mySW09() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 384, 437);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);

		btn = new JButton("숫자맞춰보기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}

			
		});
		btn.setBounds(81, 87, 169, 23);
		contentPane.add(btn);

		lb = new JLabel("맞춤수");
		lb.setBounds(50, 42, 57, 15);
		contentPane.add(lb);

		tf = new JTextField();
		tf.setBounds(170, 39, 144, 21);
		contentPane.add(tf);
		tf.setColumns(10);

		ta = new JTextArea();
		ta.setBounds(50, 133, 264, 240);
		contentPane.add(ta);
		rndCom();
	}
	private void myClick() {
		String mine = tf.getText();
		int iMine = Integer.parseInt(mine);
		
		String line ="";
		System.out.println(com);
			if(com < iMine) {
				line = mine+" down \n";
			}else if(com > iMine) {
				line = mine+" up \n";
			}else {
				line = mine+ " ok \n";
				numberInput(iMine);
				ta.setText("");
			}
			String str_old = ta.getText();
			ta.setText(str_old+line);
			tf.setText("");
	}
	void rndCom() {
		com = (int) (Math.random() * 99)+1;
		
	}
	
	 void numberInput(int iMine) {
	        JOptionPane.showMessageDialog(null, "정답 \n"+iMine);
	        
	   }
	
	

	
}
