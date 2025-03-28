from torchvision.models import get_model
model = get_model("vgg11", weights = None)
model #this loads the pre-trained model in pytorch 

