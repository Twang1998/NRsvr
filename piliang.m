clear all;
result = [];
result2 = [];
%addpath('lib');
%addpath('E:\taowang');
load test_region.mat
load train_region.mat
addpath('C:\Users\Orange\Desktop\lownr\NRIQA\BLIINDS2');
%cd ;
%save('E:\taowang\NR\BRISQUE\test.mat', 'test_region_path')
 for j = 1:1500 %��һ��ȡͼ��
            image_name = strcat('E:\taowang\Texture\',train_region_path(j,:));% ͼ����
            disp(image_name);% ��ʾ���ڴ����ͼ����
            img = double(rgb2gray(imread(image_name)));
            feat = bliinds2_feature_extraction(img);
            % local mean and variance
            result = [result;feat];
            %result = [result; ee];
            %ͼ������� ʡ�� 
 end
save('E:\taowang\NR\BMPRI\train_region_feature.mat', 'result')
  for j = 1:300 %��һ��ȡͼ��
            image_name = strcat('E:\taowang\Texture\',test_region_path(j,:));% ͼ����
            disp(image_name);% ��ʾ���ڴ����ͼ����
            img = double(rgb2gray(imread(image_name)));
            feat = bliinds2_feature_extraction(img);
            % local mean and variance
            result2 = [result2;feat];
            %result = [result; ee];
            %ͼ������� ʡ��
  end
save('E:\taowang\NR\BMPRI\test_region_feature.mat', 'result2')