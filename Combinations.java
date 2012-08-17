package dropboxChallenge;

import java.awt.List;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class Combinations 
{
	private static ArrayList<Integer> data_positive = new ArrayList<Integer>();
	private static ArrayList<String> activity_positive = new ArrayList<String>();
	private static ArrayList<Integer> data_negative = new ArrayList<Integer>();
	private static ArrayList<String> activity_negative = new ArrayList<String>();
	private static int pos_comb;
	private static int neg_comb;
	
	public static void readInput()
	{
		try
    	{
		  FileInputStream fstream = new FileInputStream("input.txt");
		  DataInputStream in = new DataInputStream(fstream);
		  BufferedReader br = new BufferedReader(new InputStreamReader(in));
		  
		  String strLine;
		  int size = Integer.parseInt(br.readLine());
		  
		  while ((strLine = br.readLine()) != null)   
		  {
			  int i = Integer.parseInt(strLine.split(" ")[1]); 
			  if ( i > 0)
			  {
				  activity_positive.add(strLine.split(" ")[0]);
				  data_positive.add(i);
			  }
			  else
			  {
				  activity_negative.add(strLine.split(" ")[0]);
				  data_negative.add(i);
			  }
			  
		  }		  
		  
		  in.close();		    
		}
    	
		catch (Exception e)
    	{
    		System.err.println("Error: " + e.getMessage());
		}  

	}
	
	public static void positiveDescending(int[] sum_positive, ArrayList<ArrayList<Integer>> positive_arraylist)
	{
		int max_len = sum_positive.length;
		int temp_int = 0;
		ArrayList<Integer> temp_arrlist = new ArrayList<Integer>();
		for (int i=0; i<max_len-1;i++)
		{
			for (int j = i+1; j<max_len;j++)
			{
				if (sum_positive[i] > sum_positive[j])	// Ascending now					
				{
					// sort the sum array in descending order
					temp_int = sum_positive[i];
					sum_positive[i] = sum_positive[j];
					sum_positive[j] = temp_int;
					
					// change the order of combinations to match the sum array's new order
					temp_arrlist = positive_arraylist.get(i);
					positive_arraylist.set(i, positive_arraylist.get(j));
					positive_arraylist.set(j, temp_arrlist);
				}
			}
		}
	}
	
	
	public static void negativeAscending(int[] sum_negative, ArrayList<ArrayList<Integer>> negative_arraylist)
	{
		int max_len = sum_negative.length;
		int temp_int = 0;
		ArrayList<Integer> temp_arrlist = new ArrayList<Integer>();
		for (int i=0; i<max_len-1;i++)
		{
			for (int j = i+1; j<max_len;j++)
			{
				if (sum_negative[i] < sum_negative[j]) // Descending now						
				{
					// sort the sum array in descending order
					temp_int = sum_negative[i];
					sum_negative[i] = sum_negative[j];
					sum_negative[j] = temp_int;
					
					// change the order of combinations to match the sum array's new order
					temp_arrlist = negative_arraylist.get(i);
					negative_arraylist.set(i, negative_arraylist.get(j));
					negative_arraylist.set(j, temp_arrlist);
				}
			}
		}
	}
	
	public static void getAllSubset(int[] input, ArrayList<ArrayList<Integer>> list)
	{
		int size = input.length;
		int limit = (int) Math.pow(2, size);
		for (int i=1; i<limit; i++)
		{
			String binary = Integer.toBinaryString(i);
			while (binary.length()<size)
			{
				binary = "0" + binary;
			}
			ArrayList<Integer> temp = new ArrayList<Integer>();
			for (int j=0; j<size; j++)
			{
				if (binary.charAt(j) == '1')
				{
					temp.add(input[j]);
				}
			}
			list.add(temp);
		}

	}
	
	public static int[] sumAll(ArrayList<ArrayList<Integer>> list)
	{
		int[] sum = new int[list.size()];
		for (int i=0;i<list.size();i++)
		{
			for (int j=0;j<list.get(i).size();j++)
			{
				sum[i] = sum[i] + list.get(i).get(j);
			}
		}
		return sum;
		
	}
	
	public static boolean findMatch(int[] positive, int[] negative)
	{
		int i = 0; 
		int j = 0; 
		int sum = positive[i] + negative[j];
		while ((sum!=0)&&(i<positive.length-1)&&(j<negative.length-1))
		{
			if ( sum > 0) 
			{
				j = j + 1; // for positive ascending and negative descending
						   // to figure out the combination with minimum combinations
			}
			else
			{
				i = i + 1;				
			}
			sum = positive[i] + negative[j];
		}
		pos_comb = i;
		neg_comb = j;
		
		if (sum==0) return true;
		else return false;
	}
	
	
	
	
	public static String hasSolution(ArrayList<Integer> pos, ArrayList<Integer> neg)
	{
		int pos_size = pos.size();
		int neg_size = neg.size();
		String output = "";
		int[] pos_temp = new int[pos_size];
		int[] neg_temp = new int[neg_size];
		
		for(int i=0; i<pos_size; i++)
		{
			for(int j=0; j<data_positive.size();j++ )
			{
				if ( pos.get(i) - data_positive.get(j) == 0)  
				{
					output = output + activity_positive.get(j) + " ";
					break;
				}
			}
		}
		
		for(int i=0; i<neg_size; i++)
		{
			for(int j=0; j<data_negative.size();j++ )
			{
				if ( neg.get(i) - data_negative.get(j) == 0)  
				{
					output = output + activity_negative.get(j) + " ";
					break;
				}
			}
		}				
		return output;
	}
	
	public static void outputHasSolution(String output)
	{
		try
		{ 
			  FileWriter fstream = new FileWriter("output.txt");
			  BufferedWriter out = new BufferedWriter(fstream);
			  String[] out_str = output.split(" ");
			  for (int i = 0; i<out_str.length; i++)
			  {
				  out.write(out_str[i]);
				  out.newLine();
			  }			
			  out.close();
		}
		catch (Exception e)
			{
				System.err.println("Error: " + e.getMessage());
			}
	
	}
	
	public static void outputHasNoSolution()
	{
		try
		{ 
			  FileWriter fstream = new FileWriter("output.txt");
			  BufferedWriter out = new BufferedWriter(fstream);
			  out.write("No solution");
			  out.close();
		}
		catch (Exception e)
			{
				System.err.println("Error: " + e.getMessage());
			}
	
	}
	
	public static void main(String[] args) 
	{		
		// read input from a text file
		readInput();
		
		// prepare data by separate positive data from negative data
		int[] list1 = new int[data_positive.size()];
		for (int i =0; i<list1.length;i++)
		{
			list1[i] = data_positive.get(i);
		}		
		ArrayList<ArrayList<Integer>> positive_arraylist = new ArrayList<ArrayList<Integer>>();
		// get all subsets of the set of positive data
		// and store them in positive_arraylist
		getAllSubset(list1, positive_arraylist);
		// sum all elements of each subset and store them in sum_positive
		int[] sum_positive = sumAll(positive_arraylist);
		// sort sum_positive in descending order 
		// and make sure the order of each subset is changed accordingly in positive_arraylist  
		positiveDescending(sum_positive, positive_arraylist);
				
		// pretty much the same procedure as above, except sort the negative sum in ascending order
		int[] list2 = new int[data_negative.size()];
		for (int i =0; i<list2.length;i++)
		{
			list2[i] = data_negative.get(i);
		}
		ArrayList<ArrayList<Integer>> negative_arraylist = new ArrayList<ArrayList<Integer>>();
		getAllSubset(list2, negative_arraylist);
		int[] sum_negative = sumAll(negative_arraylist);
		negativeAscending(sum_negative, negative_arraylist);
		
		// if either of the negative or positive set is empty, no solution
		if ((sum_positive.length == 0) || (sum_negative.length == 0))
		{
			outputHasNoSolution();
		}
		// check if there is any sum between 2 elements of the two sum arrays returns zero
		// if so, get the indexes of each element in their corresponding arrays
		// and trace back to get the corresponding activity.
		else
		{
			if (findMatch(sum_positive,sum_negative))
			{
				outputHasSolution(hasSolution(positive_arraylist.get(pos_comb), negative_arraylist.get(neg_comb)));
			}
			else
			{
				outputHasNoSolution();
			}
		}
	}

}
