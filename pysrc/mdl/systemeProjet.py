import functools
class SystemeProjet : 
    def __init__(self,r1,r2,K1,K2,alpha,beta,gamma,delta,title) : 
        self._r1 = r1
        self._K1 = K1
        self._alpha = alpha
        self._gamma = gamma
        self._r2 = r2
        self._K2 = K2
        self._beta = beta
        self._delta = delta
        self._title = title        

    def get_r1(self) : 
        return self._r1
    def get_K1(self) : 
        return self._K1
    def get_alpha(self) : 
        return self._alpha
    def get_gamma(self) : 
        return self._gamma  
    def get_r2(self) : 
        return self._r2
    def get_K2(self) : 
        return self._K2
    def get_beta(self) : 
        return self._beta
    def get_delta(self) : 
        return self._delta
    def get_title(self) : 
        return self._title
    def get_rhs ( self ) :
        return functools.partial( self . _rhs )

    def set_r1(self,r1) : 
        self._r1 = r1
    def set_r2(self,r2) : 
        self._r2 = r2
    def set_K1(self,K1) : 
        self._K1 = K1
    def set_K2(self,K2) : 
        self._K2 = K2
    def set_alpha(self,alpha) : 
        self._alpha = alpha
    def set_beta(self,beta) : 
        self._beta = beta
    def set_gamma(self,gamma) : 
        self._gamma = gamma
    def set_delta(self,delta) : 
        self._delta = delta
    

    def get_field ( self , x , y ) :
        r1 = self.get_r1()
        K1 = self.get_K1()
        alpha = self.get_alpha()
        gamma = self.get_gamma()
        r2 = self.get_r2()
        K2 = self.get_K2()
        beta = self.get_beta()
        delta = self.get_delta()
        f = r1 * x * (K1 - x - alpha * y) / K1 + gamma * x * y
        g = r2 * y * (K2 - y - beta * x) / K2 - delta * x * y
        return [f, g]

    def  _rhs(self , z, t):
        r1 = self.get_r1()
        K1 = self.get_K1()
        alpha = self.get_alpha()
        gamma = self.get_gamma()
        r2 = self.get_r2()
        K2 = self.get_K2()
        beta = self.get_beta()
        delta = self.get_delta()
        x = z[0]
        y = z[1]
        dxdt = r1 * x * (K1 - x - alpha * y) / K1 + ( gamma * x * y ) 
        dydt = r2 * y * (K2 - y - beta * x) / K2 - ( delta * x * y ) 
        return [dxdt , dydt]