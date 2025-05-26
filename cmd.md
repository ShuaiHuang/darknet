# Commands

## Train model on the VOC

```
./darknet detector train cfg/voc.data cfg/yolov3-voc.cfg darknet53.conv.74
```

## Test model trained on the VOC

```
./darknet detector test cfg/voc.data cfg/myyolov3-voc.cfg backup/myyolov3-voc.backup data/dog.jpg
```

## Train model on the COCO

```
./darknet detector train cfg/coco.data cfg/yolov3.cfg darknet53.conv.74

nohup ./darknet detector train cfg/coco.data cfg/yolov3.cfg darknet53.conv.74 > train-coco.log 2>&1 &
```

## Set Up Image Lists (COCO)

```
paste <(awk "{print \"$PWD\"}" <5k.part) 5k.part | tr -d '\t' > 5k.txt
paste <(awk "{print \"$PWD\"}" <trainvalno5k.part) trainvalno5k.part | tr -d '\t' > trainvalno5k.txt
```


## Test model trained on the COCO

```
./darknet detector test cfg/coco.data cfg/yolov3.cfg backup/yolov3.backup data/dog.jpg
```
