import java.io.*;
import java.lang.*;

class DijkstraAlgorithm
{
    public static void main(String args[]) throws IOException {

        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            String str[] = read.readLine().trim().split(" ");
            int V = Integer.parseInt(str[0]);
            int E = Integer.parseInt(str[1]);
    
            ArrayList<ArrayList<ArrayList<Integer>>> adj = new ArrayList<ArrayList<ArrayList<Integer>>>();
            for(int i=0;i<V;i++)
            {
                adj.add(new ArrayList<ArrayList<Integer>>());
            }
            
            int i=0;
            while (i++<E) {
                String S[] = read.readLine().trim().split(" ");
                int u = Integer.parseInt(S[0]);
                int v = Integer.parseInt(S[1]);
                int w = Integer.parseInt(S[2]);
                ArrayList<Integer> t1 = new ArrayList<Integer>();
                ArrayList<Integer> t2 = new ArrayList<Integer>();
                t1.add(v);
                t1.add(w);
                t2.add(u);
                t2.add(w);
                adj.get(u).add(t1);
                adj.get(v).add(t2);
            }
            
            int S = Integer.parseInt(read.readLine());
            
            Solution ob = new Solution();
            
            int[] ptr = ob.dijkstra(V, adj, S);
            
            for(i=0; i<V; i++)
                System.out.print(ptr[i] + " ");
            System.out.println();
        }
    }
}// } Driver Code Ends


//User function Template for Java
class Pair implements Comparable<Pair>
{
    int v; int wt;
    
    public Pair(int v, int wt)
    {
        this.v = v;
        this.wt = wt;
    }
    
    public int compareTo(Pair that)
    {
        return this.wt-that.wt;
    }
    
}

class Solution
{
    //Function to find the shortest distance of all the vertices
    //from the source vertex S.
    static int[] dijkstra(int V, ArrayList<ArrayList<ArrayList<Integer>>> adj, int S)
    {
        // Write your code here
        
        PriorityQueue<Pair> q = new PriorityQueue<>();
        
        q.offer(new Pair(S,0));
        
        int cost[] = new int[V];
        Arrays.fill(cost, Integer.MAX_VALUE);
        
        cost[S] = 0;
        
        while(!q.isEmpty())
        {
            Pair curr = q.poll();
            
            int u = curr.v;
            
           
            
            ArrayList<ArrayList<Integer>> neighbours = adj.get(u);
            
            for(ArrayList<Integer> list: neighbours)
            {
                int vertex = list.get(0);
                int weight = list.get(1);
                
                if(cost[vertex] > cost[u] + weight)
                {
                cost[vertex] = cost[u]+weight;
                q.offer(new Pair(vertex,cost[vertex]));
                
            }
        }
    }
    
    return cost;
}
}
