<?php

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         $this->val = $val;
 *         $this->left = $left;
 *         $this->right = $right;
 *     }
 * }
 */
class Solution {

    /**
     * @param TreeNode $root
     * @return Integer
     */
    // 1. DFS 
    function deepestLeavesSum($root) {
        $nodes = [];

        $this->dfs($root, 0, $nodes);

        return array_sum($nodes[count($nodes) - 1]);
    }

    function dfs($node, $level, &$nodes) {
        if ($node === null) {
            return;
        }

        $nodes[$level][] = $node->val;

        $this->dfs($node->left, $level + 1, $nodes);
        $this->dfs($node->right, $level + 1, $nodes);
    }
    // -----------我是分隔線----------------
    // 2. BFS
    function deepestLeavesSum($root) {
        $queue = [$root];
        $sum = 0;

        while (!empty($queue)) {
            $sum = 0;
            $size = count($queue);

            for ($i = 0; $i < $size; $i++) {
                $node = array_shift($queue);
                $sum += $node->val;

                if ($node->left !== null) {
                    $queue[] = $node->left;
                }

                if ($node->right !== null) {
                    $queue[] = $node->right;
                }
            }
        }

        return $sum;
    }
    // -----------我是分隔線----------------
    // 3. DFS
    function __construct(
        public int $sum = 0,
        public int $deepest = 0,
    ) {}
    
    function deepestLeavesSum($root, $depth = 0) {
        if ($root === null) return;  // current node is NULL - just return.

        if ($root->left === null && $root->right === null) {
            if ($depth === $this->deepest) {
                $this->sum += $root->val;  // if $depth is exactly equal to $deepest, add to $sum
            } else if ($depth > $this->deepest) {
                $this->sum = $root->val;
                $this->deepest = $depth; // found a more deeper leaf node, reset $sum and update $deepest
            }
 
            $this->deepestLeavesSum($root->left, $depth + 1);   // recurse for the left, 
            $this->deepestLeavesSum($root->right, $depth + 1);  // and the right node of the current node
        } // if current is a leaf node

        return $this->sum; // finally return the $sum accumulated till now which will be $sum of value of $deepest leaves
    }
}

$root1 = [1,2,3,4,5,null,6,7,null,null,null,null,8];
$root2 =  [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5];

var_export((new Solution())->sum);

// $result1 = (new Solution())->deepestLeavesSum($root1);
// $result2 = (new Solution())->deepestLeavesSum($root2);

// var_export($result1);
// echo PHP_EOL;
// var_export($result2);
