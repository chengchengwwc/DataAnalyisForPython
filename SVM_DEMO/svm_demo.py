#!/usr/bin/env python
# -*- coding:utf-8 -*-

import  pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import  train_test_split
from sklearn import svm
from sklearn import metrics
from sklearn.preprocessing import StandardScaler




def read_csv(file_path):
    return pd.read_csv(file_path)



#探索数据
def discove_data(data):
    columns_list = data.columns
    # print(data.head(5))
    # print(data.describe())
    features_mean = list(columns_list[2:12])
    features_se = list(columns_list[12:22])
    features_worst = list(columns_list[22:32])
    return features_mean,features_se,features_worst


#清洗数据
def clean_data(data):
    #ID列没有用，删除该列
    data.drop("id",axis=1,inplace=True)
    #将B良性替换为0,M恶性替换成1
    data["diagnosis"] = data['diagnosis'],map({'M':1,"B":0})
    return data


#数据可视化
def visualiza_data(data,features_mean):
    #将肿瘤睁段结果可视化
    sns.countplot(data['diagnosis'],label="Count")
    plt.show()

    #计算列之间的相关性
    corr = data[features_mean].corr()

    plt.figure(figsize=(14,14))
    #显示每个方格的数据
    sns.heatmap(corr,annot=True)
    plt.show()


def choice_characteristics(data):
    features_mean = data.columns[1:31]
    print (features_mean)
    print("-"*100)
    #抽取30%的数据作为测试集合，其他作为训练集合
    train,test = train_test_split(data,test_size=0.3)
    train_x = train[features_mean]
    train_y = train['diagnosis']
    test_x = test[features_mean]
    test_y = test['diagnosis']

    #采用Z-SCORE规范化数据 保证每个特征维度的数据均值为0，方差为1
    ss = StandardScaler()
    train_x = ss.fit_transform(train_x)
    test_x  = ss.fit_transform(test_x)

    #创建SVM分类器
    model = svm.LinearSVC()
    #用训练集做训练
    model.fit(train_x,train_y)
    #用测试集做预测
    prediction = model.predict(test_x)
    # metrics 评估方法
    # accuracy_score：分类准确率分数是指所有分类正确的百分比。分类准确率这一衡量分类器的标准比较容易理解，
    # 但是它不能告诉你响应值的潜在分布，并且它也不能告诉你分类器犯错的类型。
    #recall_score：召回率 =提取出的正确信息条数 /样本中的信息条数。通俗地说，就是所有准确的条目有多少被检索出来了。
    #Auc：计算AUC值，其中x,y分别为数组形式，根据(xi,yi)在坐标上的点，生成的曲线，然后计算AUC值；
    #roc_auc_score：直接根据真实值（必须是二值）、预测值（可以是0/1,也可以是proba值）计算出auc值，中间过程的roc计算省略
    #roc_curve：ROC曲线指受试者工作特征曲线/接收器操作特性(receiver operating characteristic，ROC)曲线,是反映灵敏性和特效性连续变量的综合指标,
    # 是用构图法揭示敏感性和特异性的相互关系，它通过将连续变量设定出多个不同的临界值，从而计算出一系列敏感性和特异性。



    print(metrics.accuracy_score(prediction,test_y))



























if __name__ == "__main__":
    tmp_file = "./data.csv"
    target_data = read_csv(tmp_file)
    features_mean, features_se, features_worst = discove_data(target_data)
    visualiza_data(data=target_data,features_mean=features_mean)








