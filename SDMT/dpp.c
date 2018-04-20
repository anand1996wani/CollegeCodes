#include <stdio.h>
#include <unistd.h>
#include <semaphore.h>
#include <pthread.h>

#define N 5
#define THINKING 0
#define HUNGRY	1
#define EATING	2
#define LEFT (phID+4)%N
#define RIGHT (phID+1)%N


/*
	sem_wait is like P opeartion
	sem_post is like V operation
*/

sem_t mutex;	//so that all cannot be hungry together or test together
sem_t S[N];	//for allowing to take fork after testing

void * philosopher(void *num);
void takeFork(int);
void putFork(int);
void test(int);

int state[N];
int phIDArray[N] = {0,1,2,3,4};

int main(){
	pthread_t threadID[N];
	sem_init(&mutex,0,1); //not shared and initialized to 1
	for(int i = 0;i<N;i++)
		sem_init(&S[i],0,0);	//not shared and initialized to 0
	for(int i = 0;i<N;i++){
		pthread_create(&threadID[i],NULL,philosopher,&phIDArray[i]);
		printf("Philosopher %d is Thinking\n",i+1);	
	}
	for(int i = 0;i<N;i++){
		pthread_join(threadID[i],NULL);
	}	
	return 0;
}

void * philosopher(void * num){
	while(1){
		int *philosopherNum = num;
		sleep(1);
		takeFork(*philosopherNum);
		sleep(0);
		putFork(*philosopherNum);
	}
}

void takeFork(int phID){
	sem_wait(&mutex);
	state[phID] = HUNGRY;
	printf("Philosopher %d Is Hungry\n",phID+1);
	test(phID);
	sem_post(&mutex);
	sem_wait(&S[phID]);
	sleep(1);	
}

void test(int phID){
	if(state[phID]==HUNGRY && state[LEFT]!=EATING && state[RIGHT]!=EATING){
		state[phID] = EATING;
		sleep(2);
		printf("\n Philosopher %d takes fork %d and %d and started Eating.\n",phID+1,LEFT+1,phID+1);
		sem_post(&S[phID]);
	}	
}

void putFork(int phID){
	sem_wait(&mutex);
	state[phID] = THINKING;
	printf("Philosopher %d putting fork %d and %d down and started Thinking.\n",phID+1,LEFT+1,phID+1);
	test(LEFT);
	test(RIGHT);
	sem_post(&mutex);
}
