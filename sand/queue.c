#include <stdio.h>

typedef struct q {
    int contains[100005];
    int head;
    int tail;
    int length;
} Queue;

void print_queue(Queue *q) {
    int i;
    printf("[");
    for(i = q->head; i < q->tail - 1; i++) {
        printf("%d, ", q->contains[i]);
    }
    printf("%d]\n", q->contains[q->tail - 1]);
}

void init(Queue *q) {
    int i;
    for(i = 0; i < 100005; i++) q->contains[i] = 0;
    q->head = 0;
    q->tail = 0;
    q->length = 0;
}

int is_empty(Queue *q){
    if (q->head == q->tail) return 0;
    return -1;
}

int is_full(Queue *q) {
    if (q->length == 100005) return 0;
    return -1;
}

int enqueue(Queue *q, int x) {
    if (is_full(q) == 0) return -1;
    q->contains[q->tail] = x;
    q->tail += 1;
    q->length += 1;
    return 0;
}

int dequeue(Queue *q) {
    if (is_empty(q) == 0) return -1;
    int x = q->contains[q->head];
    q->head += 1;
    q->length -= 1;
    return x;
}

int main() {
    Queue q;
    init(&q);
    enqueue(&q, 10);
    enqueue(&q, 100);
    enqueue(&q, 5555);
    print_queue(&q); // [10, 100, 5555]
    int x = dequeue(&q);
    int y = dequeue(&q);
    print_queue(&q); // [5555]
    printf("x, y = %d, %d\n", x, y);
    enqueue(&q, 19);
    print_queue(&q); // [5555, 19]
    return 0;
}