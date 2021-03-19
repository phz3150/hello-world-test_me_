def acceleration( u1 , u2 , t1 ,t2) :
    """Function that calculates the acceleration of body between times t1 and t2 when the corresponding
    speed of the body is u1 and u2. 
    Input: u1 [ m/s ], u2 [ m/s ], t1 [ s ], t2 [ s ]
    Output: a [ m/s^2 ] """
    
    a = ( u2 - u1 ) / ( t2 - t1 )
    return a