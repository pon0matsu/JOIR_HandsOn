import torch
import timm
import torchvision.transforms as transforms
import torch.utils.data as data
import numpy as np
from PIL import Image
from tqdm.notebook import tqdm
import argparse

# コマンドライン引数の設定
def get_args():
    parser = argparse.ArgumentParser(description="Age Prediction Script")
    parser.add_argument('--model_path', type=str, required=True, help="Path to the model file")
    parser.add_argument('--image_paths', type=str, nargs='+', required=True, help="Paths to the images for prediction")
    return parser.parse_args()

# 乱数固定化の定義
def torch_seed(seed=1):
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.backends.cudnn.deterministic = True
        torch.use_deterministic_algorithms(True)

# Datasetクラスの作成
class Dataset(data.Dataset):
    def __init__(self, img_list, transform=None):
        self.img_list = img_list
        self.transform = transform
    
    def __len__(self):
        return len(self.img_list)
    
    def __getitem__(self, index):
        img_path = self.img_list[index]
        img = Image.open(img_path)
        img = self.transform(img)   
        return img

# メイン処理
def main():
    # 引数を取得
    args = get_args()
    model_path = args.model_path
    img_list = args.image_paths

    # モデル枠組み読み込み
    model = timm.create_model(model_name='swin_base_patch4_window12_384', num_classes=1, pretrained=False)

    # GPU使用する場合
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model = model.to(device)

    # 学習済みモデル読み込み
    model.load_state_dict(torch.load(model_path, map_location=device))

    # imageNetに合わせた画像の正規化
    mean = (0.485, 0.456, 0.406)
    std = (0.229, 0.224, 0.225)

    # transformの定義
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean, std),
    ])

    # Datasetの作成
    dataset = Dataset(
        img_list=img_list, transform=transform
    )

    # Dataloaderの作成
    loader = data.DataLoader(
        dataset, batch_size=1, shuffle=False
    )

    # 乱数固定化
    torch_seed()

    # 年齢予測
    pred_r = []

    model.eval()
    with torch.no_grad():
        for inputs in tqdm(loader):
            inputs = inputs.to(device)
            outputs = model(inputs)
            pred_r.append(outputs.data.cpu().numpy())
        
    pred = np.concatenate(pred_r)

    # 結果出力
    print("Predicted Ages:", pred)

if __name__ == "__main__":
    main()