////////////////////////////////////////////////////////////
// Author:       Mae-Jeanne Preville
// Course:       Cryptography
// Professor:		 Dr. Griffin
// Semester:     Fall 2020
// Program:			 Assignment #6
///////////////////////////////////////////////////////////

#include <iostream>
#include <fstream>

using namespace std;
  
int main()
{   
  //Input and output files declaration
  ifstream infile;
  ofstream outfile;

  //infile.open("MaeTestInput.txt");
  infile.open("MaeInput.txt");
  outfile.open("MaeOutput.txt"); 

  cout << "Name: Mae-Jeanne Preville" << endl;
	
    int numVal = 0; 
    int counter = 1;
    
    while(infile >> numVal) //Read in num values
    {  
      //Code to find out whether input num is prime 
      int primeNum = 0;
      if (primeNum == 0)
      {
        cout << "Number " << counter << " : " << numVal << " - Factors: ";
        for(int i = 2; i <= numVal/2; i++)
        {
          if(numVal % i == 0)
          {          
            cout << " " << i << " *";
          }           
        }
        cout << endl;       
      }
      else if (primeNum == 1)
      {
        cout << "Prime" << endl;
      }       
      counter++;
    }

	outfile.close();   
	infile.close(); 
	system("pause");
	return 0;
}

