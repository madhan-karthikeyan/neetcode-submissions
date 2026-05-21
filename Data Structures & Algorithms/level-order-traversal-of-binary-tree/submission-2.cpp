/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    void traversal(TreeNode* root,int level, vector<vector<int>> &nodes) {
        if (!root) {
            return;
        }
        if (nodes.size()<=level) {
            nodes.push_back({});
        }

        nodes[level].push_back(root->val);
        traversal(root->left, level+1, nodes);
        traversal(root->right, level+1, nodes);

    }
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> array;
        traversal(root, 0, array);
        return array;        
    }
};
