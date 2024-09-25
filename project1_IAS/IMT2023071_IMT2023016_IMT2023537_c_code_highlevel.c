#include <stdio.h>
int x_power_y(int x,int y){
	int result=1;
	for (int i=0;i<y;i++){
		result=result*x;
	}
	return result;
}
int len(int n){
  	//finding the number of digits in the number
	int count=0;	//the final value of count will be the number of digits
	while (n!=0){
		n=n/10;
		count++;
	}
	return count;
}

int armstrong(int n){
	//finding the sum when each digit is raised to the power of the number of digits in the number
	int count=len(n);
	int sum=0;
	int temp=n;
	while (temp!=0){
		int units=temp%10;
		sum=sum+(x_power_y(units,count));
		temp=temp/10;
	}

	if (sum==n){
		return 1;
	}

	else{
		return 0;
	}

}
void main(){
	int n;
	printf("Enter a number:");
	scanf("%d",&n);
	printf("Final result (1: if Armstrong number, 0: if not)\n");
	printf("%d\n",armstrong(n));
}


