lgbm_model.py

light GBM �� Ч��չʾ���룬����Ϊ����ı�׼����

��Ҫע���ʱ������ʱ��Ӧ�ñ�֤lgm_model_path Ϊ��ʵ��Ч·����
model��ص��������ӿ���ֱ�ӷ���΢��ٷ���վ



params = {
    "task": "train",        #����Ŀ��
    "boosting": "gbdt",       #boosting��ʽ
    "objective": "binary",  #Ŀ��  ������
    "tree_learner": "serial",   #������Ϸ�ʽ
    "metric": ['auc','binary_logloss'], #���۷���
    "training_metric": True,
    "train_data": './../../../data/train_data.txt',  #ѵ���ĵ�·��
    "test_data":  './../../../data/test_data.txt',  #��֤�ĵ�·��
    "header": "true",   #�ĵ����Ƿ��������ͷ
    "label_column": "name:target",   #��ǩ��
    #"weight_column": "name:weight", #Ȩ���У����Ե���ѵ�����ݶ��ڽ����Ӱ��
    "ignore_column" : "name:applicantFirst", #������
    "categorical_feature": '',  #����� ���ر�������ǰ�������
    "num_trees": 100,  #  ������������
    "learning_rate": 0.225, #ѧϰ��
    "num_leaves": 64,   #Ҷ�ڵ�����
    "feature_fraction": 0.8, #�����������
    "min_data_in_leaf": 100, # ��Ҷ��С������
    "num_threads": 12, #�������� ��ע�� boost�㷨ֻ֧����������Ĳ�������֧��������������Ĳ�����
    "convert_model_language": "cpp",  #ת��cpp�ļ���
    "output_model": "model.md",
    "output_result":"gbm_pre.txt"
    }


�����
