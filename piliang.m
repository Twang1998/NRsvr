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
 for j = 1:1500 %逐一读取图像
            image_name = strcat('E:\taowang\Texture\',train_region_path(j,:));% 图像名
            disp(image_name);% 显示正在处理的图像名
            img = double(rgb2gray(imread(image_name)));
            feat = bliinds2_feature_extraction(img);
            % local mean and variance
            result = [result;feat];
            %result = [result; ee];
            %图像处理过程 省略 
 end
save('E:\taowang\NR\BMPRI\train_region_feature.mat', 'result')
  for j = 1:300 %逐一读取图像
            image_name = strcat('E:\taowang\Texture\',test_region_path(j,:));% 图像名
            disp(image_name);% 显示正在处理的图像名
            img = double(rgb2gray(imread(image_name)));
            feat = bliinds2_feature_extraction(img);
            % local mean and variance
            result2 = [result2;feat];
            %result = [result; ee];
            %图像处理过程 省略
  end
save('E:\taowang\NR\BMPRI\test_region_feature.mat', 'result2')