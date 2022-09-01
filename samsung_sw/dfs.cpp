#include <iostream>

using namespace std;

int n;
int Test_case;
int graph[101][101];
int result_list[101];
int copy_graph[101][101];


bool dfs(int x, int y , int copy_graph[][101] , int matrix_size) {
    
    if (x <= -1 || x >=matrix_size || y <= -1 || y >=matrix_size) {
        return false;
    }
    
    if (copy_graph[x][y] == 0) {
        
        copy_graph[x][y] = 1;
        
        dfs(x - 1, y , copy_graph , matrix_size);
        dfs(x, y - 1 , copy_graph , matrix_size);
        dfs(x + 1, y , copy_graph , matrix_size);
        dfs(x, y + 1 , copy_graph , matrix_size);
        return true;
    }
    return false;
}

int main(int argc , char** argv) {
   
    
    cin >> Test_case;
    
    for(int test_size =0 ; test_size< Test_case; test_size++){
        cin >> n;
        int matrix_size = n;
        int max =0;
        int max_result =0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                scanf(" %d", &graph[i][j]);
                if (graph[i][j] > max){
                    max = graph[i][j];
                }
            }
        }
        int criteria;
        for(int criteria = 1; criteria <  max; criteria++){
            int copy_graph[101][101] ={0};

            for (int k = 0; k < n; k++) {
                for (int j = 0; j < n; j++) {

                    if(graph[k][j] <=criteria){
                        copy_graph[k][j] = 1;
                    }
                }
            }
            int result = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (dfs(i, j , copy_graph , matrix_size)) {
                        result += 1;
                    }
                }
            }

            if (result > max_result){
                max_result = result;
            }
        }    
        result_list[test_size] = max_result;
    }   
        
    for(int t = 0 ; t < Test_case; t++){
            cout << "#" <<  t +1 << " " << result_list[t] << endl;
        }
        
    
   return 0; 
}
