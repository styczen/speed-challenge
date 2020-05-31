# speed-challenge
Solution to Comma.ai speed prediction challenge

Have a look at notebook **architecure_engineering.ipynb** which is a playground with Tensorflow methods like encoding PNGs, shuffling or batching and prefetching which is used to load data in the background while model is training. 

Look at **predict_from_three_frames.ipynb** to check current solution for predicting speed from images from dashcam. Model uses three consecutive frames and predicts speed for the middle frame. In this solution to estimate speed, model is using frame from the previous timestamp, current frame and next frame. 

One problem of this solution is that there is one frame delay for speed which is not the big problem if framerate is high or car is moving slowly but it might results in problems when car is moving fast.

To avoid this problem, model can be changed so that it uses only previous and current frame so there would not be any delay because of chosen architecture design.
