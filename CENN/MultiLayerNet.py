from config import *

class MultiLayerNet(torch.nn.Module):
    def __init__(self, D_in, H, D_out):
        """
        In the constructor we instantiate two nn.Linear modules and assign them as
        member variables.
        """
        super(MultiLayerNet, self).__init__()
        self.linear1 = torch.nn.Linear(D_in, H)
        self.linear2 = torch.nn.Linear(H, H)
        self.linear3 = torch.nn.Linear(H, H)
        self.linear4 = torch.nn.Linear(H, D_out)
        
        self.a1 = torch.nn.Parameter(torch.Tensor([0.1]))
        self.a2 = torch.nn.Parameter(torch.Tensor([0.1]))
        self.a3 = torch.nn.Parameter(torch.Tensor([0.1]))
        
        # self.a1 = torch.Tensor([0.1])
        # self.a2 = torch.Tensor([0.1])
        # self.a3 = torch.Tensor([0.1])

        torch.nn.init.constant_(self.linear1.bias, 0.)
        torch.nn.init.constant_(self.linear2.bias, 0.)
        torch.nn.init.constant_(self.linear3.bias, 0.)
        torch.nn.init.constant_(self.linear4.bias, 0.)

        torch.nn.init.normal_(self.linear1.weight, mean=0, std=np.sqrt(2/(D_in+H)))
        torch.nn.init.normal_(self.linear2.weight, mean=0, std=np.sqrt(2/(H+H)))
        torch.nn.init.normal_(self.linear3.weight, mean=0, std=np.sqrt(2/(H+H)))
        torch.nn.init.normal_(self.linear4.weight, mean=0, std=np.sqrt(2/(H+D_out)))
        # torch.nn.init.normal_(self.linear1.weight, mean=0, std=0.1)
        # torch.nn.init.normal_(self.linear2.weight, mean=0, std=0.1)
        # torch.nn.init.normal_(self.linear3.weight, mean=0, std=0.1)
        # torch.nn.init.normal_(self.linear4.weight, mean=0, std=0.1)

    def forward(self, x):
        """
        In the forward function we accept a Tensor of input data and we must return
        a Tensor of output data. We can use Modules defined in the constructor as
        well as arbitrary operators on Tensors.
        """

        y1 = torch.tanh(10*self.a1*self.linear1(x))
        y2 = torch.tanh(10*self.a1*self.linear2(y1))
        y3 = torch.tanh(10*self.a1*self.linear3(y2))
        y = self.linear4(y3)
        return y
    
class MultiLayerNet_p(torch.nn.Module):
    def __init__(self, D_in, H, D_out):
        """
        particular solution
        """
        super(MultiLayerNet_p, self).__init__()
        self.linear1 = torch.nn.Linear(D_in, H)
        self.linear2 = torch.nn.Linear(H, H)
        self.linear3 = torch.nn.Linear(H, H)
        self.linear4 = torch.nn.Linear(H, H)
        self.linear5 = torch.nn.Linear(H, D_out)

        torch.nn.init.constant_(self.linear1.bias, 0.)
        torch.nn.init.constant_(self.linear2.bias, 0.)
        torch.nn.init.constant_(self.linear3.bias, 0.)
        torch.nn.init.constant_(self.linear4.bias, 0.)
        torch.nn.init.constant_(self.linear5.bias, 0.)
        
        torch.nn.init.normal_(self.linear1.weight, mean=0, std=0.1)
        torch.nn.init.normal_(self.linear2.weight, mean=0, std=0.1)
        torch.nn.init.normal_(self.linear3.weight, mean=0, std=0.1)
        torch.nn.init.normal_(self.linear4.weight, mean=0, std=0.1)
        torch.nn.init.normal_(self.linear5.weight, mean=0, std=0.1)
    def forward(self, x):
        """
        In the forward function we accept a Tensor of input data and we must return
        a Tensor of output data. We can use Modules defined in the constructor as
        well as arbitrary operators on Tensors.
        """

        y1 = torch.tanh(self.linear1(x))
        y2 = torch.tanh(self.linear2(y1))
        y3 = torch.tanh(self.linear3(y2))
        y4 = torch.tanh(self.linear4(y3))
        y = self.linear5(y4)
        return y
    
class MultiLayerNet_d(torch.nn.Module):
    def __init__(self, D_in, H, D_out):
        """
        distance function
        """
        super(MultiLayerNet_d, self).__init__()
        self.linear1 = torch.nn.Linear(D_in, H)
        # self.linear2 = torch.nn.Linear(H, H)
        # self.linear3 = torch.nn.Linear(H, H)
        # self.linear4 = torch.nn.Linear(H, H)
        # self.linear5 = torch.nn.Linear(H, H)
        self.linear6 = torch.nn.Linear(H, D_out)

        torch.nn.init.constant_(self.linear1.bias, 0.)
        # torch.nn.init.constant_(self.linear2.bias, 0.)
        # torch.nn.init.constant_(self.linear3.bias, 0.)
        # torch.nn.init.constant_(self.linear4.bias, 0.)
        # torch.nn.init.constant_(self.linear5.bias, 0.)
        torch.nn.init.constant_(self.linear6.bias, 0.)
        
        torch.nn.init.normal_(self.linear1.weight, mean=0, std=0.1)
        # torch.nn.init.normal_(self.linear2.weight, mean=0, std=0.1)
        # torch.nn.init.normal_(self.linear3.weight, mean=0, std=0.1)
        # torch.nn.init.normal_(self.linear4.weight, mean=0, std=0.1)
        # torch.nn.init.normal_(self.linear5.weight, mean=0, std=0.1)
        torch.nn.init.normal_(self.linear6.weight, mean=0, std=0.1)
    def forward(self, x):
        """
        In the forward function we accept a Tensor of input data and we must return
        a Tensor of output data. We can use Modules defined in the constructor as
        well as arbitrary operators on Tensors.
        
        """

        y1 = torch.tanh(self.linear1(x))
        # y2 = torch.tanh(self.linear2(y1))
        # y3 = torch.tanh(self.linear3(y2))+y1
        # y4 = torch.tanh(self.linear4(y3))
        # y5 = torch.tanh(self.linear5(y4))
        y = torch.sigmoid(self.linear6(y1))
        return y
    
class MultiLayerNet_d_b(torch.nn.Module):
      # Shallow network designed specifically for cantilever beam, last layer cannot be sigmoid because distance is up to 4
    def __init__(self, D_in, H, D_out):
        """
        distance function
        """
        super(MultiLayerNet_d_b, self).__init__()
        self.linear1 = torch.nn.Linear(D_in, H)
        self.linear2 = torch.nn.Linear(H, D_out)

        torch.nn.init.constant_(self.linear1.bias, 0.)
        torch.nn.init.constant_(self.linear2.bias, 0.)

        
        torch.nn.init.normal_(self.linear1.weight, mean=0, std=0.1)
        torch.nn.init.normal_(self.linear2.weight, mean=0, std=0.1)

    def forward(self, x):
        """
        In the forward function we accept a Tensor of input data and we must return
        a Tensor of output data. We can use Modules defined in the constructor as
        well as arbitrary operators on Tensors.
        """

        y1 = torch.tanh(self.linear1(x))
        y = torch.relu(self.linear2(y1))
        return y