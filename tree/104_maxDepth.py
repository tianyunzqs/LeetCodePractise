# -*- coding: utf-8 -*-
# @Time        : 2021/4/28 10:28
# @Author      : tianyunzqs
# @Description :

"""
https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""

import uuid
from random import sample
from typing import List
from graphviz import Digraph


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_tree(nums, cnt=[0]):
    """
    创建二叉树
    :param nums: 根据前序遍历整理的数组，空节点用None表示，叶子节点的左右节点都是None
    :param cnt: 计数器
    :return:
    """
    if not nums:
        return None

    x = nums[cnt[0]]
    cnt[0] += 1
    if x is None:
        bt = None
    else:
        bt = TreeNode(x)
        bt.left = build_tree(nums, cnt)
        bt.right = build_tree(nums, cnt)

    return bt


def print_tree_preorder(root: TreeNode):
    """
    前序遍历
    :param root: 二叉树的根节点
    :return:
    """
    res = []

    def preoder(root):
        if root:
            res.append(root.val)
            preoder(root.left)
            preoder(root.right)
        else:
            res.append(None)

    preoder(root)
    return res


def print_tree_inorder(root: TreeNode):
    """
    中序遍历
    :param root: 二叉树的根节点
    :return:
    """
    res = []

    def inoder(root):
        if root:
            inoder(root.left)
            res.append(root.val)
            inoder(root.right)
        else:
            res.append(None)

    inoder(root)
    return res


def print_tree_postorder(root: TreeNode):
    """
    后序遍历
    :param root: 二叉树的根节点
    :return:
    """
    res = []

    def postoder(root):
        if root:
            postoder(root.left)
            postoder(root.right)
            res.append(root.val)
        else:
            res.append(None)

    postoder(root)
    return res


def print_tree_levelorder1(root: TreeNode):
    """
    层序遍历
    :param root: 二叉树的根节点
    :return:
    """
    res = []
    if not root:
        return []
    queue = [root]
    while len(queue) > 0:  # 直到队列中节点全部被取出
        node = queue.pop(0)   # 先入对列先出（模拟队列）
        res.append(node.val)
        # 左右孩子节点都入列队，出队列的时候，按先进先出原则
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res


def print_tree_levelorder(root: TreeNode):
    """
    层序遍历
    :param root: 二叉树的根节点
    :return:
    """
    res = []
    if not root:
        return []
    queue = [root]
    while len(queue) > 0:  # 直到队列中节点全部被取出
        tmp = []
        level_size = len(queue)
        for i in range(level_size):  # 队列中保存的是每一层的节点
            node = queue.pop(0)   # 先入对列先出（模拟队列）
            tmp.append(node.val)
            # 左右孩子节点都入列队，出队列的时候，按先进先出原则
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(tmp)
    return res


def print_tree_max_depth(root: TreeNode):
    if not root:
        return 0
    max_left_depth = print_tree_max_depth(root.left)
    max_right_depth = print_tree_max_depth(root.right)
    return max_left_depth + 1 if max_left_depth > max_right_depth else max_right_depth + 1


# 利用Graphviz实现二叉树的可视化
def view_tree(root, save_path='Binary_Tree.gv', label=False):
    dot = Digraph(comment='Binary Tree')
    # colors for labels of nodes
    colors = ['skyblue', 'tomato', 'orange', 'purple', 'green', 'yellow', 'pink', 'red']

    # 绘制以某个节点为根节点的二叉树
    def print_node(node, node_tag):
        # 节点颜色
        color = sample(colors, 1)[0]
        if node.left is not None:
            left_tag = str(uuid.uuid1())            # 左节点的数据
            dot.node(left_tag, str(node.left.val), style='filled', color=color)    # 左节点
            label_string = 'L' if label else ''    # 是否在连接线上写上标签，表明为左子树
            dot.edge(node_tag, left_tag, label=label_string)   # 左节点与其父节点的连线
            print_node(node.left, left_tag)

        if node.right is not None:
            right_tag = str(uuid.uuid1())
            dot.node(right_tag, str(node.right.val), style='filled', color=color)
            label_string = 'R' if label else ''  # 是否在连接线上写上标签，表明为右子树
            dot.edge(node_tag, right_tag, label=label_string)
            print_node(node.right, right_tag)

    # 如果树非空
    if root.val is not None:
        root_tag = str(uuid.uuid1())                # 根节点标签
        dot.node(root_tag, str(root.val), style='filled', color=sample(colors, 1)[0])     # 创建根节点
        print_node(root, root_tag)

    dot.render(save_path)
    # dot.view(save_path)


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_left_depth = self.maxDepth(root.left)
        max_right_depth = self.maxDepth(root.right)
        return max_left_depth + 1 if max_left_depth > max_right_depth else max_right_depth + 1


if __name__ == '__main__':
    # nums = [3, 1, None, None, 4, 2, None, None, None]
    # nums = [1, 2, 3, None, None, 4, None, None, 2, 4, None, None, 3, None, None]
    # nums = [1, 2, None, 3, None, None, 2, None, 3, None, None]
    nums = [1, None, None]
    # nums = [3, 9, None, None, 20, 15, None, None, 7, None, None]
    tree_root = build_tree(nums, [0])
    print(print_tree_levelorder(tree_root))
    print(print_tree_max_depth(tree_root))
    print(Solution().maxDepth(tree_root))
