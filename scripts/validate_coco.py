from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval


def getImgIds(pred_json):
    with open(pred_json) as fobj:
        lines = fobj.readlines()
        ids = []
        for line in lines:
            id_str = line.split('_')[-1][:-5]
            cur_id = int(id_str)
            if cur_id not in ids:
                ids.append(cur_id)
    return ids


if __name__ == '__main__':
    anno_json = r'/home/shuai/workspace/dataset/COCO/coco2014/annotations/instances_val2014.json'
    pred_json = r'/home/shuai/workspace/network-slimming/darknet/results/coco_results.json'
    val_txt = r'/home/shuai/workspace/dataset/COCO/coco2014/5k.txt'

    anno = COCO(anno_json)    # init annotations api
    pred = anno.loadRes(pred_json)  # init predictions api
    eval = COCOeval(anno, pred, 'bbox')

    eval.params.imgIds = getImgIds(val_txt)

    eval.evaluate()
    eval.accumulate()
    eval.summarize()
    map, map50 = eval.stats[:2]  # update results (mAP@0.5:0.95, mAP@0.5)
    print(eval.stats)
    print(map)
    print(map50)