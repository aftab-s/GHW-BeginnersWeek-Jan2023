#include<iostream.h>
#include<cstdlib.h>

//using namespace std;

int main()
{
    cout<<"\n Welcome to password generator!\n";
    string username, option;
    cout<<"\nEnter your username : ";
    cin>>username;
    cout<<"\nShall we proceed to generate password?\nEnter yes/no after making sure your surrounding is secure enough : ";
    cin>>option;
    if(option == "Yes" || option == "yes" )
        {
            int n;
            cout<<"\nEnter no. of characters required : ";
            cin>>n;
            cout<<"\n Generated password : ";
            static const char ucase[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
            const size_t ucase_count = sizeof(ucase) - 1; // ucase includes terminating '\0'
            size_t i, j;

             srand(time(NULL));


                for(j = 0; j < n; j++)
                {
                    char random_char;
                    int random_index = (double)rand() / RAND_MAX * ucase_count;

                    random_char = ucase[random_index];
                    printf("%c", random_char);
                }
        }
    else
        {
            cout<<"\n Get ready and run the program once again!\n";
        }

    return 0;
}
