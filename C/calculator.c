#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <ctype.h>
#include <windows.h>

#define UP 72
#define DOWN 80
#define LEFT 75
#define RIGHT 77

int length;
int bend_no;
int len;
char key;
void record();
void load();
int life;
void Delay(long double);
void Move();
void Food();
int Score();
void Print();
void gotoxy(int x, int y);
void GotoXY(int x,int y);
void Bend();
void Boarder();
void Down();
void Left();
void Up();
void Right();
void ExitGame();
int Scoreonly();

struct coordinate
{
    int x;
    int y;
    int direction;
};

typedef struct coordinate coordinate;

coordinate head, bend[500], food, body[30];

int main()
{
    Print();
    system("cls");
    load();

    length = 5;
    head.x = 25;
    head.y = 20;
    head.direction = RIGHT;

    Boarder();
    Food();

    life = 3;
    bend[0] = head;

    Move();

    return 0;
}

void Move()
{
    int a, i;

    do
    {
        Food();
        fflush(stdin);

        len = 0;

        for (i = 0; i < 30; i++)
        {
            body[i].x = 0;
            body[i].y = 0;

            if (i == length)
                break;
        }

        Delay(length);
        Boarder();

        if (head.direction == RIGHT)
            Right();
        else if (head.direction == LEFT)
            Left();
        else if (head.direction == DOWN)
            Down();
        else if (head.direction == UP)
            Up();

        ExitGame();

    } while (!kbhit());

    a = getch();

    if (a == 27)
    {
        system("cls");
        exit(0);
    }

    key = getch();

    if ((key == RIGHT && head.direction != LEFT) ||
        (key == LEFT && head.direction != RIGHT) ||
        (key == UP && head.direction != DOWN) ||
        (key == DOWN && head.direction != UP))
    {
        bend_no++;
        bend[bend_no] = head;
        head.direction = key;
        Move();
    }
    else if (key == 27)
    {
        system("cls");
        exit(0);
    }
    else
    {
        printf("\a");
        Move();
    }
}

void gotoxy(int x, int y)
{
    COORD coord;
    coord.X = x;
    coord.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

void GotoXY(int x, int y)
{
    HANDLE a;
    COORD b;
    fflush(stdout);
    b.X = x;
    b.Y = y;
    a = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleCursorPosition(a, b);
}

void load()
{
    int row, col, r, c, q;
    gotoxy(36, 14);
    printf("loading...");
    gotoxy(30, 15);
    for (r = 1; r <= 20; r++)
    {
        for (q = 0; q <= 100000000; q++); // Delay for loading animation
        printf("%c", 177);
    }
    getch();
}

// Other functions (Right, Left, Down, Up, ExitGame, etc.)
