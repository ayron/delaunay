#include <iostream>
#include "Delaunay.hpp"

using namespace std;

// Test Data
// ---------

// Vertices
vector<int> XS{24, 11, 39, 16, 7, 40, 90, 79, 75, 22, 53, 28, 17, 11, 22, 91, 82, 80, 79, 19};
vector<int> YS{31, 62, 72, 84, 87, 9, 60, 66, 50, 18, 47, 9, 92, 85, 54, 30, 90, 57, 87, 84};

// Triangles - it is possible these could be in any order
//[(0, 1, 2), (0, 2, 5), (6, 0, 5), (9, 10, 2), (12, 13, 10), (15, 2, 1), (15, 1, 9), (21, 9, 1), (21, 25, 26), (21, 26, 29), (30, 9, 2), (30, 2, 15), (30, 15, 9), (39, 5, 13), (39, 6, 5), (45, 46, 0), (45, 0, 6), (45, 6, 39), (45, 39, 46), (57, 1, 0), (57, 0, 25), (57, 25, 21), (57, 21, 1), (69, 10, 9), (69, 9, 21), (69, 21, 29), (69, 29, 12), (69, 12, 10), (84, 39, 13), (84, 13, 12), (90, 26, 12), (90, 12, 29), (90, 29, 26), (99, 25, 39), (99, 39, 84), (99, 84, 12), (99, 12, 26), (99, 26, 25), (114, 25, 0), (114, 0, 46), (114, 46, 39), (114, 39, 25)]

int main()
{  
  // Initialize the Delaunay Triangulation Class
  DelaunayTriangulation DT(99, 99);

  //cout << "Reporting" << endl;
  //DT.print();

  cout << "Adding Points" << endl;
  
  for (int i = 0; i < XS.size(); i++)
  {
    cout << "i: " << i << " / " << XS.size() << endl;
    DT.AddPoint(Point(XS[i], YS[i]));
  }
  
  cout << "Reporting" << endl;
  DT.print();


  return 0;
}

