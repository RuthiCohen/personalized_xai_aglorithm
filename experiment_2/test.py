import os
import torch
import numpy as np
import argparse
import time
import torch.nn.functional as F

from tqdm import trange
from datetime import datetime
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
from torch.autograd import Variable

from dataset_utility import dataset, ToTensor
from dcnet import DCNet

os.environ['CUDA_VISIBLE_DEVICES'] ='0'
torch.backends.cudnn.benchmark = True

parser = argparse.ArgumentParser()
parser.add_argument('--model_name', type=str, default='all')

parser.add_argument('--dataset', type=str, default='RAVEN-10000')
parser.add_argument('--root', type=str, default='./dataset/RAVEN-10000')
parser.add_argument('--pretrained_model', type=str, default='model_02.pth')

parser.add_argument('--batch_size', type=int, default=32)
parser.add_argument('--img_size', type=int, default=96)
parser.add_argument('--workers', type=int, default=16)
parser.add_argument('--seed', type=int, default=123)

args = parser.parse_args()
device = torch.device('mps' if torch.cuda.is_available() else 'cpu')

if torch.cuda.is_available():
    torch.cuda.manual_seed(args.seed)
elif torch.backends.mps.is_available():
    torch.manual_seed(args.seed)  # torch.manual_seed works for CPU & MPS

tf = transforms.Compose([ToTensor()])

model = DCNet().to(device)
model.load_state_dict(torch.load(args.pretrained_model))

def test(test_loader):
    model.eval()
    metrics = {'correct': [], 'count': []}

    test_loader_iter = iter(test_loader)
    for _ in trange(len(test_loader_iter)):
        image, target = next(test_loader_iter)

        image = Variable(image, requires_grad=False).to(device)
        target = Variable(target, requires_grad=False).to(device)

        with torch.no_grad():
            predict = model(image)

        pred = torch.max(predict, 1)[1]
        correct = pred.eq(target.data).cpu().sum().numpy()

        metrics['correct'].append(correct)
        metrics['count'].append(target.size(0))

        accuracy = 100 * np.sum(metrics['correct']) / np.sum(metrics['count'])

    return metrics


if __name__ == '__main__':

    if args.dataset == 'RAVEN-10000':
        fig_types = ['center_single', 'distribute_four', 'distribute_nine',
        'left_center_single_right_center_single', 'up_center_single_down_center_single',
        'in_center_single_out_center_single', 'in_distribute_four_out_center_single']

        accuracy_list = []
        for i in range(len(fig_types)):
            test_set = dataset(args.root, 'test', fig_types[i], args.img_size, tf)
            test_loader = DataLoader(test_set, batch_size=args.batch_size, shuffle=False, num_workers=args.workers, pin_memory=True)

            metrics_test = test(test_loader)
            acc_test = 100 * np.sum(metrics_test['correct']) / np.sum(metrics_test['count'])
            accuracy_list.append(acc_test)
            print(np.sum(metrics_test['correct']), np.sum(metrics_test['count']) , "----------------")
            print ('FigType: {:s}, Accuracy: {:.3f} \n'.format(fig_types[i], acc_test))

        print (accuracy_list)
        print ('Average Accuracy: {:.3f} \n'.format(np.mean(accuracy_list)))

    elif args.dataset == 'pgm':
        test_set = dataset(args.root, 'val', 'interpolation', args.img_size, tf)  # interpolation, extrapolation
        test_loader = DataLoader(test_set, batch_size=args.batch_size, shuffle=False, num_workers=args.workers, pin_memory=True)

        metrics_test = test(test_loader)
        acc_test = 100 * np.sum(metrics_test['correct']) / np.sum(metrics_test['count'])

        print ('Average Accuracy: {:.3f} \n'.format(acc_test))


