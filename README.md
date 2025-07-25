# Yang-Liu_Project
How I train the model:
1.	After you find the pictures you need on the internet,go back to your VS Code.
2.	Run the Docker contain:     cd ~/jetson-inference/   ./docker/run.sh
3.	Go into you classification folder:     cd python training classification
4.	Run the train.py :     python3 train.py --model-dir=models/testdataset data/testdataset
5.	We need to convert the PyTorch model to ONNX:     python3 onnx_export.py --model-dir=models/testdataset
6.	Now save the currentmodel paths:     NET=models/dog_breeds   DATASET=data/dog_breeds
7.	Load your model and test it with one image:     
                                                                  imagenet.py \
                                                                              --model=$NET/resnet18.onnx \
                                                                              --labels=$NET/labels.txt \
                                                                               --input_blob=input_0 \
                                                                               --output_blob=output_0 \
                                                                               $DATASET/test/dog_breeds/03.jpg output.jpg


How I collect the dataset
 1.    Open Kaggle and search https://www.kaggle.com/datasets/gpiosenka/70-dog-breedsimage-data-set?select=dogs.csv.
 2.    Choose "All datasets" and search dog breeds.
         3.    Find folders that have a lot of pictures and download it.
         4.    sort the images in three directories: test, train, and val.


Walkthrough video: https://drive.google.com/file/d/1Qz9YbpJK9EgLcGCcJfG1R7nD6B4-wurB/view?usp=sharing
                                                                          

