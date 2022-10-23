// Problem Link: https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/
class Solution
{
public:
    int hardestWorker(int n, vector<vector<int>> &logs)
    {
        // TC: nlog(n), SC: O(n)
        // vector<int> diff;
        // for(int i = 0; i < logs.size(); i++){
        //     if(i == 0)
        //         diff.push_back(logs[0][1]);
        //     else
        //         diff.push_back(logs[i][1] - logs[i - 1][1]);
        // }
        // int x = *max_element(diff.begin(), diff.end());
        // vector<pair<int,int>> pairs;
        // for(int i = 0; i < diff.size(); i++){
        //     if(diff[i] == x)
        //         pairs.push_back(make_pair(logs[i][0], diff[i]));
        // }
        // sort(pairs.begin(), pairs.end());
        // return pairs[0].first;

        // TC: O(n), SC: O(1)
        int prev = 0, id = -1, maximum = INT_MIN;
        for (int i = 0; i < logs.size(); i++)
        {
            // Find the maximum time difference
            if (maximum < logs[i][1] - prev)
            {
                maximum = logs[i][1] - prev;
                id = logs[i][0];
            }
            // If the difference is same take the value with minimum id value
            else if (maximum == logs[i][1] - prev)
                id = min(id, logs[i][0]);
            prev = logs[i][1];
        }
        // Return the id.
        return id;
    }
};