package day_05;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JButton;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySw11 extends JFrame {
	JTextArea ta;
	private JPanel contentPane;
	private JTextField tf;
//	int numArr[] = new int[3];
//	int inputArr[] = new int[3];
	String com = "";
//	int strike = 0;
//	int ball = 0;
//	String[] res = new String[3];

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySw11 frame = new MySw11();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * 1에서 10까지 3자리를 가져오는데 중복 없이 가져오기 매칭해서 볼 , 스트라이크 검증하기
	 * 
	 */
	public MySw11() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 326, 537);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);

		JLabel lbl = new JLabel("야구게임");
		lbl.setBounds(39, 31, 68, 18);
		contentPane.add(lbl);

		JButton btn = new JButton("맞춰보기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick ();
			}

		});
		btn.setBounds(39, 71, 97, 23);
		contentPane.add(btn);

		ta = new JTextArea();
		ta.setBounds(38, 109, 232, 369);
		contentPane.add(ta);

		tf = new JTextField();
		tf.setBounds(202, 31, 68, 32);
		contentPane.add(tf);
		tf.setColumns(10);
		ranCom();
	}

//	private void playGame() {
//
//		while (true) {
//			for (int i = 0; i < inputArr.length; i++) {
//
//				inputArr[i] = tf.getText().charAt(i);
//
//			}
//			
//			for(int i = 0; i < numArr.length; i++) {
//				numArr[i] = (int)(Math.random() * 9 + 1); 
//			    	for(int j = 0; j < i; j++) {
//			        
//			        	if(numArr[j] == numArr[i]) {
//			            	
//			                	i--; 
//			                    	break;
//			                }
//			        }
//			}
//			
//			
//
//			for (int i = 0; i < numArr.length; i++) {
//				for (int j = 0; j < inputArr.length; j++) {
//
//					if (numArr[i] == inputArr[j] && i == j) {
//						res[i] = "strike";
//
//					} else if (numArr[i] == inputArr[j] && i != j) {
//
//						res[i] = "ball";
//					}
//				}
//
//				for (int j = 0; j < inputArr.length; j++) {
//
//					ta.setText(res[j]);
//				}
//				ta.setText("\n");
//				
//				if (strike == 3) {
//					
//					break;
//				}
//
//			}
//
//		}
//		
//	}// paly game
	
	void ranCom() {
		
		int[] arr = {1,2,3,4,5,6,7,8,9};
		
		for (int i = 0; i < 100	; i++) {
			int rnd = (int)(Math.random()*9);
				int a = arr[0];
				arr[0] = arr[rnd];
				arr[rnd] = a;
		}
		
		com = arr[0]+""+arr[1]+""+arr[2];
		System.out.println(com);
		
	}
	
	int getS(String com , String mine) {
		int ret = 0;
		
		String c1 = com.substring(0,1);
		String c2 = com.substring(1,2);
		String c3 = com.substring(2,3);
		
		String m1 = mine.substring(0,1);
		String m2 = mine.substring(1,2);
		String m3 = mine.substring(2,3);
		
		if(c1.equals(m1)) ret++;
		if(c2.equals(m2)) ret++;
		if(c3.equals(m3)) ret++;
		
		
		return ret;
	}
	int getB(String com , String mine) {
		int ret = 0;
		
		String c1 = com.substring(0,1);
		String c2 = com.substring(1,2);
		String c3 = com.substring(2,3);
		
		String m1 = mine.substring(0,1);
		String m2 = mine.substring(1,2);
		String m3 = mine.substring(2,3);
		
		if(c1.equals(m2) || c1.equals(m3)) ret++;
		if(c2.equals(m1) || c2.equals(m3)) ret++;
		if(c3.equals(m2) || c3.equals(m1)) ret++;
		
		
		return ret;
	}
	
	void myclick () {
		
		String mine = tf.getText();
		int s = getS(com, mine);
		int b = getB(com, mine);
		System.out.println("s" + s);
		System.out.println("b" + b);
		
		String line = mine +"\t" + "s:"+s + "b:" + b + "\n";
		
		String str_old = ta.getText();
		
		ta.setText(str_old+line);
		ta.setText("");
		
		if(s==3) {
			JOptionPane.showMessageDialog(null, " 축하합니다 \n" + mine);
		}
	}

}
