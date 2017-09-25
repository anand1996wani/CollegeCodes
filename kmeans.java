import java.util.*; 
import java.lang.*;

import com.sun.xml.internal.bind.v2.runtime.unmarshaller.XsiNilLoader.Array;
public class kmeans {
	public double euclidDistance(double x[],double y[]){
		double temp = 0;
		for(int i = 0;i<x.length;i++){
			temp = temp + Math.pow((x[i]-y[i]),2);
		}
		return Math.sqrt(temp);
	} 
	public static void main(String args[]){
		Scanner s = new Scanner(System.in);
		System.out.println("Enter number of elements");
		int num_ele = s.nextInt();
		System.out.println("Enter number of attributes");
		int num_att = s.nextInt();
		double[][] matrix = new double[num_ele][num_att];
		System.out.println("Enter the elements");
		for(int i = 0;i<num_ele;i++){
			for(int j = 0;j<num_att;j++){
				matrix[i][j] = s.nextDouble();
			}
		}
		System.out.println("Enter number of clusters");
		int k = s.nextInt();
		double[][] distance = new double[k][num_ele];
		double[][] centers = new double[k][num_att];
		for(int i = 0;i<k;i++){
			for(int j = 0;j<num_att;j++){
				centers[i][j] = matrix[i][j];
			}
		}
		int [] result = new int[num_ele];
		int [] prev = new int[num_ele];
		/*System.out.println("Matrix is :");
		for(int i = 0;i<num_ele;i++){
			for(int j = 0;j<num_att;j++){
				System.out.print(matrix[i][j]);
			}
			System.out.println();
		}
		System.out.println("Initial Centers are :");
		for(int i = 0;i<k;i++){
			for(int j = 0;j<num_att;j++){
				System.out.print(centers[i][j]);
			}
			System.out.println();
		}*/
		kmeans km = new kmeans();
		while(true){
			for(int i = 0;i<k;i++){
				for(int j = 0;j<num_ele;j++){
					distance[i][j] = km.euclidDistance(centers[i],matrix[j]);
				}
			}
			//System.out.println("Initial Distance iS:");
			/*
			for(int i = 0;i<k;i++){
				for(int j = 0;j<num_ele;j++){
					System.out.print(distance[i][j]);
					System.out.print(" ");
				}
				System.out.println();
			}*/
			for(int i = 0;i<k;i++){
				System.out.print("Cluster center ");
				System.out.print(i+1);
				System.out.print(" is : ");
				for(int j = 0;j<num_att;j++){
					System.out.print(centers[i][j]);
					System.out.print(" ");
				}
				System.out.println();
			}
			System.out.println();
			double min = 0.0;
			int a = 0;
			for(int i = 0;i < num_ele;i++){
				min = distance[0][i];
				a = 0;
				for(int j = 1;j < k;j++){
					if(min > distance[j][i]){
						min = distance[j][i];
						a = j;
					}
				}
				result[i] = a;
			}
			for(int i = 0;i<num_ele;i++){
				System.out.print("Element No ");
				System.out.print(i+1);
				System.out.print(" belongs to cluster NO ");
				System.out.println(result[i]+1);
			}
			System.out.println();
			for(int i = 0;i<k;i++){
				for(int j = 0;j<num_att;j++){
					int n = 0;
					double sum = 0.0;
					for(int z = 0;z < result.length;z++){
						if(result[z]==i){
							sum = sum + matrix[z][j];
							n = n + 1;
						}
					}
					centers[i][j] = sum/n;
				}
			}
			if(Arrays.equals(result,prev)){
				break;
			}
			else{
				prev = Arrays.copyOf(result, result.length);
			}
			System.out.println("------------------------------------------------------------------");
		}
	}
}
