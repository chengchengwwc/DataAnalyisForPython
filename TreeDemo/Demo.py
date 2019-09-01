#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
"""
普通树：
要么为空，要么包含了一个有限的节点集合T，有一个和所有节点不同的节点r，称为根，此外
集合T-{r}被划分为不相连的子集，每个子集都是一个普通树
二叉树：一个二叉树要么为空，要么包含一个根节点，外加一个左子树和一个右子树 每个子树都是二差树

树最重要的是父节点和子节点之间的关系，这些关系是结构化数据所必备的
高度为H的树，节点数为 2^(H+1) - 1
由于在从根节点到一个叶子节点的给定路径上，如果访问一个满二叉树上的一个给定的节点的话，所需要的最大工作量为O(logN)
二叉树的三种应用：
1 堆
二叉树中的数据通常都提取自有序的集合，其中的项是可以比较的，一个最小的堆，就是其中的每一个节点都小于或是等于其两个子节点
的一个二叉树，一个最大堆 就是将最大的节点放置在最靠近根节点的位置

2 二叉搜索树

3 表达式树

二叉树遍历：
1 前序遍历：
先访问树的根节点，然后以类似的方式分别遍历左子树和右子树，按照前序便利的方式访问节点
2 中序遍历：
中序遍历的算法是先遍历左子树，然后访问根节点，最后遍历右子树
3 后序遍历
后序遍历算法会先遍历左子树，然后是右子树 最后是根节点
4 层序遍历
首先从0级开始，在每一个层级按照从左到右的顺序访问子节点
"""


    
